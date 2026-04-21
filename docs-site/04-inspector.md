---
title: 4. Inspector MCP (L5)
---

# Lección 5 — El Inspector MCP

El SDK incluye una interfaz web para probar tu servidor **sin escribir código cliente**. Muy útil para validar tools antes de integrarlas.

## 1. Liberar el puerto 6277

```bash
fuser -k 6277/tcp
```

No imprime nada si estaba libre o si mató un proceso — en ambos casos puedes continuar.

## 2. Arrancar el inspector

Abre `bigcheese-mcp-starter/mcp-inspector.txt`. Copia todo su contenido (ya tiene tus URLs de CloudFront configuradas) y pégalo en la terminal.

> ✓ Deberías ver `Starting MCP inspector... Proxy server listening on localhost:6277`.

Si falla con "módulo no encontrado" o `uv` inexistente, asegúrate que `(.venv)` esté activo en la terminal.

## 3. Abrir el inspector en el navegador

Nueva pestaña → `<tu-url-cloudfront>/mcp-inspector/` (con `/` al final).

## 4. Configurar la conexión

| Campo | Valor |
|---|---|
| Inspector Proxy Address | `<tu-url-cloudfront>/proxy/6277/` (con `/` final) |
| Proxy Session Token | *(vacío)* |
| Request Timeout | **`60000`** ⚠️ |

> ⚠️ Si no cambias **Request Timeout a 60000**, todas las llamadas fallan por timeout aunque el servidor funcione bien.

Click **Connect**.

## 5. Probar `read_doc_contents`

Sección **Tools** → **List Tools** → deben aparecer `read_doc_contents` y `edit_document`.

Expande `read_doc_contents`, ingresa `doc_id = deposition.md`, **Run Tool**.

> ✓ Devuelve: `"This deposition covers the testimony of Angela Smith, P.E."`

## 6. Probar `edit_document`

- `doc_id` = `deposition.md`
- `old_str` = `This`
- `new_str` = `A report`

**Run Tool** → `"Documento editado con éxito"`.

Vuelve a `read_doc_contents` con `deposition.md` → el contenido ahora empieza por `A report deposition...`. ✅

## Errores comunes

| Error | Solución |
|---|---|
| `502` / `Not Connected` | `fuser -k 6277/tcp` y repite desde el paso 2 |
| `Request Timed Out` | Verifica que Request Timeout sea **60000** |
| `Tool not found` | ¿Guardaste `mcp_server.py` después de los cambios de la L4? |

---

Siguiente: [Cliente MCP (Lección 6)](05-cliente).
