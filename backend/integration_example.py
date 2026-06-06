"""
Integration example: How to use the backend in your Streamlit app

Replace portions of app.py with this modular approach
"""

import io
import json
import streamlit as st
import pandas as pd

# Import from backend
from backend.parser import FITParser
from backend.metrics import MetricsCalculator


def setup_athlete_profile():
    """Setup athlete data in sidebar"""
    st.sidebar.header("Athlete Profile")

    athlete = {
        "ftp": st.sidebar.number_input(
            "FTP (watts)",
            min_value=0,
            max_value=600,
            value=280,
            help="Functional Threshold Power. Leave 0 to estimate from data."
        ),
        "max_hr": st.sidebar.number_input(
            "Max HR (bpm)",
            min_value=100,
            max_value=250,
            value=195,
            help="Your maximum heart rate"
        ),
        "weight_kg": st.sidebar.number_input(
            "Weight (kg)",
            min_value=30,
            max_value=150,
            value=75,
            help="Your body weight for VO2max calculation"
        ),
        "sport": st.sidebar.selectbox(
            "Sport Type",
            ["cycling", "running", "multisport"]
        )
    }

    return athlete


def display_session_summary(session):
    """Display main session metrics"""
    st.header("Session Summary")

    # Key metrics in columns
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Duration", session.duration_str)
    with col2:
        st.metric("Distance", f"{session.distance_km:.1f} km")
    with col3:
        st.metric("Avg HR", f"{session.avg_hr:.0f} bpm")
    with col4:
        st.metric("Max HR", f"{session.max_hr} bpm")


def display_power_metrics(session):
    """Display power-related metrics (cycling)"""
    if not session.has_power:
        st.info("No power data available in this file")
        return

    st.header("Power Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Avg Power", f"{session.avg_power:.0f} W")
    with col2:
        st.metric("Max Power", f"{session.max_power:.0f} W")
    with col3:
        st.metric("Norm. Power", f"{session.normalized_power:.0f} W")
    with col4:
        st.metric("FTP", f"{session.ftp:.0f} W",
                 delta="(estimated)" if session.ftp_estimated else "(user input)")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Intensity Factor", f"{session.intensity_factor:.2f}")
    with col2:
        st.metric("TSS Score", f"{session.tss:.1f}")
    with col3:
        st.metric("VO2max Est.", f"{session.vo2max:.1f} ml/kg/min")


def display_running_metrics(session, athlete):
    """Display running-specific metrics"""
    st.header("Running Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Avg Pace", session.avg_pace_str)
    with col2:
        st.metric("Best Pace", session.best_pace_str)
    with col3:
        st.metric("Avg Speed", f"{session.avg_speed_kmh:.1f} km/h")
    with col4:
        st.metric("Max Speed", f"{session.max_speed_kmh:.1f} km/h")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Avg Cadence", f"{session.avg_cadence:.0f} steps/min")
    with col2:
        st.metric("SPM", f"{session.spm:.0f}")
    with col3:
        st.metric("Efficiency", f"{session.running_efficiency:.3f}")


def display_elevation_metrics(session):
    """Display elevation metrics"""
    st.header("Elevation & Geography")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Elevation Gain", f"{session.elevation_gain_m:.0f} m")
    with col2:
        st.metric("Elevation Loss", f"{session.elevation_loss_m:.0f} m")
    with col3:
        vam = (session.elevation_gain_m / (session.duration_sec / 3600)) if session.duration_sec > 0 else 0
        st.metric("VAM", f"{vam:.0f} m/h")


def display_zone_analysis(calc, df, ftp):
    """Display zone distribution charts"""
    st.header("Zone Analysis")

    zones_dict = calc.get_zone_distribution(df, ftp=ftp)

    tab1, tab2 = st.tabs(["Heart Rate Zones", "Power Zones"])

    with tab1:
        if not zones_dict["hr_zones"].empty:
            st.dataframe(
                zones_dict["hr_zones"][["Zone", "Minutes", "Percentage"]],
                use_container_width=True
            )

            # Chart
            chart_data = zones_dict["hr_zones"].set_index("Zone")["Percentage"]
            st.bar_chart(chart_data)
        else:
            st.info("No HR data available")

    with tab2:
        if "power_zones" in zones_dict and not zones_dict["power_zones"].empty:
            st.dataframe(
                zones_dict["power_zones"][["Zone", "Minutes", "Percentage"]],
                use_container_width=True
            )

            # Chart
            chart_data = zones_dict["power_zones"].set_index("Zone")["Percentage"]
            st.bar_chart(chart_data)
        else:
            st.info("No power data available")


def export_session_data(session, athlete, filename="session_export"):
    """Create download buttons for session data"""
    st.header("Export Data")

    col1, col2, col3 = st.columns(3)

    # JSON export
    with col1:
        session_dict = session.to_dict()
        json_str = json.dumps(session_dict, indent=2, default=str)
        st.download_button(
            label="Download as JSON",
            data=json_str,
            file_name=f"{filename}.json",
            mime="application/json"
        )

    # CSV export
    with col2:
        session_df = pd.DataFrame([session.to_dict()])
        csv_data = session_df.to_csv(index=False)
        st.download_button(
            label="Download as CSV",
            data=csv_data,
            file_name=f"{filename}.csv",
            mime="text/csv"
        )

    # Text summary
    with col3:
        summary_text = f"""
Session Summary Report
======================

Duration: {session.duration_str}
Distance: {session.distance_km:.1f} km
Avg HR: {session.avg_hr:.0f} bpm
Max HR: {session.max_hr} bpm

Power Metrics:
Avg Power: {session.avg_power:.0f} W
Normalized Power: {session.normalized_power:.0f} W
FTP: {session.ftp:.0f} W
TSS: {session.tss:.1f}
Intensity Factor: {session.intensity_factor:.2f}

Performance:
VO2max: {session.vo2max:.1f} ml/kg/min
Elevation Gain: {session.elevation_gain_m:.0f} m
Elevation Loss: {session.elevation_loss_m:.0f} m

Athlete Info:
FTP: {athlete.get('ftp', 'N/A')} W
Max HR: {athlete.get('max_hr', 'N/A')} bpm
Weight: {athlete.get('weight_kg', 'N/A')} kg
Sport: {athlete.get('sport', 'N/A')}
"""
        st.download_button(
            label="Download as Text",
            data=summary_text,
            file_name=f"{filename}.txt",
            mime="text/plain"
        )


# ─────────────────────────────────────────────
# MAIN STREAMLIT APP
# ─────────────────────────────────────────────

def main():
    """Main Streamlit application using backend modules"""

    st.set_page_config(
        page_title="Fasttimes - FIT Analysis",
        page_icon="⚡",
        layout="wide"
    )

    st.title("⚡ Fasttimes — Performance Analysis")
    st.markdown("Analyze your Garmin FIT files with comprehensive metrics")

    # Setup athlete profile
    athlete = setup_athlete_profile()

    # File upload
    uploaded_file = st.file_uploader(
        "Upload FIT file",
        type="fit",
        help="Select a .fit file from your Garmin device"
    )

    if uploaded_file is None:
        st.info("👆 Upload a FIT file to get started")
        return

    try:
        # Parse FIT file
        with st.spinner("Parsing FIT file..."):
            parser = FITParser()
            df = parser.parse(uploaded_file)

            if df is None or df.empty:
                st.error("Could not parse FIT file. Make sure it's a valid Garmin file.")
                return

        st.success(f"✓ Loaded {len(df)} data points")

        # Analyze session
        with st.spinner("Calculating metrics..."):
            calc = MetricsCalculator(athlete)
            session = calc.analyze_session(df)

        # Display results
        display_session_summary(session)

        # Sport-specific metrics
        if athlete["sport"] == "cycling":
            display_power_metrics(session)
        elif athlete["sport"] == "running":
            display_running_metrics(session, athlete)

        # Common metrics
        display_elevation_metrics(session)
        display_zone_analysis(calc, df, session.ftp if session.has_power else 0)

        # Export options
        export_session_data(session, athlete)

        # Raw data explorer
        with st.expander("Raw Data Explorer"):
            st.write(df)

            # Statistics
            st.subheader("Data Statistics")
            st.write(df.describe())

    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        st.error("Please check your FIT file format.")


if __name__ == "__main__":
    main()
