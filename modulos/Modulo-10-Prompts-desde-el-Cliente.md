# Módulo 10: Prompts desde el Cliente

## Objetivos de Aprendizaje

Al finalizar este módulo, vas a poder:

- Implementar `list_prompts` y `get_prompt` en `mcp_client.py`
- Activar el comando `/format` en el chatbot
- Verificar el flujo completo de principio a fin

---

## Paso 1: Implementar list_prompts

Abrí `mcp_client.py`. Buscá el método `list_prompts` con su comentario `TODO`. Borralo y escribí:

```python
async def list_prompts(self) -> list[types.Prompt]:
    result = await self.session().list_prompts()
    return result.prompts
```

Esta función obtiene el catálogo de prompts del servidor. La app la llama cuando el usuario escribe `/` para mostrar el menú de comandos.

---

## Paso 2: Implementar get_prompt

Buscá el método `get_prompt` con su comentario `TODO`. Borralo y escribí:

```python
async def get_prompt(self, prompt_name, args: dict[str, str]):
    result = await self.session().get_prompt(prompt_name, args)
    return result.messages
```

Esta función obtiene el prompt del servidor con las variables ya interpoladas, listo para enviar al modelo.

Guardá con `Ctrl+S`.

---

## Paso 3: Probar el Flujo Completo con /format

```bash
uv run main.py
```

1. Escribí `/` en el chatbot y esperá el menú.
2. Seleccioná `format` con las flechas y presioná Enter.
3. Seleccioná `plan.md` de la lista.
4. Observá cómo el modelo lee el documento, lo convierte a Markdown y lo guarda automáticamente.

**Verificación:** el proceso completo funciona con un solo comando. Podés verificar el resultado escribiendo:

```
What's in the @plan.md document?
```

---

## Resumen

Al finalizar este módulo, deberías tener el servidor MCP completo con las tres primitivas implementadas y funcionando:

- **Herramientas:** `read_doc_contents`, `edit_document` → el modelo las usa cuando las necesita
- **Recursos:** `docs://documents`, `docs://documents/{doc_id}` → la app los usa para la UI y el contexto
- **Prompts:** `format` → el usuario lo activa con `/format`

---

**Anterior:** [Módulo 9 — Prompts en el Servidor](./Modulo-9-Prompts-en-el-Servidor.md) | **Siguiente:** [Módulo 11 — Demo: Propuesta Comercial](./Modulo-11-Demo-Propuesta-Comercial.md)
