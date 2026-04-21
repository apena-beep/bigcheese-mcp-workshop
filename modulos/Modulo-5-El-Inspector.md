# Módulo 5: El Inspector

## Objetivos de Aprendizaje

Al finalizar este módulo, vas a poder:

- Iniciar el inspector MCP en el entorno de desarrollo
- Conectar el inspector con el servidor
- Probar las herramientas creadas en el Módulo 4 de forma visual

---

## ¿Qué es el Inspector?

El SDK de MCP incluye una interfaz web para probar el servidor de forma interactiva. Te permite ejecutar herramientas, ver recursos y probar prompts directamente en el navegador, sin necesidad de escribir código cliente.

Es la herramienta más útil durante el desarrollo porque te permite verificar que cada componente funciona correctamente de forma aislada, antes de integrarlo al chatbot completo.

---

## Paso 1: Liberar el Puerto

Antes de iniciar el inspector, asegurate de que el puerto 6277 esté libre:

```bash
fuser -k 6277/tcp
```

Este comando termina cualquier proceso que esté usando el puerto. No muestra ningún mensaje si el puerto estaba libre. En ambos casos es seguro continuar.

---

## Paso 2: Iniciar el Inspector

En el explorador de archivos de VS Code, abrí el archivo `mcp-inspector.txt`. Tiene el comando exacto con los valores de tu entorno ya configurados.

Seleccioná todo el contenido (`Ctrl+A`), copiálo (`Ctrl+C`), pegalo en la terminal (`Ctrl+Shift+V`) y presioná Enter.

**Verificación:** la terminal muestra mensajes indicando que el servidor arrancó y el inspector está disponible.

> **Si aparece un error de módulo no encontrado:** verificá que `(.venv)` esté activo al inicio de la terminal. Si no está activo, abrí una nueva terminal e intentá nuevamente.

---

## Paso 3: Abrir el Inspector en el Navegador

Abrí una nueva pestaña en el navegador y escribí tu URL de CloudFront seguida de `/mcp-inspector/` (con la barra al final).

**Verificación:** ves la interfaz web del inspector con las secciones **Tools**, **Resources** y **Prompts**.

---

## Paso 4: Configurar la Conexión

Antes de hacer clic en **Connect**, actualizá estos tres campos:

| Campo | Valor |
|-------|-------|
| Inspector Proxy Address | Tu URL de CloudFront + `/proxy/6277/` (con barra al final) |
| Proxy Session Token | (dejarlo completamente vacío) |
| Request Timeout | `60000` ← borrá el valor que tenga y escribí este |

> **El campo más importante es Request Timeout.** Si no lo cambiás a `60000`, todas las llamadas van a fallar con error de tiempo agotado aunque el servidor esté funcionando perfectamente.

---

## Paso 5: Conectar y Probar las Herramientas

Hacé clic en **Connect**. Luego andá a **Tools → List Tools**.

**Verificación:** aparecen `read_doc_contents` y `edit_document` con sus descripciones y parámetros.

### Probar read_doc_contents

Hacé clic en `read_doc_contents`, ingresá `doc_id = "deposition.md"` y hacé clic en **Run Tool**.

**Verificación:** el inspector muestra el contenido del documento.

### Probar edit_document

Hacé clic en `edit_document` y completá los tres campos:
- `doc_id`: `deposition.md`
- `old_str`: `This`
- `new_str`: `A report`

Hacé clic en **Run Tool**.

**Verificación:** el inspector muestra `"Documento editado con éxito"`.

Volvé a ejecutar `read_doc_contents` con `doc_id = "deposition.md"` para confirmar que el cambio se aplicó.

**Verificación:** el contenido ahora empieza con `"A report deposition..."` en lugar de `"This deposition..."`.

---

## Troubleshooting

| Error | Qué hacer |
|-------|-----------|
| Error 502 / Not Connected | Ejecutá `fuser -k 6277/tcp` y repetí el Paso 2 |
| Request Timed Out | Verificá que el Request Timeout sea exactamente `60000` |
| Tool not found | Verificá que `mcp_server.py` esté guardado con los cambios del Módulo 4 |

---

## Resumen

Al finalizar este módulo, deberías tener:

- Inspector MCP corriendo y conectado
- Herramientas `read_doc_contents` y `edit_document` verificadas y funcionando

---

**Anterior:** [Módulo 4 — Herramientas en el Servidor](./Modulo-4-Herramientas-en-el-Servidor.md) | **Siguiente:** [Módulo 6 — Cliente MCP](./Modulo-6-Cliente-MCP.md)
