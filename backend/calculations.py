"""
Low-level calculations module
Pure functions for metric calculations
"""

import math
import numpy as np
import pandas as pd
from typing import List, Tuple, Union


# ─────────────────────────────────────────────
# Power Metrics
# ─────────────────────────────────────────────

def normalized_power(power_series: pd.Series, window: int = 30) -> float:
    """
    Calculate Normalized Power (NP)

    Uses 30-second rolling window, then fourth-root mean calculation
    Formula: NP = (mean(power^4)) ^ 0.25

    Parameters
    ----------
    power_series : pd.Series
        Power values in watts
    window : int
        Rolling window size (default 30 seconds)

    Returns
    -------
    float
        Normalized power in watts
    """
    p = power_series.dropna()
    if p.empty:
        return 0.0

    p_rolled = p.rolling(window, min_periods=1).mean()
    np_value = float((p_rolled ** 4).mean() ** 0.25)
    return round(np_value, 1)


def estimate_ftp(power_series: pd.Series, method: str = "best_20min") -> float:
    """
    Estimate FTP (Functional Threshold Power)

    Uses best 20-minute power × 0.95

    Parameters
    ----------
    power_series : pd.Series
        Power values in watts
    method : str
        Estimation method: 'best_20min' or 'mean'

    Returns
    -------
    float
        Estimated FTP in watts
    """
    p = power_series.dropna()
    if p.empty:
        return 0.0

    if method == "best_20min":
        window = min(1200, len(p) - 1)  # 20 min = 1200 seconds
        if window < 60:
            return round(float(p.mean()), 1)
        return round(float(p.rolling(window).mean().max() * 0.95), 1)
    else:
        return round(float(p.mean()), 1)


def intensity_factor(normalized_power: float, ftp: float) -> float:
    """
    Calculate Intensity Factor (IF)

    IF = NP / FTP

    Parameters
    ----------
    normalized_power : float
        Normalized power in watts
    ftp : float
        FTP in watts

    Returns
    -------
    float
        Intensity factor (typically 0.5 - 2.0)
    """
    if ftp <= 0:
        return 0.0
    return round(normalized_power / ftp, 3)


def training_stress_score(
    duration_sec: float, normalized_power: float, ftp: float
) -> float:
    """
    Calculate Training Stress Score (TSS)

    TSS = (duration_sec × NP × IF) / (FTP × 3600) × 100

    Parameters
    ----------
    duration_sec : float
        Session duration in seconds
    normalized_power : float
        Normalized power in watts
    ftp : float
        FTP in watts

    Returns
    -------
    float
        Training stress score (typically 0 - 500+)
    """
    if ftp <= 0 or normalized_power <= 0:
        return 0.0

    if_ = intensity_factor(normalized_power, ftp)
    tss = (duration_sec * normalized_power * if_) / (ftp * 3600) * 100
    return round(tss, 1)


def power_zones(ftp: float) -> dict:
    """
    Generate power training zones (Coggan method)

    Based on percentage of FTP:
    - Z1: < 55% (Recovery)
    - Z2: 55-75% (Endurance)
    - Z3: 75-90% (Tempo)
    - Z4: 90-105% (Threshold)
    - Z5: 105-120% (VO2max)
    - Z6: > 120% (Anaerobic)

    Parameters
    ----------
    ftp : float
        FTP in watts

    Returns
    -------
    dict
        Zones mapping zone names to (min, max) tuples
    """
    if ftp <= 0:
        return {}

    return {
        "Z1 Recovery": (0, round(ftp * 0.55)),
        "Z2 Endurance": (round(ftp * 0.55), round(ftp * 0.75)),
        "Z3 Tempo": (round(ftp * 0.75), round(ftp * 0.90)),
        "Z4 Threshold": (round(ftp * 0.90), round(ftp * 1.05)),
        "Z5 VO2max": (round(ftp * 1.05), round(ftp * 1.20)),
        "Z6 Anaerobic": (round(ftp * 1.20), 9999),
    }


def time_in_power_zones(df: pd.DataFrame, ftp: float) -> pd.DataFrame:
    """
    Calculate time distribution across power zones

    Parameters
    ----------
    df : pd.DataFrame
        Record dataframe with 'power_w' column
    ftp : float
        FTP in watts

    Returns
    -------
    pd.DataFrame
        Zone distribution with columns: Zona, Segundos, Minutos, Porcentaje
    """
    if "power_w" not in df.columns or ftp <= 0:
        return pd.DataFrame()

    zones = power_zones(ftp)
    p = df["power_w"].dropna()
    total = len(p)

    if total == 0:
        return pd.DataFrame()

    rows = []
    for name, (lo, hi) in zones.items():
        count = int(((p >= lo) & (p < hi)).sum())
        rows.append({
            "Zone": name,
            "Seconds": count,
            "Minutes": round(count / 60, 1),
            "Percentage": round(count / total * 100, 1),
        })

    return pd.DataFrame(rows)


# ─────────────────────────────────────────────
# Heart Rate Metrics
# ─────────────────────────────────────────────

def hr_zones(max_hr: int) -> dict:
    """
    Generate HR training zones

    Based on percentage of max HR:
    - Z1: < 60% (Recovery)
    - Z2: 60-70% (Aerobic base)
    - Z3: 70-80% (Aerobic moderate)
    - Z4: 80-90% (Anaerobic threshold)
    - Z5: 90%+ (VO2max)

    Parameters
    ----------
    max_hr : int
        Maximum heart rate in bpm

    Returns
    -------
    dict
        Zones mapping zone names to (min, max) tuples
    """
    return {
        "Z1 Recovery": (0, round(max_hr * 0.60)),
        "Z2 Aerobic Base": (round(max_hr * 0.60), round(max_hr * 0.70)),
        "Z3 Aerobic Moderate": (round(max_hr * 0.70), round(max_hr * 0.80)),
        "Z4 Anaerobic Threshold": (round(max_hr * 0.80), round(max_hr * 0.90)),
        "Z5 VO2max": (round(max_hr * 0.90), max_hr + 1),
    }


def time_in_hr_zones(df: pd.DataFrame, max_hr: int) -> pd.DataFrame:
    """
    Calculate time distribution across HR zones

    Parameters
    ----------
    df : pd.DataFrame
        Record dataframe with 'hr' column
    max_hr : int
        Maximum heart rate in bpm

    Returns
    -------
    pd.DataFrame
        Zone distribution with columns: Zone, Seconds, Minutes, Percentage
    """
    if "hr" not in df.columns or max_hr <= 0:
        return pd.DataFrame()

    zones = hr_zones(max_hr)
    hr = df["hr"].dropna()
    total = len(hr)

    if total == 0:
        return pd.DataFrame()

    rows = []
    for name, (lo, hi) in zones.items():
        count = int(((hr >= lo) & (hr < hi)).sum())
        rows.append({
            "Zone": name,
            "Seconds": count,
            "Minutes": round(count / 60, 1),
            "Percentage": round(count / total * 100, 1),
        })

    return pd.DataFrame(rows)


def estimate_vo2max(
    avg_hr: float, max_hr: float, ftp: float = 0, weight_kg: float = 70
) -> float:
    """
    Estimate VO2max from heart rate and power data

    Uses two methods:
    1. Power-based (if FTP available): VO2max = (FTP / weight) × 10.8 + 7
    2. HR-based (fallback): VO2max = ((avg_hr / max_hr) - 0.37) / 0.634 × 100

    Parameters
    ----------
    avg_hr : float
        Average heart rate in bpm
    max_hr : float
        Maximum heart rate in bpm
    ftp : float
        FTP in watts (optional)
    weight_kg : float
        Body weight in kg (default 70)

    Returns
    -------
    float
        Estimated VO2max in ml/kg/min
    """
    if ftp > 0 and weight_kg > 0:
        return round((ftp / weight_kg) * 10.8 + 7, 1)

    if max_hr > 0 and 0 < avg_hr < max_hr:
        hr_r_pct = avg_hr / max_hr
        vo2 = (hr_r_pct - 0.37) / 0.634 * 100
        return round(max(20.0, min(90.0, vo2)), 1)

    return 0.0


def calculate_hrv_rmssd(rr_intervals: List[float]) -> float:
    """
    Calculate HRV (Heart Rate Variability) using RMSSD

    RMSSD = sqrt(mean(differences_between_rr_intervals^2))

    Parameters
    ----------
    rr_intervals : list
        R-R intervals in milliseconds

    Returns
    -------
    float
        RMSSD in milliseconds
    """
    if len(rr_intervals) < 2:
        return 0.0

    rr_array = np.array(rr_intervals)
    diffs = np.diff(rr_array)
    rmssd = float(math.sqrt(np.mean(diffs ** 2)))
    return round(rmssd, 2)


def running_efficiency(avg_speed_ms: float, avg_hr: float) -> float:
    """
    Calculate running efficiency factor

    EF = (speed × 60) / HR

    Parameters
    ----------
    avg_speed_ms : float
        Average speed in m/s
    avg_hr : float
        Average heart rate in bpm

    Returns
    -------
    float
        Efficiency factor
    """
    if avg_hr <= 0 or avg_speed_ms <= 0:
        return 0.0

    return round((avg_speed_ms * 60) / avg_hr, 3)


# ─────────────────────────────────────────────
# Elevation & Geography
# ─────────────────────────────────────────────

def calculate_elevation_metrics(altitude_series: pd.Series) -> dict:
    """
    Calculate elevation gain and loss

    Parameters
    ----------
    altitude_series : pd.Series
        Altitude values in meters

    Returns
    -------
    dict
        Dictionary with 'elevation_gain_m' and 'elevation_loss_m'
    """
    if altitude_series is None or altitude_series.empty:
        return {"elevation_gain_m": 0.0, "elevation_loss_m": 0.0}

    alt = altitude_series.dropna()
    if alt.empty:
        return {"elevation_gain_m": 0.0, "elevation_loss_m": 0.0}

    diff = alt.diff()
    gain = round(float(diff.clip(lower=0).sum()), 0)
    loss = round(float(diff.clip(upper=0).abs().sum()), 0)

    return {
        "elevation_gain_m": gain,
        "elevation_loss_m": loss,
    }


def calculate_vam(
    altitude_series: pd.Series, elapsed_sec: pd.Series
) -> float:
    """
    Calculate VAM (Velocidad Ascensional Media / Climbing speed)

    VAM = elevation_gain / time_in_hours

    Parameters
    ----------
    altitude_series : pd.Series
        Altitude values in meters
    elapsed_sec : pd.Series
        Elapsed time in seconds

    Returns
    -------
    float
        VAM in meters per hour
    """
    if (altitude_series is None or altitude_series.empty or
        elapsed_sec is None or elapsed_sec.empty):
        return 0.0

    alt = altitude_series.dropna()
    if alt.empty:
        return 0.0

    gain = alt.diff().clip(lower=0).sum()
    duration_hours = elapsed_sec.max() / 3600.0

    if duration_hours <= 0:
        return 0.0

    vam = gain / duration_hours
    return round(vam, 1)


# ─────────────────────────────────────────────
# Pace & Speed
# ─────────────────────────────────────────────

def calculate_pace_metrics(df: pd.DataFrame) -> dict:
    """
    Calculate pace/speed metrics

    Parameters
    ----------
    df : pd.DataFrame
        Record dataframe

    Returns
    -------
    dict
        Dictionary with pace and speed metrics
    """
    result = {}

    if "speed_kmh" in df.columns:
        spd = df["speed_kmh"].dropna()
        if not spd.empty:
            result["avg_speed_kmh"] = round(float(spd.mean()), 2)
            result["max_speed_kmh"] = round(float(spd.max()), 2)

    if "pace_min_km" in df.columns:
        pace = df["pace_min_km"].replace([np.inf, -np.inf], np.nan).dropna()
        if not pace.empty:
            result["avg_pace_min_km"] = round(float(pace.mean()), 2)
            result["best_pace_min_km"] = round(float(pace.min()), 2)

    return result


def pace_to_string(pace_decimal: float) -> str:
    """
    Convert decimal pace to MM:SS format

    Parameters
    ----------
    pace_decimal : float
        Pace in decimal minutes per km

    Returns
    -------
    str
        Formatted pace string "MM:SS /km"
    """
    if pace_decimal <= 0 or pd.isna(pace_decimal):
        return "N/A"

    minutes = int(pace_decimal)
    seconds = int((pace_decimal - minutes) * 60)
    return f"{minutes}:{seconds:02d} /km"


def seconds_to_hms(seconds: float) -> str:
    """
    Convert seconds to HH:MM:SS format

    Parameters
    ----------
    seconds : float
        Duration in seconds

    Returns
    -------
    str
        Formatted time string
    """
    h, r = divmod(int(seconds), 3600)
    m, sec = divmod(r, 60)
    return f"{h:02d}:{m:02d}:{sec:02d}"
