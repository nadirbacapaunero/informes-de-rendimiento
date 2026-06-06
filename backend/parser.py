"""
FIT Parser Module
Extracts raw data from .fit files using fitparse library
"""

import io
import pandas as pd
from fitparse import FitFile
from typing import Union, BinaryIO, List


class FITParser:
    """Parser for Garmin FIT file format"""

    def __init__(self):
        self.raw_records = []
        self.df = None

    def parse(self, source: Union[str, BinaryIO]) -> pd.DataFrame:
        """
        Parse FIT file from file path or file-like object

        Parameters
        ----------
        source : str or file-like object
            Path to .fit file or file-like object (BytesIO)

        Returns
        -------
        pd.DataFrame
            DataFrame with record data from FIT file
        """
        # Load FIT file
        if hasattr(source, "read"):
            raw = source.read()
            if hasattr(source, "seek"):
                try:
                    source.seek(0)
                except Exception:
                    pass
            fitfile = FitFile(io.BytesIO(raw))
        else:
            fitfile = FitFile(source)

        # Extract all records
        self.raw_records = []
        for record in fitfile.get_messages("record"):
            row = {}
            for field in record:
                row[field.name] = field.value
            self.raw_records.append(row)

        # Convert to DataFrame
        self.df = pd.DataFrame(self.raw_records)
        self._normalize_columns()

        return self.df

    def _normalize_columns(self) -> None:
        """Normalize column names and data types"""
        if self.df is None or self.df.empty:
            return

        # Timestamp processing
        if "timestamp" in self.df.columns:
            self.df["timestamp"] = pd.to_datetime(self.df["timestamp"], utc=True)
            self.df = self.df.sort_values("timestamp").reset_index(drop=True)
            self.df["elapsed_sec"] = (
                self.df["timestamp"] - self.df["timestamp"].iloc[0]
            ).dt.total_seconds()

        # Distance normalization
        if "distance" in self.df.columns:
            self.df["distance_km"] = self.df["distance"] / 1000.0

        # Speed normalization
        if "speed" in self.df.columns:
            self.df["speed_kmh"] = self.df["speed"] * 3.6
            self.df["pace_min_km"] = self.df["speed"].apply(
                lambda s: 1000 / (s * 60) if s and s > 0 else None
            )

        # Heart rate normalization
        if "heart_rate" in self.df.columns:
            self.df["hr"] = self.df["heart_rate"]

        # Power normalization
        if "power" in self.df.columns:
            self.df["power_w"] = self.df["power"]

        # Cadence normalization
        if "cadence" in self.df.columns:
            self.df["cadence_rpm"] = self.df["cadence"]

        # Altitude normalization
        if "altitude" in self.df.columns:
            self.df["altitude_m"] = self.df["altitude"]

    def get_data(self) -> pd.DataFrame:
        """Get parsed DataFrame"""
        return self.df

    def get_session_type(self) -> str:
        """
        Infer session type from available metrics

        Returns
        -------
        str
            'cycling', 'running', 'multisport', or 'unknown'
        """
        if self.df is None or self.df.empty:
            return "unknown"

        has_power = "power_w" in self.df.columns and self.df["power_w"].notna().sum() > 100
        has_cadence = "cadence_rpm" in self.df.columns and self.df["cadence_rpm"].notna().sum() > 100

        if has_power and not has_cadence:
            return "cycling"
        elif not has_power and has_cadence:
            return "running"
        elif has_power and has_cadence:
            return "multisport"
        else:
            return "unknown"

    def get_time_range(self) -> tuple:
        """
        Get timestamp range of session

        Returns
        -------
        tuple
            (start_time, end_time) as pandas Timestamps
        """
        if self.df is None or self.df.empty or "timestamp" not in self.df.columns:
            return (None, None)

        return (self.df["timestamp"].min(), self.df["timestamp"].max())

    def get_lap_data(self) -> pd.DataFrame:
        """
        Extract lap/interval data from FIT file

        Returns
        -------
        pd.DataFrame
            Lap data with time, distance, avg/max metrics
        """
        if not hasattr(self, 'raw_records') or not self.raw_records:
            return pd.DataFrame()

        # Try to extract lap messages
        try:
            laps = []
            for record in self.raw_records:
                if 'lap' in str(record).lower():
                    laps.append(record)

            if laps:
                return pd.DataFrame(laps)
        except Exception:
            pass

        return pd.DataFrame()


def parse_fit_file(source: Union[str, BinaryIO]) -> pd.DataFrame:
    """
    Standalone function to parse FIT file

    Parameters
    ----------
    source : str or file-like
        Path to .fit file or file-like object

    Returns
    -------
    pd.DataFrame
        Parsed record data
    """
    parser = FITParser()
    return parser.parse(source)
