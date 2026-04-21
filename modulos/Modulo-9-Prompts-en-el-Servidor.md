# Módulo 9: Prompts MCP en el Servidor

## Objetivos de Aprendizaje

Al finalizar este módulo, vas a poder:

- Entender qué es un Prompt MCP y cuándo usarlo
- Crear un prompt en `mcp_server.py`
- Verificarlo en el inspector

---

## ¿Qué son los Prompts?

Los prompts son flujos de trabajo preconfigurados que el usuario activa con un comando. A diferencia de las herramientas (que el modelo activa solo) y los recursos (que la app obtiene directamente), los prompts los activa el usuario de forma intencional.

La ventaja es que el equipo puede empaquetar en un prompt las instrucciones óptimas para una tarea compleja, probadas y refinadas. El usuario activa el prompt y obtiene consistentemente el mismo nivel de calidad, sin necesitar saber cómo formular la instrucción correcta.

---

## Paso 1: Agregar el Import del Módulo Base

En `mcp_server.py`, agregá esta línea al bloque de imports:

```python
from mcp.server.fastmcp.prompts import base
```

Este módulo contiene la clase `UserMessage` que usamos para construir el mensaje que se envía al modelo.

---

## Paso 2: Definir el Prompt

Buscá esta línea en `mcp_server.py`:

```python
# TODO: Write a prompt to rewrite a doc in markdown format
```

Borrá esa línea y escribí:

```python
@mcp.prompt(
    name="format",
    description="Rewrites the contents of a document in Markdown format."
)
def format_document(
    doc_id: str = Field(description="Id of the document to format")
) -> list[base.Message]:
    prompt = f"""
    Your goal is to reformat a document to be written with markdown syntax.

    The id of the document you need to reformat is:
    <document_id>
    {doc_id}
    </document_id>

    Add in headers, bullet points, tables, etc as necessary.
    Use the 'edit_document' tool to save the formatted version.
    After saving, respond with the final version. Don't explain your changes.
    """
    return [base.UserMessage(prompt)]
```

El decorador `@mcp.prompt` registra esta función como un prompt disponible. La función recibe el `doc_id`, lo interpola dentro de las instrucciones y devuelve el mensaje completo listo para enviar al modelo.

Guardá con `Ctrl+S`.

---

## Paso 3: Verificar en el Inspector

Reiniciá el inspector, recargá la página y conectá nuevamente. Andá a **Prompts → List Prompts**.

**Verificación:** aparece el prompt `format` con su descripción.

---

## ¿Qué Ocurre Cuando el Usuario Activa /format?

1. El usuario escribe `/format` y selecciona un documento.
2. El cliente envía el nombre del prompt y el `doc_id` al servidor.
3. El servidor interpola el `doc_id` en las instrucciones y devuelve el mensaje completo.
4. La app envía ese mensaje directamente al modelo.
5. El modelo sigue las instrucciones: usa `read_doc_contents`, reformatea el documento y usa `edit_document` para guardar la versión formateada.

---

## Resumen

- Import de `base` agregado
- Prompt `format` creado y verificado en el inspector

---

**Anterior:** [Módulo 8 — Recursos desde el Cliente](./Modulo-8-Recursos-desde-el-Cliente.md) | **Siguiente:** [Módulo 10 — Prompts desde el Cliente](./Modulo-10-Prompts-desde-el-Cliente.md)
