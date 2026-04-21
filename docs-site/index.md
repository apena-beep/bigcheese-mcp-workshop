---
title: Workshop MCP — BigCheese
---

# Workshop MCP — Plataforma de Atención Conversacional

Taller práctico para aprender **Model Context Protocol (MCP)** sobre **Amazon Bedrock**. Vas a construir desde cero un cliente MCP y un servidor MCP, integrados en una aplicación de chat por línea de comandos.

## ¿A quién va dirigido?

A perfiles técnicos (desarrolladores, arquitectos, DevOps) con Python básico y nociones de AWS.

## ¿Qué vas a construir?

Un chatbot CLI que:

- Habla con **Claude** a través de **Amazon Bedrock**
- Descubre y ejecuta herramientas vía **servidor MCP**
- Expone documentos como **recursos MCP** con autocompletado `@documento`
- Corre flujos preconfigurados vía **prompts MCP** con comandos `/comando`
- **Bonus:** genera propuestas comerciales y búsquedas de talento en HTML

## Estructura del repo

```
bigcheese-mcp-starter/            ← Punto de partida con TODOs (aquí trabajas)
bigcheese-mcp-solution/   ← Solución de referencia completa
docs-site/              ← Este sitio (GitHub Pages)
code-server-workshop.yaml ← CloudFormation para el entorno EC2 + code-server
```

En `bigcheese-mcp-starter` cada `# TODO` está precedido de un hint mínimo con el esqueleto MCP (decorador + firma). Si te bloqueas, la solución completa está en `bigcheese-mcp-starter/SOLUTIONS.md`.

## Plan de ruta

| # | Lección | Tiempo aprox. |
|---|---|---|
| 0 | [Setup (CloudFormation + code-server)](01-setup) | 10-15 min (mientras aprovisiona) |
| 1-3 | [Conceptos + acceder al proyecto](02-conceptos) | 10 min |
| 4 | [Tools en el servidor](03-tools-server) | 10 min |
| 5 | [El Inspector MCP](04-inspector) | 10 min |
| 6 | [Cliente MCP](05-cliente) | 10 min |
| 7 | [Resources en el servidor](06-resources-server) | 5 min |
| 8 | [Leer resources desde el cliente](07-cliente-resources) | 10 min |
| 9 | [Prompts en el servidor](08-prompts-server) | 10 min |
| 10 | [Prompts desde el cliente](09-cliente-prompts) | 5 min |
| 11-12 | [Demos: `/proposal` y `/talent_search`](10-demos) | Demostración del facilitador |

Si algo falla, revisa [Troubleshooting](troubleshooting).

## Arquitectura

```
Usuario (terminal)
      ↓
  CliApp (core/cli.py)          ← Autocompletado, historial
      ↓
  CliChat (core/cli_chat.py)    ← Procesa @menciones y /comandos
      ↓
  Chat (core/chat.py)           ← Bucle agentic + tool use
      ↓
  ├──► Bedrock (core/bedrock.py)
  └──► ToolManager ──► MCPClient (mcp_client.py) ──► mcp_server.py (stdio)
```

Cliente y servidor MCP se comunican por **stdio** (proceso hijo).

---

¿Listo? Empieza por [Setup](01-setup).
