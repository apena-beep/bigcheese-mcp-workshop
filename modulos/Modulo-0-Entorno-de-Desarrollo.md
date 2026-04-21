# Módulo 0: Entorno de Desarrollo

## Descripción del Workshop

Acompañá a **SAntiago**, CTO de **XYZ S.A.**, mientras construís desde cero un servidor y un cliente MCP integrados en un chatbot CLI con AWS Bedrock.

El workshop está organizado en módulos progresivos. Los módulos 0 al 10 construyen el servidor MCP paso a paso. Los módulos 11 y 12 muestran dos casos de uso de negocio reales corriendo sobre esa misma arquitectura.

---

## Prerequisitos

- Cuenta AWS con permisos para desplegar stacks de CloudFormation y crear roles IAM
- Región recomendada: **us-east-1 (US East - N. Virginia)**
- Navegador moderno (Chrome o Firefox recomendado)

> **Nota:** El entorno de desarrollo corre completamente en la nube. No necesitás instalar Python, Node.js ni ninguna dependencia local.

---

## Paso 1 — Abrir CloudFormation

Ingresá a la [Consola de AWS](https://console.aws.amazon.com). En el buscador de servicios escribí **CloudFormation** y seleccioná el servicio.

![Buscar CloudFormation en la consola de AWS](https://raw.githubusercontent.com/mguerrerobigcheese/bigcheese-mcp-workshop/main/docs/assets/img/cloud_formation.png)

Una vez en la pantalla principal de CloudFormation, hacé clic en **Create stack** y seleccioná **With new resources (standard)**.

![Crear stack con nuevos recursos](https://raw.githubusercontent.com/mguerrerobigcheese/bigcheese-mcp-workshop/main/docs/assets/img/stack_1.png)

---

## Paso 2 — Subir el Template

En la pantalla *Specify template*:

1. Seleccioná **Upload a template file**
2. Hacé clic en **Choose file** y seleccioná el archivo `code-server-workshop.yaml`
3. Hacé clic en **Next**

![Subir el template code-server-workshop.yaml](https://raw.githubusercontent.com/mguerrerobigcheese/bigcheese-mcp-workshop/main/docs/assets/img/stack_2.png)

> Este template usa el nombre del stack para aislar la VPC y el secreto de la contraseña. Podés lanzar varios en la misma cuenta sin conflictos.

---

## Paso 3 — Configurar los Parámetros

En la pantalla *Specify stack details* completá los campos así:

| Campo | Valor |
|-------|-------|
| Stack name | `bigcheese-mcp` (sin espacios) |
| Instance name | `CodeServer` (valor por defecto) |
| Instance volume size | `40` (valor por defecto) |
| Instance type | `t3.large` **← este es el único campo que debés cambiar** |
| Instance operating system | `Ubuntu-24` (valor por defecto) |

![Configurar el nombre del stack y el Instance type t3.large](https://raw.githubusercontent.com/mguerrerobigcheese/bigcheese-mcp-workshop/main/docs/assets/img/stack_3.png)

> **El Instance type por defecto es `c7i.xlarge`.** Cambialo a `t3.large` antes de continuar.

Hacé clic en **Next**. En la pantalla siguiente no cambies nada y volvé a hacer clic en **Next**.

---

## Paso 4 — Confirmar y Crear

En la pantalla de revisión final, desplazate hasta la sección **Capabilities**, marcá el checkbox y hacé clic en **Submit**.

![Marcar el checkbox de IAM resources y hacer Submit](https://raw.githubusercontent.com/mguerrerobigcheese/bigcheese-mcp-workshop/main/docs/assets/img/stack_4.png)

---

## Paso 5 — Esperar el Despliegue

El stack tarda entre **8 y 10 minutos** en completarse. Podés ver el progreso en la pestaña **Events**.

Recursos que se crean automáticamente:
- 1 instancia EC2 con VS Code Server instalado y configurado
- 1 distribución CloudFront que expone VS Code de forma segura
- VPC, subred y grupos de seguridad
- Dependencias de Python (`uv`, `mcp[cli]`, `boto3`) preinstaladas

Esperá hasta que el estado del stack cambie a `CREATE_COMPLETE`.

> **Si el estado cambia a `CREATE_FAILED`:** revisá la pestaña Events para identificar el recurso que falló. El error más común es no haber cambiado el Instance type a `t3.large`.

---

## Paso 6 — Guardar los Outputs

Con el stack en `CREATE_COMPLETE`, abrí la pestaña **Outputs** y copiá los tres valores:

| Output | Para qué lo usarás |
|--------|-------------------|
| `URL` | Para abrir VS Code en el navegador (desde el Módulo 3) |
| `Password` | Para autenticarte cuando abras VS Code |
| `MCPInspectorProxy` | Para configurar el inspector MCP (Módulo 5) |

> **Atención:** No cierres esta pestaña sin copiar los tres valores.

---

## Paso 7 — Descargar el Código del Workshop

El código base está disponible en el repo. Lo vas a necesitar a partir del Módulo 3.

| Carpeta | Descripción |
|---------|-------------|
| `bigcheese-mcp-starter/` | Punto de partida con TODOs — aquí trabajás |
| `bigcheese-mcp-solution/` | Solución completa de referencia |

---

## Resumen

Al finalizar este módulo, deberías tener:

- Stack CloudFormation `bigcheese-mcp` en estado `CREATE_COMPLETE`
- Tres valores del Output copiados: URL, Password y MCPInspectorProxy
- Código del workshop descargado

---

**Siguiente:** [Módulo 1 — Introducción a MCP](./Modulo-1-Introduccion-MCP.md)
