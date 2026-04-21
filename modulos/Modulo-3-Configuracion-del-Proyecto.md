# Módulo 3: Configuración del Proyecto

## Objetivos de Aprendizaje

Al finalizar este módulo, vas a poder:

- Acceder al entorno de desarrollo en el navegador
- Verificar que el entorno virtual de Python está activo
- Ejecutar el chatbot base y confirmar la conexión con AWS Bedrock

---

## Prerequisitos

- Haber completado el [Módulo 0](./Modulo-0-Entorno-de-Desarrollo.md) y tener los tres valores del Output guardados: URL, Password y MCPInspectorProxy.

---

## Paso 1: Abrir VS Code en el Navegador

1. Abrí el navegador y pegá la URL que copiaste del Output del stack. Termina en `.cloudfront.net`.
2. Ingresá la contraseña del Output `Password` y presioná Enter.

**Verificación:** VS Code carga en el navegador con el explorador de archivos en el panel izquierdo y una terminal en la parte inferior.

> **Si VS Code no carga:** esperá dos minutos y recargá la página. El servidor puede estar todavía inicializando si el stack terminó de crearse hace menos de un minuto.

---

## Paso 2: Verificar el Entorno Virtual de Python

Mirá la terminal en la parte inferior de VS Code. Al inicio de la línea de comandos deberías ver `(.venv)` antes de la ruta.

**Verificación:** la terminal muestra `(.venv)` al inicio. Ejemplo:
```
(.venv) participant@CodeServer:/workshop/cli_starter$
```

> **Si no ves `(.venv)`:** cerrá la terminal haciendo clic en el ícono de la papelera y abrí una nueva desde **Terminal → New Terminal**. El entorno virtual se activa automáticamente al abrir una nueva terminal.

---

## Paso 3: Navegar a la Carpeta del Proyecto

```bash
cd /workshop/cli_starter
```

**Verificación:** la ruta en la terminal cambia a `/workshop/cli_starter`.

---

## Paso 4: Primera Prueba del Chatbot Base

Antes de agregar capacidades MCP, verificá que el chatbot base funciona y que la conexión con AWS Bedrock está configurada:

```bash
uv run main.py
```

Cuando aparezca el prompt de entrada, escribí la siguiente pregunta y presioná Enter:

```
What's one plus one?
```

**Verificación:** el modelo responde con algo como *"One plus one equals two"*. La conexión con AWS Bedrock funciona correctamente.

Cerrá el chatbot presionando `Ctrl+C`. En los módulos siguientes le vas a agregar las capacidades MCP paso a paso.

> **Si el modelo no responde:** verificá que las variables `BEDROCK_REGION` y `BEDROCK_MODEL_ID` estén configuradas en el archivo `.env`. Consultá el `README.md` del proyecto para ver cómo hacerlo.

---

## Resumen

Al finalizar este módulo, deberías tener:

- VS Code abierto en el navegador con `(.venv)` activo en la terminal
- Navegado a la carpeta `/workshop/cli_starter`
- Chatbot base respondiendo correctamente

---

**Anterior:** [Módulo 2 — Clientes MCP](./Modulo-2-Clientes-MCP.md) | **Siguiente:** [Módulo 4 — Herramientas en el Servidor](./Modulo-4-Herramientas-en-el-Servidor.md)
