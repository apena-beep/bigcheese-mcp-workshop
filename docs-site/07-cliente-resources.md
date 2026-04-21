---
title: 7. Cliente + Resources (L8)
---

# Lección 8 — Leer resources desde el cliente

Habilitas el menú de autocompletado de `@` y la inyección automática de contenido.

## 1. Imports

En `mcp_client.py`:

```python
import json
from pydantic import AnyUrl
```

## 2. Implementar `read_resource`

```python
async def read_resource(self, uri: str) -> Any:
    result = await self.session().read_resource(AnyUrl(uri))
    resource = result.contents[0]
    if isinstance(resource, types.TextResourceContents):
        if resource.mimeType == "application/json":
            return json.loads(resource.text)
        return resource.text
```

> Pide el recurso al servidor, toma el primer elemento y decide el parseo según el MIME type. La app siempre recibe el dato en el formato que puede usar.

Guarda.

## 3. Probar el menú `@`

```bash
uv run main.py
```

Escribe `@` y espera (sin Enter).

> ✓ Aparece un menú desplegable con todos los documentos. Navega con flechas.

## 4. Probar inyección de contexto

```
What's in the @report.pdf document?
```

> ✓ El modelo responde con el contenido **sin usar ninguna herramienta**. La app inyectó el contenido en el mensaje antes de mandarlo a Bedrock. **Más rápido y sin tokens de tool use.**

---

Siguiente: [Prompts en el servidor (Lección 9)](08-prompts-server).
