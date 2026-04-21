# Módulo 4: Herramientas MCP en el Servidor

## Objetivos de Aprendizaje

Al finalizar este módulo, vas a poder:

- Entender qué es una herramienta MCP y cuándo usarla
- Crear las primeras herramientas en `mcp_server.py`
- Guardar el servidor correctamente para el siguiente módulo

---

## ¿Qué es una Herramienta MCP?

Las herramientas son acciones que el modelo puede ejecutar cuando lo considera necesario, basándose en la pregunta del usuario. El modelo decide cuándo usarlas, la app las ejecuta a través del cliente MCP, y el servidor las implementa.

En este módulo vas a crear dos herramientas básicas:
- **`read_doc_contents`** — para que el modelo pueda leer el contenido de cualquier documento
- **`edit_document`** — para que el modelo pueda editar el contenido de un documento

---

## Paso 1: Abrir mcp_server.py

En el explorador de archivos del panel izquierdo de VS Code, hacé clic en `mcp_server.py` para abrirlo en el editor.

Tomáte un momento para leerlo. Ya tiene:
- La instancia del servidor `FastMCP` creada
- Un diccionario `docs` con documentos de prueba en memoria

**Verificación:** podés ver el diccionario `docs` con entradas como `deposition.md`, `report.pdf` y otros documentos de prueba.

---

## Paso 2: Agregar el Import de Field

Buscá el bloque de importaciones al inicio del archivo y agregá esta línea:

```python
from pydantic import Field
```

`Field` permite agregar descripciones a los parámetros de las herramientas. El modelo las lee para entender cómo usar cada herramienta correctamente. Sin descripciones claras, el modelo puede usar las herramientas de forma incorrecta.

---

## Paso 3: Crear la Herramienta de Lectura

Buscá esta línea exacta en el archivo:

```python
# TODO: Write a tool to read a doc
```

Borrá esa línea de comentario y en su lugar escribí:

```python
@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string."
)
def read_document(
    doc_id: str = Field(description="Id of the document to read"),
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]
```

El decorador `@mcp.tool` registra esta función como una herramienta disponible para el modelo. El `name` es cómo el modelo la va a llamar. La `description` le explica para qué sirve.

---

## Paso 4: Crear la Herramienta de Edición

Buscá esta línea:

```python
# TODO: Write a tool to edit a doc
```

Borrá esa línea y escribí:

```python
@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the document's content with a new string"
)
def edit_document(
    doc_id: str = Field(description="Id of the document that will be edited"),
    old_str: str = Field(description="The text to replace. Must match exactly, including whitespace"),
    new_str: str = Field(description="The new text to insert in place of the old text"),
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)
    return "Documento editado con éxito"
```

> **Nota sobre `old_str`:** la descripción le indica al modelo que debe coincidir exactamente, incluyendo espacios y mayúsculas. Si el texto no coincide exactamente con lo que hay en el documento, el reemplazo no ocurre.

---

## Paso 5: Guardar el Archivo

Guardá el archivo con `Ctrl+S`.

**Verificación:** el punto de cambios junto al nombre del archivo en la pestaña desaparece, confirmando que el archivo está guardado.

> **Si ves un error de sintaxis:** verificá que la indentación use exactamente 4 espacios por nivel. Python no acepta mezcla de espacios y tabulaciones.

---

## Resumen

Al finalizar este módulo, deberías tener:

- `from pydantic import Field` agregado a los imports
- Función `read_document` con decorador `@mcp.tool` en el servidor
- Función `edit_document` con decorador `@mcp.tool` en el servidor
- Archivo `mcp_server.py` guardado

---

**Anterior:** [Módulo 3 — Configuración del Proyecto](./Modulo-3-Configuracion-del-Proyecto.md) | **Siguiente:** [Módulo 5 — El Inspector](./Modulo-5-El-Inspector.md)
