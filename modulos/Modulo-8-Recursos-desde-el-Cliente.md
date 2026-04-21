# Módulo 8: Recursos desde el Cliente

## Objetivos de Aprendizaje

Al finalizar este módulo, vas a poder:

- Implementar `read_resource` en `mcp_client.py`
- Usar el autocompletar con `@` en el chatbot
- Inyectar contexto de documentos directamente en los mensajes

---

## Paso 1: Agregar los Imports Necesarios

Abrí `mcp_client.py` y agregá estas dos líneas al bloque de imports al inicio del archivo:

```python
import json
from pydantic import AnyUrl
```

`json` lo usamos para convertir las respuestas JSON a objetos Python. `AnyUrl` valida que la URI tenga el formato correcto antes de enviarla al servidor.

---

## Paso 2: Implementar read_resource

Buscá el método `read_resource` con su comentario `TODO`. Borralo y escribí:

```python
async def read_resource(self, uri: str) -> Any:
    result = await self.session().read_resource(AnyUrl(uri))
    resource = result.contents[0]
    if isinstance(resource, types.TextResourceContents):
        if resource.mimeType == "application/json":
            return json.loads(resource.text)
        return resource.text
```

Si el servidor declaró el recurso como `application/json`, la función lo convierte a Python. Si es `text/plain`, lo devuelve directamente. La app siempre recibe el dato en el formato que necesita.

Guardá con `Ctrl+S`.

---

## Paso 3: Probar el Autocompletar con @

```bash
uv run main.py
```

Cuando aparezca el prompt de entrada, escribí el símbolo `@` y esperá un momento sin presionar Enter.

**Verificación:** aparece un menú desplegable con la lista de todos los documentos disponibles.

---

## Paso 4: Probar la Inyección de Contexto

Escribí la siguiente pregunta completa y presioná Enter:

```
What's in the @report.pdf document?
```

**Verificación:** el modelo responde con el contenido del documento **sin haber usado ninguna herramienta**. El contenido de `report.pdf` fue inyectado automáticamente por la app en el mensaje antes de enviárselo al modelo.

---

## Resumen

- `read_resource` implementado en `mcp_client.py`
- Autocompletar con `@` funcionando
- Inyección de contexto verificada

---

**Anterior:** [Módulo 7 — Recursos en el Servidor](./Modulo-7-Recursos-en-el-Servidor.md) | **Siguiente:** [Módulo 9 — Prompts en el Servidor](./Modulo-9-Prompts-en-el-Servidor.md)
