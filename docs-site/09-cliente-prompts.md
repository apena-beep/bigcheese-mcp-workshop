---
title: 9. Cliente + Prompts (L10)
---

# Lección 10 — Prompts desde el cliente

Los últimos dos métodos del cliente. Con esto, el comando `/` queda funcional end-to-end.

## 1. `list_prompts`

```python
async def list_prompts(self) -> list[types.Prompt]:
    result = await self.session().list_prompts()
    return result.prompts
```

Pobla el menú cuando el usuario escribe `/`.

## 2. `get_prompt`

```python
async def get_prompt(self, prompt_name, args: dict[str, str]):
    result = await self.session().get_prompt(prompt_name, args)
    return result.messages
```

El servidor interpola los argumentos y devuelve los mensajes listos para Bedrock.

Guarda.

## 3. Probar el flujo completo

```bash
uv run main.py
```

1. Escribe `/` → selecciona `format` con las flechas → Enter
2. Selecciona `plan.md`
3. Observa: el modelo lee con `read_doc_contents` → convierte a Markdown → guarda con `edit_document`

Verifica con:

```
What's in the @plan.md document?
```

> ✓ `plan.md` ahora está en Markdown.

Prueba también `/summarize report.pdf`.

---

🎉 **Ya tienes un chatbot MCP completo con tools, resources y prompts.**

Siguiente: [Demos: `/proposal` y `/talent_search`](10-demos).
