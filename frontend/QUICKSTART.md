# Quick Start Guide - Fasttimes Frontend

Get the Streamlit app running in 5 minutes.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A Garmin device or activity file (FIT format)

## Installation

### 1. Clone or Navigate to Project
```bash
cd "c:\Users\Noxie-PC\Documents\Claude\Projects\Generador de Informes de Rendimiento"
```

### 2. Create Virtual Environment
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies
```bash
cd frontend
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

## First Time Setup

### Step 1: Complete Your Athlete Profile
1. Fill in your name
2. Select your sport (Running, Cycling, Triathlon)
3. Choose your experience level
4. Enter your FTP (or leave at default)
5. Input your body weight
6. Specify your max and resting heart rate
7. Click "Save Profile"

**💡 Tip:** You can estimate FTP later - start with a rough estimate

### Step 2: Upload Your FIT File
1. Export a FIT file from Garmin Connect (see instructions in the app)
2. Drag the file onto the upload box or click to browse
3. Wait for validation (green checkmark = ready)

### Step 3: Generate Report
1. Click "Generate Performance Report"
2. Wait for analysis (usually 5-10 seconds)
3. Explore the charts and metrics

### Step 4: Download Your Report
1. Click "Generate PDF Report" to create a downloadable report
2. Or click "Export CSV Data" for raw data analysis

## How to Export FIT File from Garmin Connect

### Via Garmin Connect Web
1. Go to [Garmin Connect](https://connect.garmin.com/)
2. Log in with your credentials
3. Click **Activities** → **Workouts**
4. Find your workout
5. Click the **⋮ (three dots)** menu
6. Select **Export**
7. Choose **Export Original** (.FIT format)
8. Save the file
9. Upload to Fasttimes

### Via Garmin Device
1. Connect your Garmin device to your computer
2. Navigate to the GARMIN folder on the device
3. Open **Activities** folder
4. Find your latest activity (newest file)
5. Copy the `.fit` file
6. Paste to your computer
7. Upload to Fasttimes

## Common Issues & Solutions

### "File must be a .FIT file"
- Check file extension is `.fit` (not `.gpx` or `.csv`)
- Try exporting again from Garmin Connect
- Ensure you selected "Export Original"

### "Analysis fails" or "Error processing FIT file"
- File may be corrupted - try uploading a different activity
- Check that the activity has complete data (timestamps, heart rate, distance)
- Older Garmin devices may export incomplete data

### Form validation errors
- **Weight/HR:** Make sure values are reasonable (e.g., max HR 120-220)
- **FTP:** Can be 0 - app will estimate
- **Age:** Enter your age (12-100 range)

### Can't see the app
- App opens at `http://localhost:8501` - if not automatic, type this in browser
- Try `streamlit run app.py --logger.level=debug` for troubleshooting
- Restart Streamlit if you modified code: Press Ctrl+C and run again

### Slow performance
- Close other browser tabs to free memory
- Reduce data table size (only shows first 100 rows)
- Use a modern browser (Chrome, Firefox, Safari)

## Configuration

### Customize Colors
Edit `frontend/config.py`:
```python
COLOR_PRIMARY = "#c8ff00"       # Change this to your accent color
COLOR_SECONDARY = "#00bfff"     # Change secondary accent
COLOR_BACKGROUND = "#0a0a0f"    # Change dark background
```

### Add Form Fields
Edit `frontend/app.py` in the athlete profile form section:
```python
new_field = st.number_input("New Field", min_value=0, value=100)
st.session_state.athlete_profile["new_key"] = new_field
```

### Change File Upload Limit
Edit `frontend/config.py`:
```python
MAX_FILE_SIZE_MB = 100  # Change from 50 to 100MB
```

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Stop Streamlit server |
| `R` | Rerun app |
| `K` | Open command palette |
| `Tab` | Focus next form field |
| `Enter` | Submit form |

## Tips for Best Results

1. **Use Recent Activities:** Fresh data from your Garmin device gives best analysis
2. **Complete Profile:** Accurate FTP and max HR improve zone calculations
3. **Clear Browser Cache:** If charts don't update, clear cache and refresh
4. **Use Descriptive Names:** Save athlete names so reports are easy to identify

## Next Steps

### After Your First Report
1. Review the charts and KPIs
2. Compare with previous sessions
3. Export PDF for your coach
4. Adjust FTP if zones don't feel right

### Advanced Features
- Check `config.py` for zone customization
- Modify chart colors and styling in `app.py`
- Add custom metrics by extending the analysis

## Performance Benchmarks

| Task | Typical Time |
|------|--------------|
| File upload | <1 second |
| Profile save | <0.5 seconds |
| FIT analysis | 5-10 seconds |
| PDF generation | 10-15 seconds |
| CSV export | 2-3 seconds |

## Support & Troubleshooting

### Check Logs
```bash
streamlit run app.py --logger.level=debug
```

### Verify Installation
```bash
python -c "import streamlit; print(streamlit.__version__)"
python -c "import fitparse; print(fitparse.__version__)"
python -c "import plotly; print(plotly.__version__)"
```

### Report Issues
Check error messages in:
- **Browser console:** Press F12 → Console
- **Terminal output:** Check where Streamlit is running
- **Session state:** Check `st.session_state` for debug info

## Health Check Script

Copy and run this to verify setup:
```python
# verify_setup.py
import sys
import importlib

required_modules = ['streamlit', 'pandas', 'numpy', 'plotly', 'fitparse']

print("🔍 Checking Fasttimes dependencies...\n")
for module in required_modules:
    try:
        mod = importlib.import_module(module)
        version = getattr(mod, '__version__', 'unknown')
        print(f"✓ {module:12} v{version}")
    except ImportError:
        print(f"✗ {module:12} NOT INSTALLED")
        sys.exit(1)

print("\n✓ All dependencies installed!")
print("\nTo start the app, run:")
print("  streamlit run frontend/app.py")
```

## Next: Customization

Once running, check these files to customize:
- `config.py` - Colors, zones, limits
- `app.py` - Layout, charts, features
- `requirements.txt` - Dependencies

Enjoy analyzing your FIT files! 🚀
