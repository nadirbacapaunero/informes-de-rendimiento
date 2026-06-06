# 🚀 GUÍA RÁPIDA: Cómo Implementar en Canva

## PASO 1: Configurar tu Brand Kit en Canva

### A) Crear Brand Colors
1. Abre Canva → **Apps → Brand Kit**
2. Haz clic en **"Create a Brand Kit"**
3. Carga estos colores:

| Nombre | HEX | Uso |
|--------|-----|-----|
| Rojo Dinámico | #E63946 | Botones, Headlines |
| Azul Marino | #1B2E5A | Headers, Fondos |
| Azul Cielo | #4A90E2 | Ciclismo |
| Turquesa | #17A2B8 | Natación |
| Púrpura | #6F42C1 | Triatlón |
| Verde Éxito | #27AE60 | Logros |
| Naranja Alerta | #F39C12 | Advertencias |
| Gris Oscuro | #2C3E50 | Texto principal |
| Gris Medio | #7F8C8D | Subtexto |
| Gris Claro | #E8EAED | Bordes |

✅ Guarda como **"Fast Times Official"**

### B) Agregar Fuentes
1. En el mismo Brand Kit → **Fonts**
2. Agrega:
   - **Primary (Headlines):** Inter Bold (descarga: fonts.google.com/specimen/inter)
   - **Secondary (Body):** Inter Regular
   - **Data (Números):** Courier Prime

✅ Guardar

---

## PASO 2: Crear Templates Reutilizables

### Template 1: POST EDUCATIVO (1080 x 1350px)

**Estructura:**
```
[Layer 1 - Fondo]
Gradiente 135deg: #1B2E5A → #E63946

[Layer 2 - Logo]
Tu logo en esquina inferior derecha
Opacidad: 40%
Tamaño: 60x60px

[Layer 3 - Disciplina Badge]
Badge en esquina superior izquierda
Ej: "🏃 RUNNING"
Fondo: #E63946, Texto blanco 14px

[Layer 4 - Headline]
Tamaño: 48px
Weight: Bold
Color: Blanco
Texto: "Las 4 Zonas de Entrenamiento"

[Layer 5 - Descripción]
Tamaño: 28px
Weight: Regular
Color: Blanco
Alineación: Centro

[Layer 6 - Zones Grid]
4 boxes (2x2):
- 🔵 AERÓBICA
- 🟡 TEMPO
- 🟠 VO2 MAX
- 🔴 ANAERÓBICA

[Layer 7 - CTA]
"Comenta tu zona →"
Tamaño: 16px
Color: Blanco
Posición: Abajo
```

**Pasos en Canva:**
1. Crea diseño **1080 x 1350px**
2. Agrega **background → Gradient → Custom**
3. Selecciona colores #1B2E5A y #E63946, ángulo 135°
4. Añade **Text** → "Las 4 Zonas de Entrenamiento" (48px, Bold, Blanco)
5. Agrupa componentes en **sections** para reutilizar
6. Guarda como **Template**

---

### Template 2: POST OFERTA (1080 x 1350px)

**Estructura:**
```
[Layer 1 - Fondo]
Color: Blanco #FFFFFF

[Layer 2 - Header Banner]
Altura: 200px
Fondo: #E63946
Texto: "METE TU MEJOR MARCA"
Tamaño: 40px, Bold, Blanco

[Layer 3 - Planes Comparison]
3 cards horizontales:

PLAN 1 (Izquierda):
├─ Nombre: AMATEUR
├─ Precio: $99/mes (28px, Bold, Rojo)
├─ Features: • Análisis basico
│            • Planes automáticos
└─ Border: Gris claro

PLAN 2 (Centro - DESTACADO):
├─ Nombre: COMPETITIVO
├─ Precio: $299/mes (28px, Bold, Rojo)
├─ Features: • Data Engine completo
│            • Video reviews
│            • +30 atletas
└─ Border: Rojo 2px, Sombra

PLAN 3 (Derecha):
├─ Nombre: PRO
├─ Precio: $799/mes
├─ Features: • Todo lo anterior
│            • Mentoría 1-1
└─ Border: Gris claro

[Layer 4 - CTA Button]
"HABLEMOS"
Fondo: #E63946
Texto: Blanco, 16px, Bold, UPPERCASE
Padding: 12px 24px
Border-radius: 6px
```

**Pasos en Canva:**
1. Crea diseño 1080 x 1350px
2. **Fondo blanco** (Background → Solid Color)
3. Agrega **shape rectangle** rojo para header
4. Agrega **text** con nombre de plan
5. Agrupa 3 cards usando **Groups**
6. Botón CTA al final
7. Guarda como **Template de Oferta**

---

### Template 3: TESTIMONIO (1080 x 1350px)

**Estructura:**
```
[Layer 1 - Fondo]
Gradiente vertical blanco → gris claro

[Layer 2 - Testimonial Header]
Avatar circular: 60x60px (foto cliente)
Nombre: "Juan Pérez"
Subtítulo: "Corredor • PB en 10K"

[Layer 3 - Quote]
"El análisis fisiológico fue clave"
Tamaño: 24px
Weight: Bold
Color: #E63946
Italic: Sí
Borde izquierdo: 4px #E63946

[Layer 4 - Stats Grid (3 columnas)]
Antes: 55:30
Flecha: →
Después: 48:45

Mejora: -6:45 (12%)

[Layer 5 - Testimonial Body]
"El plan personalizado me ayudó a..."
Tamaño: 16px
Color: #2C3E50

[Layer 6 - Rating]
⭐⭐⭐⭐⭐
"Altamente recomendado"

[Layer 7 - CTA]
"Quiero mi transformación →"
Fondo: #E63946
Texto: Blanco
```

---

### Template 4: CAROUSEL (1080 x 1350px, múltiples slides)

**Slide 1 (Cover):**
```
Headline: "Las 4 Zonas de Entrenamiento"
Icono grande: ⚡
Texto pequeño: "Desliza → para descubrir"
Colores: Gradiente azul → rojo
```

**Slides 2-5 (Contenido):**
```
Zona Badge circular (100x100px):
- 🔵 AERÓBICA (Color azul)
- 🟡 TEMPO (Color naranja)
- 🟠 VO2 MAX (Color rojo)
- 🔴 ANAERÓBICA (Color púrpura)

Descripción:
"Zona Aeróbica
Conversación fácil
FC: 120-150 bpm
% FTP: 60-70%"

Métrica importante:
"El 40% de runners NO usan esta zona"
```

**Slide 6 (CTA):**
```
"¿Cuál es TU zona?"
Botón: "Dime tu mejor marca →"
```

---

## PASO 3: Crear Stock de Assets

### Descarga estos recursos GRATIS:

1. **Iconos** → Lucide Icons (lucide.dev)
   - Descargar SVG: Running, Cycling, Swimmer, etc.
   
2. **Fondos** → Unsplash (unsplash.com)
   - Buscar: "runner", "athlete", "sports"
   
3. **Avatares** → Placeit (placeit.net)
   - Generar avatares de clientes ficticios

### Organiza en Canva:
1. **Uploads → Create Folder**
2. Crea carpetas:
   - `FastTimes_Icons`
   - `FastTimes_Backgrounds`
   - `FastTimes_Avatars`
   - `FastTimes_Logos`

---

## PASO 4: Crear Templates Reutilizables en Canva

### Guardar como Plantillas Personales

**Para cada template:**
1. Termina el diseño
2. Haz clic en **"Share" → "Create a template"**
3. Nombre: `[TIPO] - Fast Times - [VARIANTE]`

Ejemplos:
- `EDUCATIVO - Fast Times - Zonas`
- `OFERTA - Fast Times - Planes`
- `TESTIMONIO - Fast Times - Juan`
- `CAROUSEL - Fast Times - Tips`

4. Haz clic en **"Save as template"**
5. ✅ Ahora aparecerá en tus **Templates** para próximos posts

---

## PASO 5: Posting Schedule en Instagram

### Lunes: POST EDUCATIVO
1. Abre Canva → Tu template EDUCATIVO
2. Cambia:
   - Headline (semana diferente)
   - Imagen de fondo
   - CTA
3. Descarga como PNG (1080x1350px)
4. Sube a Instagram con caption (ver abajo)

### Miércoles: REELS (Video)
1. Crea en Canva o Adobe Premiere
2. Duración: 15-30s
3. Captions/CC incluidos
4. Descarga MP4
5. Sube a Instagram Reels

### Viernes: CAROUSEL o OFERTA
1. Usa template CAROUSEL o OFERTA
2. Crea 5-7 slides (si es carousel)
3. Descarga como PDF (múltiples páginas)
4. Convierte PDF → JPG (1 JPG por slide)
5. Sube a Instagram como Carousel

### Domingo: TESTIMONIO o DETRÁS DE ESCENAS
1. Template TESTIMONIO
2. O video Stories simple
3. Publica en Stories o Feed

---

## PASO 6: Captions Optimizadas (Según Tipo de Post)

### CAPTION EDUCATIVO
```
📊 El 89% de runners entrena en la zona EQUIVOCADA 🔴

¿Cuál es tu zona?
🔵 AERÓBICA - Conversación fácil
🟡 TEMPO - Incierto pero aguantable
🟠 VO2 MAX - Difícil, rápido
🔴 ANAERÓBICA - Máximo esfuerzo

📌 Guarda este post para entrenar mañana
💬 Comenta: ¿Cuál es tu zona fuerte?
🔗 Planes personalizados → link en bio

#Running #Triatlón #Entrenamiento #DataDriven
```

### CAPTION OFERTA
```
🚀 METE TU MEJOR MARCA CON DATA

320+ PBs rotos | 94% retención | +10 años entrenando

✅ PLANES PERSONALIZADOS
🏃 Running | 🚴 Ciclismo | 🏊 Natación | 🏁 Triatlón

📊 ANÁLISIS FISIOLÓGICO REAL
Potencia • Frecuencia cardíaca • Lactato

👇 3 OPCIONES:
💰 AMATEUR - $99/mes
💪 COMPETITIVO - $299/mes (Recomendado)
👑 PRO - $799/mes (Agotado)

🔗 Hablemos → link en bio
💬 O escribe por WhatsApp

#CoachingPersonalizado #AtletasSerios #ResultadosComprobados
```

### CAPTION TESTIMONIO
```
📈 ANTES → DESPUÉS

Juan Pérez
Corredor amateur | PB en 10K

⏱️ TIEMPO:
55:30 → 48:45 (-6:45 en 6 meses)

💬 "El análisis fisiológico fue crucial. Entendí mis zonas y pude entrenar al máximo"

⭐⭐⭐⭐⭐ "Altamente recomendado"

🎯 ¿Tu siguiente transformación?
🔗 Link en bio para tu plan personalizado

#Transformación #PB #Entrenamiento #DataDriven
```

---

## PASO 7: Herramientas Complementarias

### Para Optimizar Diseño:
- **Figma** (versión gratuita para más control)
- **Adobe Express** (similar a Canva pero más poderoso)
- **Photopea** (editor online gratuito)

### Para Gestionar Instagram:
- **Later** (scheduling + analytics)
- **Buffer** (multiplatform)
- **Meta Business Suite** (nativo, gratuito)

### Para Captions:
- **ChatGPT** (genera captions para cada post)
- **Jasper AI** (especializado en marketing)

---

## CHECKLIST PRE-PUBLICAR

Antes de subir cada post:

- [ ] ¿Imagen está en 1080x1350px?
- [ ] ¿Logo Fast Times visible (esquina abajo derecha)?
- [ ] ¿Disciplina badge en esquina arriba izquierda?
- [ ] ¿Hay al menos 1 elemento rojo (#E63946)?
- [ ] ¿CTA es claro y visible?
- [ ] ¿Tipografía es legible en mobile?
- [ ] ¿Contrast está bien (4.5:1 mínimo)?
- [ ] ¿Colores del brand kit están usados?
- [ ] ¿Sin emojis confusos o demasiados?
- [ ] ¿Caption tiene hashtags relevantes?
- [ ] ¿Link en bio actualizado?

---

## PRÓXIMAS ACCIONES

### SEMANA 1:
- [ ] Crear Brand Kit en Canva
- [ ] Descargar fonts Google (Inter, Courier Prime)
- [ ] Crear 4 templates base (Educativo, Oferta, Testimonio, Carousel)
- [ ] Guardar como Templates personales

### SEMANA 2:
- [ ] Crear asset library (iconos, fondos, avatares)
- [ ] Diseñar primeros 4 posts (Semana 1 del calendario)
- [ ] Descargar PNGs en alta resolución
- [ ] Escribir captions para cada uno

### SEMANA 3:
- [ ] Publicar según calendario (Lun/Mié/Vie/Dom)
- [ ] Monitorear engagement
- [ ] Ajustar según lo que funciona
- [ ] Crear más variantes de templates

### SEMANA 4+:
- [ ] Escalar a 2 posts semanales
- [ ] Iniciar Stories diarios
- [ ] Crear Reels (1-2 por semana)
- [ ] Re-targetear con ads si presupuesto lo permite

---

## 💡 TIPS PROFESIONALES

1. **Batch create:** Diseña 4 posts de una vez (eficiencia 4x)
2. **Reutiliza templates:** Usa la misma estructura, solo cambia contenido
3. **Deja "breathing room":** No llenes todo el espacio, blanco es bueno
4. **Test & iterate:** Publica, analiza qué funciona, haz más de eso
5. **Calls to Action claros:** Siempre pide algo (comenta, guarda, visita bio)
6. **Consistency es key:** Mis posts a misma hora, mismo estilo, mismo tono

---

## 📊 MÉTRICAS A MONITOREAR

- **Reach:** Personas que ven tu contenido (meta: +100/semana)
- **Impressions:** Veces que se muestra (meta: +300/semana)
- **Engagement rate:** (Likes + Comentarios) / Followers (meta: 3-5%)
- **Saves:** Personas que guardan tu post (importante para algoritmo)
- **Clicks al bio:** Tráfico a tu landing page (meta: 50+/semana)
- **DMs:** Mensajes de interés (meta: 5-10/semana)

---

**Listo para empezar?** Abre Canva ahora y crea tu primer template. 🚀

*Design System v1.0 | Fast Times 2026*
