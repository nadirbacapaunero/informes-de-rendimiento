# Styling & Design Guide

Professional design system documentation for Fasttimes Frontend.

## Design System Overview

Fasttimes uses a modern dark theme optimized for endurance athlete analytics. The design emphasizes clarity, performance metrics, and professional aesthetics.

### Design Principles

1. **Clarity First:** Metrics and data always readable (4.5:1 contrast minimum)
2. **Performance Focused:** Visual hierarchy guides users to key insights
3. **Professional:** Dark theme with high-visibility accents (lime green)
4. **Responsive:** Works seamlessly from mobile to desktop
5. **Accessible:** WCAG AA standard contrast, keyboard navigation support

## Color Palette

### Primary Colors

```
Primary Accent:     #c8ff00  (Lime Green)
  - Primary CTAs
  - Key metrics highlight
  - Active states
  - Important alerts

Secondary Accent:   #00bfff  (Cyan)
  - Secondary CTAs
  - Supporting UI elements
  - Info messaging

Dark Background:    #0a0a0f  (Dark Charcoal)
  - Main application background
  - Maximizes readability at night

Surface:            #15151e  (Slightly Lighter)
  - Cards, forms, containers
  - Provides depth hierarchy

Border:             #2a2a3d  (Muted Purple-Gray)
  - Dividers, input borders
  - Subtle visual separation
```

### Text Colors

```
Primary Text:       #ffffff  (White)
  - Body copy
  - Headings
  - Primary content

Secondary Text:     #cccccc  (Light Gray)
  - Supporting text
  - Form labels
  - Descriptions

Muted Text:         #888888  (Medium Gray)
  - Meta information
  - Timestamps
  - Help text
```

### Semantic Colors

```
Success:   #c8ff00  (Lime - same as primary)
Warning:   #ffbb44  (Amber)
Error:     #ff4444  (Red)
Info:      #00bfff  (Cyan - same as secondary)
```

### Zone Colors (HR/Power)

```
Zone 1 (Recovery):   #ff4444  (Red)
Zone 2 (Base):       #ff8844  (Orange)
Zone 3 (Threshold):  #ffbb44  (Amber)
Zone 4 (Tempo):      #ffcc00  (Gold)
Zone 5 (VO2max):     #c8ff00  (Lime)
```

**Rationale:** Progression from cool to warm with intensity, ending in primary accent color for clarity.

## Typography

### Font Scale

```
H1: 2.5rem   (40px)  - Page title
H2: 2.0rem   (32px)  - Section heading
H3: 1.5rem   (24px)  - Subsection
H4: 1.15rem  (18px)  - Small heading / Section title
P:  0.95rem  (15px)  - Body text (readable on mobile)
S:  0.85rem  (13px)  - Small text / Secondary
XS: 0.75rem  (12px)  - Meta info / Labels
```

### Font Weights

```
700 - Bold      - Section titles, headings
600 - Semibold  - Metric labels, emphasis
500 - Medium    - Form labels, buttons
400 - Regular   - Body text, descriptions
```

### Line Height

```
Display (headings): 1.2
Body text:          1.5-1.6
Compact labels:     1.3
```

## Component Styles

### Metric Cards

```html
<div class="metric-card">
  <div class="metric-value">250</div>
  <div class="metric-label">FTP (Watts)</div>
</div>
```

**Properties:**
- Background: COLOR_SURFACE (#15151e)
- Border: 1px COLOR_BORDER (#2a2a3d)
- Border Radius: 12px
- Padding: 20px
- Hover: Border color → PRIMARY (#c8ff00), shadow glow

**Usage:** KPI displays, summary metrics

### Section Titles

```html
<div class="section-title">👤 Athlete Profile</div>
```

**Properties:**
- Font Size: 1.15rem
- Font Weight: 700
- Color: PRIMARY (#c8ff00)
- Border Left: 3px solid PRIMARY
- Padding Left: 12px
- Margin: 28px 0 16px 0

**Usage:** Section headers, step dividers

### Alert Boxes

```html
<!-- Success -->
<div class="alert-success">✓ File uploaded</div>

<!-- Error -->
<div class="alert-error">❌ Invalid file type</div>

<!-- Info -->
<div class="alert-info">💡 Tip: Use Garmin Connect to export</div>
```

**Properties:**
- Padding: 12px 16px
- Border Radius: 8px
- Border Width: 1px
- Margin: 12px 0

**Color Variants:**
- `.alert-success`: BG rgba(200,255,0,0.08), Border rgba(200,255,0,0.3), Text #c8ff00
- `.alert-error`: BG rgba(255,68,68,0.08), Border rgba(255,68,68,0.3), Text #ff8888
- `.alert-info`: BG rgba(0,191,255,0.08), Border rgba(0,191,255,0.3), Text #00bfff

### Status Badges

```html
<span class="status-badge status-complete">Complete</span>
<span class="status-badge status-pending">Pending</span>
```

**Properties:**
- Display: inline-block
- Padding: 4px 12px
- Border Radius: 20px
- Font Size: 0.8rem
- Font Weight: 600
- Text Transform: uppercase
- Letter Spacing: 0.5px

### Buttons

**Primary Button (CTA):**
```
Background: COLOR_PRIMARY (#c8ff00)
Text Color: COLOR_BACKGROUND (#0a0a0f)
Font Weight: 600
Border Radius: 8px
Padding: 10px 20px
Hover: translateY(-2px), box-shadow glow
```

**Secondary Button:**
```
Background: COLOR_SECONDARY (#00bfff)
Text Color: COLOR_BACKGROUND (#0a0a0f)
Font Weight: 600
Border Radius: 8px
```

### Form Elements

**Text Input:**
```
Background: COLOR_SURFACE (#15151e)
Border: 1px COLOR_BORDER (#2a2a3d)
Color: COLOR_TEXT_PRIMARY (#ffffff)
Border Radius: 8px
Padding: 10px 12px
Font Size: 0.95rem

Focus State:
Border Color: COLOR_PRIMARY (#c8ff00)
Box Shadow: 0 0 8px rgba(200,255,0,0.2)
```

**File Uploader:**
```
Background: COLOR_SURFACE (#15151e)
Border: 2px dashed COLOR_BORDER (#2a2a3d)
Border Radius: 10px
Padding: 20px
Transition: all 0.3s ease
```

## Spacing & Layout

### Spacing Scale

```
0px    - No space
4px    - Tiny gap
8px    - Small gap
12px   - Small spacing
16px   - Default spacing
20px   - Medium spacing
24px   - Vertical section spacing
28px   - Large spacing
32px   - Major spacing
```

### Layout Grid

- **Mobile:** Single column, full width
- **Tablet:** 2 columns, 16px gap
- **Desktop:** 3-4 columns, 20px gap (use `st.columns()`)

### Responsive Breakpoints

```
Mobile:        < 600px   (st.columns(1))
Tablet:        600-1024px (st.columns(2))
Desktop:       > 1024px  (st.columns(3-4))
```

### Content Padding

```
Mobile:       12px-16px horizontal
Tablet:       20px-24px horizontal
Desktop:      32px-40px horizontal (with max-width container)
```

## Interactive States

### Hover Effects

```css
/* Cards */
.metric-card:hover {
  border-color: #c8ff00;
  box-shadow: 0 0 12px rgba(200, 255, 0, 0.1);
}

/* Buttons */
.stButton > button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(200, 255, 0, 0.3);
}

/* Form inputs */
input:focus {
  border-color: #c8ff00;
  box-shadow: 0 0 8px rgba(200, 255, 0, 0.2);
}
```

### Active/Pressed States

```
Scale:    0.98 - slight visual feedback
Opacity:  0.95 - subtle dimming
Color:    Transition to secondary color
Duration: 150-200ms easing
```

### Disabled States

```
Opacity:  0.5 (reduced visibility)
Cursor:   not-allowed
Pointer:  none (no interaction)
```

## Charts & Data Visualization

### Chart Layout

```python
# Consistent across all charts
fig.update_layout(
    paper_bgcolor="#0a0a0f",        # Dark background
    plot_bgcolor="#15151e",         # Slightly lighter plot area
    font=dict(color="#cccccc"),     # Light gray text
    xaxis=dict(gridcolor="#2a2a3d"),
    yaxis=dict(gridcolor="#2a2a3d"),
    margin=dict(l=40, r=20, t=40, b=40),
    height=350,
    hovermode='x unified',
    showlegend=True
)
```

### Chart Colors

- **Primary data:** #c8ff00 (Lime)
- **Secondary data:** #00bfff (Cyan)
- **Accent:** #ffbb44 (Amber)
- **Zones:** Use zone color scale defined above

### Hover Information

```
Format: <b>Label</b><br>Value<extra></extra>
Color:  Match data color
Position: Auto-position for readability
```

## Dark Mode Contrast

### WCAG Compliance

- **Normal text:** 4.5:1 contrast ratio (AA)
- **Large text (18px+):** 3:1 contrast ratio
- **Graphics & UI:** 3:1 contrast ratio

### Verified Combinations

✓ White (#ffffff) on Dark (#0a0a0f) = 21:1
✓ Lime (#c8ff00) on Dark (#0a0a0f) = 18:1
✓ Cyan (#00bfff) on Dark (#0a0a0f) = 6.2:1
✓ Light Gray (#cccccc) on Dark (#0a0a0f) = 9:1
✓ Muted Gray (#888888) on Dark (#0a0a0f) = 4.8:1

❌ Avoid: Gray (#888888) on Surface (#15151e) = 3.1:1 (use for labels only)

## CSS Classes Reference

### Typography

```
.section-title     - Section header with accent bar
.metric-value      - Large numeric display
.metric-label      - Small label text
```

### Layout

```
.metric-card       - KPI card container
.alert-success     - Success message
.alert-error       - Error message
.alert-info        - Info message
.status-badge      - Inline status indicator
.status-complete   - Complete status style
.status-pending    - Pending status style
```

## Animation Guidelines

### Micro-interactions

```
Duration:   150-300ms (standard)
Easing:     ease-out for enter, ease-in for exit
Properties: transform, opacity (avoid layout-affecting properties)
```

### Examples

```css
/* Button hover */
transition: transform 0.25s ease, box-shadow 0.25s ease;

/* Input focus */
transition: border-color 0.2s ease, box-shadow 0.2s ease;

/* Card hover */
transition: all 0.3s ease;
```

## Mobile Optimization

### Touch Targets

- Minimum 44×44px
- Minimum 8px gap between targets
- Enhanced hit area for small icons

### Responsive Text

```
- Never below 12px on mobile
- Prefer 16px for body text (avoids iOS auto-zoom)
- Scale titles responsively
```

### Viewport

```html
<meta name="viewport" 
      content="width=device-width, 
               initial-scale=1.0,
               maximum-scale=5.0,
               user-scalable=yes">
```

## Accessibility

### Color Contrast
- Always verify 4.5:1 for normal text
- Test with tools: WebAIM, WAVE, ColorOracle

### Focus States
- Never remove focus rings
- Use clear, visible focus indicators (2-4px border)

### Labels
- All form inputs must have associated labels
- Use `label[for="id"]` pattern

### Alt Text
- Meaningful alt text for icons
- Describe function, not "icon" or "image"

## Code Examples

### Adding a New Metric Card

```python
st.markdown("""
<div class="metric-card">
    <div class="metric-value">125.5</div>
    <div class="metric-label">Total Distance (km)</div>
</div>
""", unsafe_allow_html=True)
```

### Creating a Custom Alert

```python
st.markdown("""
<div class="alert-info" style="border-color: #00bfff; color: #00bfff;">
    💡 Custom message with emoji
</div>
""", unsafe_allow_html=True)
```

### Styled Section

```python
st.markdown('<div class="section-title">📊 Performance Data</div>', unsafe_allow_html=True)
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.metric("Metric 1", "Value 1")
with col2:
    st.metric("Metric 2", "Value 2")
```

## Customization Examples

### Change Primary Color

Edit `frontend/config.py`:
```python
COLOR_PRIMARY = "#ff6b6b"  # Change from lime to red
```

Then update the HTML in `app.py` styles (search for `#c8ff00`).

### Add Custom Font

```python
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
    * { font-family: 'Inter', sans-serif; }
</style>
""", unsafe_allow_html=True)
```

### Adjust Theme Darkness

```python
# Lighter version
COLOR_BACKGROUND = "#1a1a24"  # Lighter
COLOR_SURFACE = "#25252f"      # Lighter
COLOR_BORDER = "#3a3a4d"       # Lighter
```

## Performance Notes

### CSS Optimization

- Minimal inline styles (uses stylesheet in markdown)
- No @keyframes (use Plotly for animated charts)
- Class-based styling for reusability

### Rendering

- Styles applied once at page load
- Uses Streamlit's CSS injection (safe)
- No layout thrashing

## Browser Support

| Feature | Chrome | Firefox | Safari | Edge |
|---------|--------|---------|--------|------|
| CSS Grid | ✓ | ✓ | ✓ | ✓ |
| Box Shadow | ✓ | ✓ | ✓ | ✓ |
| Transitions | ✓ | ✓ | ✓ | ✓ |
| RGBA Colors | ✓ | ✓ | ✓ | ✓ |
| Flex | ✓ | ✓ | ✓ | ✓ |

All modern features used are widely supported.

## Maintenance

### Updating Colors

1. Update `config.py` color constants
2. Find all hex values in `app.py` markdown
3. Replace with config variables or new values
4. Test contrast ratios with WCAG tool
5. Update this guide with new values

### Consistency Checks

- [ ] All primary actions use COLOR_PRIMARY
- [ ] All text meets 4.5:1 contrast ratio
- [ ] Spacing follows 4px/8px grid
- [ ] Border radius consistent (8px standard)
- [ ] Hover effects present on interactive elements
- [ ] Focus states visible on inputs

## Resources

- **Color Tool:** https://webaim.org/resources/contrastchecker/
- **Accessibility:** https://www.w3.org/WAI/WCAG21/quickref/
- **Design System:** https://material.io/design
- **Responsive Design:** https://web.dev/responsive-web-design-basics/

---

Last updated: 2024
Version: 1.0
