---
title: 1. Setup — Fase 0
---

# Fase 0 — Levantar el entorno de desarrollo

El template de CloudFormation crea una instancia EC2 con **code-server** (VS Code en el navegador), expuesta vía CloudFront, con Python, `uv`, MCP y Claude Code preinstalados.

## 1. Abrir CloudFormation

En la consola AWS → **CloudFormation** → **Create stack** → **With new resources (standard)**.

## 2. Subir el template

En **Specify template** selecciona **Upload a template file**, sube `code-server-workshop.yaml` y click en **Next**.

> El stack usa el nombre de la pila para aislar la VPC y el secreto de la contraseña. Puedes lanzar varios en la misma cuenta sin conflictos.

## 3. Configurar el stack

| Campo | Valor |
|---|---|
| Stack name | `bigcheese-mcp` (o el que prefieras) |
| Instance name | `CodeServer` |
| Instance volume size | `40` |
| **Instance type** | **`t3.large`** ← cambia de `c7i.xlarge` |
| Instance OS | `Ubuntu-24` |

Acepta IAM (`I acknowledge that AWS CloudFormation might create IAM resources`) y **Submit**.

## 4. Esperar (~8-10 min)

Cuando el estado sea `CREATE_COMPLETE`, ve a la pestaña **Outputs**.

## 5. Guardar los outputs

| Output | Uso |
|---|---|
| `URL` | Abrir VS Code Server en el navegador |
| `Password` | Contraseña de code-server |
| `MCPInspectorProxy` | URL del proxy para el Inspector MCP (Lección 5) |

## 6. Abrir code-server

- Abre la `URL` en el navegador
- Ingresa el `Password`
- Deberías ver VS Code con una terminal abierta y `(.venv)` al inicio de la línea

## 7. Obtener el código del workshop

El código ya queda clonado dentro de `/workshop/` en la instancia. Confirma:

```bash
ls /workshop
```

Debes ver `bigcheese-mcp-starter/` y `bigcheese-mcp-solution/`.

---

Siguiente: [Conceptos y acceso al proyecto](02-conceptos).
