# Módulo 7: Recursos MCP en el Servidor

## Objetivos de Aprendizaje

Al finalizar este módulo, vas a poder:

- Entender la diferencia entre herramientas y recursos
- Crear dos recursos en `mcp_server.py`
- Verificarlos en el inspector

---

## ¿Qué son los Recursos?

Los recursos son datos que la aplicación obtiene directamente del servidor, sin pasar por el modelo. Esto es útil cuando la interfaz necesita información para funcionar —como mostrar una lista de opciones— sin que ese acceso genere costos de procesamiento.

En este módulo vas a crear dos recursos que habilitan funcionalidades específicas en el chatbot:

- **Recurso directo (`docs://documents`):** devuelve la lista de todos los documentos disponibles. La app lo usa para el menú de autocompletar cuando el usuario escribe `@`.
- **Recurso con plantilla (`docs://documents/{doc_id}`):** devuelve el contenido de un documento específico. La app lo usa para inyectar el contenido en el mensaje cuando el usuario menciona `@nombre-documento`.

---

## Paso 1: Crear el Recurso de Lista de Documentos

En `mcp_server.py`, buscá esta línea:

```python
# TODO: Write a resource to return all document ids
```

Borrá esa línea y escribí:

```python
@mcp.resource("docs://documents", mime_type="application/json")
def list_docs() -> list[str]:
    return list(docs.keys())
```

Este recurso tiene una URI fija. Cada vez que la app lo solicite, devuelve la lista completa de nombres de documentos en formato JSON.

---

## Paso 2: Crear el Recurso de Contenido de Documento

Buscá esta línea:

```python
# TODO: Write a resource to return the content of a particular document
```

Borrá esa línea y escribí:

```python
@mcp.resource("docs://documents/{doc_id}", mime_type="text/plain")
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with ID {doc_id} not found")
    return docs[doc_id]
```

El `{doc_id}` en la URI es un parámetro que el SDK extrae automáticamente y pasa como argumento a la función. Si la app solicita `docs://documents/report.pdf`, la función recibe `doc_id = "report.pdf"`.

Guardá el archivo con `Ctrl+S`.

---

## Paso 3: Verificar en el Inspector

Detenés el inspector (`Ctrl+C` en la terminal donde está corriendo), volvés a ejecutarlo con el comando del archivo `mcp-inspector.txt`, recargás la página del navegador y conectás nuevamente.

Luego en la sección **Resources**:

1. Hacé clic en **List Resources**. Debe aparecer `docs://documents`.
2. Hacé clic en **List Resource Templates**. Debe aparecer `fetch_doc`.
3. Seleccioná `docs://documents` → **Read Resource**. Devuelve la lista de documentos en JSON.
4. Seleccioná `fetch_doc`, ingresá `doc_id = "deposition.md"` → **Read Resource**. Devuelve el contenido.

**Verificación:** los dos recursos responden correctamente.

---

## Resumen

- Recurso `docs://documents` creado y verificado
- Recurso `docs://documents/{doc_id}` creado y verificado
- Inspector muestra ambos recursos funcionando

---

**Anterior:** [Módulo 6 — Cliente MCP](./Modulo-6-Cliente-MCP.md) | **Siguiente:** [Módulo 8 — Recursos desde el Cliente](./Modulo-8-Recursos-desde-el-Cliente.md)
