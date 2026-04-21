# BigCheese — Workshop MCP

Taller técnico de **Model Context Protocol (MCP)** sobre **Amazon Bedrock**. Construís desde cero un servidor y un cliente MCP integrados en un chatbot CLI, y terminás con dos demos de negocio reales: generador de propuesta comercial y selección inteligente de candidatos.

---

## Estructura del Repositorio

```
bigcheese-mcp-workshop/
├── bigcheese-mcp-starter/     ← Punto de partida con TODOs (aquí trabajás)
├── bigcheese-mcp-solution/    ← Solución de referencia completa
├── modulos/                   ← Guía paso a paso (léela en GitHub)
├── docs-site/                 ← Sitio web del workshop (GitHub Pages)
├── workshop-materials/        ← Documentos de las demos (FinTrack S.A.)
└── mcp-inspector.txt          ← Comando del inspector para tu entorno
```

---

## Módulos del Workshop

| Módulo | Descripción | Tiempo |
|--------|-------------|--------|
| [Módulo 0](modulos/Modulo-0-Entorno-de-Desarrollo.md) | Levantar el entorno — CloudFormation + VS Code | 10-15 min |
| [Módulo 1](modulos/Modulo-1-Introduccion-MCP.md) | Introducción a MCP — qué es y qué problema resuelve | 5 min |
| [Módulo 2](modulos/Modulo-2-Clientes-MCP.md) | Clientes MCP — qué hace el cliente y cómo orquesta | 5 min |
| [Módulo 3](modulos/Modulo-3-Configuracion-del-Proyecto.md) | Configuración del proyecto — primer arranque del chatbot | 5 min |
| [Módulo 4](modulos/Modulo-4-Herramientas-en-el-Servidor.md) | Herramientas MCP — las primeras herramientas del servidor | 10 min |
| [Módulo 5](modulos/Modulo-5-El-Inspector.md) | El inspector — probar el servidor sin código cliente | 10 min |
| [Módulo 6](modulos/Modulo-6-Cliente-MCP.md) | Cliente MCP — conectar la app con el servidor | 10 min |
| [Módulo 7](modulos/Modulo-7-Recursos-en-el-Servidor.md) | Recursos MCP — exponer datos para la app | 5 min |
| [Módulo 8](modulos/Modulo-8-Recursos-desde-el-Cliente.md) | Recursos desde el cliente — autocompletar con `@` | 10 min |
| [Módulo 9](modulos/Modulo-9-Prompts-en-el-Servidor.md) | Prompts MCP — empaquetar flujos en comandos | 10 min |
| [Módulo 10](modulos/Modulo-10-Prompts-desde-el-Cliente.md) | Prompts desde el cliente — comandos con `/` | 5 min |
| [Módulo 11](modulos/Modulo-11-Demo-Propuesta-Comercial.md) | Demo — generador de propuesta comercial con IA | Demostración |
| [Módulo 12](modulos/Modulo-12-Demo-Seleccion-de-Candidatos.md) | Demo — selección inteligente de candidatos | Demostración |
| [Módulo 13](modulos/Modulo-13-Repaso-Las-Tres-Primitivas.md) | Repaso — las tres primitivas y referencia rápida | 5 min |

---

## Inicio Rápido

```bash
# 1. Clonar el repositorio
git clone https://github.com/ugrosso-bch/bigcheese-mcp-workshop.git
cd bigcheese-mcp-workshop

# 2. Seguir el Módulo 0 para levantar el entorno en AWS
# → modulos/Modulo-0-Entorno-de-Desarrollo.md

# 3. El código de trabajo está en:
cd bigcheese-mcp-starter
uv run main.py
```

---

## Las Dos Carpetas de Código

### `bigcheese-mcp-starter/` — Para los participantes

Contiene el código base con comentarios `# TODO` en los puntos exactos donde hay que implementar cada funcionalidad. Cada TODO incluye el esqueleto mínimo (decorador + firma) para que sepas qué escribir.

Si te bloqueás, la guía de cada módulo tiene el código completo. Y si preferís ver todo de golpe, está en `bigcheese-mcp-starter/SOLUTIONS.md`.

### `bigcheese-mcp-solution/` — Solución de referencia

La implementación completa y funcionando. Útil para comparar, debuggear o simplemente ver el resultado final.

---

## Las Demos — Casos de Uso Reales

Los módulos 11 y 12 muestran dos casos de negocio corriendo sobre la misma arquitectura que construiste.

### Módulo 11 — Generador de propuesta comercial

El servidor tiene cuatro documentos del caso FinTrack S.A. cargados. Un comando genera una propuesta comercial personalizada en HTML en segundos.

```
/proposal → selecciona los documentos → propuesta_comercial_fintrack.html
```

### Módulo 12 — Selección inteligente de candidatos

El servidor tiene 13 CVs del equipo BigCheese. A partir de un requerimiento de cargo, clasifica cada perfil en Fit Alto / Fit Medio / Fit Bajo y genera un informe ejecutivo en HTML.

```
/talent_search → talent_requirement.md → shortlist con tarjetas por candidato
```

---

## Arquitectura del Proyecto

```
Usuario (terminal)
      ↓
  CliApp (core/cli.py)           ← Autocompletado, historial
      ↓
  CliChat (core/cli_chat.py)     ← Procesa @menciones y /comandos
      ↓
  Chat (core/chat.py)            ← Bucle agentic + tool use
      ↓
  ├──► Bedrock (core/bedrock.py) ← Modelo de lenguaje (AWS Bedrock)
  └──► MCPClient (mcp_client.py) ──► mcp_server.py (stdio)
```

Cliente y servidor MCP se comunican por **stdio** en local. En producción: servidor remoto con HTTPS, autenticación IAM por tenant y audit log en CloudTrail.

---

## Prerrequisitos

- Cuenta AWS con permisos para desplegar CloudFormation y crear roles IAM
- Región recomendada: **us-east-1**
- Navegador moderno (Chrome o Firefox)

---

## Recursos Adicionales

- [Documentación oficial MCP — AWS](https://awslabs.github.io/mcp/)
- [Model Context Protocol — Anthropic](https://modelcontextprotocol.io/introduction)
- [AWS Bedrock](https://aws.amazon.com/bedrock/)
- [GitHub Pages del workshop](https://ugrosso-bch.github.io/bigcheese-mcp-workshop/) *(activar en Settings → Pages → docs-site)*
