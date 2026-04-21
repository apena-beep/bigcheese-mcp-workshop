from pydantic import Field
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
    "discovery_transcript.md": open("docs/proposal/discovery_transcript.md", encoding="utf-8").read(),
    "client_brief.md": open("docs/proposal/client_brief.md", encoding="utf-8").read(),
    "bigcheese.md": open("docs/proposal/bigcheese.md", encoding="utf-8").read(),
    "reference_cases.md": open("docs/proposal/reference_cases.md", encoding="utf-8").read(),
    "proposal_output.md": "",
    # --- CVs del equipo BigCheese ---
    "carlos_rios_solutions_architect.md": open("docs/talent/carlos_rios_solutions_architect.md", encoding="utf-8").read(),
    "valentina_gomez_devops_sre.md": open("docs/talent/valentina_gomez_devops_sre.md", encoding="utf-8").read(),
    "mateo_fernandez_data_engineer.md": open("docs/talent/mateo_fernandez_data_engineer.md", encoding="utf-8").read(),
    "sofia_paredes_backend_developer.md": open("docs/talent/sofia_paredes_backend_developer.md", encoding="utf-8").read(),
    "rodrigo_salinas_finops.md": open("docs/talent/rodrigo_salinas_finops.md", encoding="utf-8").read(),
    "ana_lucia_torres_security.md": open("docs/talent/ana_lucia_torres_security.md", encoding="utf-8").read(),
    "diego_morales_cloud_infra.md": open("docs/talent/diego_morales_cloud_infra.md", encoding="utf-8").read(),
    "camila_reyes_frontend.md": open("docs/talent/camila_reyes_frontend.md", encoding="utf-8").read(),
    "nicolas_vargas_qa.md": open("docs/talent/nicolas_vargas_qa.md", encoding="utf-8").read(),
    "paula_vega_account_executive.md": open("docs/talent/paula_vega_account_executive.md", encoding="utf-8").read(),
    "andres_molina_project_manager.md": open("docs/talent/andres_molina_project_manager.md", encoding="utf-8").read(),
    "lucia_herrera_scrum_master.md": open("docs/talent/lucia_herrera_scrum_master.md", encoding="utf-8").read(),
    "martin_dotta_bi_analyst.md": open("docs/talent/martin_dotta_bi_analyst.md", encoding="utf-8").read(),
    "talent_requirement.md": open("docs/talent/talent_requirement.md", encoding="utf-8").read(),
}


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
    description="Edit a document by replacing a string in the documents content with a new string",
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


@mcp.tool(
    name="save_to_file",
    description="Saves content to a file in the current working directory.",
)
def save_to_file(
    filename: str = Field(description="Name of the file to save, e.g. 'proposal_output.md'"),
    content: str = Field(description="Content to write into the file"),
):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return f"File '{filename}' saved successfully."


@mcp.tool(
    name="list_template_placeholders",
    description="Lists all placeholders in a template so you know which fields to fill. Use this BEFORE calling generate_html_from_template.",
)
def list_template_placeholders(
    template_name: str = Field(description="Name of the template: 'proposal' or 'talent'"),
):
    import re

    template_map = {
        "proposal": "docs/templates/proposal_template.html",
        "talent": "docs/templates/talent_template.html",
    }

    if template_name not in template_map:
        raise ValueError(f"Template '{template_name}' not found. Valid options: {list(template_map.keys())}")

    template_path = template_map[template_name]
    with open(template_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Extract all unique placeholders
    placeholders = sorted(set(re.findall(r'\[([A-Z_0-9]+)\]', html_content)))
    
    return {
        "template": template_name,
        "total_placeholders": len(placeholders),
        "placeholders": placeholders
    }


@mcp.tool(
    name="generate_html_from_template",
    description="Generates an HTML file from a template by replacing placeholders with provided values. Use list_template_placeholders first to see all required fields.",
)
def generate_html_from_template(
    template_name: str = Field(description="Name of the template: 'proposal' or 'talent'"),
    output_filename: str = Field(description="Name of the output HTML file, e.g. 'propuesta_comercial.html'"),
    values: dict[str, str] = Field(description="Dictionary mapping placeholder names to their replacement values. Example: {\"PROPOSAL_TITLE\": \"Migración AWS\", \"CLIENT_NAME\": \"FinTrack S.A.\"}"),
):
    import re

    template_map = {
        "proposal": "docs/templates/proposal_template.html",
        "talent": "docs/templates/talent_template.html",
    }

    if template_name not in template_map:
        raise ValueError(f"Template '{template_name}' not found. Valid options: {list(template_map.keys())}")

    template_path = template_map[template_name]
    with open(template_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    for placeholder, value in values.items():
        html_content = html_content.replace(f"[{placeholder}]", str(value))

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    remaining = re.findall(r'\[([A-Z_0-9]+)\]', html_content)
    if remaining:
        unique = list(set(remaining))[:8]
        return f"File '{output_filename}' saved. Warning: {len(set(remaining))} placeholders not replaced: {', '.join(unique)}"

    return f"File '{output_filename}' saved successfully. All placeholders replaced."


@mcp.resource("docs://documents", mime_type="application/json")
def list_docs() -> list[str]:
    return list(docs.keys())


@mcp.resource("docs://documents/{doc_id}", mime_type="text/plain")
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]


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
    2. Produce a summary with:
       - A one-sentence TL;DR.
       - 3 to 6 bullet points with the key ideas, facts, or decisions.
       - A short "Next steps or open questions" section only if the document implies them.

    Rules:
    - Do not invent information that is not in the document.
    - Keep the summary shorter than the original (aim for ~20% of its length).
    - Respond only with the summary. Do not explain your process.
    """
    return [base.UserMessage(prompt)]


@mcp.prompt(
    name="proposal",
    description="Generates a commercial proposal as a styled HTML file based on a discovery transcript, a client brief, and reference cases. Accepts doc_ids as a comma-separated string.",
)
def generate_proposal(
    doc_id: str = Field(
        description="Comma-separated list of doc ids to use as input. Expected: discovery_transcript.md,client_brief.md,reference_cases.md"
    ),
) -> list[base.Message]:
    prompt = f"""
    Tu objetivo es generar una propuesta comercial profesional como archivo HTML, escrita en español.

    Los siguientes documentos contienen los insumos que necesitas (doc ids separados por coma):
    <doc_ids>
    {doc_id}
    </doc_ids>

    Proceso:
    1. Separa los doc_ids por coma y usa 'read_doc_contents' para leer cada documento.
    2. Analiza el contenido y extrae información clave del cliente, desafíos, soluciones y casos de éxito.
    3. USA 'list_template_placeholders' con template_name="proposal" para ver TODOS los placeholders que debes llenar.
    4. Genera un nombre de archivo descriptivo basado en el cliente y tema.
       Formato: "propuesta_comercial_<cliente>_<tema>.html"
       Ejemplo: "propuesta_comercial_fintrack_migracion_aws.html"
       Usa snake_case (minúsculas con guiones bajos), sin tildes.
    5. Crea un diccionario con TODOS los placeholders de la lista (del paso 3) como keys y contenido real como values.
    6. Usa 'generate_html_from_template' UNA SOLA VEZ con:
       - template_name: "proposal"
       - output_filename: el nombre que generaste en el paso 4
       - values: el diccionario completo con TODOS los placeholders llenos

    IMPORTANTE:
    - Llama a list_template_placeholders PRIMERO para saber exactamente qué campos llenar
    - Llena TODOS los placeholders en una sola llamada a generate_html_from_template
    - NO hagas múltiples llamadas a generate_html_from_template (sobrescribe el archivo)
    - Sé específico: usa números reales del cliente, su stack y restricciones
    - Referencia casos de éxito por nombre cuando sean relevantes
    - No inventes información que no esté en los documentos
    - Después de generar, confirma el nombre del archivo generado
    """
    return [base.UserMessage(prompt)]


TALENT_CV_IDS = [
    "carlos_rios_solutions_architect.md",
    "valentina_gomez_devops_sre.md",
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


@mcp.prompt(
    name="talent_search",
    description="Searches the talent pool (CVs) to find profiles that match a given requirement document. Accepts a doc_id pointing to a requirement file.",
)
def search_talent(
    doc_id: str = Field(
        description="Id of the requirement document to use as search criteria. E.g. 'talent_requirement.md'"
    ),
) -> list[base.Message]:
    cv_ids_str = "\n".join(f"- {cv_id}" for cv_id in TALENT_CV_IDS)
    prompt = f"""
    Tu objetivo es analizar el banco de CVs disponible y encontrar los perfiles que mejor se ajustan al requerimiento indicado.
    El resultado debe ser un archivo HTML visual con tarjetas por candidato.

    El requerimiento está en el siguiente documento — léelo primero:
    <requirement_doc_id>
    {doc_id}
    </requirement_doc_id>

    Los CVs disponibles son:
    <cv_ids>
{cv_ids_str}
    </cv_ids>

    Proceso:
    1. Usa 'read_doc_contents' para leer el documento de requerimiento ({doc_id}).
    2. Usa 'read_doc_contents' para leer TODOS los CVs de la lista.
    3. Clasifica cada perfil: Fit Alto, Fit Medio o Fit Bajo respecto al requerimiento.
    4. Selecciona los mejores candidatos (máximo 5) y los descartados.
    5. USA 'list_template_placeholders' con template_name="talent" para ver TODOS los placeholders que debes llenar.
    6. Genera un nombre de archivo descriptivo basado en el rol o perfil buscado.
       Formato: "talent_search_result_<rol_clave>_<contexto>.html"
       Ejemplo: "talent_search_result_solutions_architect_fintech.html"
       Usa snake_case (minúsculas con guiones bajos), sin tildes ni caracteres especiales.
    7. Crea un diccionario con TODOS los placeholders de la lista (del paso 5) como keys y contenido real como values.
    8. Usa 'generate_html_from_template' UNA SOLA VEZ con:
       - template_name: "talent"
       - output_filename: el nombre que generaste en el paso 6
       - values: el diccionario completo con TODOS los placeholders llenos

    IMPORTANTE:
    - Llama a list_template_placeholders PRIMERO para saber exactamente qué campos llenar
    - Llena TODOS los placeholders en una sola llamada a generate_html_from_template
    - NO hagas múltiples llamadas a generate_html_from_template (sobrescribe el archivo)
    - Sé específico: cita habilidades, certificaciones y experiencias concretas de los CVs
    - No inventes información que no esté en los CVs
    - Después de generar, confirma con un mensaje breve indicando el nombre del archivo generado
    """
    return [base.UserMessage(prompt)]


if __name__ == "__main__":
    mcp.run(transport="stdio")
