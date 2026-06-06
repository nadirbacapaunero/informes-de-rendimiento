"""
Example usage and sample data for FIT file analysis backend

This module demonstrates how to use the FIT parser, metrics calculator,
and perform complete session analysis.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from parser import FITParser, parse_fit_file
from metrics import MetricsCalculator
from calculations import (
    normalized_power,
    estimate_ftp,
    training_stress_score,
    estimate_vo2max,
    calculate_elevation_metrics,
    power_zones,
    hr_zones,
    seconds_to_hms,
    pace_to_string,
)


# ─────────────────────────────────────────────
# SAMPLE DATA GENERATION
# ─────────────────────────────────────────────

def generate_sample_cycling_session() -> pd.DataFrame:
    """
    Generate sample cycling session data

    Returns
    -------
    pd.DataFrame
        Sample record data with 1-second intervals
    """
    # 1 hour cycling session
    num_points = 3600
    start_time = datetime.now() - timedelta(hours=1)

    data = {
        "timestamp": [
            start_time + timedelta(seconds=i) for i in range(num_points)
        ],
        "elapsed_sec": np.arange(num_points, dtype=float),
        "distance_km": np.linspace(0, 42, num_points),
        "hr": np.random.normal(150, 8, num_points).astype(int),
        "power_w": np.random.normal(250, 40, num_points).astype(int),
        "speed_kmh": np.random.normal(42, 2, num_points),
        "cadence_rpm": np.random.normal(90, 5, num_points),
        "altitude_m": 100 + 10 * np.sin(np.linspace(0, 4 * np.pi, num_points)),
    }

    # Ensure non-negative values
    data["hr"] = np.clip(data["hr"], 60, 220)
    data["power_w"] = np.clip(data["power_w"], 0, 2000)
    data["speed_kmh"] = np.clip(data["speed_kmh"], 0, 80)
    data["cadence_rpm"] = np.clip(data["cadence_rpm"], 0, 180)

    df = pd.DataFrame(data)
    return df


def generate_sample_running_session() -> pd.DataFrame:
    """
    Generate sample running session data

    Returns
    -------
    pd.DataFrame
        Sample record data with 1-second intervals
    """
    # 45-minute running session
    num_points = 2700
    start_time = datetime.now() - timedelta(minutes=45)

    data = {
        "timestamp": [
            start_time + timedelta(seconds=i) for i in range(num_points)
        ],
        "elapsed_sec": np.arange(num_points, dtype=float),
        "distance_km": np.linspace(0, 8.5, num_points),
        "hr": np.random.normal(160, 6, num_points).astype(int),
        "speed_kmh": np.random.normal(11.3, 0.5, num_points),
        "cadence_rpm": np.random.normal(170, 8, num_points),
        "altitude_m": 50 + 5 * np.sin(np.linspace(0, 3 * np.pi, num_points)),
    }

    # Ensure non-negative values
    data["hr"] = np.clip(data["hr"], 80, 220)
    data["speed_kmh"] = np.clip(data["speed_kmh"], 0, 20)
    data["cadence_rpm"] = np.clip(data["cadence_rpm"], 100, 200)

    df = pd.DataFrame(data)
    # Add pace for running
    df["pace_min_km"] = df["speed_kmh"].apply(
        lambda s: 60 / s if s > 0 else None
    )
    return df


# ─────────────────────────────────────────────
# EXAMPLE 1: BASIC FIT FILE PARSING
# ─────────────────────────────────────────────

def example_parse_fit_file():
    """
    Example: Parse FIT file from disk or file-like object
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 1: FIT File Parsing")
    print("=" * 60)

    # Using standalone function
    # df = parse_fit_file("path/to/activity.fit")

    # Using FITParser class
    parser = FITParser()

    # In real usage:
    # df = parser.parse("path/to/activity.fit")
    # Or from file-like object:
    # df = parser.parse(uploaded_file)

    print("✓ Parser ready to handle:")
    print("  - File paths: parser.parse('activity.fit')")
    print("  - File objects: parser.parse(file_obj)")
    print("  - BytesIO: parser.parse(io.BytesIO(data))")


# ─────────────────────────────────────────────
# EXAMPLE 2: POWER METRICS (CYCLING)
# ─────────────────────────────────────────────

def example_power_metrics():
    """
    Example: Calculate power-based training metrics
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Power Metrics (Cycling Session)")
    print("=" * 60)

    # Generate sample data
    df = generate_sample_cycling_session()
    print(f"\nGenerated sample cycling session: {len(df)} records")
    print(f"Duration: {df['elapsed_sec'].max():.0f} seconds")
    print(f"Distance: {df['distance_km'].max():.1f} km")

    # Calculate key power metrics
    power_series = df["power_w"]
    np_value = normalized_power(power_series)
    estimated_ftp = estimate_ftp(power_series)

    print(f"\n--- Power Metrics ---")
    print(f"Avg Power:        {power_series.mean():.1f} W")
    print(f"Max Power:        {power_series.max():.1f} W")
    print(f"Normalized Power: {np_value:.1f} W")
    print(f"Estimated FTP:    {estimated_ftp:.1f} W")

    # Training Stress Score
    duration = df["elapsed_sec"].max()
    tss = training_stress_score(duration, np_value, estimated_ftp)
    intensity_f = np_value / estimated_ftp

    print(f"\n--- Training Stress ---")
    print(f"Duration:         {seconds_to_hms(duration)}")
    print(f"Intensity Factor: {intensity_f:.2f}")
    print(f"TSS Score:        {tss:.1f}")

    # Power zones
    zones = power_zones(estimated_ftp)
    print(f"\n--- Power Zones (FTP = {estimated_ftp:.0f} W) ---")
    for zone_name, (zone_min, zone_max) in zones.items():
        print(f"  {zone_name}: {zone_min} - {zone_max} W")


# ─────────────────────────────────────────────
# EXAMPLE 3: HR & VO2MAX METRICS
# ─────────────────────────────────────────────

def example_hr_vo2max():
    """
    Example: Heart rate and VO2max analysis
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Heart Rate & VO2max Analysis")
    print("=" * 60)

    # Generate sample data
    df = generate_sample_running_session()

    # HR metrics
    max_hr_session = int(df["hr"].max())
    avg_hr = df["hr"].mean()

    print(f"\n--- Heart Rate ---")
    print(f"Avg HR:     {avg_hr:.0f} bpm")
    print(f"Max HR:     {max_hr_session} bpm")
    print(f"Min HR:     {int(df['hr'].min())} bpm")

    # Athlete parameters
    max_hr_athlete = 195
    weight_kg = 70

    # VO2max estimation (HR-based)
    vo2_hr = estimate_vo2max(avg_hr, max_hr_athlete)
    print(f"\n--- VO2max Estimation ---")
    print(f"Estimated (HR-based): {vo2_hr:.1f} ml/kg/min")

    # HR zones
    zones = hr_zones(max_hr_athlete)
    print(f"\n--- HR Zones (Max HR = {max_hr_athlete} bpm) ---")
    for zone_name, (zone_min, zone_max) in zones.items():
        print(f"  {zone_name}: {zone_min} - {zone_max} bpm")


# ─────────────────────────────────────────────
# EXAMPLE 4: COMPLETE SESSION ANALYSIS
# ─────────────────────────────────────────────

def example_complete_session_analysis():
    """
    Example: Full session analysis with MetricsCalculator
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Complete Session Analysis")
    print("=" * 60)

    # Generate sample cycling session
    df = generate_sample_cycling_session()

    # Athlete data
    athlete_data = {
        "ftp": 280,
        "max_hr": 195,
        "weight_kg": 75,
        "sport": "cycling",
    }

    # Create calculator and analyze
    calculator = MetricsCalculator(athlete_data)
    session = calculator.analyze_session(df)

    # Print summary
    print(f"\n--- Session Summary ---")
    print(f"Duration:          {session.duration_str}")
    print(f"Distance:          {session.distance_km:.1f} km")
    print(f"Avg Speed:         {session.avg_speed_kmh:.1f} km/h")
    print(f"Max Speed:         {session.max_speed_kmh:.1f} km/h")
    print(f"Elevation Gain:    {session.elevation_gain_m:.0f} m")
    print(f"Elevation Loss:    {session.elevation_loss_m:.0f} m")

    print(f"\n--- Heart Rate ---")
    print(f"Avg HR:            {session.avg_hr:.0f} bpm")
    print(f"Max HR:            {session.max_hr} bpm")
    print(f"Min HR:            {session.min_hr} bpm")

    print(f"\n--- Power Metrics ---")
    print(f"Avg Power:         {session.avg_power:.1f} W")
    print(f"Max Power:         {session.max_power:.1f} W")
    print(f"Normalized Power:  {session.normalized_power:.1f} W")
    print(f"FTP:               {session.ftp:.1f} W {'(estimated)' if session.ftp_estimated else '(user input)'}")
    print(f"Intensity Factor:  {session.intensity_factor:.2f}")
    print(f"TSS Score:         {session.tss:.1f}")

    print(f"\n--- Performance ---")
    print(f"VO2max Est.:       {session.vo2max:.1f} ml/kg/min")
    print(f"Avg Cadence:       {session.avg_cadence:.0f} rpm")

    return session


# ─────────────────────────────────────────────
# EXAMPLE 5: ZONE DISTRIBUTION
# ─────────────────────────────────────────────

def example_zone_distribution():
    """
    Example: Analyze time spent in each training zone
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 5: Zone Distribution Analysis")
    print("=" * 60)

    # Generate sample data
    df = generate_sample_cycling_session()

    athlete_data = {
        "ftp": 280,
        "max_hr": 195,
        "weight_kg": 75,
        "sport": "cycling",
    }

    calculator = MetricsCalculator(athlete_data)

    # Get zone distributions
    zones = calculator.get_zone_distribution(df, ftp=280)

    if "hr_zones" in zones and not zones["hr_zones"].empty:
        print(f"\n--- Heart Rate Zone Distribution ---")
        print(zones["hr_zones"].to_string(index=False))

    if "power_zones" in zones and not zones["power_zones"].empty:
        print(f"\n--- Power Zone Distribution ---")
        print(zones["power_zones"].to_string(index=False))


# ─────────────────────────────────────────────
# EXAMPLE 6: ELEVATION ANALYSIS
# ─────────────────────────────────────────────

def example_elevation_analysis():
    """
    Example: Elevation and climbing metrics
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 6: Elevation & Climbing Analysis")
    print("=" * 60)

    # Generate sample data
    df = generate_sample_cycling_session()

    # Calculate elevation metrics
    elev = calculate_elevation_metrics(df["altitude_m"])

    print(f"\n--- Elevation Metrics ---")
    print(f"Elevation Gain:    {elev['elevation_gain_m']:.0f} m")
    print(f"Elevation Loss:    {elev['elevation_loss_m']:.0f} m")

    # Altitude profile
    print(f"\n--- Altitude Profile ---")
    print(f"Min Altitude:      {df['altitude_m'].min():.0f} m")
    print(f"Max Altitude:      {df['altitude_m'].max():.0f} m")
    print(f"Avg Altitude:      {df['altitude_m'].mean():.0f} m")


# ─────────────────────────────────────────────
# EXAMPLE 7: RUNNING ANALYSIS
# ─────────────────────────────────────────────

def example_running_analysis():
    """
    Example: Running-specific metrics
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 7: Running Session Analysis")
    print("=" * 60)

    # Generate sample running data
    df = generate_sample_running_session()

    athlete_data = {
        "ftp": 0,  # Not applicable for running
        "max_hr": 195,
        "weight_kg": 75,
        "sport": "running",
    }

    calculator = MetricsCalculator(athlete_data)
    session = calculator.analyze_session(df)

    print(f"\n--- Running Metrics ---")
    print(f"Duration:          {session.duration_str}")
    print(f"Distance:          {session.distance_km:.1f} km")
    print(f"Avg Pace:          {session.avg_pace_str}")
    print(f"Best Pace:         {session.best_pace_str}")
    print(f"Avg Speed:         {session.avg_speed_kmh:.1f} km/h")

    print(f"\n--- Heart Rate ---")
    print(f"Avg HR:            {session.avg_hr:.0f} bpm")
    print(f"Max HR:            {session.max_hr} bpm")

    print(f"\n--- Cadence ---")
    print(f"Avg Cadence:       {session.avg_cadence:.0f} steps/min")
    print(f"SPM (Steps/min):   {session.spm:.0f}")

    print(f"\n--- Performance ---")
    print(f"Running Efficiency: {session.running_efficiency:.3f}")
    print(f"VO2max Est.:        {session.vo2max:.1f} ml/kg/min")


# ─────────────────────────────────────────────
# MAIN EXECUTION
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("FASTTIMES FIT ANALYSIS BACKEND - EXAMPLES")
    print("=" * 60)

    # Run all examples
    example_parse_fit_file()
    example_power_metrics()
    example_hr_vo2max()
    example_zone_distribution()
    example_elevation_analysis()
    example_complete_session_analysis()
    example_running_analysis()

    print("\n" + "=" * 60)
    print("All examples completed!")
    print("=" * 60 + "\n")
