# Módulo 12: Demo — Selección Inteligente de Candidatos

> **Este módulo es una demostración.** El equipo de BigCheese lo presenta en vivo. No se requiere que hagas cambios en el código durante este módulo.

---

## El Escenario

BigCheese necesita asignar un Solutions Architect Senior al proyecto de FinTrack. El perfil es muy específico: experiencia en migraciones fintech, conocimiento de PCI-DSS en AWS, y capacidad de trabajar con el CTO y el VP de Ingeniería del cliente. Timeline ajustado: piloto en 60 días.

Sin esta arquitectura, el equipo de talento pasaría medio día o más leyendo hojas de vida. Con MCP, el proceso toma segundos.

---

## ¿Cuál es el Problema que Resuelve?

La preselección de candidatos consume tiempo significativo del equipo de talento humano. Revisar 40 o 50 hojas de vida, filtrar por el perfil específico que pidió el área y preparar el documento de presentación para el jefe puede tomar medio día o más.

Con esta configuración el modelo hace la lectura y clasificación inicial en segundos. El equipo de talento sigue siendo quien valida los criterios y toma las decisiones. Lo que cambia es el tiempo dedicado al trabajo manual de revisión.

---

## ¿Qué Recibe el Jefe de Área?

Por cada candidato seleccionado, la plataforma entrega:

| Elemento | Descripción |
|----------|-------------|
| Experiencia relevante | Lo que aplica específicamente al cargo solicitado |
| Habilidades que coinciden | Comparación directa con el perfil pedido |
| Puntos para profundizar | Preguntas sugeridas para la entrevista |
| Calificación de afinidad | Fit Alto / Fit Medio / Fit Bajo |

---

## ¿Cómo Está Construido?

Las hojas de vida están organizadas como archivos de texto individuales, uno por candidato, expuestos como Recursos en el servidor MCP.

| Componente MCP | Función en esta demo |
|----------------|---------------------|
| Recursos | Cada hoja de vida es un archivo expuesto como recurso bajo el esquema `docs://documents/{doc_id}`. La app los lista con `docs://documents` y los carga individualmente cuando el modelo los necesita. |
| Herramientas | `read_doc_contents(doc_id)` trae el CV completo de un perfil. `list_template_placeholders(template_name)` devuelve los campos que hay que llenar. `generate_html_from_template(...)` renderiza el resultado final en HTML. |
| Prompt | `talent_search` orquesta todo el flujo: lee el requerimiento, lee todos los CVs, clasifica cada perfil como Fit Alto / Medio / Bajo, selecciona los mejores y genera el HTML con tarjetas por candidato. |

Si mañana llegan candidatos nuevos, se agregan sus archivos al servidor y el modelo ya los tiene disponibles en la siguiente búsqueda. No hay que modificar nada en la aplicación.

---

## El Banco de CVs Disponible

```python
TALENT_CV_IDS = [
    "carlos_rios_solutions_architect.md",   # 9 años, migraciones fintech, PCI-DSS
    "valentina_gomez_devops_sre.md",        # 7 años, CI/CD, banca digital
    "mateo_fernandez_data_engineer.md",
    "sofia_paredes_backend_developer.md",
    "rodrigo_salinas_finops.md",
    "ana_lucia_torres_security.md",
    "diego_morales_cloud_infra.md",
    "camila_reyes_frontend.md",
    "nicolas_vargas_qa.md",
    "paula_vega_account_executive.md",
    "andres_molina_project_manager.md",
    "lucia_herrera_scrum_master.md",
    "martin_dotta_bi_analyst.md",
]
```

---

## Cómo Activar la Demo

```
/talent_search talent_requirement.md
```

O con un rol específico:

```
/talent_search {rol_buscado}
```

---

## ¿Qué Hace Esto?

Busca y clasifica perfiles del banco de talento de BigCheese según el documento de requerimientos. Al ejecutar este comando, el agente:

1. Lee el documento de requerimiento indicado para entender el perfil buscado.
2. Lee todos los CVs disponibles en el banco de talento (13 perfiles).
3. Clasifica cada perfil como Fit Alto, Fit Medio o Fit Bajo respecto al requerimiento.
4. Selecciona los mejores candidatos (máximo 5) y los descartados.
5. Consulta los placeholders de la plantilla HTML de talento.
6. Genera un archivo `.html` con nombre en formato `talent_search_result_<rol>_<contexto>.html`, con tarjetas visuales por candidato, citando habilidades, certificaciones y experiencias concretas de los CVs.

**Documento esperado:**

`talent_requirement.md` — define el perfil buscado: rol, habilidades requeridas, contexto del proyecto.

---

## ¿Cómo Ver el Resultado en el Navegador?

Tanto `/proposal` como `/talent_search` producen archivos `.html` en el directorio donde corre la aplicación. Para verlos en el navegador, levantá un servidor web estático desde esa misma carpeta:

```bash
python -m http.server 8081
```

Luego abrí en el navegador:

```
https://{URL_Workshop}/proxy/8081
```

Vas a ver un listado de archivos. Hacé clic en el `.html` generado, por ejemplo `talent_search_result_solutions_architect_fintech.html`, y se renderizan las tarjetas de los candidatos con todo el estilo de la plantilla.

---

**Anterior:** [Módulo 11 — Demo: Propuesta Comercial](./Modulo-11-Demo-Propuesta-Comercial.md) | **Siguiente:** [Módulo 13 — Repaso: Las Tres Primitivas](./Modulo-13-Repaso-Las-Tres-Primitivas.md)
