---
title: 3. Tools en el servidor (L4)
---

# Lección 4 — Herramientas MCP en el servidor

Abre `bigcheese-mcp-starter/mcp_server.py`. Ya tiene la instancia `FastMCP` y un dict `docs` en memoria.

## 1. Importar `Field`

Arriba del archivo:

```python
from pydantic import Field
```

> 💡 En `bigcheese-mcp-starter/mcp_server.py` verás un hint `# Lección 4: from pydantic import Field` — solo descoméntalo.

## 2. Herramienta de lectura

Busca `# TODO: Write a tool to read a doc` y reemplázalo por:

```python
@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string.",
)
def read_document(
    doc_id: str = Field(description="Id of the document to read"),
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]
```

## 3. Herramienta de edición

Busca `# TODO: Write a tool to edit a doc`:

```python
@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the document's content with a new string",
)
def edit_document(
    doc_id: str = Field(description="Id of the document that will be edited"),
    old_str: str = Field(
        description="The text to replace. Must match exactly, including whitespace"
    ),
    new_str: str = Field(
        description="The new text to insert in place of the old text"
    ),
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)
    return "Documento editado con éxito"
```

> 📝 La descripción de `old_str` le dice al modelo que el match debe ser **exacto** (incluidos espacios). Guarda con `Ctrl+S`.

## ¿Por qué importa?

Las **tools** son las acciones que el modelo **decide** invocar. El `description` y los `Field(description=...)` son el contrato que el modelo lee para saber cuándo y cómo usarlas. Escribirlas con claridad es parte del diseño.

---

Siguiente: [El Inspector MCP (Lección 5)](04-inspector).
