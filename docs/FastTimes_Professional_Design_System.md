# 🎨 FAST TIMES - PROFESSIONAL DESIGN SYSTEM
## Instagram Branding System (Aligned with fasttimes-web.vercel.app)

**Brand:** Fast Times | Elite Coaching + Data-Driven Training  
**Web Fonts:** Barlow Condensed (Headlines) | Barlow (Body) | JetBrains Mono (Data)  
**Color System:** Navy + Red Gradient Aesthetic  
**Design Philosophy:** Minimalist Professional | Dark Mode First | Data-Centric  

---

## 1️⃣ COLOR PALETTE (Direct from Website)

### Core Brand Colors

```
NAVY SYSTEM (Backgrounds)
━━━━━━━━━━━━━━━━━━━━━━
Navy-0 (Primary BG)
HEX:     #060a1c
RGB:     6, 10, 28
Usage:   Post backgrounds, hero sections

Navy-1 (Card BG)
HEX:     #0a1230
RGB:     10, 18, 48
Usage:   Cards, elevated surfaces

Navy-2 (Hover State)
HEX:     #0e1638
RGB:     14, 22, 56
Usage:   Hover backgrounds, separators

Navy-3 (Active State)
HEX:     #131e44
RGB:     19, 30, 68
Usage:   Selected states, borders

━━━━━━━━━━━━━━━━━━━━━━
RED SYSTEM (Primary Accent)
━━━━━━━━━━━━━━━━━━━━━━
Red Primary
HEX:     #E11D2E
RGB:     225, 29, 46
Usage:   CTA buttons, headlines, emphasis

Red High (Hover/Glow)
HEX:     #ff3a4b
RGB:     255, 58, 75
Usage:   Hover state, animations, glow effects

Red Soft (Background)
HEX:     rgba(225,29,46,0.16)
RGB:     225, 29, 46 @ 16% opacity
Usage:   Eyebrow badges, background tints

━━━━━━━━━━━━━━━━━━━━━━
ACCENT COLORS (Secondary)
━━━━━━━━━━━━━━━━━━━━━━
Cyan (Data/Metrics)
HEX:     #18E6D8
RGB:     24, 230, 216
Usage:   Numbers, data highlights, interactive elements

Green (Success/Positive)
HEX:     #2BD67B
RGB:     43, 214, 123
Usage:   Achievements, positive metrics, growth

Gold (Premium/Highlight)
HEX:     #FFB020
RGB:     255, 176, 32
Usage:   Premium indicators, special highlights

Violet (Secondary Accent)
HEX:     #9D7BFF
RGB:     157, 123, 255
Usage:   Tertiary CTA, subtle highlights

━━━━━━━━━━━━━━━━━━━━━━
TEXT & UTILITIES
━━━━━━━━━━━━━━━━━━━━━━
Text Primary
HEX:     #f4f6ff
RGB:     244, 246, 255
Usage:   Headlines, primary text

Mute (Secondary Text)
HEX:     rgba(232,237,255,0.6)
RGB:     232, 237, 255 @ 60% opacity
Usage:   Body text, descriptions

Mute-2 (Tertiary Text)
HEX:     rgba(232,237,255,0.4)
RGB:     232, 237, 255 @ 40% opacity
Usage:   Captions, metadata

Line (Borders)
HEX:     rgba(255,255,255,0.08)
RGB:     255, 255, 255 @ 8% opacity
Usage:   Dividers, subtle borders

Line-2 (Stronger Borders)
HEX:     rgba(255,255,255,0.14)
RGB:     255, 255, 255 @ 14% opacity
Usage:   Card borders, visible separators
```

### Gradient System

```
HERO GRADIENT (Red → Orange → Gold)
Direction: 135deg
From:      #ff3a4b (Red-Hi)
Via:       #ff7a35 (Orange)
To:        #ffb020 (Gold)
Usage:     Headlines, gradients, bold accents

CARD GRADIENT (Subtle Red Tint)
Direction: 135deg
From:      rgba(225,29,46,.18)
To:        rgba(225,29,46,.05)
Border:    rgba(225,29,46,.25)
Usage:     CTA pill backgrounds, featured cards

BACKGROUND GRADIENT (Radial + Linear)
Radial 1:  1200px 700px @ 80% -10% | rgba(225,29,46,0.18) → transparent
Radial 2:  900px 600px @ 10% 20% | rgba(20,40,120,0.5) → transparent
Linear:    180deg | #060a1c 0% → #080d22 100%
Usage:     Page background layering
```

---

## 2️⃣ TYPOGRAPHY SYSTEM

### Fonts Stack (Google Fonts)

**Primary Font - Headlines:**
```
Font:      Barlow Condensed
Weights:   400, 700, 800, 900
Styles:    Normal, Italic
Usage:     H1, H2, hero, brand, emphasis
Family:    'Barlow Condensed', sans-serif
Characteristics: Condensed, high-impact, sporty, modern
Import:    fonts.googleapis.com/css2?family=Barlow+Condensed
```

**Secondary Font - Body:**
```
Font:      Barlow
Weights:   400, 500, 600, 700
Usage:     Body text, descriptions, UI labels
Family:    'Barlow', system-ui, sans-serif
Characteristics: Clean, readable, professional
Import:    fonts.googleapis.com/css2?family=Barlow
```

**Monospace Font - Data:**
```
Font:      JetBrains Mono
Weights:   400, 500, 600
Usage:     Metrics, numbers, code-like data
Family:    'JetBrains Mono', monospace
Characteristics: Precise, data-focused, technical
Import:    fonts.googleapis.com/css2?family=JetBrains+Mono
```

### Typography Scale

```
────────────────────────────────────────────────────────

H1 - MAIN HEADLINE (Hero/Title)
  Font Family:    Barlow Condensed
  Font Size:      clamp(48px, 7vw, 116px) [Responsive]
  Font Weight:    900
  Font Style:     Italic
  Line Height:    0.88
  Letter Spacing: -0.01em
  Text Transform: UPPERCASE
  Color:          Gradient (Red→Orange→Gold) or #f4f6ff
  Margin:         0 0 28px 0
  Max Width:      520px
  Word Break:     break-word, hyphens: auto
  
  Example: "METE TU MEJOR MARCA"
  
────────────────────────────────────────────────────────

H2 - SECONDARY HEADLINE
  Font Family:    Barlow Condensed
  Font Size:      clamp(32px, 5vw, 72px)
  Font Weight:    800
  Font Style:     Italic
  Line Height:    1.0
  Letter Spacing: 0em
  Text Transform: UPPERCASE
  Color:          #f4f6ff
  Margin:         0 0 20px 0
  
  Example: "PLANES DE ENTRENAMIENTO"

────────────────────────────────────────────────────────

H3 - TERTIARY HEADLINE
  Font Family:    Barlow Condensed
  Font Size:      clamp(24px, 4vw, 48px)
  Font Weight:    700
  Font Style:     Italic
  Line Height:    1.1
  Letter Spacing: 0em
  Text Transform: UPPERCASE
  Color:          #f4f6ff
  Margin:         0 0 16px 0
  
  Example: "ZONA AERÓBICA"

────────────────────────────────────────────────────────

LEAD - MAIN DESCRIPTION
  Font Family:    Barlow
  Font Size:      17px
  Font Weight:    400
  Line Height:    1.55
  Letter Spacing: 0em
  Color:          rgba(232,237,255,0.6) [Mute]
  Margin:         0 0 36px 0
  Max Width:      520px
  
  Bold emphasis:  font-weight: 600, color: #f4f6ff
  
  Example: "El 89% de runners entrena en la zona equivocada"

────────────────────────────────────────────────────────

BODY TEXT
  Font Family:    Barlow
  Font Size:      16px
  Font Weight:    400
  Line Height:    1.6
  Letter Spacing: 0em
  Color:          rgba(232,237,255,0.6) [Mute]
  Margin:         0 0 16px 0
  
  Example: Caption text, descriptions, paragraphs

────────────────────────────────────────────────────────

LABEL - UI TEXT
  Font Family:    Barlow
  Font Size:      13px
  Font Weight:    600
  Letter Spacing: 0.14em
  Text Transform: UPPERCASE
  Color:          #f4f6ff
  
  Example: Button text, navigation, labels

────────────────────────────────────────────────────────

EYEBROW - DATA TAG
  Font Family:    JetBrains Mono
  Font Size:      12px
  Font Weight:    600
  Letter Spacing: 0.18em
  Text Transform: UPPERCASE
  Color:          #ffd9de (light red)
  Emphasis:       color: #18E6D8 [Cyan] for numbers
  Margin:         0 0 28px 0
  Padding:        8px 14px
  Border Radius:  999px
  Background:     rgba(225,29,46,0.08)
  Border:         1px solid rgba(225,29,46,0.3)
  
  Example: "10+ AÑOS ENTRENANDO"

────────────────────────────────────────────────────────

METRIC - DATA NUMBERS
  Font Family:    JetBrains Mono
  Font Size:      18px-32px (context-dependent)
  Font Weight:    600
  Letter Spacing: 0em
  Color:          #18E6D8 [Cyan] or Gradient
  
  Example: "320+", "94%", "55:30"

────────────────────────────────────────────────────────

CAPTION - SMALL TEXT
  Font Family:    Barlow
  Font Size:      14px
  Font Weight:    400
  Line Height:    1.5
  Color:          rgba(232,237,255,0.4) [Mute-2]
  
  Example: Metadata, dates, minor text
```

---

## 3️⃣ SPACING & SIZING

### Base Unit System
```
Base Unit: 8px (8, 14, 16, 18, 28, 36, 40, 60, 80px)
Grid:      80px x 80px overlay
Breakpoints:
  - Mobile:       320px - 767px
  - Tablet:       768px - 1024px
  - Desktop:      1025px+
```

### Padding & Margins

```
INSTAGRAM POSTS
  Header Padding:     14px horizontal, 14px vertical
  Image Area:         Fullbleed (no padding)
  Caption Padding:    18px
  CTA Button Padding: 18px horizontal, 22px vertical
  Safe Area Margin:   48px (for text at edges)

CARDS & COMPONENTS
  Card Padding:       18px-28px (varies by context)
  Card Margin:        16px bottom
  Border Radius:      14px (buttons), 10px (secondary)
  
  Button Padding:     18px 22px (primary)
                      16px 20px (secondary)
  
  Gap/Gap between:    14px (horizontal), 14px (vertical)
  
SECTIONS
  Horizontal Margin:  40px (desktop), 28px (tablet), 20px (mobile)
  Vertical Margin:    60px (large), 36px (medium), 28px (small)
  Max Content Width:  1320px

HERO SECTION
  Padding Top:        60px
  Padding Bottom:     80px
  Padding Horizontal: 40px
  Min Height:         calc(100vh - 80px)
  Grid Gap:           60px
```

---

## 4️⃣ COMPONENTS & EFFECTS

### Buttons

```
PRIMARY BUTTON (CTA)
  Background:       linear-gradient(135deg, #ff3a4b 0%, #E11D2E 100%)
  Text Color:       #ffffff
  Text Weight:      700
  Text Transform:   UPPERCASE
  Font Size:        14px
  Letter Spacing:   0.06em
  Padding:          18px 22px
  Border Radius:    14px
  Border:           1px solid transparent
  Box Shadow:       0 10px 40px -10px rgba(225,29,46,0.7),
                    inset 0 1px 0 rgba(255,255,255,0.18)
  Hover:
    - Transform:    translateY(-1px)
    - Box Shadow:   0 16px 50px -10px rgba(225,29,46,0.85),
                    inset 0 1px 0 rgba(255,255,255,0.25)
  Transition:       transform 0.15s ease, box-shadow 0.2s ease
  
  Example Text: "HABLEMOS"

GHOST BUTTON (Secondary)
  Background:       rgba(255,255,255,0.03)
  Border:           1px solid rgba(255,255,255,0.14)
  Text Color:       #f4f6ff
  Text Weight:      700
  Padding:          18px 22px
  Border Radius:    14px
  Hover:
    - Background:   rgba(255,255,255,0.06)
    - Border:       1px solid rgba(255,255,255,0.2)

ICON BUTTON
  Width/Height:     38px
  Border Radius:    10px
  Background:       rgba(255,255,255,0.04)
  Border:           1px solid rgba(255,255,255,0.08)
  Color:            #f4f6ff
  Hover Background: rgba(255,255,255,0.08)
```

### Cards

```
STANDARD CARD
  Background:       #0a1230 [Navy-1] or rgba(225,29,46,0.08)
  Border:           1px solid rgba(255,255,255,0.08)
  Border Radius:    14px
  Padding:          18px-28px
  Box Shadow:       None (minimal aesthetic)
  Hover Border:     rgba(255,255,255,0.14)
  Transition:       border-color 0.2s ease

FEATURED/HIGHLIGHT CARD
  Background:       Gradient: 135deg from rgba(225,29,46,0.18) to rgba(225,29,46,0.05)
  Border:           1px solid rgba(225,29,46,0.25)
  Padding:          18px 28px
  Border Radius:    14px
  Glow:             0 0 20px rgba(225,29,46,0.1)
```

### Badges & Pills

```
EYEBROW BADGE (Red Tint)
  Background:       rgba(225,29,46,0.08)
  Border:           1px solid rgba(225,29,46,0.3)
  Border Radius:    999px (full pill)
  Padding:          8px 14px
  Font:             JetBrains Mono, 12px, 600
  Text Transform:   UPPERCASE
  Letter Spacing:   0.18em
  Color:            #ffd9de (light red)
  
  Highlight color:  #18E6D8 [Cyan] for numbers/emphasis

METRIC BADGE
  Background:       rgba(24,230,216,0.1) [Cyan tint]
  Border:           1px solid rgba(24,230,216,0.3)
  Color:            #18E6D8
  Font:             JetBrains Mono
  Padding:          6px 12px
  Border Radius:    8px

DISCIPLINE BADGE
  Background:       One of: #ff3a4b (running), #18E6D8 (swim), etc.
  Color:            #ffffff
  Font:             Barlow Condensed, 14px, 700, UPPERCASE
  Padding:          8px 16px
  Border Radius:    10px
  Text Style:       Italic
```

### Visual Effects

```
BACKDROP BLUR
  Used on: Navigation, modals, overlays
  Blur:    10px
  Browser: -webkit-backdrop-filter: blur(10px)
           backdrop-filter: blur(10px)

GLOW / BOX SHADOW
  Subtle:  0 2px 8px rgba(0,0,0,0.2)
  Medium:  0 8px 24px rgba(0,0,0,0.3)
  Strong:  0 16px 48px rgba(0,0,0,0.4)
  Red Glow: 0 0 20px rgba(225,29,46,0.3)

TEXTURE OVERLAY
  Type:    SVG Fractal Noise (feTurbulence)
  Opacity: 0.5
  Blend:   Mix-blend-mode: overlay
  Effect:  Subtle grainy texture across all pages

GRID OVERLAY
  Pattern: 80px x 80px grid
  Color:   rgba(255,255,255,0.03)
  Opacity: 0.35
  Mask:    Radial gradient (visible at center-top)
  Effect:  Subtle technical grid aesthetic

GRADIENTS
  Hero:    linear-gradient(135deg, #ff3a4b, #ff7a35, #ffb020)
  Text:    -webkit-background-clip: text
           background-clip: text
           -webkit-text-fill-color: transparent
           color: transparent

TRANSITIONS
  Fast:    0.15s ease (transforms)
  Medium:  0.2s ease (colors, shadows)
  Slow:    0.3s ease (complex animations)
```

---

## 5️⃣ INSTAGRAM POST TEMPLATES

### TEMPLATE A: EDUCATIVO (Dark + Gradient Headline)

```
LAYOUT (1080 x 1350px):
┌─────────────────────────────────────────┐
│  [EYEBROW BADGE]                        │
│  "💪 10+ AÑOS ENTRENANDO"               │
│                                         │
│  [H1 HEADLINE - GRADIENT]               │
│  "METE TU MEJOR MARCA"                  │
│  (Red→Orange→Gold gradient text)        │
│                                         │
│  [LEAD TEXT - MUTE]                     │
│  "El 89% de runners entrena en la       │
│   zona equivocada. ¿Cuál es la tuya?"   │
│                                         │
│  [METRIC BOXES - CYAN]                  │
│  4 boxes in 2x2 grid:                   │
│  🔵 AERÓBICA          🟡 TEMPO          │
│  🟠 VO2 MAX           🔴 ANAERÓBICA     │
│                                         │
│  [CTA TEXT]                             │
│  "📌 Guarda | 💬 Comenta tu zona"       │
│                                         │
└─────────────────────────────────────────┘

COLORS:
  Background:     #060a1c [Navy-0]
  Headline:       Gradient (Red→Gold)
  Body Text:      rgba(232,237,255,0.6) [Mute]
  CTA:            #18E6D8 [Cyan]
  Boxes:          rgba(24,230,216,0.1) backgrounds with cyan borders
```

### TEMPLATE B: OFERTA (Card-Based Comparison)

```
LAYOUT (1080 x 1350px):
┌─────────────────────────────────────────┐
│  [HEADER BANNER - RED GRADIENT]         │
│  "PLANES PERSONALIZADOS"                │
│  Red→Orange gradient, white text        │
│                                         │
│  [3 PLAN CARDS IN ROW]                  │
│                                         │
│  Card 1 (Left):                         │
│  ┌──────────────────────┐               │
│  │ AMATEUR              │               │
│  │ $99/mes              │               │
│  │ • Análisis básico    │               │
│  │ • Planes automáticos │               │
│  └──────────────────────┘               │
│  Border: rgba(255,255,255,0.08)         │
│                                         │
│  Card 2 (Center - FEATURED):            │
│  ┌──────────────────────┐               │
│  │ COMPETITIVO ✓        │               │
│  │ $299/mes             │               │
│  │ • Data Engine        │               │
│  │ • Video reviews      │               │
│  │ • +30 atletas        │               │
│  └──────────────────────┘               │
│  Background: rgba(225,29,46,0.08)       │
│  Border: 2px #ff3a4b [Red-Hi]           │
│  Glow: 0 0 20px rgba(225,29,46,0.2)     │
│                                         │
│  Card 3 (Right):                        │
│  ┌──────────────────────┐               │
│  │ PRO                  │               │
│  │ $799/mes             │               │
│  │ • Todo lo anterior   │               │
│  │ • Mentoría 1-1       │               │
│  └──────────────────────┘               │
│  Border: rgba(255,255,255,0.08)         │
│                                         │
│  [PRIMARY CTA BUTTON]                   │
│  "HABLEMOS"                             │
│  Gradient: Red→Dark Red                 │
│  Shadow: 0 10px 40px -10px red-glow     │
│                                         │
└─────────────────────────────────────────┘

COLOR SCHEME:
  Background:     #060a1c [Navy-0]
  Cards:          #0a1230 [Navy-1] or with red tint
  Featured:       Red gradient card (emphasized)
  Text:           #f4f6ff (headers), rgba(232,237,255,0.6) (body)
  Button:         Red gradient with glow
```

### TEMPLATE C: TESTIMONIO (Before/After + Stats)

```
LAYOUT (1080 x 1350px):
┌─────────────────────────────────────────┐
│  [CUSTOMER PROFILE HEADER]              │
│  Avatar (48x48px circular)              │
│  "Juan Pérez" (H3)                      │
│  "Corredor • PB en 10K" (Small)         │
│                                         │
│  [QUOTE - GRADIENT STYLED]              │
│  "El análisis fisiológico fue clave"    │
│  Color: Red gradient, Italic            │
│  Size: 24px, Barlow Condensed           │
│  Border-left: 2px #ff3a4b               │
│                                         │
│  [STATS GRID - 3 COLUMNS]               │
│  ┌──────────────────────────────────┐   │
│  │ 55:30  │  →  │  48:45             │   │
│  │ ANTES  │     │  DESPUÉS           │   │
│  │        │     │                    │   │
│  │   MEJORA: -6:45 (12%)             │   │
│  │   COLOR: #18E6D8 [Cyan]           │   │
│  └──────────────────────────────────┘   │
│                                         │
│  [TESTIMONIAL BODY]                     │
│  "El plan personalizado me ayudó a...   │
│   entender mis zonas de entrenamiento"  │
│                                         │
│  [RATING]                               │
│  ⭐⭐⭐⭐⭐                             │
│  "Altamente recomendado"                │
│                                         │
│  [CTA]                                  │
│  "Quiero mi transformación →"           │
│  Button: Red gradient                   │
│                                         │
└─────────────────────────────────────────┘

COLOR PALETTE:
  Background:     #060a1c [Navy-0]
  Quote:          Gradient (Red→Orange)
  Stats:          #18E6D8 [Cyan] for numbers
  Rating:         #ffb020 [Gold] for stars
  CTA Button:     Red gradient
```

### TEMPLATE D: DATA-DRIVEN CAROUSEL (Slide Example)

```
STRUCTURE: 5-7 slides of 1080x1350px each

SLIDE 1 (Cover):
┌─────────────────────────────────────────┐
│  [EYEBROW]                              │
│  "📊 ANÁLISIS FISIOLÓGICO"              │
│                                         │
│  [H1 GRADIENT]                          │
│  "LAS 4 ZONAS"                          │
│                                         │
│  [METRIC BADGE - CYAN]                  │
│  "320+ RESULTADOS"                      │
│                                         │
│  [SMALL TEXT]                           │
│  "Desliza → para descubrir tu zona"     │
│                                         │
└─────────────────────────────────────────┘

SLIDES 2-5 (Content):
┌─────────────────────────────────────────┐
│  [ZONE ICON - LARGE CIRCLE]             │
│  🔵 (Colored by zone)                   │
│                                         │
│  [ZONE NAME - H2 ITALIC]                │
│  "ZONA AERÓBICA"                        │
│                                         │
│  [METRICS - CYAN]                       │
│  FC: 120-150 bpm                        │
│  % FTP: 60-70%                          │
│  Esfuerzo: Conversación fácil           │
│                                         │
│  [STAT - EYEBROW BADGE]                 │
│  "El 40% no maximiza esta zona"         │
│                                         │
│  [VISUAL ELEMENT]                       │
│  Small graph or icon                    │
│                                         │
└─────────────────────────────────────────┘

ZONE COLOR CODING:
  Aeróbica:     #18E6D8 [Cyan]
  Tempo:        #FFB020 [Gold]
  VO2 Max:      #ff3a4b [Red]
  Anaeróbica:   #9D7BFF [Violet]
```

### TEMPLATE E: REELS (Video 9:16)

```
DIMENSIONS: 1080 x 1920px (16:9 safe area)
DURATION:   15-30 seconds
SAFE ZONES: Top 80px, Bottom 100px

STRUCTURE:

[0-1s] HOOK (Eye-catching)
  Text (size 56px, bold, Barlow Condensed):
    "3 ERRORES EN RUNNING"
  Background: Red gradient (Red→Orange)
  No image needed, just bold text

[1-5s] CONTENT (Educational)
  Split screen or transitions
  Subtitles CC (white text, JetBrains Mono)
  Transitions: 200ms ease-out
  Music: Motivational / Energetic

[5-8s] DEMONSTRATION (Data)
  Animated graphs / numbers
  Metrics in cyan (#18E6D8)
  Growing/scaling animations

[8-10s] CTA (Clear Call to Action)
  Large text (48px):
    "VER PLAN COMPLETO"
  Button: Red gradient
  Subtext: "Link en bio"
  Color: #f4f6ff

AUDIO:
  Music:       Motivational, tempo 120-130 BPM
  Voice:       Clear Spanish, natural pace
  SFX:         Subtle (pop/ding on transitions)
  CC:          Always enabled, white text

COLOR USAGE:
  Background:  Navy-0 (#060a1c)
  Text:        #f4f6ff or white
  Highlights:  #ff3a4b (Red-Hi), #18E6D8 (Cyan)
  CTA:         Red gradient button
  Transitions: Smooth dissolves or wipes
```

---

## 6️⃣ MANDATORY ELEMENTS PER POST

✅ **Every Post Must Have:**

1. **Eyebrow Badge (Top-Left)**
   - JetBrains Mono, 12px, uppercase
   - Example: "💪 10+ AÑOS" or "📊 DATO"
   - Background: rgba(225,29,46,0.08)
   - Border: rgba(225,29,46,0.3)

2. **Main Headline (H1)**
   - Barlow Condensed, 48px+, 900, ITALIC, UPPERCASE
   - Color: Gradient (Red→Gold) OR #f4f6ff
   - Max 5 words

3. **Body Text (H3 or Lead)**
   - Barlow, 16-17px, regular
   - Color: rgba(232,237,255,0.6)
   - Clarifies the headline

4. **Data Element**
   - JetBrains Mono, cyan color (#18E6D8)
   - Example: "320+", "94%", "55:30"
   - Minimum 1 metric per post

5. **Primary CTA (Button)**
   - Red gradient background
   - White text, 14px, bold, uppercase
   - Clear action: "HABLEMOS", "VER PLANES", "APRENDE"
   - Box shadow with red glow

6. **Brand Mark (Optional but Recommended)**
   - Small logo bottom-right
   - 40% opacity
   - 60x60px

---

## 7️⃣ INSTAGRAM STORIES (Optional)

```
DIMENSIONS: 1080 x 1920px
DURATION:   5-10 seconds

STORY TYPE 1 - QUICK TIP
  Background: Red gradient (Red→Orange)
  Headline: 48px, Barlow Condensed, white, UPPERCASE
  Subtext: 24px, Barlow, white
  
  Example:
  "TIP RÁPIDO"
  "Never start at goal pace"

STORY TYPE 2 - POLL/QUESTION
  Background: Navy-0
  Question: 32px, white, Barlow Condensed
  Options: Cyan borders, Interactive
  
  Example:
  "¿Cuál es tu zona fuerte?"
  [Aeróbica] [Tempo] [VO2] [Anaero]

STORY TYPE 3 - COUNTDOWN
  Background: Red gradient
  Large number (72px+): #18E6D8 [Cyan]
  Message: 24px, white
  
  Example:
  "3" (days)
  "INSCRIPCIONES ABREN"

STORY TYPE 4 - PROMO
  Background: Navy + red tint
  Offer: Bold, large
  CTA: Red gradient button overlay
  Urgency: Time-sensitive message
  
  Example:
  "HOY: -20% EN PLANES"
  [APROVECHA AHORA]
```

---

## 8️⃣ CHECKLIST PRE-PUBLICAR

```
DESIGN QUALITY
  ☐ Headline uses Barlow Condensed, uppercase, italic
  ☐ Body text uses Barlow, 16px+, proper color
  ☐ Data uses JetBrains Mono, cyan color
  ☐ Background is Navy-0 (#060a1c) or dark
  ☐ Red element present (#ff3a4b or #E11D2E)

COLORS & CONTRAST
  ☐ Text contrast meets 4.5:1 minimum (light on dark)
  ☐ Buttons have red gradient + shadow
  ☐ Badge colors match brand palette
  ☐ No generic colors, all from palette

SPACING & SIZING
  ☐ Headline has 28px margin-bottom
  ☐ Body has 36px margin-bottom
  ☐ CTA button is 18px padding (V) x 22px (H)
  ☐ All spacing in multiples of 8px (safe)

CTA & ENGAGEMENT
  ☐ Clear CTA present (comment, save, link, DM)
  ☐ CTA is in red gradient button style
  ☐ CTA text is uppercase & bold
  ☐ Multiple CTAs if applicable (icon + text)

PROFESSIONALISM
  ☐ No emoji clutter (max 3 strategic)
  ☐ Font sizes are responsive & readable
  ☐ Borders use rgba lines, not solid
  ☐ Shadows are subtle, not harsh
  ☐ Brand consistency with web design
```

---

## 9️⃣ COLOR REFERENCE QUICK LOOKUP

| Use Case | Color | HEX | RGB |
|----------|-------|-----|-----|
| Post Background | Navy-0 | #060a1c | 6,10,28 |
| Headline Gradient | Red→Orange→Gold | #ff3a4b→#ff7a35→#ffb020 | — |
| Primary Text | Off-White | #f4f6ff | 244,246,255 |
| Secondary Text | Mute | rgba(232,237,255,0.6) | 232,237,255@60% |
| CTA Button | Red Gradient | #ff3a4b→#E11D2E | — |
| Data Highlights | Cyan | #18E6D8 | 24,230,216 |
| Success Indicator | Green | #2BD67B | 43,214,123 |
| Premium Mark | Gold | #FFB020 | 255,176,32 |
| Card Border | Line | rgba(255,255,255,0.08) | 255,255,255@8% |
| Featured Border | Line-2 | rgba(255,255,255,0.14) | 255,255,255@14% |

---

## 🔟 FONTS IMPORT CODE

```html
<!-- Add to HTML <head> -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,400;0,700;0,800;0,900;1,800;1,900&family=Barlow:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

---

## ➖ WHAT NOT TO DO (Anti-Patterns)

❌ Use system fonts (Arial, Helvetica) instead of brand fonts  
❌ Light text on light backgrounds (contrast fails)  
❌ Use bright colors outside palette (breaks consistency)  
❌ Emojis as main design elements  
❌ More than 3 font sizes per post  
❌ Posts without red (#ff3a4b) accent  
❌ Vague CTAs ("Click here" instead of "HABLEMOS")  
❌ All uppercase body text (headlines only)  
❌ Harsh shadows (must be subtle)  
❌ Gradients that don't use brand colors  

---

## 📋 NEXT STEPS

1. **Export this palette** → Create Canva Brand Kit
2. **Install fonts** → Google Fonts (Barlow Condensed, Barlow, JetBrains Mono)
3. **Create 5 templates** → Using layouts A-E
4. **Design batch** → 4 posts (test the system)
5. **Launch** → Monitor engagement, iterate

---

**Professional Design System v2.0**  
*Aligned with fasttimes-web.vercel.app*  
*Built on Barlow + JetBrains Mono + Navy + Red Aesthetic*  
*June 2026*
