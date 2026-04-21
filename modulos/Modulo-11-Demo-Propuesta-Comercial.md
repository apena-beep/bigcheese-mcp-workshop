# Módulo 11: Demo — Generador de Propuesta Comercial

> **Este módulo es una demostración.** El equipo de BigCheese lo presenta en vivo. No se requiere que hagas cambios en el código durante este módulo.

---

## El Escenario

El equipo comercial de BigCheese necesita enviar una propuesta a FinTrack S.A. Hoy ese proceso toma entre 3 y 4 horas: revisar la transcripción de la llamada de discovery, cruzar los dolores del cliente con el portafolio, redactar, formatear y revisar.

Con esta configuración MCP, el proceso toma segundos.

---

## ¿Qué Documentos se Usan?

| Documento | Contenido |
|-----------|-----------|
| `bigcheese.md` | Quiénes somos, filosofía, AWS Premier Partner, líneas de servicio, casos de éxito y métricas |
| `client_brief.md` | Brief ejecutivo del cliente FinTrack S.A.: plataforma SaaS B2B de gestión de gastos corporativos |
| `discovery_transcript.md` | Transcripción de la llamada de descubrimiento con el prospecto |
| `reference_cases.md` | Casos de éxito de BigCheese que sirven como referencia para la propuesta |

---

## ¿Por Qué Esto Importa para el Negocio?

Construir una propuesta comercial personalizada de calidad toma horas. Hay que revisar lo que dijo el cliente en la llamada, cruzar esa información con el portafolio, redactar, formatear y revisar. Con esta configuración, el modelo hace ese trabajo de síntesis en segundos.

El resultado no es una plantilla genérica. El modelo lee la transcripción de la llamada, identifica los puntos de dolor específicos del prospecto y construye los argumentos desde ahí. El equipo comercial dedica su tiempo a revisar, ajustar el tono y cerrar la venta.

---

## ¿Cómo Está Construido?

| Componente MCP | Función en esta demo |
|----------------|---------------------|
| Recursos | Los cuatro documentos se cargan y se inyectan como contexto antes de enviar el mensaje al modelo |
| Herramientas | El modelo puede consultar secciones específicas de los documentos durante la generación si necesita más detalle |
| Prompt | Define la estructura de la propuesta: resumen ejecutivo, problema, solución, casos de éxito relevantes, inversión y próximos pasos |

La misma arquitectura que construiste en las lecciones anteriores es la que alimenta esta demo. Solo cambian los documentos de entrada y la estructura del prompt.

---

## Cómo Activar la Demo

En el chatbot, escribí `/` y seleccioná `proposal`. Cuando pida los documentos, ingresá:

```
/proposal
discovery_transcript.md,client_brief.md,reference_cases.md,bigcheese.md
```

---

## ¿Qué Hace Esto?

Genera automáticamente una propuesta comercial profesional en formato HTML a partir de los documentos de entrada. Al ejecutar este comando, el agente:

1. Lee el contenido de cada documento indicado (separados por coma) usando el servidor MCP.
2. Analiza la información del cliente, sus desafíos técnicos, objetivos y presupuesto.
3. Consulta los placeholders disponibles en la plantilla HTML de propuesta.
4. Produce un archivo `.html` con nombre descriptivo en formato `propuesta_comercial_<cliente>_<tema>.html`, con todos los campos completados con datos reales extraídos de los documentos.

---

## ¿Cómo Ver el Resultado en el Navegador?

Una vez que el agente terminó y confirmó el nombre del archivo generado, levantá un servidor web estático desde la misma carpeta:

```bash
python -m http.server 8081
```

Luego abrí en el navegador:

```
https://{URL_Workshop}/proxy/8081
```

Vas a ver un listado de archivos. Hacé clic en el `.html` generado, por ejemplo `propuesta_comercial_fintrack_migracion_aws.html`, y se renderiza la propuesta con todo el estilo de la plantilla.

---

**Anterior:** [Módulo 10 — Prompts desde el Cliente](./Modulo-10-Prompts-desde-el-Cliente.md) | **Siguiente:** [Módulo 12 — Demo: Selección de Candidatos](./Modulo-12-Demo-Seleccion-de-Candidatos.md)
