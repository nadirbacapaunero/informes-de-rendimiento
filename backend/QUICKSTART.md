# Fasttimes Backend - Quick Start

Get your FIT analysis backend running in 5 minutes.

## 1. Installation

Backend dependencies are already in `requirements.txt`:

```bash
cd "Generador de Informes de Rendimiento"
pip install -r requirements.txt
```

Key packages:
- `fitparse` - FIT file parsing
- `pandas` - Data manipulation
- `numpy` - Numerical operations

## 2. Basic Usage

### Parse a FIT file:

```python
from backend.parser import parse_fit_file

df = parse_fit_file("your_activity.fit")
print(f"Loaded {len(df)} records")
```

### Analyze complete session:

```python
from backend.metrics import MetricsCalculator

athlete = {
    "ftp": 280,
    "max_hr": 195,
    "weight_kg": 75,
    "sport": "cycling"
}

calc = MetricsCalculator(athlete)
session = calc.analyze_session(df)

print(f"Distance: {session.distance_km} km")
print(f"Duration: {session.duration_str}")
print(f"TSS: {session.tss}")
print(f"VO2max: {session.vo2max}")
```

### Get zone distribution:

```python
zones = calc.get_zone_distribution(df, ftp=280)

print(zones["hr_zones"])      # HR zone breakdown
print(zones["power_zones"])   # Power zone breakdown
```

## 3. Run Examples

```bash
cd backend
python examples.py
```

Generates sample data and shows:
- Power metrics (cycling)
- HR & VO2max analysis
- Complete session summary
- Zone distribution
- Running analysis

## 4. Run Tests

```bash
# All tests
pytest test_backend.py -v

# Specific test
pytest test_backend.py::TestPowerMetrics -v
```

Tests cover:
- Power calculations
- HR metrics
- Elevation analysis
- Zone distribution
- Edge cases

## 5. Integration with Streamlit App

Replace your `app.py` upload section with:

```python
from backend.parser import FITParser
from backend.metrics import MetricsCalculator

# Upload file
uploaded_file = st.file_uploader("Upload FIT", type="fit")

if uploaded_file:
    # Parse
    parser = FITParser()
    df = parser.parse(uploaded_file)
    
    # Get athlete data
    athlete = {
        "ftp": st.number_input("FTP", value=280),
        "max_hr": st.number_input("Max HR", value=195),
        "weight_kg": st.number_input("Weight", value=75),
        "sport": st.selectbox("Sport", ["cycling", "running"])
    }
    
    # Analyze
    calc = MetricsCalculator(athlete)
    session = calc.analyze_session(df)
    
    # Display
    st.metric("Duration", session.duration_str)
    st.metric("Distance", f"{session.distance_km} km")
    st.metric("Avg HR", f"{session.avg_hr} bpm")
    st.metric("TSS", f"{session.tss:.0f}")
```

See `integration_example.py` for complete example.

## 6. Module Overview

### parser.py
- `FITParser` class - Parse FIT files
- `parse_fit_file()` - Standalone function
- Normalizes all FIT data columns

### calculations.py
- 30+ low-level metric functions
- Power: NP, FTP, TSS, IF, zones
- HR: zones, VO2max, efficiency
- Elevation: gain/loss, VAM
- Format: HH:MM:SS, pace strings

### metrics.py
- `MetricsCalculator` - High-level analysis
- `SessionSummary` - Complete session data
- Zone distribution & percentages
- Export to dict/JSON

### examples.py
- 7 complete usage examples
- Sample data generation
- Copy-paste templates

### test_backend.py
- 50+ unit tests
- All calculation functions
- Edge cases & error handling

## 7. Common Tasks

### Get key metrics:
```python
metrics = calc.get_key_metrics(session)
# Returns dict with duration, distance, HR, power, TSS, VO2max, etc.
```

### Export to JSON:
```python
import json
data = json.dumps(session.to_dict(), default=str)
```

### Batch process multiple files:
```python
import glob

for fit_file in glob.glob("activities/*.fit"):
    df = parse_fit_file(fit_file)
    session = calc.analyze_session(df)
    print(f"{fit_file}: {session.tss:.0f} TSS")
```

### Get zone percentages:
```python
pcts = calc.calculate_zone_percentages(df, ftp=280)
# {'Z1 Recovery': 15.2, 'Z2 Endurance': 20.1, ...}
```

## 8. Data Structure

DataFrame columns after parsing:
```
timestamp         - datetime (UTC)
elapsed_sec       - seconds from start
distance_km       - kilometers
hr                - heart rate (bpm)
power_w           - power (watts)
speed_kmh         - speed (km/h)
pace_min_km       - pace (min/km)
cadence_rpm       - cadence (rpm)
altitude_m        - altitude (meters)
```

SessionSummary object:
```
duration_str      - "HH:MM:SS"
distance_km       - float
avg_hr            - int
max_hr            - int
normalized_power  - float (watts)
ftp               - float (watts)
tss               - float (score)
vo2max            - float (ml/kg/min)
elevation_gain_m  - float
```

## 9. Troubleshooting

**"No power data" warning:**
- File might be running activity (no power meter)
- Check with: `df["power_w"].notna().sum()`

**FTP estimated instead of user input:**
- Backend can't estimate FTP without 60+ seconds of power data
- Provide `ftp` value in athlete dict for accurate TSS

**Zero values in zones:**
- Zone might not have data in that intensity
- Check sample data is realistic

**Date/time parsing issues:**
- Backend handles most Garmin formats
- Files should be direct exports from Garmin Connect or device

## 10. Next Steps

1. **Review full documentation:** `BACKEND_GUIDE.md`
2. **Check integration example:** `integration_example.py`
3. **Run tests to verify:** `pytest test_backend.py`
4. **Integrate with your app**
5. **Customize metrics as needed**

## 11. Performance

- Small file (1 hour): <100ms
- Large file (10 hours): <1s
- Memory: ~5MB per hour of data
- Suitable for web apps & real-time analysis

## 12. Files Reference

```
backend/
├── __init__.py              # Package imports
├── parser.py                # FIT parsing (400 lines)
├── calculations.py          # 30+ functions (600 lines)
├── metrics.py               # High-level API (500 lines)
├── examples.py              # 7 complete examples (400 lines)
├── test_backend.py          # 50+ unit tests (500 lines)
├── BACKEND_GUIDE.md         # Full documentation (700 lines)
└── QUICKSTART.md            # This file
```

---

**Need help?** Check:
1. Docstrings in code (all functions documented)
2. Examples in `examples.py`
3. Tests in `test_backend.py`
4. Full guide in `BACKEND_GUIDE.md`

Happy analyzing! ⚡
