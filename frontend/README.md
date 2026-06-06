# Fasttimes FIT Analysis Frontend

Professional Streamlit application for analyzing Garmin FIT files and generating performance reports.

## Features

### 1. **File Upload Section**
- Drag-and-drop FIT file uploader with validation
- File type and size verification (max 50MB)
- Clear upload instructions with Garmin Connect export guide
- Real-time file preview with metadata

### 2. **User Profile Form**
- **Required Fields:**
  - Athlete name
  - Sport (Running, Cycling, Triathlon)
  - Experience level (Beginner, Intermediate, Advanced)
  - FTP (Functional Threshold Power in watts)
  - Body weight (kg)
  - Maximum heart rate (bpm)
  - Resting heart rate (bpm)

- **Optional Fields:**
  - Age
  - Gender
  - Training goal (General Fitness, Build Endurance, Improve Speed, Race Prep, Recovery)

- **Form Validation:**
  - Required field checks
  - Range validation for all numeric inputs
  - Session state persistence

### 3. **Report Generation**
- Single-click "Generate Report" button
- Real-time loading indicator with spinner
- Disabled state when file or profile is incomplete
- Graceful error handling with user-friendly messages

### 4. **Performance Analysis & Visualization**
- **Summary Metrics (KPIs):**
  - Total distance
  - Session duration
  - Average/max heart rate
  - Average/max power output

- **Interactive Charts:**
  - **HR Zone Distribution:** Donut chart showing time in each heart rate zone
  - **Power Distribution:** Bar chart by power zone (if power data available)
  - **Pace Timeline:** Line chart showing pace progression throughout session
  - **Session Details:** Scrollable data table with 100+ data points

### 5. **Export Options**
- **PDF Report:** Download complete analysis as professional PDF
- **CSV Export:** Raw session data for further analysis

### 6. **Professional Design**
- Dark theme with lime green (#c8ff00) accents
- Responsive column layouts (adaptable to mobile)
- Clear visual hierarchy and spacing
- Smooth transitions and hover effects
- Accessible color contrast (WCAG AA standard)
- Professional typography with semantic sizing

## Installation

### Requirements
- Python 3.8 or higher
- pip package manager

### Setup

1. **Create virtual environment:**
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate      # macOS/Linux
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Copy parent modules (if needed):**
```bash
# Ensure analyzer.py and pdf_generator.py are accessible
# from the parent directory
```

## Usage

### Running the Application

```bash
streamlit run frontend/app.py
```

The app will open at `http://localhost:8501`

### Workflow

1. **Complete Your Profile:**
   - Fill in athlete name, sport, and experience level
   - Enter FTP and body weight
   - Input max HR and resting HR
   - (Optional) Add age, gender, and training goal
   - Click "Save Profile"

2. **Upload FIT File:**
   - Drag FIT file onto uploader or click to browse
   - File validation occurs automatically
   - Instructions available for exporting from Garmin Connect

3. **Generate Report:**
   - Click "Generate Performance Report" button
   - Wait for analysis to complete
   - System displays loading spinner during processing

4. **Review Results:**
   - View KPIs summary
   - Explore charts using tab navigation
   - Check detailed session data table
   - Download PDF or CSV as needed

## File Structure

```
frontend/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Architecture

### Components

#### Page Configuration
- Wide layout for optimal data visualization
- Expanded sidebar state
- Custom favicon and page title

#### Session State Management
- `uploaded_file`: Stores FIT file object
- `analysis_complete`: Boolean flag for analysis status
- `fit_data`: Parsed FIT data as DataFrame
- `athlete_profile`: Dictionary with athlete information

#### Styling System
```python
- COLOR_PRIMARY = "#c8ff00"      # Lime green
- COLOR_SECONDARY = "#00bfff"    # Cyan
- COLOR_BACKGROUND = "#0a0a0f"   # Dark charcoal
- COLOR_SURFACE = "#15151e"      # Card backgrounds
- COLOR_BORDER = "#2a2a3d"       # Subtle borders
```

#### Helper Functions

**`validate_fit_file(file) -> tuple[bool, str]`**
- Validates file type and size
- Returns validation status and message

**`estimate_ftp(age, max_hr, weight_kg) -> int`**
- Estimates FTP from athlete metrics
- Uses age adjustment factor

**`create_hr_zones_chart(hr_zones_data) -> go.Figure`**
- Creates interactive donut chart
- Shows time distribution across HR zones

**`create_power_distribution_chart(power_data) -> go.Figure`**
- Bar chart of power zone distribution
- Color-coded by zone intensity

**`create_pace_timeline_chart(pace_data) -> go.Figure`**
- Line chart with fill for pace progression
- Interactive hover tooltips

## Key Design Decisions

### UX/UI
1. **Form-First Design:** Profile input before file upload reduces confusion
2. **Progressive Disclosure:** Optional fields collapsed under "Optional Information"
3. **Visual Feedback:** Status badges, color changes, hover effects for interactivity
4. **Responsive Layout:** Column-based design adapts to screen size
5. **Clear Hierarchy:** Section titles with accent bars guide attention

### Performance
1. **Session State Caching:** Profile and file data cached to prevent recomputation
2. **Lazy Loading:** Charts generated on-demand via tabs
3. **Data Slicing:** Large datasets limited to 100 rows in table view
4. **Efficient Validation:** Early returns on validation checks

### Error Handling
1. **Graceful Degradation:** Missing data doesn't crash app
2. **User-Friendly Messages:** Technical errors translated to actionable guidance
3. **Try-Catch Blocks:** PDF and CSV export wrapped with error recovery
4. **Disabled States:** Buttons disabled until prerequisites met

## Styling Reference

### CSS Classes
- `.metric-card` - KPI card styling with hover effect
- `.metric-value` - Large numeric display (lime green)
- `.metric-label` - Small label text (muted gray)
- `.section-title` - Section heading with accent bar
- `.alert-success` - Green success message
- `.alert-error` - Red error message
- `.alert-info` - Blue info message
- `.status-badge` - Inline status indicator
- `.status-complete` - Green status
- `.status-pending` - Blue status

### Responsive Breakpoints
- Mobile: Single column layout (default)
- Tablet: Two-column form/upload layout
- Desktop: Full width with multiple columns per section

## Integration with Backend

The frontend expects the following modules from the parent directory:

```python
# analyzer.py
parse_fit_file(file) -> pd.DataFrame
analyze_session(df, athlete_data) -> dict
time_in_hr_zones(df, athlete_data) -> dict
time_in_power_zones(df, athlete_data) -> dict
hr_zones: dict
power_zones: dict

# pdf_generator.py
generate_session_pdf(athlete_data, session_data, **kwargs) -> bytes
```

## Customization

### Colors
Modify the color constants at the top of `app.py`:
```python
COLOR_PRIMARY = "#c8ff00"      # Change primary accent
COLOR_SECONDARY = "#00bfff"    # Change secondary accent
COLOR_BACKGROUND = "#0a0a0f"   # Change dark background
```

### Form Fields
Add/remove fields by modifying the profile form in the left column:
```python
new_field = st.number_input("Field Label", ...)
st.session_state.athlete_profile["key"] = new_field
```

### Charts
Replace or extend chart functions to add new visualizations:
```python
def create_custom_chart(data) -> go.Figure:
    fig = go.Figure(...)
    fig.update_layout(...)
    return fig
```

## Troubleshooting

### FIT File Not Recognized
- Ensure file is `.FIT` extension (case-insensitive)
- File must be valid Garmin FIT format
- Try re-exporting from Garmin Connect

### Analysis Fails
- Check that `analyzer.py` is in parent directory
- Verify FIT file has required data fields
- Check console for detailed error messages

### PDF Export Error
- Ensure `pdf_generator.py` is in parent directory
- Check that fpdf2 is installed: `pip install fpdf2`

### Charts Not Displaying
- Verify plotly is installed: `pip install plotly`
- Check that data columns match expected format
- Review browser console for JavaScript errors

## Performance Notes

- App handles files up to 50MB
- Data tables limit display to 100 rows (for performance)
- Charts use client-side rendering (Plotly)
- Session state prevents re-analysis on rerun

## Browser Support

- Chrome/Chromium: Full support
- Firefox: Full support
- Safari: Full support (iOS 12+)
- Edge: Full support

## Future Enhancements

- [ ] Multi-session comparison
- [ ] Training load tracking
- [ ] Peak performance analysis
- [ ] Workout recommendations
- [ ] Social sharing features
- [ ] Historical data trending
- [ ] Custom zone configuration
- [ ] Advanced metrics (TSS, IF, VI)

## License

Proprietary - Fasttimes Coaching

## Author

Nadir Baca Paunero  
Built with Streamlit · Python · Plotly
