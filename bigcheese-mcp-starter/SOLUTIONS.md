# Soluciones — fallback por si te bloqueas

Usa este archivo **solo** si estás atascado. Intenta primero siguiendo la guía.

---

## Lección 4 — Tools en `mcp_server.py`

```python
from pydantic import Field


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

---

## Lección 6 — Tools en `mcp_client.py`

```python
async def list_tools(self) -> list[types.Tool]:
    result = await self.session().list_tools()
    return result.tools


async def call_tool(
    self, tool_name: str, tool_input: dict
) -> types.CallToolResult | None:
    return await self.session().call_tool(tool_name, tool_input)
```

---

## Lección 7 — Resources en `mcp_server.py`

```python
@mcp.resource("docs://documents", mime_type="application/json")
def list_docs() -> list[str]:
    return list(docs.keys())


@mcp.resource("docs://documents/{doc_id}", mime_type="text/plain")
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]
```

---

## Lección 8 — Resources en `mcp_client.py`

```python
import json
from pydantic import AnyUrl


async def read_resource(self, uri: str) -> Any:
    result = await self.session().read_resource(AnyUrl(uri))
    resource = result.contents[0]
    if isinstance(resource, types.TextResourceContents):
        if resource.mimeType == "application/json":
            return json.loads(resource.text)
        return resource.text
```

---

## Lección 9 — Prompts en `mcp_server.py`

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

---

## Lección 10 — Prompts en `mcp_client.py`

```python
async def list_prompts(self) -> list[types.Prompt]:
    result = await self.session().list_prompts()
    return result.prompts


async def get_prompt(self, prompt_name, args: dict[str, str]):
    result = await self.session().get_prompt(prompt_name, args)
    return result.messages
```

---

## Demos (L11-L12) — código completo

Para no duplicar código extenso, ver directamente:

- `bigcheese-mcp-solution/mcp_server.py` — incluye `save_to_file`, `list_template_placeholders`, `generate_html_from_template`, y los prompts `/proposal` y `/talent_search`
- `bigcheese-mcp-solution/docs/templates/` — plantillas HTML con placeholders
