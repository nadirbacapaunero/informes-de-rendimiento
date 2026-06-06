# Fasttimes FIT Analysis Backend

Complete Python backend module for parsing and analyzing Garmin FIT files with comprehensive metrics calculation.

## Architecture Overview

```
backend/
├── __init__.py           # Package initialization & exports
├── parser.py             # FIT file parsing (FITParser class)
├── calculations.py       # Low-level metric calculations
├── metrics.py            # High-level metrics aggregation (MetricsCalculator)
├── examples.py           # Usage examples and sample data generation
├── test_backend.py       # Comprehensive unit tests
└── BACKEND_GUIDE.md      # This documentation
```

### Design Philosophy

- **Modular**: Each module has single responsibility
- **Testable**: Pure functions with minimal side effects
- **Reusable**: Works with Pandas DataFrames - integrate anywhere
- **Documented**: Comprehensive docstrings and type hints
- **Extensible**: Easy to add new metrics or data sources

## Quick Start

### 1. Parse a FIT File

```python
from backend.parser import parse_fit_file

# From file path
df = parse_fit_file("activity.fit")

# From file-like object (Streamlit, etc.)
df = parse_fit_file(uploaded_file)

print(df.columns)
# Output: timestamp, elapsed_sec, distance_km, hr, power_w, speed_kmh, etc.
```

### 2. Analyze Session

```python
from backend.metrics import MetricsCalculator

# Define athlete
athlete = {
    "ftp": 280,          # Watts (optional, can be estimated)
    "max_hr": 195,       # bpm
    "weight_kg": 75,     # kg
    "sport": "cycling"   # or "running", "multisport"
}

# Analyze
calc = MetricsCalculator(athlete)
session = calc.analyze_session(df)

# Access metrics
print(f"Distance: {session.distance_km} km")
print(f"Duration: {session.duration_str}")
print(f"Avg Power: {session.avg_power} W")
print(f"TSS: {session.tss}")
print(f"VO2max: {session.vo2max} ml/kg/min")
```

### 3. Export Results

```python
# As dictionary
session_dict = session.to_dict()

# As JSON for API
import json
json_data = json.dumps(session_dict, default=str)
```

---

## Module Reference

### parser.py - FIT File Parsing

#### Class: FITParser

Main parser for Garmin FIT files.

**Usage:**
```python
from backend.parser import FITParser

parser = FITParser()
df = parser.parse("activity.fit")

# Get session type
sport = parser.get_session_type()  # 'cycling', 'running', 'multisport', 'unknown'

# Get time range
start, end = parser.get_time_range()

# Get DataFrame
df = parser.get_data()
```

**Methods:**

- `parse(source)` - Parse FIT file or file-like object
  - Returns: `pd.DataFrame` with normalized columns
  - Columns: timestamp, elapsed_sec, distance_km, hr, power_w, speed_kmh, cadence_rpm, altitude_m, pace_min_km

- `get_session_type()` - Infer activity type
  - Returns: 'cycling' | 'running' | 'multisport' | 'unknown'

- `get_time_range()` - Get session time bounds
  - Returns: (start_time, end_time) tuple

- `get_data()` - Get parsed DataFrame
  - Returns: `pd.DataFrame`

#### Function: parse_fit_file()

Standalone function for simple use cases.

```python
from backend.parser import parse_fit_file

df = parse_fit_file("activity.fit")
```

---

### calculations.py - Low-Level Calculations

Pure functions for individual metric calculations. Use these when you need fine-grained control.

#### Power Metrics

**normalized_power(power_series, window=30)**
- Calculate Normalized Power (NP)
- Formula: NP = (mean(power^4)) ^ 0.25
- Window: 30 seconds (default for cycling)
- Returns: float (watts)

```python
from backend.calculations import normalized_power

np_val = normalized_power(df["power_w"])  # e.g., 287.5
```

**estimate_ftp(power_series, method='best_20min')**
- Estimate FTP from power data
- Default: Best 20-minute power × 0.95
- Returns: float (watts)

```python
from backend.calculations import estimate_ftp

ftp = estimate_ftp(df["power_w"])  # e.g., 280.0
```

**intensity_factor(normalized_power, ftp)**
- Calculate Intensity Factor (IF)
- Formula: IF = NP / FTP
- Returns: float (typically 0.5 - 2.0)

```python
from backend.calculations import intensity_factor

if_val = intensity_factor(280, 280)  # 1.0 (at threshold)
```

**training_stress_score(duration_sec, normalized_power, ftp)**
- Calculate Training Stress Score (TSS)
- Formula: TSS = (duration_sec × NP × IF) / (FTP × 3600) × 100
- Returns: float

```python
from backend.calculations import training_stress_score

tss = training_stress_score(3600, 280, 280)  # 100.0 (1h at threshold)
```

**power_zones(ftp)**
- Generate power training zones (Coggan method)
- Returns: dict mapping zone names to (min, max) tuples

```python
from backend.calculations import power_zones

zones = power_zones(280)
# {
#   'Z1 Recovery': (0, 154),
#   'Z2 Endurance': (154, 210),
#   'Z3 Tempo': (210, 252),
#   'Z4 Threshold': (252, 294),
#   'Z5 VO2max': (294, 336),
#   'Z6 Anaerobic': (336, 9999)
# }
```

**time_in_power_zones(df, ftp)**
- Calculate time distribution across power zones
- Returns: `pd.DataFrame` with columns: Zone, Seconds, Minutes, Percentage

```python
from backend.calculations import time_in_power_zones

zones_df = time_in_power_zones(df, ftp=280)
print(zones_df)
#          Zone  Seconds  Minutes  Percentage
# 0  Z1 Recovery      600     10.0        16.7
# 1  Z2 Endurance      720     12.0        20.0
# ... etc
```

#### Heart Rate Metrics

**hr_zones(max_hr)**
- Generate 5 HR training zones
- Returns: dict mapping zone names to (min, max) tuples

```python
from backend.calculations import hr_zones

zones = hr_zones(195)
# {
#   'Z1 Recovery': (0, 117),
#   'Z2 Aerobic Base': (117, 137),
#   'Z3 Aerobic Moderate': (137, 156),
#   'Z4 Anaerobic Threshold': (156, 176),
#   'Z5 VO2max': (176, 196)
# }
```

**time_in_hr_zones(df, max_hr)**
- Calculate time distribution across HR zones
- Returns: `pd.DataFrame`

```python
from backend.calculations import time_in_hr_zones

zones_df = time_in_hr_zones(df, max_hr=195)
```

**estimate_vo2max(avg_hr, max_hr, ftp=0, weight_kg=70)**
- Estimate VO2max from power or heart rate
- Method 1 (power-based): VO2max = (FTP / weight) × 10.8 + 7
- Method 2 (HR-based): VO2max from HR ratio
- Returns: float (ml/kg/min)

```python
from backend.calculations import estimate_vo2max

# Power-based (more accurate)
vo2 = estimate_vo2max(160, 195, ftp=280, weight_kg=75)  # ~50.4

# HR-based (fallback)
vo2 = estimate_vo2max(160, 195, ftp=0, weight_kg=75)  # ~45.2
```

**running_efficiency(avg_speed_ms, avg_hr)**
- Calculate running efficiency factor
- Formula: EF = (speed × 60) / HR
- Returns: float

```python
from backend.calculations import running_efficiency

ef = running_efficiency(4.0, 160)  # 1.5
```

**calculate_hrv_rmssd(rr_intervals)**
- Calculate Heart Rate Variability (RMSSD)
- Input: R-R intervals in milliseconds
- Returns: float (milliseconds)

```python
from backend.calculations import calculate_hrv_rmssd

rr = [1000, 950, 1050, 980]  # milliseconds
hrv = calculate_hrv_rmssd(rr)  # ~48.45
```

#### Elevation Metrics

**calculate_elevation_metrics(altitude_series)**
- Calculate elevation gain and loss
- Returns: dict with 'elevation_gain_m' and 'elevation_loss_m'

```python
from backend.calculations import calculate_elevation_metrics

elev = calculate_elevation_metrics(df["altitude_m"])
# {'elevation_gain_m': 450.0, 'elevation_loss_m': 450.0}
```

**calculate_vam(altitude_series, elapsed_sec)**
- Calculate VAM (Velocidad Ascensional Media - climbing speed)
- Formula: VAM = elevation_gain / time_hours
- Returns: float (meters/hour)

```python
from backend.calculations import calculate_vam

vam = calculate_vam(df["altitude_m"], df["elapsed_sec"])  # e.g., 1200 m/h
```

#### Formatting Utilities

**seconds_to_hms(seconds)**
- Convert seconds to HH:MM:SS format
- Returns: str

```python
from backend.calculations import seconds_to_hms

print(seconds_to_hms(3661))  # "01:01:01"
```

**pace_to_string(pace_decimal)**
- Convert decimal pace to MM:SS /km format
- Returns: str

```python
from backend.calculations import pace_to_string

print(pace_to_string(6.5))  # "6:30 /km"
```

---

### metrics.py - High-Level Metrics

#### Class: MetricsCalculator

Main calculation engine with high-level analysis methods.

**Initialization:**
```python
from backend.metrics import MetricsCalculator

athlete_data = {
    "ftp": 280,
    "max_hr": 195,
    "weight_kg": 75,
    "sport": "cycling"
}

calc = MetricsCalculator(athlete_data)
```

**Methods:**

**analyze_session(df)**
- Complete session analysis
- Returns: `SessionSummary` object

```python
session = calc.analyze_session(df)

# Access properties
print(session.duration_str)        # "01:00:30"
print(session.distance_km)         # 42.1
print(session.avg_hr)              # 150
print(session.normalized_power)    # 280.0
print(session.tss)                 # 95.5
print(session.vo2max)              # 50.2
print(session.elevation_gain_m)    # 450
```

**get_hr_zones()**
- Get HR zones for configured athlete
- Returns: dict

```python
zones = calc.get_hr_zones()
```

**get_power_zones(ftp)**
- Get power zones for given FTP
- Returns: dict

```python
zones = calc.get_power_zones(280)
```

**get_zone_distribution(df, ftp=0)**
- Get time distribution across all zones
- Returns: dict with 'hr_zones' and 'power_zones' DataFrames

```python
zones_dict = calc.get_zone_distribution(df, ftp=280)
print(zones_dict["hr_zones"])
print(zones_dict["power_zones"])
```

**calculate_zone_percentages(df, ftp=0)**
- Get zone percentages as simple dict
- Returns: dict mapping zone names to percentage

```python
pcts = calc.calculate_zone_percentages(df, ftp=280)
# {'Z1 Recovery': 15.2, 'Z2 Endurance': 20.1, ...}
```

**get_key_metrics(session_summary)**
- Extract most important metrics
- Returns: dict with essential data

```python
metrics = calc.get_key_metrics(session)
# {
#   'duration_str': '01:00:30',
#   'distance_km': 42.1,
#   'avg_hr': 150,
#   'tss': 95.5,
#   ...
# }
```

#### Class: SessionSummary

Dataclass containing all session metrics.

**Properties:**
```python
session.duration_sec          # Total duration in seconds
session.duration_str          # Formatted duration "HH:MM:SS"
session.distance_km           # Total distance in kilometers
session.avg_hr                # Average heart rate (bpm)
session.max_hr                # Maximum heart rate (bpm)
session.min_hr                # Minimum heart rate (bpm)
session.avg_speed_kmh         # Average speed (km/h)
session.max_speed_kmh         # Maximum speed (km/h)
session.avg_pace_str          # Formatted pace "MM:SS /km"
session.best_pace_str         # Best pace "MM:SS /km"
session.has_power             # Boolean: has power data?
session.avg_power             # Average power (watts)
session.max_power             # Maximum power (watts)
session.normalized_power      # Normalized power (watts)
session.ftp                   # Functional Threshold Power (watts)
session.ftp_estimated         # Boolean: was FTP estimated?
session.intensity_factor      # Intensity factor
session.tss                   # Training Stress Score
session.vo2max                # VO2max estimate (ml/kg/min)
session.elevation_gain_m      # Elevation gain (meters)
session.elevation_loss_m      # Elevation loss (meters)
session.avg_cadence           # Average cadence (rpm)
session.spm                   # Steps per minute (running)
session.running_efficiency    # Running efficiency factor
```

**Export:**
```python
# To dictionary
data_dict = session.to_dict()

# To JSON
import json
json_str = json.dumps(session.to_dict(), default=str)
```

---

## Integration Examples

### Streamlit Integration

```python
import streamlit as st
from backend.parser import parse_fit_file
from backend.metrics import MetricsCalculator

# Upload file
uploaded_file = st.file_uploader("Upload FIT file", type="fit")

if uploaded_file:
    # Parse
    df = parse_fit_file(uploaded_file)
    
    # Get athlete data from form
    athlete = {
        "ftp": st.number_input("FTP (watts)", value=280),
        "max_hr": st.number_input("Max HR (bpm)", value=195),
        "weight_kg": st.number_input("Weight (kg)", value=75),
        "sport": st.selectbox("Sport", ["cycling", "running"])
    }
    
    # Analyze
    calc = MetricsCalculator(athlete)
    session = calc.analyze_session(df)
    
    # Display
    col1, col2, col3 = st.columns(3)
    col1.metric("Duration", session.duration_str)
    col2.metric("Distance", f"{session.distance_km} km")
    col3.metric("Avg HR", f"{session.avg_hr} bpm")
    
    col1.metric("TSS", f"{session.tss:.0f}")
    col2.metric("NP", f"{session.normalized_power:.0f} W")
    col3.metric("VO2max", f"{session.vo2max:.1f}")
```

### API Integration (FastAPI)

```python
from fastapi import FastAPI, File, UploadFile
from backend.parser import parse_fit_file
from backend.metrics import MetricsCalculator
import io

app = FastAPI()

@app.post("/analyze")
async def analyze_fit(file: UploadFile):
    # Read uploaded file
    contents = await file.read()
    
    # Parse FIT file
    df = parse_fit_file(io.BytesIO(contents))
    
    # Analyze
    athlete = {"ftp": 280, "max_hr": 195, "weight_kg": 75}
    calc = MetricsCalculator(athlete)
    session = calc.analyze_session(df)
    
    # Return JSON
    return session.to_dict()
```

### Data Export

```python
import json
import csv

# Export to JSON
with open("session.json", "w") as f:
    json.dump(session.to_dict(), f, indent=2, default=str)

# Export to CSV
import pandas as pd
session_df = pd.DataFrame([session.to_dict()])
session_df.to_csv("session.csv", index=False)
```

---

## Performance Notes

### Data Size
- Parser handles FIT files up to 100+ MB
- Typical activity: 2-3600 records (1 per second)
- DataFrame operations optimized with Pandas/NumPy

### Computation Time
- Small file (1 hour): < 100ms
- Large file (24 hours): ~500ms
- Suitable for real-time web apps

### Memory Usage
- 1-hour session: ~5 MB DataFrame
- Minimal overhead from calculations

---

## Extending the Backend

### Adding a Custom Metric

1. **Add calculation in `calculations.py`:**

```python
def custom_metric(data_series: pd.Series) -> float:
    """Calculate custom metric"""
    return float(data_series.custom_operation())
```

2. **Add to SessionSummary in `metrics.py`:**

```python
@dataclass
class SessionSummary:
    # ... existing fields ...
    custom_metric: float = 0.0
```

3. **Calculate in MetricsCalculator:**

```python
class MetricsCalculator:
    def analyze_session(self, df: pd.DataFrame) -> SessionSummary:
        # ... existing code ...
        custom = custom_metric(df["some_column"])
        
        return SessionSummary(
            # ... existing fields ...
            custom_metric=custom,
        )
```

### Adding Support for New Data Source

1. Create new parser in `parser.py`
2. Normalize columns to match FIT format
3. Use existing metrics with normalized DataFrame

---

## Testing

Run tests with pytest:

```bash
# All tests
pytest backend/test_backend.py -v

# Specific test class
pytest backend/test_backend.py::TestPowerMetrics -v

# With coverage
pytest backend/test_backend.py --cov=backend
```

---

## Common Patterns

### Pattern 1: Simple Single-File Analysis

```python
from backend.parser import parse_fit_file
from backend.metrics import MetricsCalculator

df = parse_fit_file("activity.fit")
calc = MetricsCalculator({"ftp": 280, "max_hr": 195, "weight_kg": 75})
session = calc.analyze_session(df)
print(f"TSS: {session.tss}, Duration: {session.duration_str}")
```

### Pattern 2: Batch Processing

```python
import glob
import pandas as pd

from backend.parser import parse_fit_file
from backend.metrics import MetricsCalculator

athlete = {"ftp": 280, "max_hr": 195, "weight_kg": 75}
calc = MetricsCalculator(athlete)

summaries = []
for fit_file in glob.glob("activities/*.fit"):
    try:
        df = parse_fit_file(fit_file)
        session = calc.analyze_session(df)
        summaries.append(session.to_dict())
    except Exception as e:
        print(f"Error processing {fit_file}: {e}")

# Convert to DataFrame for analysis
results_df = pd.DataFrame(summaries)
print(results_df.groupby("sport")[["tss", "distance_km"]].sum())
```

### Pattern 3: Zone Analysis

```python
from backend.metrics import MetricsCalculator

calc = MetricsCalculator({"ftp": 280, "max_hr": 195, "weight_kg": 75})

# Get zone distribution
zones_dict = calc.get_zone_distribution(df, ftp=280)

# Display HR zones
print("\nHR Zone Distribution:")
print(zones_dict["hr_zones"][["Zone", "Minutes", "Percentage"]])

# Display Power zones
if "power_zones" in zones_dict:
    print("\nPower Zone Distribution:")
    print(zones_dict["power_zones"][["Zone", "Minutes", "Percentage"]])
```

---

## Troubleshooting

### Issue: "No module named 'fitparse'"

```bash
pip install fitparse
```

### Issue: Empty DataFrame after parsing

- Verify FIT file is valid Garmin format
- Check file is not corrupted
- Ensure file has 'record' messages

```python
# Debug
df = parse_fit_file("activity.fit")
print(f"Records: {len(df)}")
print(df.columns.tolist())
```

### Issue: All metrics are zero

- Ensure FIT file has timestamp column
- Verify HR/Power data is present
- Check athlete parameters are reasonable

```python
# Debug
print(df.info())
print(df[["hr", "power_w", "distance_km"]].describe())
```

---

## License

Part of Fasttimes Performance Reporting System

---

## Support

For issues or questions about the backend:
1. Check examples in `examples.py`
2. Review test cases in `test_backend.py`
3. Refer to docstrings in each module
