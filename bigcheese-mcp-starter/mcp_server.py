from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
# Lección 4: from pydantic import Field

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}


# Lección 4 — Tools: el modelo decide cuándo invocarlas
# @mcp.tool(name="read_doc_contents", description="...")
# def read_document(doc_id: str = Field(...)): ...
# TODO: Write a tool to read a doc

# @mcp.tool(name="edit_document", description="...")
# def edit_document(doc_id, old_str, new_str): ...
# TODO: Write a tool to edit a doc


# Lección 7 — Resources: la app los pide directo, sin pasar por el modelo
# @mcp.resource("docs://documents", mime_type="application/json")
# def list_docs() -> list[str]: ...
# TODO: Write a resource to return all doc id's

# @mcp.resource("docs://documents/{doc_id}", mime_type="text/plain")
# def fetch_doc(doc_id: str) -> str: ...
# TODO: Write a resource to return the contents of a particular doc


# Lección 9 — Prompts: el usuario los dispara con /comando
# @mcp.prompt(name="format", description="...")
# def format_document(doc_id) -> list[base.Message]: ...
# TODO: Write a prompt to rewrite a doc in markdown format

# @mcp.prompt(name="summarize", description="...")
# def summarize_document(doc_id) -> list[base.Message]: ...
# TODO: Write a prompt to summarize a doc


# Lecciones 11-12 (demos avanzadas) — se muestran desde bigcheese-mcp-solution/:
#   /proposal       → genera propuesta comercial HTML a partir de múltiples docs
#   /talent_search  → clasifica CVs del banco de talento según un requerimiento
# Requieren: save_to_file, list_template_placeholders, generate_html_from_template
# Ver bigcheese-mcp-solution/mcp_server.py si quieres explorarlas.


if __name__ == "__main__":
    mcp.run(transport="stdio")
