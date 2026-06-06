"""
Metrics Calculator Module
High-level metrics aggregation and session analysis
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict

from .calculations import (
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
    calculate_vam,
    calculate_pace_metrics,
    pace_to_string,
    seconds_to_hms,
)


@dataclass
class SessionSummary:
    """Summary metrics for entire session"""

    # Duration & Distance
    duration_sec: float
    duration_str: str
    distance_km: float

    # Heart Rate
    avg_hr: float
    max_hr: float
    min_hr: float

    # Speed / Pace
    avg_speed_kmh: float
    max_speed_kmh: float
    avg_pace_str: str
    best_pace_str: str

    # Power (if available)
    has_power: bool
    avg_power: float = 0.0
    max_power: float = 0.0
    normalized_power: float = 0.0

    # Training metrics
    ftp: float = 0.0
    ftp_estimated: bool = False
    intensity_factor: float = 0.0
    tss: float = 0.0
    vo2max: float = 0.0

    # Elevation
    elevation_gain_m: float = 0.0
    elevation_loss_m: float = 0.0

    # Cadence
    avg_cadence: float = 0.0
    spm: float = 0.0  # Steps per minute (running)

    # Efficiency
    running_efficiency: float = 0.0

    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return asdict(self)


@dataclass
class LapMetrics:
    """Metrics for a single lap/interval"""

    lap_number: int
    duration_sec: float
    duration_str: str
    distance_km: float

    avg_hr: float
    max_hr: float

    avg_power: float = 0.0
    max_power: float = 0.0

    avg_speed_kmh: float = 0.0
    avg_pace_str: str = ""

    elevation_gain_m: float = 0.0

    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return asdict(self)


class MetricsCalculator:
    """Main metrics calculation engine"""

    def __init__(self, athlete_data: Optional[Dict] = None):
        """
        Initialize metrics calculator

        Parameters
        ----------
        athlete_data : dict, optional
            Athlete parameters with keys:
            - ftp: FTP in watts (if known)
            - max_hr: Maximum heart rate in bpm (default 190)
            - weight_kg: Body weight in kg (default 70)
            - sport: 'cycling', 'running', or 'multisport'
        """
        self.athlete_data = athlete_data or {}
        self.ftp_input = self.athlete_data.get("ftp", 0)
        self.max_hr = self.athlete_data.get("max_hr", 190)
        self.weight_kg = self.athlete_data.get("weight_kg", 70)
        self.sport = self.athlete_data.get("sport", "cycling")

    def analyze_session(self, df: pd.DataFrame) -> SessionSummary:
        """
        Analyze complete training session

        Parameters
        ----------
        df : pd.DataFrame
            Record dataframe from FIT parser

        Returns
        -------
        SessionSummary
            Complete session metrics
        """
        # Duration
        duration_sec = float(df["elapsed_sec"].max()) if "elapsed_sec" in df.columns else 0.0
        duration_str = seconds_to_hms(duration_sec)

        # Distance
        distance_km = round(float(df["distance_km"].max()), 2) if "distance_km" in df.columns else 0.0

        # Heart rate
        avg_hr = 0.0
        max_hr = 0.0
        min_hr = 0.0
        if "hr" in df.columns:
            hr = df["hr"].dropna()
            if not hr.empty:
                avg_hr = round(float(hr.mean()), 0)
                max_hr = int(hr.max())
                min_hr = int(hr.min())

        # Speed / Pace
        avg_speed_kmh = 0.0
        max_speed_kmh = 0.0
        avg_pace_str = "N/A"
        best_pace_str = "N/A"

        pace_metrics = calculate_pace_metrics(df)
        avg_speed_kmh = pace_metrics.get("avg_speed_kmh", 0.0)
        max_speed_kmh = pace_metrics.get("max_speed_kmh", 0.0)

        if "pace_min_km" in df.columns:
            pace = df["pace_min_km"].replace([np.inf, -np.inf], np.nan).dropna()
            if not pace.empty:
                avg_pace_str = pace_to_string(float(pace.mean()))
                best_pace_str = pace_to_string(float(pace.min()))

        # Power analysis
        has_power = ("power_w" in df.columns and
                    df["power_w"].dropna().shape[0] > 60)
        avg_power = 0.0
        max_power = 0.0
        np_value = 0.0
        ftp = self.ftp_input
        intensity_fact = 0.0
        tss_value = 0.0
        ftp_estimated = False

        if has_power:
            p = df["power_w"].dropna()
            avg_power = round(float(p.mean()), 1)
            max_power = round(float(p.max()), 1)
            np_value = normalized_power(df["power_w"])

            ftp = ftp if ftp > 0 else estimate_ftp(df["power_w"])
            ftp_estimated = self.ftp_input == 0

            intensity_fact = intensity_factor(np_value, ftp)
            tss_value = training_stress_score(duration_sec, np_value, ftp)

        # VO2max
        vo2max = estimate_vo2max(avg_hr, self.max_hr, ftp, self.weight_kg)

        # Elevation
        elev_metrics = calculate_elevation_metrics(
            df["altitude_m"] if "altitude_m" in df.columns else None
        )
        elevation_gain_m = elev_metrics["elevation_gain_m"]
        elevation_loss_m = elev_metrics["elevation_loss_m"]

        # Cadence
        avg_cadence = 0.0
        spm = 0.0
        if "cadence_rpm" in df.columns:
            cad = df["cadence_rpm"].dropna()
            if not cad.empty:
                avg_cadence = round(float(cad.mean()), 0)
                if self.sport == "running":
                    spm = round(float(cad.mean()) * 2, 0)

        # Running efficiency
        running_eff = 0.0
        if avg_speed_kmh > 0 and avg_hr > 0 and self.sport == "running":
            from .calculations import running_efficiency
            running_eff = running_efficiency(avg_speed_kmh / 3.6, avg_hr)

        return SessionSummary(
            duration_sec=duration_sec,
            duration_str=duration_str,
            distance_km=distance_km,
            avg_hr=avg_hr,
            max_hr=max_hr,
            min_hr=min_hr,
            avg_speed_kmh=avg_speed_kmh,
            max_speed_kmh=max_speed_kmh,
            avg_pace_str=avg_pace_str,
            best_pace_str=best_pace_str,
            has_power=has_power,
            avg_power=avg_power,
            max_power=max_power,
            normalized_power=np_value,
            ftp=ftp,
            ftp_estimated=ftp_estimated,
            intensity_factor=intensity_fact,
            tss=tss_value,
            vo2max=vo2max,
            elevation_gain_m=elevation_gain_m,
            elevation_loss_m=elevation_loss_m,
            avg_cadence=avg_cadence,
            spm=spm,
            running_efficiency=running_eff,
        )

    def get_hr_zones(self) -> dict:
        """Get HR zones for athlete"""
        return hr_zones(self.max_hr)

    def get_power_zones(self, ftp: float) -> dict:
        """Get power zones for given FTP"""
        return power_zones(ftp)

    def get_zone_distribution(self, df: pd.DataFrame, ftp: float = 0) -> Dict[str, pd.DataFrame]:
        """
        Get time distribution across all zones

        Parameters
        ----------
        df : pd.DataFrame
            Record dataframe
        ftp : float
            FTP value (for power zones)

        Returns
        -------
        dict
            Dictionary with 'hr_zones' and 'power_zones' DataFrames
        """
        result = {}

        # HR zones
        hr_zones_df = time_in_hr_zones(df, self.max_hr)
        result["hr_zones"] = hr_zones_df

        # Power zones
        if ftp > 0 and "power_w" in df.columns:
            power_zones_df = time_in_power_zones(df, ftp)
            result["power_zones"] = power_zones_df

        return result

    def analyze_laps(self, df: pd.DataFrame) -> List[LapMetrics]:
        """
        Analyze metrics per lap/split

        Parameters
        ----------
        df : pd.DataFrame
            Record dataframe

        Returns
        -------
        list
            List of LapMetrics objects
        """
        if "elapsed_sec" not in df.columns:
            return []

        # Detect lap boundaries (simple method: group by distance intervals)
        # More sophisticated: look for explicit lap markers in FIT file
        laps = []

        # For now, return empty list - implement lap detection if available
        # in raw FIT data

        return laps

    def calculate_zone_percentages(self, df: pd.DataFrame, ftp: float = 0) -> dict:
        """
        Get simple zone distribution as percentages

        Parameters
        ----------
        df : pd.DataFrame
            Record dataframe
        ftp : float
            FTP (optional, for power zones)

        Returns
        -------
        dict
            Dictionary mapping zone names to percentage time
        """
        result = {}

        # HR zones
        hr_zones_df = time_in_hr_zones(df, self.max_hr)
        if not hr_zones_df.empty:
            for _, row in hr_zones_df.iterrows():
                result[row["Zone"]] = row["Percentage"]

        # Power zones
        if ftp > 0 and "power_w" in df.columns:
            power_zones_df = time_in_power_zones(df, ftp)
            if not power_zones_df.empty:
                for _, row in power_zones_df.iterrows():
                    result[row["Zone"]] = row["Percentage"]

        return result

    def get_key_metrics(self, session_summary: SessionSummary) -> dict:
        """
        Extract most important metrics

        Parameters
        ----------
        session_summary : SessionSummary
            Complete session summary

        Returns
        -------
        dict
            Dictionary with key metrics
        """
        return {
            "duration_str": session_summary.duration_str,
            "distance_km": session_summary.distance_km,
            "avg_hr": session_summary.avg_hr,
            "max_hr": session_summary.max_hr,
            "avg_speed_kmh": session_summary.avg_speed_kmh,
            "max_speed_kmh": session_summary.max_speed_kmh,
            "avg_pace_str": session_summary.avg_pace_str,
            "elevation_gain_m": session_summary.elevation_gain_m,
            "normalized_power": session_summary.normalized_power,
            "ftp": session_summary.ftp,
            "tss": session_summary.tss,
            "vo2max": session_summary.vo2max,
            "avg_cadence": session_summary.avg_cadence,
            "spm": session_summary.spm,
            "running_efficiency": session_summary.running_efficiency,
        }

    def export_summary(self, session_summary: SessionSummary) -> dict:
        """
        Export complete session as dictionary

        Parameters
        ----------
        session_summary : SessionSummary
            Session summary object

        Returns
        -------
        dict
            Complete session data
        """
        return session_summary.to_dict()
