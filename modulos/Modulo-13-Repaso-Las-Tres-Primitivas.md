# Módulo 13: Repaso — Las Tres Primitivas

## Lo que Construiste

A lo largo de este workshop construiste un servidor MCP completo con los tres tipos de componentes que define el protocolo. Este módulo consolida cuándo usar cada uno y cómo se conectan con los casos de uso de negocio que viste en los módulos 11 y 12.

---

## Las Tres Primitivas

La pregunta de diseño es siempre la misma: **¿quién debería controlar esta funcionalidad?**

| Primitiva | Quién la controla | Cuándo usarla |
|-----------|------------------|---------------|
| **Herramienta** | El modelo | Cuando el modelo necesita ejecutar una acción o consultar datos en tiempo real según lo que pidió el usuario. La app no sabe de antemano qué se necesita: el modelo lo decide. |
| **Recurso** | Tu aplicación | Cuando la interfaz necesita datos para funcionar: listas de opciones, contexto del usuario, contenido a inyectar antes de que el modelo procese la pregunta. |
| **Prompt** | El usuario | Cuando hay un flujo repetitivo que requiere alta calidad consistente. El equipo diseña las instrucciones óptimas y el usuario las activa con un comando cuando las necesita. |

---

## Cómo las Usaste en el Chatbot

| Símbolo | Qué hace | Primitiva |
|---------|----------|-----------|
| `@` | Muestra documentos disponibles e inyecta el contenido seleccionado en el mensaje | Recursos |
| `/` | Muestra comandos predefinidos como `/format` | Prompts |
| texto libre | Conversación directa — el modelo invoca herramientas si las necesita | Herramientas |

---

## Cómo se Conectan con los Casos de Negocio

### Demo 11 — Propuesta Comercial

```
Recursos  → Los 4 documentos (perfil BigCheese, brief, transcripción, casos de éxito)
            se inyectan como contexto antes de llamar al modelo

Herramientas → read_doc_contents: el modelo consulta secciones específicas si necesita detalle
               generate_html_from_template: el modelo genera el archivo HTML final

Prompt    → /proposal: define el flujo completo de 5 pasos que garantiza
            consistencia en cada propuesta generada
```

### Demo 12 — Selección de Candidatos

```
Recursos  → Los CVs se cargan en el servidor y están disponibles para el modelo

Herramientas → read_doc_contents: el modelo lee cada CV uno por uno
               generate_html_from_template: genera el informe HTML con los candidatos

Prompt    → /talent_search: define la estructura del análisis y del informe
            (Fit Alto / Fit Medio / Fit Bajo + tarjeta por candidato)
```

---

## La Arquitectura en Producción

Lo que construiste en este workshop corre localmente. En producción, la misma arquitectura se despliega así:

| Aspecto | Workshop (local) | Producción (enterprise) |
|---------|-----------------|------------------------|
| Transporte | stdio (mismo proceso) | HTTPS (servidor remoto) |
| Autenticación | Sin autenticación | IAM por tenant |
| Auditoría | Sin logs | CloudTrail completo |
| Escala | Un usuario | Multi-tenant |
| Actualización | Reinicio manual | Deploy independiente |

La app no cambia. Solo cambia cómo se conecta el cliente al servidor.

---

## Referencia Rápida

### Comandos de Terminal

| Acción | Comando |
|--------|---------|
| Ir a la carpeta del proyecto | `cd /workshop/cli_starter` |
| Iniciar el chatbot | `uv run main.py` |
| Probar solo el cliente | `uv run mcp_client.py` |
| Iniciar el inspector (entorno nube) | Copiar el comando de `mcp-inspector.txt` |
| Iniciar el inspector (local) | `mcp dev mcp_server.py` |
| Liberar el puerto del inspector | `fuser -k 6277/tcp` |
| Salir del chatbot o del inspector | `Ctrl+C` |

### Troubleshooting

| Error | Qué hacer |
|-------|-----------|
| Error 502 o Not Connected en el inspector | `fuser -k 6277/tcp` y reiniciá el servidor |
| Request Timed Out | Cambiá el Request Timeout a exactamente `60000` |
| Unknown Resource | Verificá que `mcp_server.py` tenga los decoradores `@mcp.resource` guardados |
| `(.venv)` no aparece | Cerrá la terminal y abrí una nueva desde **Terminal → New Terminal** |
| El modelo no responde | Verificá `BEDROCK_REGION` y `BEDROCK_MODEL_ID` en el `.env` |
| Error de indentación en Python | Usá 4 espacios por nivel, sin mezclar con tabulaciones |

---

## Próximos Pasos

- **Conectar un sistema real:** usá uno de los [53 servidores MCP de AWS](https://awslabs.github.io/mcp/) para conectar un servicio que ya usás.
- **Construir tu propio servidor:** si tenés un sistema interno, seguí el patrón de `mcp_server.py` para exponerlo.
- **Escalar a producción:** desplegá el servidor como un endpoint HTTPS con autenticación IAM y logging en CloudTrail.

---

## Canal de Soporte Post-Workshop

| Tipo | Para qué |
|------|----------|
| **Técnico** | Código, configuración del servidor, errores de implementación |
| **Teórico** | Arquitectura, cuándo usar cada primitiva, decisiones de diseño |
| **Comercial / Estratégico** | Cómo venderlo, ROI, casos de uso por sector |

---

**Anterior:** [Módulo 12 — Demo: Selección de Candidatos](./Modulo-12-Demo-Seleccion-de-Candidatos.md)
