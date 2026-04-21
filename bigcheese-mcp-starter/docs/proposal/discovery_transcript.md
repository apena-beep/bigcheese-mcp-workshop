# Transcripción — Reunión de Discovery
**Cliente:** FinTrack S.A.  
**Fecha:** 10 de abril de 2026  
**Participantes:** Lucía Herrera (CTO, FinTrack), Andrés Molina (VP Ingeniería, FinTrack), Carlos Ríos (Solutions Architect, BigCheese), Paula Vega (Account Manager, BigCheese)

---

**Paula:** Gracias por el tiempo, Lucía. La idea de hoy es entender bien dónde están parados y qué los trajo a esta conversación.

**Lucía:** Claro. FinTrack es una plataforma de gestión de gastos corporativos. Tenemos unos 180 clientes empresariales, procesamos alrededor de 2 millones de transacciones por mes. El problema es que nuestra infraestructura actual es on-premise, en dos datacenters propios en Buenos Aires. Llevamos 6 años así y ya no da más.

**Andrés:** El tema concreto es que los picos de fin de mes nos matan. Tenemos que sobredimensionar los servidores para aguantar esos picos, y el resto del mes esa capacidad está ociosa. Estamos pagando por infraestructura que no usamos.

**Carlos:** ¿Cuánto es el delta entre el pico y el promedio?

**Andrés:** En procesamiento de transacciones, el pico puede ser 8x el promedio. En reportes financieros, que corren en batch, llegamos a 12x. Es inmanejable con hierro fijo.

**Carlos:** ¿Qué stack tecnológico tienen hoy?

**Andrés:** Backend en Java, Spring Boot. Base de datos PostgreSQL, dos instancias con replicación manual. Los batches los corremos con scripts Python sobre servidores dedicados. Frontend en React, servido desde Nginx. Todo on-premise.

**Lucía:** Y el problema de seguridad también es importante. Manejamos datos financieros sensibles. Tenemos auditorías de PCI-DSS cada año y el proceso es un dolor enorme. Queremos que la infraestructura nos ayude a cumplir, no que sea un obstáculo.

**Carlos:** ¿Tienen alguna experiencia previa con cloud?

**Andrés:** Tenemos un par de servicios menores en AWS, básicamente S3 para backups y algún Lambda experimental. Pero nada productivo crítico.

**Paula:** ¿Cuál es el driver principal: costos, escalabilidad o compliance?

**Lucía:** Los tres, pero si me obligás a ordenarlos: primero escalabilidad, después compliance, después costos. Aunque si podemos demostrar ahorro, mejor para justificar internamente.

**Carlos:** ¿Tienen un timeline en mente?

**Lucía:** Queremos estar en producción en AWS antes de fin de año. Tenemos una ronda de inversión Serie B en proceso y los inversores están mirando la infraestructura. Necesitamos mostrar solidez técnica.

**Andrés:** Idealmente un piloto en 60 días con el módulo de transacciones, y migración completa en 6 meses.

**Carlos:** ¿Presupuesto estimado?

**Lucía:** Tenemos aprobado internamente hasta USD 120.000 para el proyecto de migración. El costo operativo mensual en AWS esperamos que sea menor a lo que pagamos hoy en datacenter, que son unos USD 18.000 por mes.

**Paula:** Perfecto. Con esto ya tenemos suficiente para armar una propuesta. Les mandamos algo la semana que viene.

**Lucía:** Genial. Una cosa más: necesitamos que el partner tenga experiencia en fintech y en PCI-DSS. No podemos permitirnos aprender en producción.

**Carlos:** Entendido. Tenemos casos en ese vertical que les vamos a compartir.
