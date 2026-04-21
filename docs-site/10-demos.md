---
title: 10. Demos — Proposal y Talent Search (L11-L12)
---

# Lecciones 11-12 — Casos de uso de negocio

Estas lecciones son **demostraciones** ejecutadas por el facilitador usando `bigcheese-mcp-solution/`. Muestran qué se puede construir con los tres primitives (tools + resources + prompts) que ya implementaste.

Para ejecutarlas:

```bash
cd /workshop/bigcheese-mcp-solution
uv run main.py
```

---

## Lección 11 — Generador de propuesta comercial

### Comando

```
/proposal discovery_transcript.md,client_brief.md,reference_cases.md,bigcheese.md
```

### Documentos de entrada

| Documento | Contenido |
|---|---|
| `bigcheese.md` | Filosofía, líneas de servicio, AWS Premier Partner, métricas |
| `client_brief.md` | Brief ejecutivo del cliente ficticio FinTrack S.A. |
| `discovery_transcript.md` | Transcripción simulada de la llamada de descubrimiento |
| `reference_cases.md` | Casos de éxito de BigCheese relevantes |

### Qué hace

1. Lee cada documento con `read_doc_contents`
2. Identifica pain points específicos del prospecto
3. Consulta placeholders con `list_template_placeholders("proposal")`
4. Genera `propuesta_comercial_<cliente>_<tema>.html` con `generate_html_from_template`

### Por qué importa

Una propuesta comercial de calidad toma horas (revisar llamada → cruzar con portafolio → redactar → formatear). Con esta configuración, el modelo hace el trabajo de síntesis **en segundos**. El equipo comercial revisa, ajusta tono y cierra.

### Ver el resultado

```bash
python -m http.server 8081
# Abre en el navegador: http://localhost:8081/propuesta_comercial_fintrack_migracion_aws.html
```

---

## Lección 12 — Selección inteligente de candidatos

### Comando

```
/talent_search talent_requirement.md
```

### Qué hace

1. Lee el requerimiento del cliente
2. Lee los 13 CVs del equipo BigCheese (`docs/talent/*.md`)
3. Clasifica cada perfil: **Fit Alto / Medio / Bajo**
4. Selecciona los top candidatos
5. Genera `talent_search_result_<rol>_<contexto>.html` con tarjetas por candidato

### Qué recibe el jefe de área

| Elemento | Descripción |
|---|---|
| Experiencia relevante | Lo que aplica al cargo solicitado |
| Habilidades que coinciden | Comparación directa con el perfil |
| Puntos para profundizar | Preguntas sugeridas para la entrevista |
| Calificación de afinidad | Qué tan bien encaja con los criterios |

### Por qué importa

Filtrar 40-50 CVs puede tomar medio día. El modelo hace la lectura y clasificación inicial en segundos. El equipo de talento **sigue tomando las decisiones** — lo que cambia es el tiempo dedicado al trabajo manual. Si llegan CVs nuevos, se agregan al servidor y ya están disponibles. No se modifica la app.

### Ver el resultado

```bash
python -m http.server 8081
# http://localhost:8081/talent_search_result_<...>.html
```

---

## Lección 13 — Repaso de las tres primitivas

| Primitiva | Quién la activa | Ejemplo en este workshop |
|---|---|---|
| **Tools** | El modelo (decide en base a la pregunta) | `read_doc_contents`, `edit_document`, `generate_html_from_template` |
| **Resources** | La aplicación (directo, sin tokens) | `docs://documents` (menú `@`), `docs://documents/{doc_id}` (inyección) |
| **Prompts** | El usuario (con `/comando`) | `/format`, `/summarize`, `/proposal`, `/talent_search` |

> Esa separación es lo que hace a MCP reusable: la misma arquitectura sirve para un chatbot de docs, un generador de propuestas, un clasificador de CVs, o cualquier otro caso.

---

Si algo falla: [Troubleshooting](troubleshooting).
