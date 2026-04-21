# Módulo 1: Introducción a MCP

## ¿Qué es MCP?

MCP (Model Context Protocol) es un protocolo abierto creado por Anthropic y adoptado por AWS, Microsoft y Google. Su propósito es definir una forma estándar de conectar modelos de lenguaje con sistemas externos: bases de datos, APIs, archivos, lo que sea.

Antes de MCP, cada equipo resolvía el problema de integración de forma diferente. Cada desarrollador escribía su propio código para conectar el modelo con cada sistema. MCP estandariza esa conexión.

> La analogía más útil: **MCP es para los modelos de lenguaje lo que USB fue para los computadores.** Antes del USB cada periférico tenía su propio conector. USB estandarizó la conexión y desde entonces cualquier dispositivo funciona con cualquier computador. MCP hace lo mismo con las integraciones de IA.

---

## El Problema que Resuelve

Imaginá que tu plataforma conversacional necesita consultar el repositorio interno de documentos, el sistema de tickets y la base de conocimiento de la empresa al mismo tiempo. Para cada uno necesitarías:

- Escribir los esquemas de las herramientas para que el modelo entienda qué puede pedir
- Implementar las funciones que hacen las llamadas a cada sistema
- Manejar los errores de cada integración de forma separada
- Transformar los datos al formato que espera el modelo
- Mantener todo ese código cuando los sistemas cambian

Y si mañana hay un cuarto sistema que conectar, el proceso se repite desde cero.

### Flujo sin MCP — el camino que tomó Sebastián

```
Plataforma IA
     ↓
     ├──→ [código propio] ──→ CRM
     ├──→ [código propio] ──→ Base de datos
     ├──→ [código propio] ──→ Sistema de tickets
     └──→ [código propio] ──→ ERP

Resultado:
  - 4 integraciones acopladas a la aplicación
  - Cada API que cambia rompe la app
  - El modelo consume procesamiento en cada llamada, sin control
  - El cliente número cinco pide integrar su sistema → todo empieza de cero
```

### Flujo con MCP — la arquitectura correcta

```
Plataforma IA
     ↓
 Cliente MCP  ←── una sola interfaz estándar
     ↓
     ├──→ Servidor MCP ──→ CRM
     ├──→ Servidor MCP ──→ Base de datos
     ├──→ Servidor MCP ──→ Sistema de tickets
     └──→ Servidor MCP ──→ ERP

Resultado:
  - División de responsabilidades clara
  - La app nunca cambia cuando un sistema externo se actualiza
  - El modelo solo procesa cuando realmente necesita razonar
  - Un servidor nuevo = una integración nueva, sin tocar la app
```

---

## La Diferencia Clave

| Sin MCP | Con MCP |
|---------|---------|
| Escribís los esquemas de herramientas para cada sistema | El servidor los define una vez y los expone al modelo |
| El código de integración está pegado a tu aplicación | Las integraciones viven en el servidor, separadas de la app |
| Agregar un sistema implica tocar la aplicación | Se conecta un nuevo servidor sin modificar la app |
| Dos aplicaciones que usan el mismo sistema escriben el mismo código dos veces | Un servidor MCP puede ser reutilizado por cualquier aplicación |

---

## Los Tres Componentes

Todo servidor MCP expone tres tipos de componentes. La pregunta de diseño es siempre la misma: **¿quién debería controlar esta funcionalidad?**

| Componente | Quién lo controla | Cuándo usarlo |
|------------|-------------------|---------------|
| **Herramientas** | El modelo | Cuando el modelo necesita ejecutar una acción o consultar datos en tiempo real |
| **Recursos** | Tu aplicación | Cuando la interfaz necesita datos para funcionar: listas, contexto, contenido a inyectar |
| **Prompts** | El usuario | Cuando hay un flujo repetitivo que requiere alta calidad consistente |

---

## Arquitectura en una Línea

```
Tu app  ↔  Cliente MCP  ↔  Servidor MCP  ↔  Sistema externo
```

El cliente MCP vive en tu aplicación y sabe hablar con cualquier servidor MCP. El servidor MCP vive del lado del sistema externo y sabe cómo exponerlo. Como ambos hablan el mismo protocolo, son intercambiables: podés cambiar el servidor sin tocar el cliente, y viceversa.

---

## ¿Qué Consume Procesamiento del Modelo y Qué No?

Esta es la pregunta más importante para tomar decisiones de arquitectura.

**Genera costos de procesamiento:**
- El mensaje del usuario que llega al modelo
- Las descripciones de las herramientas disponibles
- El contenido de cada documento que el modelo lee usando una herramienta
- La respuesta que el modelo genera

**No genera costos de procesamiento:**
- Llamar a `list_tools()` para obtener el catálogo de herramientas
- Leer un Recurso directamente desde la app (autocompletar con `@`, por ejemplo)
- La ejecución del código del servidor

> **Regla para diseñar:** ¿Necesita razonamiento? → Herramienta → pasa por el modelo. ¿Son solo datos para la interfaz? → Recurso → la app lo resuelve sola. ¿Es un flujo repetitivo? → Prompt → el usuario lo activa cuando lo necesita.

---

## AWS y MCP

AWS publicó **53 servidores MCP** para sus servicios más usados. Si el sistema del cliente vive en AWS, el servidor MCP probablemente ya existe.

Categorías disponibles:
- **Datos y analítica:** DynamoDB, Aurora PostgreSQL, Aurora MySQL, Redshift, DocumentDB, ElastiCache
- **IA y Machine Learning:** Bedrock Knowledge Bases, Kendra, SageMaker
- **Infraestructura:** EKS, ECS, Lambda, CloudFormation, Serverless
- **Operaciones y costos:** CloudWatch, CloudTrail, Cost Management, Pricing
- **Integración:** SNS/SQS, Step Functions, Amazon MQ

Fuente: [awslabs.github.io/mcp](https://awslabs.github.io/mcp/)

---

**Anterior:** [Módulo 0 — Entorno de Desarrollo](./Modulo-0-Entorno-de-Desarrollo.md) | **Siguiente:** [Módulo 2 — Clientes MCP](./Modulo-2-Clientes-MCP.md)
