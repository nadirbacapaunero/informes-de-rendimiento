"""
Fasttimes Backend — FIT File Analysis Module
Performance metrics calculation and data processing
"""

from .parser import FITParser, parse_fit_file
from .metrics import MetricsCalculator
from .calculations import (
    normalized_power,
    estimate_ftp,
    intensity_factor,
    training_stress_score,
    estimate_vo2max,
    calculate_hrv_rmssd,
    running_efficiency,
)

__all__ = [
    'FITParser',
    'parse_fit_file',
    'MetricsCalculator',
    'normalized_power',
    'estimate_ftp',
    'intensity_factor',
    'training_stress_score',
    'estimate_vo2max',
    'calculate_hrv_rmssd',
    'running_efficiency',
]
