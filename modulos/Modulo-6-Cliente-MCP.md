# Módulo 6: Cliente MCP

## Objetivos de Aprendizaje

Al finalizar este módulo, vas a poder:

- Implementar los métodos `list_tools` y `call_tool` en `mcp_client.py`
- Verificar que el cliente puede comunicarse con el servidor
- Probar el chatbot completo con las herramientas funcionando

---

## Paso 1: Abrir mcp_client.py

En el explorador de VS Code, abrí `mcp_client.py`. El archivo ya tiene toda la estructura base implementada: la clase `MCPClient` con las funciones de conexión y gestión de sesión. Tu trabajo es completar los dos métodos marcados con comentarios `TODO`.

**Verificación:** identificás en el archivo las dos marcas `# TODO` que indican exactamente dónde escribir el código.

---

## Paso 2: Implementar list_tools

Buscá el método `list_tools`. Borrá el comentario `TODO` y el `pass`, y escribí:

```python
async def list_tools(self) -> list[types.Tool]:
    result = await self.session().list_tools()
    return result.tools
```

Este método le pide al servidor el catálogo de herramientas disponibles y devuelve solo la lista, extrayéndola del objeto de respuesta completo del SDK.

---

## Paso 3: Implementar call_tool

Buscá el método `call_tool`. Borrá el comentario `TODO` y el `return None`, y escribí:

```python
async def call_tool(
    self, tool_name: str, tool_input: dict
) -> types.CallToolResult | None:
    return await self.session().call_tool(tool_name, tool_input)
```

Este método recibe el nombre de la herramienta y los parámetros, los pasa directamente al servidor y devuelve el resultado tal como lo recibe.

Guardá el archivo con `Ctrl+S`.

---

## Paso 4: Verificar el Cliente de Forma Aislada

En el bloque `__main__` al final del archivo, dentro del `async with MCPClient(...)`, agregá estas dos líneas:

```python
result = await _client.list_tools()
print(result)
```

Abrí una nueva terminal (sin interrumpir el inspector si está corriendo) y ejecutá:

```bash
uv run mcp_client.py
```

**Verificación:** la terminal muestra las definiciones de las herramientas. Algo como:
```
[Tool(name='read_doc_contents', description='Read the contents...'), Tool(name='edit_document', ...)]
```

> **Nota:** las definiciones de herramientas de MCP no tienen exactamente el formato que espera AWS Bedrock. La conversión ya está implementada en `core/bedrock.py`, en la función `to_bedrock_tools()`. El sistema la usa automáticamente. No necesitás hacer nada.

---

## Paso 5: Probar con el Chatbot Completo

```bash
uv run main.py
```

Escribí las siguientes preguntas para verificar que el modelo usa las herramientas correctamente:

- `¿Qué contiene el documento report.pdf?`
- `Edita el archivo deposition.md y cambia 'A report' por 'This new version'.`

**Verificación:** para la primera pregunta el modelo devuelve el contenido del documento. Para la segunda confirma que realizó la edición.

---

## Resumen

Al finalizar este módulo, deberías tener:

- Métodos `list_tools` y `call_tool` implementados en `mcp_client.py`
- Cliente verificado de forma aislada mostrando las herramientas disponibles
- Chatbot completo usando herramientas correctamente

---

**Anterior:** [Módulo 5 — El Inspector](./Modulo-5-El-Inspector.md) | **Siguiente:** [Módulo 7 — Recursos en el Servidor](./Modulo-7-Recursos-en-el-Servidor.md)
