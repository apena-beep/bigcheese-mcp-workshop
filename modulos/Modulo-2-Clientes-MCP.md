# Módulo 2: Clientes MCP

## ¿Qué Hace el Cliente MCP?

El cliente MCP es el intermediario entre el código de tu aplicación y el servidor. Su trabajo es gestionar la conexión y exponer las operaciones que cualquier aplicación necesita.

Las dos operaciones fundamentales:

- **`list_tools()`** — le pregunta al servidor qué herramientas tiene disponibles y devuelve el catálogo completo con nombres, descripciones y parámetros de cada una.
- **`call_tool(nombre, parámetros)`** — ejecuta una herramienta específica pasando los parámetros necesarios y devuelve el resultado.

El cliente no sabe nada sobre los sistemas que hay detrás del servidor. Solo habla el protocolo MCP. Eso significa que el mismo cliente funciona sin cambios sin importar si el servidor está conectado a una base de datos, una API externa, un sistema de archivos o cualquier otra cosa.

---

## Relación 1:1 con el Servidor

La documentación oficial de AWS establece:

> *"Host applications have MCP clients that maintain 1:1 connections with MCP servers."*

Un cliente se conecta a un servidor. Si una sesión necesita hablar con GitHub, Slack y el CRM al mismo tiempo, se crean tres clientes independientes. El modelo ve el catálogo unificado de los tres y no sabe que hay tres servidores detrás.

```
Sesión del usuario
        ↓
┌───────────────────────────────────────┐
│  Cliente 1 ──→ Servidor GitHub        │
│  Cliente 2 ──→ Servidor Slack         │
│  Cliente 3 ──→ Servidor CRM           │
│                                       │
│  El modelo ve:                        │
│  - herramientas de GitHub             │
│  - herramientas de Slack              │
│  - herramientas del CRM               │
│  (catálogo unificado, sin saber       │
│   cuántos servidores hay detrás)      │
└───────────────────────────────────────┘
```

---

## Cómo Fluye una Consulta de Principio a Fin

Ejemplo: el usuario pregunta *"¿Qué candidatos tenemos con experiencia en Python?"*

1. El usuario escribe la pregunta en la interfaz del chatbot.
2. La app llama a `list_tools()` para saber qué puede hacer el servidor.
3. El cliente envía la solicitud al servidor y recibe el catálogo de herramientas.
4. La app envía al modelo la pregunta más el catálogo de herramientas disponibles.
5. El modelo lee la pregunta y el catálogo, decide que necesita usar `listar_candidatos()` y lo indica en su respuesta.
6. La app llama a `call_tool("listar_candidatos", {"habilidad": "Python"})`.
7. El servidor ejecuta la búsqueda y devuelve los candidatos que coinciden.
8. El modelo recibe los resultados y formula la respuesta final para el usuario.

Todo este proceso ocurre en segundos. Para el usuario es completamente transparente.

---

## El Código Real del Proyecto

Así está implementado el cliente en `mcp_client.py`:

```python
async def list_tools(self) -> list[types.Tool]:
    result = await self.session().list_tools()
    return result.tools

async def call_tool(
    self, tool_name: str, tool_input: dict
) -> types.CallToolResult | None:
    return await self.session().call_tool(tool_name, tool_input)
```

Dos funciones. Eso es todo lo que la aplicación necesita para interactuar con cualquier servidor MCP.

---

## Multi-Tenant: un Cliente por Empresa

En una plataforma conversacional con múltiples empresas cliente, cada sesión crea sus propios clientes con las credenciales de esa empresa:

```python
TENANT_CONFIG = {
    "empresa_a": {
        "servers": ["github_mcp", "slack_mcp", "crm_mcp"],
        "credentials": {
            "github_token": "ghp_empresaA_xxx",
            "slack_token":  "xoxb_empresaA_xxx",
        }
    },
    "empresa_b": {
        "servers": ["slack_mcp", "docs_mcp"],
        "credentials": {
            "slack_token": "xoxb_empresaB_xxx",
        }
    }
}
```

Un usuario de la empresa A nunca tiene acceso a los datos de la empresa B porque los clientes de su sesión solo se conectan a los servidores de su empresa, con sus credenciales.

---

**Anterior:** [Módulo 1 — Introducción a MCP](./Modulo-1-Introduccion-MCP.md) | **Siguiente:** [Módulo 3 — Configuración del Proyecto](./Modulo-3-Configuracion-del-Proyecto.md)
