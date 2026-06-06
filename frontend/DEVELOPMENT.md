# Development Guide

Best practices, architecture patterns, and maintenance guidelines for Fasttimes Frontend.

## Project Structure

```
frontend/
├── app.py                    # Main Streamlit application (production code)
├── config.py                 # Centralized configuration & constants
├── requirements.txt          # Python dependencies
├── README.md                 # User-facing documentation
├── QUICKSTART.md            # Getting started guide
├── STYLING_GUIDE.md         # Design system & CSS reference
└── DEVELOPMENT.md           # This file
```

## Architecture Overview

### Component Hierarchy

```
App (main page)
├── Page Config & Styling
├── Session State Initialization
├── Helper Functions
├── Main Layout
│   ├── Header
│   ├── Form Section (Left Column)
│   │   ├── Athlete Profile Form
│   │   └── Form State Management
│   ├── Upload Section (Right Column)
│   │   ├── File Uploader
│   │   ├── File Validation
│   │   └── Upload Instructions
│   ├── Report Generation
│   │   ├── Generate Button
│   │   └── Loading State
│   └── Results Section (Conditional)
│       ├── KPI Summary
│       ├── Chart Tabs
│       │   ├── HR Zones
│       │   ├── Power Distribution
│       │   ├── Pace Timeline
│       │   └── Session Details
│       └── Export Options
└── Footer
```

### Data Flow

```
User Input (Form)
    ↓
Session State Storage
    ↓
Form Validation
    ↓
File Upload
    ↓
File Validation
    ↓
FIT Parsing (analyzer.py)
    ↓
Analysis & Calculation
    ↓
Chart Generation (Plotly)
    ↓
Display Results
    ↓
Export (PDF/CSV)
```

## Session State Management

### State Variables

```python
st.session_state = {
    "uploaded_file": None,        # File object (Streamlit UploadedFile)
    "analysis_complete": bool,    # Flag: analysis finished
    "fit_data": None,            # DataFrame: parsed FIT data
    "athlete_profile": {},       # Dict: athlete information
}
```

### State Persistence

- Session state persists across reruns within same browser tab
- Cleared when user closes browser tab or manually clears cache
- Safe to store non-serializable objects (e.g., file objects)

### Best Practices

```python
# ✓ Good: Check and initialize
if "key" not in st.session_state:
    st.session_state.key = default_value

# ✓ Good: Update with validation
if is_valid(data):
    st.session_state.key = data

# ✗ Avoid: Direct mutation of nested dicts
st.session_state.profile["key"] = value  # May not trigger rerun properly

# ✓ Better: Reassign entire object
profile = st.session_state.profile.copy()
profile["key"] = value
st.session_state.profile = profile
```

## Form Handling

### Profile Form Pattern

```python
with st.form("form_id"):
    # Collect inputs
    field1 = st.text_input("Label")
    field2 = st.number_input("Label", min_value=0, max_value=100)
    
    # Submit button
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        # Validation
        if not field1:
            st.error("Field required")
        else:
            # Store to session state
            st.session_state.data = {
                "field1": field1,
                "field2": field2
            }
            st.success("Saved!")
```

### Validation Strategy

1. **Client-side validation** (immediate feedback)
   - Empty fields
   - Range checks
   - Type validation

2. **Form-level validation**
   - Check dependencies between fields
   - Validate against business rules

3. **File validation**
   - Type check (.fit extension)
   - Size check (< 50MB)
   - Content validation (valid FIT format)

## Chart Development

### Creating a New Chart

```python
def create_custom_chart(data: pd.DataFrame) -> go.Figure:
    """
    Create custom visualization.
    
    Args:
        data: DataFrame with required columns
        
    Returns:
        Plotly Figure object
    """
    fig = go.Figure(data=[
        go.Scatter(
            x=data['x_col'],
            y=data['y_col'],
            mode='lines+markers',
            name='Series 1',
            line=dict(color=COLOR_PRIMARY, width=2),
            hovertemplate='<b>%{x}</b><br>%{y:.1f}<extra></extra>'
        )
    ])
    
    fig.update_layout(
        title="Chart Title",
        xaxis_title="X Axis",
        yaxis_title="Y Axis",
        paper_bgcolor=COLOR_BACKGROUND,
        plot_bgcolor=COLOR_SURFACE,
        font=dict(color=COLOR_TEXT_SECONDARY),
        xaxis=dict(gridcolor=COLOR_BORDER),
        yaxis=dict(gridcolor=COLOR_BORDER),
        margin=dict(l=40, r=20, t=40, b=40),
        height=350,
        hovermode='x unified'
    )
    
    return fig
```

### Chart Best Practices

1. **Use consistent layout settings** (defined in config.py)
2. **Include interactive hover tooltips**
3. **Label axes clearly with units**
4. **Use theme colors consistently**
5. **Set appropriate height/width**
6. **Test with sample data**

## Testing Patterns

### Unit Test Example

```python
def test_validate_fit_file():
    """Test FIT file validation."""
    # Valid file
    is_valid, msg = validate_fit_file(mock_fit_file)
    assert is_valid == True
    
    # Invalid extension
    is_valid, msg = validate_fit_file(mock_csv_file)
    assert is_valid == False
    assert "must be a .FIT file" in msg
    
    # File too large
    is_valid, msg = validate_fit_file(mock_large_file)
    assert is_valid == False
    assert "exceeds" in msg
```

### Manual Testing Checklist

- [ ] Profile form validation
- [ ] File upload with various file types
- [ ] Report generation with real FIT data
- [ ] All charts render without errors
- [ ] Export buttons work
- [ ] Responsive layout on mobile/tablet/desktop
- [ ] Dark mode contrast verified
- [ ] Error messages display correctly
- [ ] Session state persists on rerun
- [ ] Performance acceptable (< 5s for analysis)

## Performance Optimization

### Current Performance

| Operation | Time | Optimization |
|-----------|------|--------------|
| File upload | <1s | Already optimized |
| Profile save | <0.5s | Session state caching |
| FIT parsing | 5-10s | Depends on file size |
| Chart generation | <1s | Client-side Plotly |
| PDF export | 10-15s | Requires pdf_generator |

### Optimization Techniques

#### 1. Session State Caching
```python
# Don't reparse if already in state
if st.session_state.fit_data is not None:
    df = st.session_state.fit_data
else:
    df = parse_fit_file(uploaded_file)
    st.session_state.fit_data = df
```

#### 2. Lazy Loading (Charts)
```python
# Charts only generated when tab selected
with st.tabs(["Tab 1", "Tab 2"]):
    with st_tabs[0]:
        st.plotly_chart(fig1)  # Only generated if tab open
```

#### 3. Data Limiting
```python
# Only display first 100 rows
display_df = df.head(100)
st.dataframe(display_df, height=400)
```

#### 4. Avoid Redundant Calculations
```python
# Cache expensive calculations
@st.cache_data
def expensive_calculation(data):
    return result
```

## Error Handling Strategy

### Try-Catch Pattern

```python
try:
    # Risky operation
    result = parse_fit_file(file)
    st.session_state.fit_data = result
except FileNotFoundError:
    st.error("File not found")
except ValueError as e:
    st.error(f"Invalid file format: {e}")
except Exception as e:
    st.error(f"Unexpected error: {e}")
    if DEBUG:
        st.write(str(e))  # Debug info
```

### User-Friendly Error Messages

```python
# ✗ Bad
st.error("ValueError: list index out of range")

# ✓ Good
st.error("Unable to parse FIT file. Ensure the file is a valid Garmin export.")
st.info("If the problem persists, try exporting the file again from Garmin Connect.")
```

## Extending the Application

### Adding a New Form Field

1. **Add to form:**
```python
new_field = st.number_input("New Field", min_value=0, value=100)
```

2. **Store in session:**
```python
st.session_state.athlete_profile["new_key"] = new_field
```

3. **Use in analysis:**
```python
value = st.session_state.athlete_profile.get("new_key")
```

### Adding a New Chart

1. **Create helper function:**
```python
def create_new_chart(data) -> go.Figure:
    # Implementation
    return fig
```

2. **Add to chart tabs:**
```python
with chart_tabs[4]:  # New tab
    fig = create_new_chart(df)
    st.plotly_chart(fig, use_container_width=True)
```

### Adding a New Export Format

1. **Create export function:**
```python
def export_json(data: pd.DataFrame) -> str:
    return data.to_json(orient='records')
```

2. **Add export button:**
```python
with col_json:
    if st.button("📋 Export JSON", use_container_width=True):
        json_data = export_json(df)
        st.download_button(
            label="⬇️ Download JSON",
            data=json_data,
            file_name=f"data_{date}.json",
            mime="application/json"
        )
```

## Debugging Tips

### Enable Debug Mode

```python
# In app.py
DEBUG = True

# In functions
if DEBUG:
    st.write("Variable:", variable_value)
    st.write("Session state:", st.session_state)
```

### Use Logger

```python
import logging
logger = logging.getLogger(__name__)

try:
    result = operation()
except Exception as e:
    logger.error(f"Operation failed: {e}", exc_info=True)
    st.error("Operation failed")
```

### Check Session State

```python
# Sidebar debug section
if DEBUG:
    with st.sidebar:
        st.write("Session State:")
        st.json(st.session_state)
```

## Code Quality Standards

### Style Guide

- **Naming:** snake_case for functions/variables, CamelCase for classes
- **Docstrings:** Google-style docstrings for all functions
- **Comments:** Explain "why", not "what"
- **Line length:** Maximum 100 characters
- **Imports:** Group (stdlib, third-party, local) with blank lines

### Docstring Template

```python
def function_name(param1: str, param2: int) -> dict:
    """
    Brief description of what function does.
    
    Longer description explaining purpose, behavior, and edge cases
    if needed across multiple lines.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value and structure
        
    Raises:
        ValueError: When input validation fails
        FileNotFoundError: When file doesn't exist
    """
    pass
```

### Type Hints

```python
# ✓ Good: Use type hints
def process_file(file: UploadedFile) -> pd.DataFrame:
    pass

# ✓ Good: Complex types
def analyze(data: dict[str, Any]) -> tuple[bool, str]:
    pass

# ✓ Good: Union types for multiple possibilities
def get_value(key: str) -> str | None:
    pass
```

## Deployment Checklist

Before deploying to production:

- [ ] All tests passing
- [ ] No hardcoded credentials or paths
- [ ] Error messages user-friendly
- [ ] Performance acceptable
- [ ] All required modules imported correctly
- [ ] Session state variables initialized
- [ ] Charts tested with sample data
- [ ] Responsive design verified
- [ ] Accessibility verified (contrast, labels)
- [ ] Documentation updated

## Git Workflow

### Branch Naming

```
feature/add-new-chart
fix/button-styling
refactor/session-state
docs/update-readme
```

### Commit Messages

```
# ✓ Good
feat: add HR zone pie chart
fix: correct FTP validation range
docs: update installation instructions

# ✗ Avoid
update code
fix stuff
changes
```

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Feature
- [ ] Bug fix
- [ ] Documentation

## Testing
- [ ] Tested locally
- [ ] Charts render correctly
- [ ] Forms validate properly
- [ ] Mobile responsive

## Screenshots
(If UI changes)
```

## Performance Profiling

### Identify Slow Operations

```python
import time

start = time.time()
# Operation
elapsed = time.time() - start
st.write(f"Operation took {elapsed:.2f}s")
```

### Streamlit-Specific Profiling

```bash
# Run with profiler
streamlit run app.py --logger.level=debug
```

### Measure Page Load

```python
import streamlit as st

if "load_time" not in st.session_state:
    import time
    st.session_state.load_time = time.time()

elapsed = time.time() - st.session_state.load_time
st.write(f"Page load: {elapsed:.3f}s")
```

## Common Pitfalls & Solutions

### Issue: Form resubmits on every rerun
**Solution:** Use `form_submit_button` (already done)

### Issue: Charts flicker
**Solution:** Cache with `@st.cache_data` or store in session state

### Issue: File uploads don't persist
**Solution:** Store in `st.session_state`

### Issue: Slow PDF generation
**Solution:** Show spinner, consider async generation

### Issue: Colors not updating
**Solution:** Clear browser cache (Ctrl+Shift+Del)

### Issue: Charts not displaying
**Solution:** Check data columns, verify Plotly installed

## Future Enhancement Ideas

### Short Term (1-2 sprints)
- [ ] Advanced metrics (TSS, IF, VI)
- [ ] Multiple sport support
- [ ] Custom zone configuration
- [ ] Session notes/comments

### Medium Term (3-6 months)
- [ ] Historical data trending
- [ ] Workout recommendations
- [ ] Comparative analysis
- [ ] Mobile app version

### Long Term (6+ months)
- [ ] AI-powered insights
- [ ] Social features
- [ ] Integration with other platforms
- [ ] Real-time monitoring

## Resources & Links

- **Streamlit Docs:** https://docs.streamlit.io
- **Plotly Docs:** https://plotly.com/python/
- **Pandas Docs:** https://pandas.pydata.org/docs
- **FIT Spec:** https://developer.garmin.com/fit/overview
- **Python Style:** https://pep8.org

---

Last updated: 2024  
Version: 1.0  
Maintainer: Nadir Baca Paunero
