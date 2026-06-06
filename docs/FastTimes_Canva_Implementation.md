# 🎯 FAST TIMES CANVA IMPLEMENTATION GUIDE
## Professional Design System Setup

**Status:** Ready to implement  
**Fonts:** Barlow Condensed | Barlow | JetBrains Mono  
**Color System:** Navy + Red Gradient Aesthetic  
**Templates:** 3 Main + 2 Variations  

---

## STEP 1: Setup Brand Kit in Canva

### 1.1 Create Brand Kit
1. Go to **Canva.com** → Sign in
2. Click **Apps** (bottom left) → **Brand Kit**
3. Click **"Create a new brand kit"**
4. Name it: **"Fast Times Professional"**

### 1.2 Add Core Colors

**Copy these HEX codes into Canva:**

| Color Name | HEX | Usage |
|-----------|-----|-------|
| Navy-0 | #060a1c | Post backgrounds |
| Navy-1 | #0a1230 | Cards, elevated |
| Navy-2 | #0e1638 | Hover states |
| Red Primary | #E11D2E | Buttons, accents |
| Red-Hi | #ff3a4b | Hover, glow |
| Cyan | #18E6D8 | Data, metrics |
| Gold | #FFB020 | Premium, highlights |
| Green | #2BD67B | Success |
| Violet | #9D7BFF | Secondary accent |
| Text | #f4f6ff | Headlines |
| Mute | rgba(232,237,255,0.6) | Body text |

**How to add in Canva:**
1. In Brand Kit → Click "**Add a color**"
2. Paste HEX code
3. Name the color (e.g., "Navy-0")
4. Click **"Save color"**
5. Repeat for all 11 colors

### 1.3 Add Fonts

**Go to Brand Kit → Fonts**

1. **Primary Font (Headlines):**
   - Font: **Barlow Condensed**
   - Set as: **Heading**
   - Source: Google Fonts (automatic in Canva)

2. **Secondary Font (Body):**
   - Font: **Barlow**
   - Set as: **Body**

3. **Tertiary Font (Data):**
   - Font: **JetBrains Mono**
   - Set as: **Custom**

**Save Brand Kit** → Click **"Save"** button

---

## STEP 2: Create Master Templates

### 2.1 Template A: EDUCATIVO (1080 x 1350px)

**Create New Design:**
1. Click **"Create a design"**
2. Select **Custom size**
3. Width: **1080**, Height: **1350**
4. Click **"Create design"**

**Build the Template:**

**Layer 1 - Background:**
- Click **"Elements"** → **"Shapes"** → **"Rectangle"**
- Size: Full canvas (1080 x 1350)
- Color: Navy-0 (#060a1c)
- NO border

**Layer 2 - Eyebrow Badge:**
- Click **"Text"** → Add text
- Content: "💪 10+ AÑOS ENTRENANDO"
- Font: **JetBrains Mono**, 12px, 600 weight, **UPPERCASE**
- Color: #ffd9de (light red)
- Background: Shape → Rectangle → rgba(225,29,46,0.08)
- Border radius: 20px (pill shape)
- Position: Top-left, 28px margin

**Layer 3 - Headline:**
- Click **"Text"** → Add text
- Content: "METE TU MEJOR MARCA"
- Font: **Barlow Condensed**, 56px, 900 weight, **ITALIC**, **UPPERCASE**
- Apply **GRADIENT**: Red (#ff3a4b) → Orange (#ff7a35) → Gold (#ffb020)
- Position: Top-left, below eyebrow, 28px margin
- Max width: ~400px

**Layer 4 - Description:**
- Add text
- Content: "El 89% de runners entrena en la zona equivocada"
- Font: **Barlow**, 18px, 400 weight
- Color: Mute (rgba(232,237,255,0.6))
- Line spacing: 1.6

**Layer 5 - Metric Grid (4 boxes):**
- Create 4 text boxes in 2x2 grid
- Each box:
  - Background: rgba(24,230,216,0.05)
  - Border: 1px, #18E6D8
  - Border radius: 10px
  - Text: "🔵 AERÓBICA" (or TEMPO, VO2, ANAERO)
  - Font: Barlow, 14px, 600 weight
  - Color: #18E6D8
  - Padding: 12px

**Layer 6 - CTA Text:**
- Add text: "📌 Guarda | 💬 Comenta tu zona"
- Font: Barlow, 14px, 500 weight
- Color: #18E6D8
- Position: Bottom area

**Save as Template:**
1. Click **"Share"** (top right)
2. Select **"Make it a template"**
3. Name: **"[EDUCATIVO] - Fast Times - Zones"**
4. Click **"Save as template"**

✅ **Done!** Template now appears in your library

---

### 2.2 Template B: OFERTA (1080 x 1350px)

**Create New Design:**
1. Click **"Create a design"** → Custom → 1080 x 1350

**Build:**

**Layer 1 - Background:**
- Rectangle, Navy-0, full canvas

**Layer 2 - Header Banner:**
- Rectangle: 1080 x 180px
- Apply **GRADIENT**: Red (#ff3a4b) → Dark Red (#E11D2E)
- Add text: "PLANES PERSONALIZADOS"
- Font: Barlow Condensed, 40px, 800 weight, ITALIC, UPPERCASE
- Color: White
- Position: Centered in header

**Layer 3 - Plan Cards (3 cards):**
- Create 3 rounded rectangles, arranged horizontally
- Card 1 (Left):
  - Background: #0a1230
  - Border: 1px, rgba(255,255,255,0.08)
  - Size: ~320px width, 200px height
  - Padding: 16px
  
  Content:
  - "AMATEUR" (14px, bold)
  - "$99/mes" (24px, JetBrains Mono, #ff3a4b, bold)
  - "• Análisis básico" (12px)
  - "• Planes automáticos" (12px)

- Card 2 (Center - FEATURED):
  - Background: rgba(225,29,46,0.08)
  - Border: 2px, #ff3a4b
  - Box shadow: 0 0 20px rgba(225,29,46,0.2)
  - Same content structure but "COMPETITIVO ✓"
  - Price: $299/mes
  - Add 3 features

- Card 3 (Right):
  - Same as Card 1 style
  - "PRO" / "$799/mes"

**Layer 4 - Primary Button:**
- Shape: Rectangle, border-radius 14px
- Background: GRADIENT Red→Dark Red
- Add text: "HABLEMOS"
- Font: Barlow, 14px, 700 weight, uppercase, letter-spacing 0.06em
- Color: White
- Padding: 18px 22px
- Box shadow: 0 10px 40px -10px rgba(225,29,46,0.7)
- Position: Center-bottom

**Save as Template:**
- Name: **"[OFERTA] - Fast Times - Plans"**

---

### 2.3 Template C: TESTIMONIO (1080 x 1350px)

**Create New Design:**
1. Click **"Create a design"** → Custom → 1080 x 1350

**Build:**

**Layer 1 - Background:**
- Rectangle, Navy-0, full canvas

**Layer 2 - Customer Header:**
- Avatar circle: 48 x 48px
  - Background: Gradient (Red→Cyan)
  - Position: Top-left
  
- Next to avatar:
  - "Juan Pérez" (14px, bold)
  - "Corredor • 10K" (12px, muted)

**Layer 3 - Quote:**
- Add text: "El análisis fisiológico fue clave"
- Font: Barlow Condensed, 24px, 600 weight, ITALIC
- Color: #ff3a4b
- Border-left: 3px solid #ff3a4b
- Padding-left: 12px
- Line height: 1.5

**Layer 4 - Stats (Before/After):**
- Create 3-column layout:
  - Column 1: "55:30" (JetBrains Mono, 24px, #18E6D8) | "ANTES" (12px, muted)
  - Column 2: "→" (20px)
  - Column 3: "48:45" (JetBrains Mono, 24px, #18E6D8) | "DESPUÉS" (12px, muted)
  
- Background: rgba(24,230,216,0.05)
- Border: 1px, rgba(24,230,216,0.2)
- Border-radius: 10px
- Padding: 16px

**Layer 5 - Improvement Stat:**
- Add text: "MEJORA: -6:45 (12%)"
- Font: JetBrains Mono, 16px, 600 weight
- Color: #18E6D8
- Below stats section

**Layer 6 - Testimonial Body:**
- Add text: "El plan personalizado me ayudó a entender mis zonas de entrenamiento y pude entrenar al máximo"
- Font: Barlow, 16px, 400 weight
- Color: Mute
- Line height: 1.6

**Layer 7 - Rating:**
- Add text: "⭐⭐⭐⭐⭐"
- Below: "Altamente recomendado"
- Font: Barlow, 12px

**Layer 8 - CTA Button:**
- Same style as Template B
- Text: "QUIERO MI TRANSFORMACIÓN"

**Save as Template:**
- Name: **"[TESTIMONIO] - Fast Times - Success"**

---

## STEP 3: Create Variations

### 3.1 Carousel Template (Multi-slide)

Create **5-7 slides** of 1080 x 1350px each:

**Slide 1 - Cover:**
- Background: Gradient (Red→Orange)
- Eyebrow: "📊 ANÁLISIS FISIOLÓGICO"
- Headline: "LAS 4 ZONAS"
- CTA: "Desliza → para descubrir tu zona"

**Slides 2-5 - Content:**
Each slide:
- Zone icon (large, colored)
- Zone name (H2, Barlow Condensed)
- Metrics in cyan (JetBrains Mono)
- Description (Barlow, 16px)
- Relevant stat/badge

**Color Mapping:**
- Slide 2 (Aeróbica): #18E6D8 [Cyan]
- Slide 3 (Tempo): #FFB020 [Gold]
- Slide 4 (VO2): #ff3a4b [Red]
- Slide 5 (Anaero): #9D7BFF [Violet]

**Slide 6 - CTA:**
- Large text: "¿CUÁL ES TU ZONA?"
- Button: Red gradient
- Text: "DIME TU MEJOR MARCA"

---

## STEP 4: Design Workflow

### 4.1 Daily Post Creation (20 min)

**Monday - Educational:**
1. Open Canva
2. Click **"[EDUCATIVO] - Fast Times - Zones"** (your template)
3. Edit:
   - Change headline text
   - Update metrics/data
   - Adjust colors if needed
4. Download as PNG (1080 x 1350)
5. Write caption
6. Schedule on Instagram

**Wednesday - Reels:**
1. Create in Canva or CapCut
2. 15-30 seconds
3. Add CC (captions/subtitles)
4. Export as MP4
5. Upload to Instagram Reels

**Friday - Carousel:**
1. Open **[CAROUSEL] - Fast Times** template
2. Edit each slide
3. Download all as PNG
4. Convert to JPG if needed
5. Upload as carousel (max 10 images)

**Sunday - Testimonial:**
1. Open **[TESTIMONIO] - Fast Times** template
2. Change customer name, avatar, quote, stats
3. Download PNG
4. Post with caption

### 4.2 Batch Design (4 hours, 4 posts)

**Better approach for efficiency:**
1. **Block 1 (1 hour):** Design all 4 Educativo posts
2. **Block 2 (1 hour):** Design all 4 Oferta posts
3. **Block 3 (1 hour):** Design all 4 Testimonios
4. **Block 4 (1 hour):** Download, rename, organize files

**Result:** 4 weeks of content ready, save time daily

---

## STEP 5: Caption Templates

### Educational Caption

```
📊 [METRIC/FACT]

[BODY TEXT - Problem statement]

✅ SOLUTION/KEY INSIGHT
[3-5 bullet points]

🔗 Full plan → link in bio
💬 Comenta: [Question for engagement]

#Running #Triatlón #EntrenamientoConDatos #CoachingPersonalizado
```

**Example:**
```
📊 El 89% de runners entrena EQUIVOCADO

No es culpa tuya. El 89% de corredores entrena en la zona equivocada, lo que reduce mejora del rendimiento hasta en 50%.

✅ LAS 4 ZONAS CORRECTAS
🔵 Aeróbica - Conversación fácil (120-150 bpm)
🟡 Tempo - Incierto pero aguantable (150-170 bpm)
🟠 VO2 Max - Difícil, rápido (170-190 bpm)
🔴 Anaeróbica - Máximo esfuerzo (190+ bpm)

📌 Guarda este post
💬 Comenta: ¿Cuál es TU zona fuerte?
🔗 Planes personalizados → link en bio

#Running #VO2Max #Entrenamiento #FastTimes
```

### Oferta Caption

```
🚀 [MAIN HEADLINE]

[SOCIAL PROOF]
320+ PBs rotos | 94% retención | +10 años

[WHAT YOU GET]
✅ [Benefit 1]
✅ [Benefit 2]
✅ [Benefit 3]

[3 TIERS]
💰 Amateur - $99/mes
💪 Competitivo - $299/mes (Recomendado)
👑 Pro - $799/mes (Agotado)

[CTA]
🔗 Hablemos → link en bio
💬 O escribe por WhatsApp

#EntrenamientoPersonalizado #ResultadosComprobados
```

### Testimonial Caption

```
📈 ANTES → DESPUÉS

[ATHLETE NAME]
[SPORT] | [GOAL]

⏱️ [METRIC BEFORE] → [METRIC AFTER]
🎯 Mejora: [% or time saved]

"[QUOTE]"

⭐⭐⭐⭐⭐ "[SHORT REVIEW]"

🎯 ¿Tu siguiente transformación?
🔗 Link en bio para tu plan personalizado

#Transformación #PB #ResultadosReales
```

---

## STEP 6: Publishing Workflow

### Instagram Scheduling

**Option 1: Native (Free)**
1. Open Instagram
2. Create post
3. Click "Schedule"
4. Select date/time
5. Confirm

**Option 2: Meta Business Suite (Better Analytics)**
1. Go to **business.facebook.com**
2. Connect Instagram
3. Upload image
4. Write caption
5. Schedule
6. View detailed analytics

**Option 3: Later.com (Premium)**
1. Upload images
2. Schedule across platforms
3. Auto-post at optimal times
4. Analytics dashboard

### Posting Schedule

**Optimal times (Spanish audience):**
- **Monday:** 9:00 AM
- **Wednesday:** 7:00 PM
- **Friday:** 6:00 PM
- **Sunday:** 10:00 AM

---

## STEP 7: Monitoring & Optimization

### Weekly Analytics Review

**Track these metrics:**
- Impressions (reach)
- Engagement rate (likes + comments / followers)
- Saves (most important for algorithm)
- Clicks to bio
- DMs received

**What to optimize:**
- Which template type gets highest engagement? → Do more of that
- Which CTA text works best? → Use similar language
- Which time gets highest reach? → Post more at that time
- Which colors stand out? → Emphasize in future posts

### Monthly Content Audit

1. Take 3 best-performing posts
2. Identify pattern (format, topic, CTA, color)
3. Create 4 variations of that style
4. Test for next month

---

## CHECKLIST: Pre-Launch

- [ ] Brand Kit created with 11 colors
- [ ] Fonts (Barlow Condensed, Barlow, JetBrains Mono) installed
- [ ] Template A (Educativo) created & saved
- [ ] Template B (Oferta) created & saved
- [ ] Template C (Testimonio) created & saved
- [ ] Carousel template created with 6 slides
- [ ] First 4 posts designed
- [ ] Captions written
- [ ] All PNGs downloaded (1080x1350px)
- [ ] Instagram bio updated
- [ ] Meta Business Suite connected
- [ ] First posts scheduled

---

## LAUNCH TIMELINE

**Week 1 - Setup (3-4 hours)**
- Create Brand Kit ✓
- Create 3 main templates ✓
- Design first batch (4 posts) ✓

**Week 2 - Publishing (1 hour/day)**
- Monday: Post educativo
- Wednesday: Reels
- Friday: Carousel
- Sunday: Testimonio
- Daily: Respond to comments

**Week 3-4 - Scale (2 hours/day)**
- Batch design more posts
- Analyze what works
- Create variations
- Maintain 4x/week schedule

---

## 🎯 SUCCESS METRICS (30 Days)

If you hit these numbers, you're on the right track:

- ✅ **2,000+ impressions** (good reach)
- ✅ **150-300 comments** (engagement)
- ✅ **100-200 saves** (algorithm loves this)
- ✅ **30-50 clicks to bio** (conversion traffic)
- ✅ **5-10 DMs** (interested prospects)

---

## 💡 PRO TIPS

1. **Use Canva Teams** if you hire a designer (share Brand Kit)
2. **Create Canva Folders** for organization:
   - "FT_Educational"
   - "FT_Oferta"
   - "FT_Testimonials"
   - "FT_Reels"
3. **Use Canva Scheduled Designs** to batch work
4. **Download at 150% scale** for higher quality
5. **Test different posting times** first 2 weeks
6. **Pin top-performing post** to profile
7. **Repost best content** to Stories (link in bio)

---

**You're now ready to build professional, consistent, branded content that converts.**

*Fast Times Professional Design System | Ready to Launch* ✓
