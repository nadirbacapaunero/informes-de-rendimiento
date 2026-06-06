"""
Configuration file for Fasttimes Frontend
Centralized settings for easy customization
"""

# ─────────────────────────────────────────────────────────────────────────────
# COLOR SCHEME
# ─────────────────────────────────────────────────────────────────────────────

# Primary accent color (lime green - high visibility)
COLOR_PRIMARY = "#c8ff00"

# Secondary accent color (cyan - supporting accent)
COLOR_SECONDARY = "#00bfff"

# Background colors
COLOR_BACKGROUND = "#0a0a0f"  # Main background (dark charcoal)
COLOR_SURFACE = "#15151e"      # Card and surface backgrounds (slightly lighter)
COLOR_BORDER = "#2a2a3d"       # Border and divider color

# Text colors
COLOR_TEXT_PRIMARY = "#ffffff"     # Primary text (white)
COLOR_TEXT_SECONDARY = "#cccccc"   # Secondary text (light gray)
COLOR_TEXT_MUTED = "#888888"       # Muted text (medium gray)

# Alert colors
COLOR_ERROR = "#ff4444"            # Error state
COLOR_WARNING = "#ffbb44"          # Warning state
COLOR_SUCCESS = "#c8ff00"          # Success state (same as primary)

# Zone/Metric colors
HR_ZONE_COLORS = [
    "#ff4444",  # Zone 1: Recovery (red)
    "#ff8844",  # Zone 2: Base (orange)
    "#ffbb44",  # Zone 3: Threshold (yellow)
    "#ffcc00",  # Zone 4: Tempo (gold)
    "#c8ff00",  # Zone 5: VO2max (lime)
]

# ─────────────────────────────────────────────────────────────────────────────
# FILE UPLOAD SETTINGS
# ─────────────────────────────────────────────────────────────────────────────

# Maximum file size in bytes (50MB default)
MAX_FILE_SIZE_MB = 50
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

# Allowed file extensions
ALLOWED_FILE_TYPES = ["fit", "FIT"]

# ─────────────────────────────────────────────────────────────────────────────
# ATHLETE PROFILE DEFAULTS
# ─────────────────────────────────────────────────────────────────────────────

# Sport options
SPORTS = ["Running", "Cycling", "Triathlon"]

# Experience levels
EXPERIENCE_LEVELS = ["Beginner", "Intermediate", "Advanced"]

# Training goals
TRAINING_GOALS = [
    "General Fitness",
    "Build Endurance",
    "Improve Speed",
    "Race Prep",
    "Recovery"
]

# Gender options
GENDERS = ["Male", "Female", "Other", "Prefer not to say"]

# Default values for form
DEFAULT_WEIGHT_KG = 70.0
DEFAULT_MAX_HR = 190
DEFAULT_REST_HR = 60
DEFAULT_AGE = 30
DEFAULT_FTP = 250

# Validation ranges
WEIGHT_MIN_KG = 30.0
WEIGHT_MAX_KG = 150.0
MAX_HR_MIN = 120
MAX_HR_MAX = 220
REST_HR_MIN = 30
REST_HR_MAX = 100
AGE_MIN = 12
AGE_MAX = 100
FTP_MIN = 0
FTP_MAX = 500

# ─────────────────────────────────────────────────────────────────────────────
# HR ZONE CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

# Heart rate zones as percentage of max HR
HR_ZONES = {
    "Zone 1 (Recovery)": {"min": 0.50, "max": 0.60, "label": "50-60% MAX"},
    "Zone 2 (Base)": {"min": 0.60, "max": 0.70, "label": "60-70% MAX"},
    "Zone 3 (Threshold)": {"min": 0.70, "max": 0.80, "label": "70-80% MAX"},
    "Zone 4 (Tempo)": {"min": 0.80, "max": 0.90, "label": "80-90% MAX"},
    "Zone 5 (VO2max)": {"min": 0.90, "max": 1.00, "label": "90-100% MAX"},
}

# ─────────────────────────────────────────────────────────────────────────────
# POWER ZONE CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

# Power zones as percentage of FTP
POWER_ZONES = {
    "Active Recovery": {"min": 0.00, "max": 0.56, "label": "<56% FTP"},
    "Endurance": {"min": 0.56, "max": 0.76, "label": "56-76% FTP"},
    "Tempo": {"min": 0.76, "max": 0.90, "label": "76-90% FTP"},
    "Threshold": {"min": 0.90, "max": 1.05, "label": "90-105% FTP"},
    "VO2max": {"min": 1.05, "max": 1.20, "label": "105-120% FTP"},
}

# ─────────────────────────────────────────────────────────────────────────────
# CHART SETTINGS
# ─────────────────────────────────────────────────────────────────────────────

# Chart height (pixels)
CHART_HEIGHT = 350

# Chart hover template
HOVER_TEMPLATE_DEFAULT = '<b>%{label}</b><br>%{value:.1f}<extra></extra>'

# Plotly layout defaults
PLOTLY_LAYOUT_DEFAULTS = {
    "paper_bgcolor": COLOR_BACKGROUND,
    "plot_bgcolor": COLOR_SURFACE,
    "font": {"color": COLOR_TEXT_SECONDARY, "size": 12},
    "xaxis": {"gridcolor": COLOR_BORDER},
    "yaxis": {"gridcolor": COLOR_BORDER},
    "margin": {"l": 40, "r": 20, "t": 40, "b": 40},
}

# ─────────────────────────────────────────────────────────────────────────────
# UI/UX SETTINGS
# ─────────────────────────────────────────────────────────────────────────────

# Page title and icon
PAGE_TITLE = "Fasttimes · FIT Analysis"
PAGE_ICON = "⚡"

# Sidebar state (expanded/collapsed)
SIDEBAR_STATE = "expanded"

# Toast notification duration (seconds)
TOAST_DURATION = 3

# Loading spinner messages
LOADING_MESSAGES = {
    "analyzing": "🔄 Analyzing your FIT file...",
    "generating_pdf": "📄 Generating PDF report...",
    "exporting_csv": "📊 Exporting data...",
}

# Error messages
ERROR_MESSAGES = {
    "no_file": "Please upload a FIT file first",
    "no_profile": "Please complete your athlete profile",
    "invalid_file": "File must be a .FIT file",
    "file_too_large": f"File size exceeds {MAX_FILE_SIZE_MB}MB limit",
    "invalid_range": "Please enter values within valid ranges",
}

# Success messages
SUCCESS_MESSAGES = {
    "profile_saved": "✓ Profile saved successfully!",
    "analysis_complete": "✓ Analysis complete!",
    "pdf_generated": "✓ PDF generated successfully",
    "csv_exported": "✓ CSV ready for download",
}

# ─────────────────────────────────────────────────────────────────────────────
# FTP ESTIMATION SETTINGS
# ─────────────────────────────────────────────────────────────────────────────

# Age-based adjustment factors for FTP estimation
AGE_FACTORS = {
    "young": {"age_max": 25, "factor": 0.9},      # Ages 12-25
    "peak": {"age_min": 25, "age_max": 40, "factor": 1.0},  # Ages 25-40
    "mature": {"age_min": 40, "factor": 0.85},    # Ages 40+
}

# Base watts per kg for cycling (used in FTP estimation)
BASE_WATTS_PER_KG = 3.5

# ─────────────────────────────────────────────────────────────────────────────
# DATA TABLE SETTINGS
# ─────────────────────────────────────────────────────────────────────────────

# Maximum rows to display in detail table (for performance)
MAX_DETAIL_ROWS = 100

# Columns to display in detail table
DETAIL_TABLE_COLUMNS = [
    "timestamp",
    "distance",
    "heart_rate",
    "power",
    "cadence",
    "altitude",
]

# Column display names
DETAIL_TABLE_RENAME = {
    "timestamp": "Time",
    "distance": "Distance (km)",
    "heart_rate": "HR (bpm)",
    "power": "Power (W)",
    "cadence": "Cadence (rpm)",
    "altitude": "Altitude (m)",
}

# ─────────────────────────────────────────────────────────────────────────────
# EXPORT SETTINGS
# ─────────────────────────────────────────────────────────────────────────────

# PDF report filename format
PDF_FILENAME_FORMAT = "report_{athlete_name}_{date}.pdf"

# CSV export filename format
CSV_FILENAME_FORMAT = "data_{athlete_name}_{date}.csv"

# Date format for filenames
DATE_FORMAT = "%Y%m%d"

# CSV export options
CSV_EXPORT_OPTIONS = {
    "index": False,
    "encoding": "utf-8",
}

# ─────────────────────────────────────────────────────────────────────────────
# FEATURE FLAGS
# ─────────────────────────────────────────────────────────────────────────────

# Enable/disable features
FEATURES = {
    "pdf_export": True,
    "csv_export": True,
    "ftp_estimation": True,
    "power_zones": True,
    "hr_zones": True,
    "pace_analysis": True,
    "advanced_metrics": False,  # TSS, IF, VI (future)
    "social_sharing": False,     # Future feature
    "multi_session": False,      # Future feature
}

# ─────────────────────────────────────────────────────────────────────────────
# LOGGING
# ─────────────────────────────────────────────────────────────────────────────

# Enable debug mode
DEBUG = False

# Log file path
LOG_FILE = "fasttimes.log"

# ─────────────────────────────────────────────────────────────────────────────
# API/BACKEND SETTINGS
# ─────────────────────────────────────────────────────────────────────────────

# Module import paths (relative to app.py)
ANALYZER_MODULE = "analyzer"
PDF_GENERATOR_MODULE = "pdf_generator"

# Timeout for analysis (seconds)
ANALYSIS_TIMEOUT = 30

# Retry attempts for failed exports
EXPORT_RETRIES = 2
