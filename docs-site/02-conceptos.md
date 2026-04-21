---
title: 2. Conceptos (L1-L3)
---

# Lecciones 1-3 — Conceptos y arranque del proyecto

## Lección 1 — ¿Qué problema resuelve MCP?

Antes de MCP, conectar un modelo con sistemas externos (repos, tickets, bases de conocimiento) implicaba escribir esquemas, funciones, manejo de errores y transformaciones **dentro de cada aplicación**. Ese código no era reutilizable.

**MCP mueve esa responsabilidad a un servidor dedicado.** El servidor define las integraciones una vez y cualquier aplicación que hable el protocolo las puede usar.

> Analogía: MCP es a los modelos lo que USB fue a los periféricos — un conector estándar.

### Comparación

| Sin MCP | Con MCP |
|---|---|
| Cada app reescribe los esquemas | El servidor los expone una vez |
| Integraciones acopladas a la app | Integraciones en el servidor, desacopladas |
| Un sistema nuevo = tocar la app | Un servidor nuevo = plug-and-play |
| Duplicación entre apps | Un servidor reusable |

### Arquitectura

```
Tu app  ↔  Cliente MCP  ↔  Servidor MCP  ↔  Sistema externo
```

El cliente no cambia si el servidor está local o en la nube.

## Lección 2 — El cliente MCP

El cliente MCP expone dos operaciones fundamentales:

- `list_tools()` — pide al servidor el catálogo de herramientas
- `call_tool(nombre, parámetros)` — ejecuta una herramienta

### Flujo típico de una consulta

1. Usuario escribe una pregunta
2. App llama `list_tools()` y envía catálogo + pregunta a Bedrock
3. El modelo decide usar una herramienta → lo indica en su respuesta
4. App llama `call_tool(...)` vía cliente MCP
5. Servidor ejecuta y devuelve el resultado
6. App pasa resultado al modelo → respuesta final al usuario

## Lección 3 — Acceder al proyecto

Dentro de la terminal del code-server:

```bash
cd /workshop/bigcheese-mcp-starter
uv run main.py
```

Escribe `What's one plus one?` + Enter. El chatbot responde con Claude — funciona, pero aún **no tiene capacidades MCP**. Sal con `Ctrl+C`.

> ✓ Si viste la respuesta del modelo, tu `.env` y credenciales AWS están bien configurados.

---

Siguiente: [Tools en el servidor (Lección 4)](03-tools-server).
