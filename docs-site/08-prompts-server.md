---
title: 8. Prompts en el servidor (L9)
---

# Lección 9 — Prompts MCP en el servidor

Los **prompts** son flujos preconfigurados que el **usuario activa** con `/comando`. Empaquetan instrucciones óptimas y probadas, para que el usuario no tenga que saber cómo formularlas.

> Recuerda: tools las decide el modelo, resources los trae la app, prompts los dispara el usuario.

## 1. Import del módulo `base`

En `mcp_server.py`:

```python
from mcp.server.fastmcp.prompts import base
```

Contiene `UserMessage` para construir los mensajes que se envían al modelo.

## 2. Prompt `format`

Busca `# TODO: Write a prompt to rewrite a doc in markdown format`:

```python
@mcp.prompt(
    name="format",
    description="Rewrites the contents of the document in Markdown format.",
)
def format_document(
    doc_id: str = Field(description="Id of the document to format"),
) -> list[base.Message]:
    prompt = f"""
    Your goal is to reformat a document to be written with markdown syntax.

    The id of the document you need to reformat is:
    <document_id>
    {doc_id}
    </document_id>

    Add in headers, bullet points, tables, etc as necessary. Feel free to add in extra text, but don't change the meaning of the report.
    Use the 'edit_document' tool to edit the document. After the document has been edited, respond with the final version of the doc. Don't explain your changes.
    """
    return [base.UserMessage(prompt)]
```

## 3. Prompt `summarize`

Busca `# TODO: Write a prompt to summarize a doc`:

```python
@mcp.prompt(
    name="summarize",
    description="Generates a concise summary of the given document.",
)
def summarize_document(
    doc_id: str = Field(description="Id of the document to summarize"),
) -> list[base.Message]:
    prompt = f"""
    Your goal is to produce a concise, faithful summary of a document.

    The id of the document you need to summarize is:
    <document_id>
    {doc_id}
    </document_id>

    Steps:
    1. Use the 'read_doc_contents' tool to fetch the document content.
    2. Produce a summary with a one-sentence TL;DR and 3-6 bullets with key ideas.

    Rules:
    - Do not invent information that is not in the document.
    - Keep it shorter than the original.
    - Respond only with the summary.
    """
    return [base.UserMessage(prompt)]
```

Guarda.

## 4. Verificar en el Inspector

Reinicia el inspector, reconecta, sección **Prompts** → **List Prompts**.

> ✓ Aparecen `format` y `summarize`. Selecciona uno, ingresa un `doc_id` y verás el mensaje final que se enviaría al modelo.

## ¿Qué ocurre al disparar `/format`?

1. Usuario escribe `/format` y selecciona un doc
2. Cliente envía nombre del prompt + `doc_id` al servidor
3. Servidor interpola el `doc_id` y devuelve el mensaje completo
4. App envía ese mensaje al modelo
5. Modelo usa `read_doc_contents` → reformatea → usa `edit_document` para guardar

---

Siguiente: [Prompts desde el cliente (Lección 10)](09-cliente-prompts).
