---
title: 6. Resources en el servidor (L7)
---

# Lección 7 — Resources MCP en el servidor

Los **resources** son datos que la aplicación obtiene del servidor **sin pasar por el modelo**. No consumen tokens. Útil para listas de opciones, contenidos fijos, etc.

## Los dos resources que vas a crear

1. **Lista de documentos** — alimenta el autocompletado de `@` en el chatbot
2. **Contenido de un documento** — se inyecta cuando el usuario escribe `@nombre-del-doc`

## 1. Resource de lista

En `mcp_server.py`, busca `# TODO: Write a resource to return all doc id's` y reemplaza:

```python
@mcp.resource("docs://documents", mime_type="application/json")
def list_docs() -> list[str]:
    return list(docs.keys())
```

> URI fija `docs://documents`. MIME `application/json` le dice al cliente que parsee como estructurado.

## 2. Resource con plantilla

Busca `# TODO: Write a resource to return the contents of a particular doc`:

```python
@mcp.resource("docs://documents/{doc_id}", mime_type="text/plain")
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]
```

> `{doc_id}` se extrae automáticamente de la URI. Si la app pide `docs://documents/report.pdf`, la función recibe `doc_id="report.pdf"`.

Guarda.

## 3. Verificar en el Inspector

Detén el inspector (`Ctrl+C`), reinícialo con el mismo comando de `mcp-inspector.txt`, recarga la página y **Connect**.

Sección **Resources**:

- **List Resources** → aparece `docs://documents`
- **List Resource Templates** → aparece `fetch_doc` con URI `docs://documents/{doc_id}`
- Selecciona `docs://documents` → **Read Resource** → JSON con la lista
- Selecciona `fetch_doc`, `doc_id = "deposition.md"` → contenido del doc

---

Siguiente: [Leer resources desde el cliente (Lección 8)](07-cliente-resources).
