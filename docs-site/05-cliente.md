---
title: 5. Cliente MCP (L6)
---

# Lección 6 — Cliente MCP

Implementas los dos métodos principales del cliente: `list_tools` y `call_tool`. El resto del scaffolding ya está listo.

## 1. Abrir `mcp_client.py`

Verás la clase `MCPClient` con `connect`, `session`, `cleanup` ya implementados, y varios métodos con `# TODO`.

## 2. Implementar `list_tools`

```python
async def list_tools(self) -> list[types.Tool]:
    result = await self.session().list_tools()
    return result.tools
```

## 3. Implementar `call_tool`

```python
async def call_tool(
    self, tool_name: str, tool_input: dict
) -> types.CallToolResult | None:
    return await self.session().call_tool(tool_name, tool_input)
```

Guarda con `Ctrl+S`.

## 4. Verificar el cliente de forma aislada

Al final del archivo, dentro del `async with MCPClient(...) as _client:`, agrega:

```python
result = await _client.list_tools()
print(result)
```

Nueva terminal (no cierres el inspector) y ejecuta:

```bash
uv run mcp_client.py
```

> ✓ Ves algo como `[Tool(name='read_doc_contents', ...), Tool(name='edit_document', ...)]`.

> ℹ️ La conversión MCP → formato Bedrock ya vive en `core/bedrock.py` (`to_bedrock_tools`). No tienes que tocarla.

## 5. Probar con el chatbot

```bash
uv run main.py
```

Preguntas de prueba:

- `¿Qué contiene el documento report.pdf?`
- `Edita el archivo deposition.md y cambia 'A report' por 'This new version'.`

> ✓ El modelo usa las tools y responde correctamente. Las herramientas están funcionando a través del cliente.

---

Siguiente: [Resources en el servidor (Lección 7)](06-resources-server).
