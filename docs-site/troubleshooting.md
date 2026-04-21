---
title: Troubleshooting
---

# Troubleshooting

## El stack de CloudFormation no crea

- **`ROLLBACK_COMPLETE`**: normalmente cuota IAM o límites de EC2 en la región. Revisa la pestaña **Events** del stack para ver qué recurso falló.
- **VPC limit exceeded**: ya tienes 5 VPCs en esa región. Borra una o usa otra región.

## code-server no abre

- Espera a `CREATE_COMPLETE` y unos minutos adicionales para que el bootstrap de SSM termine (instala `uv`, dependencias Python, etc.).
- Revisa los Outputs del stack — asegúrate de usar la URL completa de CloudFront, no la de EC2.

## Terminal sin `(.venv)` activo

```bash
source /workshop/.venv/bin/activate
```

O abre una nueva terminal de VS Code (debería activarse sola).

## `uv run main.py` falla con error de credenciales AWS

- Verifica que la instancia tenga un Instance Profile con permisos a Bedrock
- Verifica el `BEDROCK_REGION` en `.env` y que el modelo esté habilitado en tu cuenta de Bedrock

## Inspector MCP no conecta

| Síntoma | Solución |
|---|---|
| `502` / `Not Connected` | `fuser -k 6277/tcp` y reinicia con `mcp-inspector.txt` |
| `Request Timed Out` | Request Timeout debe ser **60000** exactamente |
| `Tool not found` | Guarda `mcp_server.py` con `Ctrl+S` |
| Página en blanco | Verifica que la URL termine con `/mcp-inspector/` (slash final) |

## El menú `@` no muestra documentos

- Revisa que implementaste `read_resource` (L8) **y** el resource `docs://documents` (L7)
- Guarda ambos archivos
- Reinicia `main.py`

## El menú `/` no muestra prompts

- `list_prompts` y `get_prompt` en el cliente (L10)
- Al menos un `@mcp.prompt` en el servidor (L9)

## El modelo no usa las tools

- Verifica que `list_tools` en el cliente devuelve `result.tools` (no `[]` por defecto)
- Revisa las descripciones de tools y parámetros — si son vagas, el modelo no sabe cuándo usarlas
- Pregunta explícita: *"Lee el documento report.pdf usando la herramienta"*

## `/proposal` o `/talent_search` no generan el HTML

- Estás corriendo desde `bigcheese-mcp-solution/` (no desde `bigcheese-mcp-starter/`)
- Las plantillas HTML existen en `docs/templates/`
- El modelo tiene que llamar **una sola vez** a `generate_html_from_template` con todos los placeholders; si sobrescribe, el HTML queda incompleto

## Fallback de soluciones

Si te quedas bloqueado, abre `bigcheese-mcp-starter/SOLUTIONS.md`. Tiene el código completo de cada lección (4, 6, 7, 8, 9, 10). Intenta entender qué hace antes de copiarlo.

## Reset total

```bash
cd /workshop
git checkout -- bigcheese-mcp-starter/
```

Vuelve el starter al estado original.
