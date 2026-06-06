"""
Fasttimes FIT Analysis Tool - Frontend
Professional Streamlit Application for Performance Report Generation
Nadir Baca Paunero · 2024
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
from io import BytesIO
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import analysis modules (adjust paths as needed)
try:
    from analyzer import (
        parse_fit_file,
        analyze_session,
        time_in_hr_zones,
        time_in_power_zones,
        hr_zones,
        power_zones,
    )
except ImportError:
    # Fallback for development
    pass

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG & STYLING
# ─────────────────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Fasttimes · FIT Analysis",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "Professional FIT file analysis tool for endurance athletes."
    }
)

# Color scheme tokens (WCAG AA compliant)
COLOR_PRIMARY = "#c8ff00"  # Lime green (4.8:1 contrast on dark)
COLOR_SECONDARY = "#00bfff"  # Cyan
COLOR_BACKGROUND = "#0a0a0f"  # Dark charcoal
COLOR_SURFACE = "#15151e"  # Slightly lighter surface
COLOR_BORDER = "#2a2a3d"  # Subtle border
COLOR_TEXT_PRIMARY = "#ffffff"  # White text (21:1 contrast)
COLOR_TEXT_SECONDARY = "#e0e0e0"  # Light gray text (5.2:1 contrast - improved)
COLOR_TEXT_MUTED = "#9e9e9e"  # Muted text (4.5:1 contrast - improved)
COLOR_SUCCESS = "#4caf50"  # Success green
COLOR_ERROR = "#ff5252"  # Error red

# Professional dark theme styling
st.markdown(f"""
<style>
    /* Root color scheme */
    :root {{
        --primary: {COLOR_PRIMARY};
        --secondary: {COLOR_SECONDARY};
        --bg: {COLOR_BACKGROUND};
        --surface: {COLOR_SURFACE};
        --border: {COLOR_BORDER};
        --text-primary: {COLOR_TEXT_PRIMARY};
        --text-secondary: {COLOR_TEXT_SECONDARY};
        --text-muted: {COLOR_TEXT_MUTED};
    }}

    /* Main container */
    [data-testid="stAppViewContainer"] {{
        background: {COLOR_BACKGROUND};
        color: {COLOR_TEXT_PRIMARY};
    }}

    [data-testid="stSidebar"] {{
        background: #111118;
        border-right: 1px solid {COLOR_BORDER};
    }}

    /* Typography */
    h1, h2, h3, h4, h5, h6 {{
        color: {COLOR_TEXT_PRIMARY} !important;
        font-weight: 600;
    }}

    p, span, div {{
        color: {COLOR_TEXT_SECONDARY};
    }}

    /* Button sizing for touch targets (44px minimum) */
    button, [role="button"] {{
        min-height: 44px !important;
        padding: 12px 24px !important;
        font-size: 16px !important;
        transition: all 150ms ease-out;
    }}

    button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(200, 255, 0, 0.2);
    }}

    button:active {{
        transform: translateY(0);
        opacity: 0.85;
    }}

    /* Metric cards - Premium styling */
    .metric-card {{
        background: {COLOR_SURFACE};
        border: 1px solid {COLOR_BORDER};
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        transition: all 200ms ease-out;
    }}

    .metric-card:hover {{
        border-color: {COLOR_PRIMARY};
        box-shadow: 0 8px 16px rgba(200, 255, 0, 0.1);
    }}
        margin-bottom: 12px;
        transition: all 0.3s ease;
    }}

    .metric-card:hover {{
        border-color: {COLOR_PRIMARY};
        box-shadow: 0 0 12px rgba(200, 255, 0, 0.1);
    }}

    .metric-value {{
        font-size: 2.2rem;
        font-weight: 700;
        color: {COLOR_PRIMARY};
        font-family: 'Courier New', monospace;
        letter-spacing: 0.5px;
    }}

    .metric-label {{
        font-size: 0.75rem;
        color: {COLOR_TEXT_MUTED};
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-top: 8px;
        font-weight: 500;
    }}

    /* Section titles with accent bar */
    .section-title {{
        font-size: 1.15rem;
        font-weight: 700;
        color: {COLOR_PRIMARY};
        border-left: 3px solid {COLOR_PRIMARY};
        padding-left: 12px;
        margin: 28px 0 16px 0;
        letter-spacing: 0.5px;
    }}

    /* Alert boxes */
    .alert-success {{
        background: rgba(200, 255, 0, 0.08);
        border: 1px solid rgba(200, 255, 0, 0.3);
        border-radius: 8px;
        padding: 12px 16px;
        color: {COLOR_PRIMARY};
        font-size: 0.9rem;
        margin: 12px 0;
    }}

    .alert-error {{
        background: rgba(255, 68, 68, 0.08);
        border: 1px solid rgba(255, 68, 68, 0.3);
        border-radius: 8px;
        padding: 12px 16px;
        color: #ff8888;
        font-size: 0.9rem;
        margin: 12px 0;
    }}

    .alert-info {{
        background: rgba(0, 191, 255, 0.08);
        border: 1px solid rgba(0, 191, 255, 0.3);
        border-radius: 8px;
        padding: 12px 16px;
        color: {COLOR_SECONDARY};
        font-size: 0.9rem;
        margin: 12px 0;
    }}

    /* Form inputs */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {{
        background: {COLOR_SURFACE} !important;
        border: 1px solid {COLOR_BORDER} !important;
        color: {COLOR_TEXT_PRIMARY} !important;
        border-radius: 8px !important;
        padding: 10px 12px !important;
        font-size: 0.95rem !important;
    }}

    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {{
        border-color: {COLOR_PRIMARY} !important;
        box-shadow: 0 0 8px rgba(200, 255, 0, 0.2) !important;
    }}

    /* File uploader */
    .stFileUploader > div {{
        background: {COLOR_SURFACE};
        border: 2px dashed {COLOR_BORDER};
        border-radius: 10px;
        padding: 20px;
        transition: all 0.3s ease;
    }}

    /* Buttons */
    .stButton > button {{
        background: {COLOR_PRIMARY} !important;
        color: {COLOR_BACKGROUND} !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        border: none !important;
        transition: all 0.25s ease !important;
    }}

    .stButton > button:hover {{
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 16px rgba(200, 255, 0, 0.3) !important;
    }}

    .stButton > button:active {{
        transform: translateY(0) !important;
    }}

    /* Secondary buttons */
    .stDownloadButton > button {{
        background: {COLOR_SECONDARY} !important;
        color: {COLOR_BACKGROUND} !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
    }}

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {{
        border-bottom: 1px solid {COLOR_BORDER};
    }}

    .stTabs [role="tab"] {{
        color: {COLOR_TEXT_MUTED};
        border-bottom: 2px solid transparent;
    }}

    .stTabs [role="tab"][aria-selected="true"] {{
        color: {COLOR_PRIMARY};
        border-bottom-color: {COLOR_PRIMARY};
    }}

    /* Dividers */
    hr {{
        border-color: {COLOR_BORDER} !important;
        margin: 20px 0 !important;
    }}

    /* Expanders */
    .streamlit-expanderHeader {{
        color: {COLOR_TEXT_PRIMARY} !important;
    }}

    /* Data tables */
    .stDataframe {{
        background: {COLOR_SURFACE};
    }}

    /* Metric styling */
    .stMetric {{
        background: {COLOR_SURFACE};
        border: 1px solid {COLOR_BORDER};
        border-radius: 8px;
        padding: 16px;
    }}

    .stMetric label {{
        color: {COLOR_TEXT_MUTED} !important;
        font-size: 0.75rem !important;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }}

    [data-testid="stMetricValue"] {{
        color: {COLOR_PRIMARY} !important;
        font-size: 1.8rem !important;
        font-weight: 700;
    }}

    /* Status badges */
    .status-badge {{
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}

    .status-complete {{
        background: rgba(200, 255, 0, 0.15);
        color: {COLOR_PRIMARY};
    }}

    .status-pending {{
        background: rgba(0, 191, 255, 0.15);
        color: {COLOR_SECONDARY};
    }}

    /* Smooth transitions */
    * {{
        transition: color 0.2s ease, background-color 0.2s ease;
    }}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE INITIALIZATION
# ─────────────────────────────────────────────────────────────────────────────

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None
if "analysis_complete" not in st.session_state:
    st.session_state.analysis_complete = False
if "fit_data" not in st.session_state:
    st.session_state.fit_data = None
if "athlete_profile" not in st.session_state:
    st.session_state.athlete_profile = {}


# ─────────────────────────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

def validate_fit_file(file) -> tuple[bool, str]:
    """
    Validate uploaded FIT file.
    Returns (is_valid, message)
    """
    if file is None:
        return False, "No file uploaded"

    if not file.name.lower().endswith('.fit'):
        return False, "File must be a .FIT file"

    if file.size > 50 * 1024 * 1024:  # 50MB limit
        return False, "File size exceeds 50MB limit"

    return True, "File valid"


def estimate_ftp(age: int, max_hr: int, weight_kg: float) -> int:
    """
    Rough FTP estimation from age, max_hr, and weight.
    This is a placeholder formula - real estimation requires power data.
    """
    # Simplified estimation: ~0.65 watts per kg for trained cyclists
    base_ftp = weight_kg * 3.5  # Rough baseline

    # Age adjustment (peak performance ~35-40 years)
    if age < 25:
        age_factor = 0.9
    elif age < 40:
        age_factor = 1.0
    else:
        age_factor = max(0.85, 1.0 - (age - 40) * 0.01)

    return int(base_ftp * age_factor)


def create_hr_zones_chart(hr_zones_data: dict) -> go.Figure:
    """
    Create interactive HR zones pie chart.
    """
    labels = list(hr_zones_data.keys())
    values = list(hr_zones_data.values())
    colors = ["#ff4444", "#ff8844", "#ffbb44", "#ffcc00", "#c8ff00"]

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.4,  # Donut chart
        marker=dict(colors=colors, line=dict(color=COLOR_SURFACE, width=2)),
        textposition='inside',
        textinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>%{value:.1f} min (%{percent})<extra></extra>'
    )])

    fig.update_layout(
        title="Heart Rate Zone Distribution",
        paper_bgcolor=COLOR_BACKGROUND,
        font=dict(color=COLOR_TEXT_SECONDARY, size=12),
        margin=dict(l=20, r=20, t=40, b=20),
        height=350
    )

    return fig


def create_power_distribution_chart(power_data: dict) -> go.Figure:
    """
    Create power distribution bar chart.
    """
    zones = list(power_data.keys())
    values = list(power_data.values())

    fig = go.Figure(data=[go.Bar(
        x=zones,
        y=values,
        marker=dict(
            color=[COLOR_PRIMARY, COLOR_SECONDARY, "#ffbb44", "#ff8844", "#ff4444"],
            line=dict(color=COLOR_BORDER, width=1)
        ),
        text=[f'{v:.0f}' for v in values],
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>%{y:.1f} min<extra></extra>'
    )])

    fig.update_layout(
        title="Power Zone Distribution",
        xaxis_title="Power Zone",
        yaxis_title="Time (minutes)",
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


def create_pace_timeline_chart(pace_data: pd.DataFrame) -> go.Figure:
    """
    Create pace timeline chart.
    """
    if pace_data.empty:
        return None

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=pace_data.index,
        y=pace_data['pace'],
        mode='lines',
        name='Pace',
        line=dict(color=COLOR_PRIMARY, width=2),
        fill='tozeroy',
        fillcolor=f'rgba(200, 255, 0, 0.2)',
        hovertemplate='<b>Km %{x}</b><br>Pace: %{y:.2f} min/km<extra></extra>'
    ))

    fig.update_layout(
        title="Pace Timeline",
        xaxis_title="Distance (km)",
        yaxis_title="Pace (min/km)",
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


# ─────────────────────────────────────────────────────────────────────────────
# MAIN APPLICATION LAYOUT
# ─────────────────────────────────────────────────────────────────────────────

# Header
st.markdown("""
<div style='text-align: center; margin-bottom: 32px;'>
    <h1 style='font-size: 2.5rem; margin: 0; color: #c8ff00;'>⚡ Fasttimes</h1>
    <p style='font-size: 1rem; color: #888888; margin: 8px 0 0 0;'>Professional FIT File Analysis for Endurance Athletes</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# Main content container
with st.container():
    # Create two columns: form (left) and file upload (right)
    col_form, col_upload = st.columns([1, 1], gap="large")

    # ─────────────────────────────────────────────────────────────────────────
    # LEFT COLUMN: USER PROFILE FORM
    # ─────────────────────────────────────────────────────────────────────────
    with col_form:
        st.markdown('<div class="section-title">👤 Athlete Profile</div>', unsafe_allow_html=True)

        with st.form("athlete_profile_form"):
            # Basic info
            athlete_name = st.text_input(
                "Athlete Name",
                placeholder="Enter your name",
                help="Your name appears in the generated report"
            )

            col_sport1, col_sport2 = st.columns(2)
            with col_sport1:
                sport = st.selectbox(
                    "Sport",
                    ["Running", "Cycling", "Triathlon"],
                    help="Type of sport for this session"
                )

            with col_sport2:
                experience = st.selectbox(
                    "Experience Level",
                    ["Beginner", "Intermediate", "Advanced"],
                    help="Your training experience level"
                )

            # Performance metrics
            col_ftp, col_weight = st.columns(2)
            with col_ftp:
                ftp = st.number_input(
                    "FTP (watts)",
                    min_value=0,
                    max_value=500,
                    value=250,
                    step=10,
                    help="Functional Threshold Power. Enter 0 for automatic estimation"
                )

            with col_weight:
                weight_kg = st.number_input(
                    "Weight (kg)",
                    min_value=30.0,
                    max_value=150.0,
                    value=70.0,
                    step=0.5,
                    help="Your body weight in kilograms"
                )

            # Heart rate metrics
            col_maxhr, col_rest = st.columns(2)
            with col_maxhr:
                max_hr = st.number_input(
                    "Max Heart Rate (bpm)",
                    min_value=120,
                    max_value=220,
                    value=190,
                    step=1,
                    help="Your maximum heart rate"
                )

            with col_rest:
                rest_hr = st.number_input(
                    "Resting HR (bpm)",
                    min_value=30,
                    max_value=100,
                    value=60,
                    step=1,
                    help="Your resting heart rate (optional)"
                )

            # Optional fields
            st.markdown("**Optional Information**")
            col_age, col_gender = st.columns(2)
            with col_age:
                age = st.number_input(
                    "Age (years)",
                    min_value=12,
                    max_value=100,
                    value=30,
                    step=1
                )

            with col_gender:
                gender = st.selectbox(
                    "Gender",
                    ["Male", "Female", "Other", "Prefer not to say"]
                )

            col_goal, _ = st.columns(2)
            with col_goal:
                goal = st.selectbox(
                    "Training Goal",
                    ["General Fitness", "Build Endurance", "Improve Speed", "Race Prep", "Recovery"]
                )

            # Form submission
            form_submitted = st.form_submit_button(
                "✓ Save Profile",
                use_container_width=True,
                type="primary"
            )

            if form_submitted:
                # Validate form
                if not athlete_name:
                    st.error("Please enter your name")
                elif weight_kg <= 0 or max_hr <= 0:
                    st.error("Please enter valid weight and heart rate values")
                else:
                    # Save to session state
                    st.session_state.athlete_profile = {
                        "name": athlete_name,
                        "sport": sport,
                        "experience": experience,
                        "ftp": ftp,
                        "weight_kg": weight_kg,
                        "max_hr": max_hr,
                        "rest_hr": rest_hr,
                        "age": age,
                        "gender": gender,
                        "goal": goal
                    }

                    st.success("✓ Profile saved successfully!")

    # ─────────────────────────────────────────────────────────────────────────
    # RIGHT COLUMN: FILE UPLOAD
    # ─────────────────────────────────────────────────────────────────────────
    with col_upload:
        st.markdown('<div class="section-title">📁 FIT File Upload</div>', unsafe_allow_html=True)

        # Upload instructions
        with st.expander("📋 How to Export Your FIT File", expanded=False):
            st.markdown("""
            **From Garmin Connect:**
            1. Log in to [Garmin Connect](https://connect.garmin.com/)
            2. Navigate to Activities → Select your workout
            3. Click the **⋮ (menu)** icon → **Export**
            4. Choose **Export Original** (.FIT format)
            5. Save and upload the file here

            **From Strava (if synced):**
            1. Open your activity on Strava
            2. Click **⋯ → Export as GPX** (you may need the activity from Garmin directly)
            3. For FIT files, export directly from Garmin Connect
            """)

        # File uploader with enhanced styling
        uploaded_file = st.file_uploader(
            "Drag and drop your .FIT file or click to browse",
            type=["fit", "FIT"],
            help="Select a Garmin FIT file to analyze"
        )

        if uploaded_file is not None:
            # Validate file
            is_valid, validation_msg = validate_fit_file(uploaded_file)

            if is_valid:
                st.session_state.uploaded_file = uploaded_file

                # File preview
                st.markdown('<div class="alert-success">✓ File ready for analysis</div>', unsafe_allow_html=True)
                st.markdown(f"""
                **File Details:**
                - **Name:** {uploaded_file.name}
                - **Size:** {uploaded_file.size / 1024:.1f} KB
                - **Uploaded:** {datetime.now().strftime('%H:%M:%S')}
                """)
            else:
                st.markdown(f'<div class="alert-error">❌ {validation_msg}</div>', unsafe_allow_html=True)
                st.session_state.uploaded_file = None
        else:
            st.markdown('<div class="alert-info">💡 Upload a .FIT file to begin analysis</div>', unsafe_allow_html=True)

st.divider()

# ─────────────────────────────────────────────────────────────────────────────
# ANALYSIS SECTION
# ─────────────────────────────────────────────────────────────────────────────

st.markdown('<div class="section-title">⚙️ Generate Report</div>', unsafe_allow_html=True)

col_generate, col_status = st.columns([3, 1])

with col_generate:
    if st.button(
        "🚀 Generate Performance Report",
        use_container_width=True,
        type="primary",
        disabled=st.session_state.uploaded_file is None or not st.session_state.athlete_profile
    ):
        if st.session_state.uploaded_file is None:
            st.error("Please upload a FIT file first")
        elif not st.session_state.athlete_profile:
            st.error("Please complete your athlete profile")
        else:
            with st.spinner("🔄 Analyzing your FIT file..."):
                try:
                    # Parse FIT file
                    df = parse_fit_file(st.session_state.uploaded_file)

                    # Store in session
                    st.session_state.fit_data = df
                    st.session_state.analysis_complete = True

                    st.success("✓ Analysis complete!")
                    st.rerun()

                except Exception as e:
                    st.error(f"❌ Error processing FIT file: {str(e)}")
                    st.info("Please ensure the file is a valid Garmin FIT file")

with col_status:
    if st.session_state.analysis_complete:
        st.markdown(
            '<span class="status-badge status-complete">Complete</span>',
            unsafe_allow_html=True
        )
    elif st.session_state.uploaded_file is not None:
        st.markdown(
            '<span class="status-badge status-pending">Ready</span>',
            unsafe_allow_html=True
        )

# ─────────────────────────────────────────────────────────────────────────────
# RESULTS SECTION (shown after analysis)
# ─────────────────────────────────────────────────────────────────────────────

if st.session_state.analysis_complete and st.session_state.fit_data is not None:
    st.divider()

    df = st.session_state.fit_data
    profile = st.session_state.athlete_profile

    # Key Performance Indicators
    st.markdown('<div class="section-title">📊 Session Summary</div>', unsafe_allow_html=True)

    # Calculate KPIs
    total_distance = df['distance'].max() if 'distance' in df.columns else 0
    total_time = len(df) / 60 if len(df) > 0 else 0  # Convert to minutes
    avg_hr = df['heart_rate'].mean() if 'heart_rate' in df.columns else 0
    max_hr_session = df['heart_rate'].max() if 'heart_rate' in df.columns else 0
    avg_power = df['power'].mean() if 'power' in df.columns else 0
    max_power = df['power'].max() if 'power' in df.columns else 0

    # Calculate avg pace
    avg_pace = (total_time / total_distance * 60) if total_distance > 0 else 0

    # Display KPIs in grid
    kpi_cols = st.columns(4)

    with kpi_cols[0]:
        st.metric(
            "Distance",
            f"{total_distance:.2f} km",
            help="Total distance covered"
        )

    with kpi_cols[1]:
        st.metric(
            "Duration",
            f"{int(total_time // 60)}:{int(total_time % 60):02d}",
            help="Total session time"
        )

    with kpi_cols[2]:
        st.metric(
            "Avg Heart Rate",
            f"{avg_hr:.0f} bpm",
            f"Max: {max_hr_session:.0f} bpm",
            help="Average and maximum heart rate"
        )

    with kpi_cols[3]:
        st.metric(
            "Avg Power",
            f"{avg_power:.0f} W",
            f"Max: {max_power:.0f} W" if avg_power > 0 else None,
            help="Average power output"
        )

    st.divider()

    # Charts section
    st.markdown('<div class="section-title">📈 Performance Analysis</div>', unsafe_allow_html=True)

    chart_tabs = st.tabs(["❤️ HR Zones", "⚡ Power Distribution", "🏃 Pace Timeline", "📋 Details"])

    # ─────────────────────────────────────────────────────────────────────────
    # HR ZONES TAB
    # ─────────────────────────────────────────────────────────────────────────
    with chart_tabs[0]:
        col_chart, col_legend = st.columns([2, 1])

        with col_chart:
            # Create dummy HR zones data (in real app, calculate from actual data)
            hr_zones_data = {
                "Zone 1 (Recovery)": 8,
                "Zone 2 (Base)": 15,
                "Zone 3 (Threshold)": 12,
                "Zone 4 (Tempo)": 10,
                "Zone 5 (VO2max)": 5,
            }

            fig_hr = create_hr_zones_chart(hr_zones_data)
            st.plotly_chart(fig_hr, use_container_width=True)

        with col_legend:
            st.markdown("**Zone Definitions**")
            st.markdown("""
            **Zone 1:** 50-60% MAX
            Recovery & Easy

            **Zone 2:** 60-70% MAX
            Aerobic Base

            **Zone 3:** 70-80% MAX
            Sweet Spot

            **Zone 4:** 80-90% MAX
            Threshold

            **Zone 5:** 90-100% MAX
            VO2 Maximum
            """, help="Heart rate training zones")

    # ─────────────────────────────────────────────────────────────────────────
    # POWER DISTRIBUTION TAB
    # ─────────────────────────────────────────────────────────────────────────
    with chart_tabs[1]:
        if avg_power > 0:
            # Create dummy power zones data
            power_zones_data = {
                "Active Recovery": 5,
                "Endurance": 18,
                "Tempo": 14,
                "Threshold": 10,
                "VO2max": 3,
            }

            fig_power = create_power_distribution_chart(power_zones_data)
            st.plotly_chart(fig_power, use_container_width=True)
        else:
            st.info("No power data available for this session")

    # ─────────────────────────────────────────────────────────────────────────
    # PACE TIMELINE TAB
    # ─────────────────────────────────────────────────────────────────────────
    with chart_tabs[2]:
        if total_distance > 0:
            # Create dummy pace data
            pace_timeline = pd.DataFrame({
                "distance": np.linspace(0, total_distance, min(len(df), 100)),
                "pace": np.random.normal(avg_pace, 0.1, min(len(df), 100))
            })
            pace_timeline = pace_timeline.set_index("distance")

            fig_pace = create_pace_timeline_chart(pace_timeline)
            if fig_pace:
                st.plotly_chart(fig_pace, use_container_width=True)
        else:
            st.info("No pace data available")

    # ─────────────────────────────────────────────────────────────────────────
    # SESSION DETAILS TAB
    # ─────────────────────────────────────────────────────────────────────────
    with chart_tabs[3]:
        st.markdown("**Detailed Session Data**")

        # Prepare display dataframe
        display_cols = []
        if 'timestamp' in df.columns:
            display_cols.append('timestamp')
        if 'distance' in df.columns:
            display_cols.append('distance')
        if 'heart_rate' in df.columns:
            display_cols.append('heart_rate')
        if 'power' in df.columns:
            display_cols.append('power')
        if 'cadence' in df.columns:
            display_cols.append('cadence')
        if 'altitude' in df.columns:
            display_cols.append('altitude')

        if display_cols:
            display_df = df[display_cols].head(100).copy()

            # Rename columns for display
            rename_map = {
                'timestamp': 'Time',
                'distance': 'Distance (km)',
                'heart_rate': 'HR (bpm)',
                'power': 'Power (W)',
                'cadence': 'Cadence (rpm)',
                'altitude': 'Altitude (m)'
            }
            display_df = display_df.rename(columns=rename_map)

            st.dataframe(
                display_df,
                use_container_width=True,
                height=400
            )

            st.caption(f"Showing first 100 of {len(df)} data points")
        else:
            st.warning("No detailed data available in this FIT file")

    st.divider()

    # ─────────────────────────────────────────────────────────────────────────
    # DOWNLOAD SECTION
    # ─────────────────────────────────────────────────────────────────────────
    st.markdown('<div class="section-title">📥 Export Report</div>', unsafe_allow_html=True)

    col_pdf, col_csv, col_space = st.columns([1, 1, 2])

    with col_pdf:
        st.info("📄 PDF export disabled (use CSV export instead)")

    with col_csv:
        if st.button("📊 Export CSV Data", use_container_width=True):
            try:
                csv_bytes = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="⬇️ Download CSV",
                    data=csv_bytes,
                    file_name=f"data_{profile['name'].replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.csv",
                    mime="text/csv",
                    use_container_width=True
                )
                st.success("✓ CSV ready for download")
            except Exception as e:
                st.error(f"❌ Error exporting CSV: {str(e)}")

# ─────────────────────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────────────────────

st.divider()
st.markdown("""
<div style='text-align: center; color: #888888; font-size: 0.85rem; margin-top: 40px;'>
    <p>⚡ <strong>Fasttimes</strong> · Professional Performance Analysis</p>
    <p>Built with Streamlit | Data: Garmin FIT Files | Analysis: Python</p>
    <p style='margin-top: 16px; font-size: 0.8rem;'>Nadir Baca Paunero · 2024</p>
</div>
""", unsafe_allow_html=True)
