"""
Unit tests for FIT analysis backend

Run with: pytest test_backend.py -v
"""

import unittest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from calculations import (
    normalized_power,
    estimate_ftp,
    intensity_factor,
    training_stress_score,
    power_zones,
    time_in_power_zones,
    hr_zones,
    time_in_hr_zones,
    estimate_vo2max,
    calculate_elevation_metrics,
    running_efficiency,
    seconds_to_hms,
    pace_to_string,
)
from metrics import MetricsCalculator, SessionSummary


class TestPowerMetrics(unittest.TestCase):
    """Test power-based calculations"""

    def setUp(self):
        """Create sample power data"""
        self.power_series = pd.Series([200, 210, 220, 215, 205, 225, 230] * 100)

    def test_normalized_power(self):
        """Test normalized power calculation"""
        np_val = normalized_power(self.power_series)
        self.assertGreater(np_val, 0)
        self.assertIsInstance(np_val, float)
        # Should be higher than mean due to fourth-power bias
        self.assertGreater(np_val, self.power_series.mean() * 0.9)

    def test_estimate_ftp(self):
        """Test FTP estimation"""
        ftp = estimate_ftp(self.power_series)
        self.assertGreater(ftp, 0)
        self.assertIsInstance(ftp, float)
        # FTP should be reasonable (0.95x of best 20min avg)
        self.assertGreater(ftp, self.power_series.mean() * 0.8)

    def test_intensity_factor(self):
        """Test intensity factor calculation"""
        if_val = intensity_factor(250, 280)
        self.assertAlmostEqual(if_val, 0.893, places=2)

    def test_intensity_factor_zero_ftp(self):
        """Test intensity factor with zero FTP"""
        if_val = intensity_factor(250, 0)
        self.assertEqual(if_val, 0.0)

    def test_training_stress_score(self):
        """Test TSS calculation"""
        tss = training_stress_score(3600, 280, 280)  # 1 hour at FTP
        self.assertEqual(tss, 100.0)

    def test_tss_zero_values(self):
        """Test TSS with zero values"""
        tss = training_stress_score(3600, 0, 280)
        self.assertEqual(tss, 0.0)

    def test_power_zones(self):
        """Test power zone generation"""
        zones = power_zones(280)
        self.assertEqual(len(zones), 6)
        self.assertIn("Z1 Recovery", zones)
        self.assertIn("Z6 Anaerobic", zones)

    def test_power_zones_zero_ftp(self):
        """Test power zones with zero FTP"""
        zones = power_zones(0)
        self.assertEqual(len(zones), 0)


class TestHeartRateMetrics(unittest.TestCase):
    """Test heart rate calculations"""

    def test_hr_zones(self):
        """Test HR zone generation"""
        zones = hr_zones(195)
        self.assertEqual(len(zones), 5)
        self.assertIn("Z1 Recovery", zones)
        self.assertIn("Z5 VO2max", zones)

    def test_estimate_vo2max_power_based(self):
        """Test VO2max estimation from power"""
        vo2 = estimate_vo2max(160, 195, ftp=280, weight_kg=75)
        # Power-based: (280/75) * 10.8 + 7
        expected = (280 / 75) * 10.8 + 7
        self.assertAlmostEqual(vo2, expected, places=1)

    def test_estimate_vo2max_hr_based(self):
        """Test VO2max estimation from heart rate"""
        vo2 = estimate_vo2max(160, 195, ftp=0, weight_kg=75)
        # HR-based method
        self.assertGreater(vo2, 0)
        self.assertLess(vo2, 90)

    def test_estimate_vo2max_invalid(self):
        """Test VO2max with invalid values"""
        vo2 = estimate_vo2max(0, 0, ftp=0, weight_kg=0)
        self.assertEqual(vo2, 0.0)

    def test_running_efficiency(self):
        """Test running efficiency calculation"""
        # Speed 4 m/s, HR 160 bpm
        ef = running_efficiency(4.0, 160)
        # (4 * 60) / 160 = 240 / 160 = 1.5
        self.assertAlmostEqual(ef, 1.5, places=2)

    def test_running_efficiency_zero(self):
        """Test running efficiency with zero values"""
        ef = running_efficiency(0, 160)
        self.assertEqual(ef, 0.0)


class TestElevationMetrics(unittest.TestCase):
    """Test elevation calculations"""

    def test_elevation_gain_loss(self):
        """Test elevation gain and loss calculation"""
        # Simulate climb then descent
        altitude = pd.Series([100, 150, 200, 250, 200, 150, 100])
        elev = calculate_elevation_metrics(altitude)

        self.assertGreater(elev["elevation_gain_m"], 0)
        self.assertGreater(elev["elevation_loss_m"], 0)

    def test_elevation_flat(self):
        """Test elevation on flat terrain"""
        altitude = pd.Series([100] * 100)
        elev = calculate_elevation_metrics(altitude)

        self.assertEqual(elev["elevation_gain_m"], 0)
        self.assertEqual(elev["elevation_loss_m"], 0)

    def test_elevation_empty(self):
        """Test elevation with empty data"""
        altitude = pd.Series([])
        elev = calculate_elevation_metrics(altitude)

        self.assertEqual(elev["elevation_gain_m"], 0.0)
        self.assertEqual(elev["elevation_loss_m"], 0.0)


class TestFormatting(unittest.TestCase):
    """Test formatting functions"""

    def test_seconds_to_hms(self):
        """Test seconds to HH:MM:SS conversion"""
        self.assertEqual(seconds_to_hms(3661), "01:01:01")
        self.assertEqual(seconds_to_hms(300), "00:05:00")
        self.assertEqual(seconds_to_hms(3600), "01:00:00")

    def test_pace_to_string(self):
        """Test pace formatting"""
        # 6 min/km pace
        pace_str = pace_to_string(6.0)
        self.assertEqual(pace_str, "6:00 /km")

        # 5:30 pace
        pace_str = pace_to_string(5.5)
        self.assertEqual(pace_str, "5:30 /km")

    def test_pace_invalid(self):
        """Test pace formatting with invalid values"""
        pace_str = pace_to_string(0)
        self.assertEqual(pace_str, "N/A")

        pace_str = pace_to_string(np.nan)
        self.assertEqual(pace_str, "N/A")


class TestZoneDistribution(unittest.TestCase):
    """Test zone time calculations"""

    def setUp(self):
        """Create sample data"""
        # Create cycling session with power
        self.df = pd.DataFrame({
            "power_w": [100, 150, 200, 250, 300, 350] * 100,
            "hr": [130, 140, 150, 160, 170, 180] * 100,
        })

    def test_time_in_power_zones(self):
        """Test power zone time distribution"""
        zones_df = time_in_power_zones(self.df, ftp=250)

        self.assertEqual(len(zones_df), 6)
        self.assertIn("Zone", zones_df.columns)
        self.assertIn("Percentage", zones_df.columns)
        # Total should be close to 100%
        total_pct = zones_df["Percentage"].sum()
        self.assertAlmostEqual(total_pct, 100.0, places=0)

    def test_time_in_hr_zones(self):
        """Test HR zone time distribution"""
        zones_df = time_in_hr_zones(self.df, max_hr=195)

        self.assertEqual(len(zones_df), 5)
        self.assertIn("Zone", zones_df.columns)
        # Total should be close to 100%
        total_pct = zones_df["Percentage"].sum()
        self.assertAlmostEqual(total_pct, 100.0, places=0)


class TestMetricsCalculator(unittest.TestCase):
    """Test high-level metrics calculator"""

    def setUp(self):
        """Create sample session data"""
        num_points = 3600
        start_time = datetime.now() - timedelta(hours=1)

        self.df = pd.DataFrame({
            "timestamp": [start_time + timedelta(seconds=i) for i in range(num_points)],
            "elapsed_sec": np.arange(num_points, dtype=float),
            "distance_km": np.linspace(0, 42, num_points),
            "hr": np.random.normal(150, 8, num_points).astype(int),
            "power_w": np.random.normal(250, 40, num_points).astype(int),
            "speed_kmh": np.random.normal(42, 2, num_points),
            "cadence_rpm": np.random.normal(90, 5, num_points),
            "altitude_m": 100 + 10 * np.sin(np.linspace(0, 4 * np.pi, num_points)),
        })

        # Ensure valid values
        self.df["hr"] = np.clip(self.df["hr"], 60, 220)
        self.df["power_w"] = np.clip(self.df["power_w"], 0, 2000)

        self.athlete_data = {
            "ftp": 280,
            "max_hr": 195,
            "weight_kg": 75,
            "sport": "cycling",
        }

    def test_calculator_init(self):
        """Test MetricsCalculator initialization"""
        calc = MetricsCalculator(self.athlete_data)
        self.assertEqual(calc.max_hr, 195)
        self.assertEqual(calc.ftp_input, 280)
        self.assertEqual(calc.weight_kg, 75)

    def test_analyze_session(self):
        """Test complete session analysis"""
        calc = MetricsCalculator(self.athlete_data)
        session = calc.analyze_session(self.df)

        self.assertIsInstance(session, SessionSummary)
        self.assertGreater(session.duration_sec, 0)
        self.assertGreater(session.distance_km, 0)
        self.assertGreater(session.avg_hr, 0)
        self.assertTrue(session.has_power)
        self.assertGreater(session.normalized_power, 0)

    def test_session_dict_export(self):
        """Test session export to dictionary"""
        calc = MetricsCalculator(self.athlete_data)
        session = calc.analyze_session(self.df)
        session_dict = session.to_dict()

        self.assertIsInstance(session_dict, dict)
        self.assertIn("duration_sec", session_dict)
        self.assertIn("distance_km", session_dict)
        self.assertIn("tss", session_dict)

    def test_zone_distribution(self):
        """Test zone distribution calculation"""
        calc = MetricsCalculator(self.athlete_data)
        zones = calc.get_zone_distribution(self.df, ftp=280)

        self.assertIn("hr_zones", zones)
        self.assertIsInstance(zones["hr_zones"], pd.DataFrame)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error handling"""

    def test_empty_series(self):
        """Test with empty data"""
        empty_series = pd.Series([])
        np_val = normalized_power(empty_series)
        self.assertEqual(np_val, 0.0)

    def test_single_value_series(self):
        """Test with single value"""
        single = pd.Series([250])
        ftp = estimate_ftp(single)
        self.assertGreater(ftp, 0)

    def test_nan_values(self):
        """Test handling of NaN values"""
        series_with_nan = pd.Series([200, np.nan, 220, np.nan, 210])
        np_val = normalized_power(series_with_nan)
        self.assertGreater(np_val, 0)

    def test_negative_values(self):
        """Test handling of negative values"""
        series = pd.Series([100, -50, 200, 150])
        # Should handle gracefully
        np_val = normalized_power(series)
        self.assertIsInstance(np_val, float)


if __name__ == "__main__":
    unittest.main()
