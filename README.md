# ⚡ Fasttimes — Generador de Informes de Rendimiento

Webapp profesional para analizar archivos `.FIT` de Garmin y generar reportes de rendimiento para triatletas y corredores.

**Desarrollado por**: Nadir Baca Paunero — Fasttimes Coaching, Buenos Aires

---

## 📁 Estructura del Proyecto

```
.
├── backend/              # Motor de análisis
│   ├── parser.py        # Lectura archivos .FIT
│   ├── metrics.py       # Cálculos de métricas
│   ├── calculations.py  # Funciones avanzadas
│   └── tests/
│
├── frontend/            # Aplicación Streamlit
│   ├── app.py          # App principal
│   └── config.py       # Configuración UI
│
├── docs/               # Documentación
├── archive/            # Archivos antiguos (ignorar)
├── requirements.txt
└── README.md
```

---

## 🚀 Inicio Rápido

### Local (desarrollo)

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar app
streamlit run frontend/app.py
```

App disponible: `http://localhost:8501`

### Deploy en Streamlit Cloud (gratis)

1. **Push a GitHub**
   ```bash
   git init && git add . && git commit -m "Fasttimes MVP"
   git remote add origin https://github.com/TU_USUARIO/fasttimes.git
   git push -u origin main
   ```

2. **Deploy en Streamlit Cloud**
   - Ir a [share.streamlit.io](https://share.streamlit.io)
   - Conectar GitHub → seleccionar repo
   - Entry point: `frontend/app.py`
   - Click Deploy ✓

3. **URL pública** (auto-generada)
   ```
   https://fasttimes-rendimiento.streamlit.app
   ```

---

## 📊 Métricas Calculadas

| Métrica | Descripción |
|---------|-------------|
| **FTP** | Umbral de Potencia (95% mejor 20min) |
| **NP** | Potencia Normalizada |
| **TSS** | Training Stress Score |
| **IF** | Intensity Factor (NP/FTP) |
| **VO2max** | Estimación cardiorrespiratoria |
| **EF** | Eficiencia (velocidad/FC) |
| **Zonas HR** | 5 zonas de frecuencia cardíaca |
| **Zonas Potencia** | 6 zonas de Coggan |
| **SPM** | Cadencia (pasos/minuto) |
| **Desnivel** | Ganancia/pérdida altitud |
| **HRV** | Variabilidad frecuencia cardíaca |
| **VAM** | Velocidad ascensional media |

---

## ✨ Características

✅ Parser .FIT binario (fitparse)  
✅ 30+ métricas de rendimiento  
✅ UI profesional (dark mode, WCAG AA)  
✅ Gráficos interactivos (Plotly)  
✅ Exportación CSV  
✅ Sin dependencias externas pesadas

---

## 🔜 Fase 2 (Próximas)

- [ ] Integración Mercado Pago (Checkout Pro)
- [ ] Autenticación de usuarios
- [ ] Base de datos (historial sesiones)
- [ ] Comparación multi-sesión
- [ ] Análisis histórico por mes/año

---

## 🛠 Stack Técnico

**Backend**
- Python 3.11+
- fitparse (parser .FIT)
- pandas, numpy (análisis)

**Frontend**
- Streamlit (webapp)
- Plotly (gráficos)
- Material Design (UI)

**Hosting**
- Streamlit Cloud (MVP)
- Vercel (próximo)

---

## 📚 Documentación

Para detalles técnicos, ver:
- `docs/BACKEND_INDEX.md` — Guía del motor
- `docs/FRONTEND_BUILD_SUMMARY.md` — Detalles UI
- `docs/RESUMEN_EJECUTIVO.md` — Visión general

---

## 💡 Uso

1. **Sube archivo .FIT** desde tu reloj Garmin
2. **Completa formulario** (FTP, peso, nivel)
3. **Genera informe** automático en segundos
4. **Descarga CSV** con datos detallados

---

**Última actualización**: Junio 2026
