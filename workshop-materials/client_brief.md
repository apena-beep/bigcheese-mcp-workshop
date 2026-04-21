# Brief Ejecutivo — FinTrack S.A.

## Sobre la empresa
FinTrack S.A. es una plataforma SaaS B2B de gestión de gastos corporativos fundada en 2018, con sede en Buenos Aires. Cuenta con 180 clientes empresariales activos, un equipo de 65 personas y procesa 2 millones de transacciones financieras por mes. Actualmente en proceso de Serie B.

## Situación actual
- Infraestructura 100% on-premise en dos datacenters propios
- Stack: Java/Spring Boot, PostgreSQL, Python (batches), React/Nginx
- Experiencia cloud limitada: S3 para backups, Lambda experimental
- Costo operativo de infraestructura: USD 18.000/mes
- Picos de procesamiento de hasta 12x el promedio en períodos de cierre mensual

## Problemas críticos
1. **Escalabilidad** — Infraestructura sobredimensionada para aguantar picos, ociosa el resto del mes
2. **Compliance** — Auditorías PCI-DSS anuales costosas y complejas sobre infraestructura on-premise
3. **Costos** — Pago por capacidad máxima aunque no se use; sin elasticidad

## Objetivos del proyecto
- Migrar la plataforma a AWS manteniendo continuidad operativa
- Reducir el costo mensual de infraestructura por debajo de USD 18.000
- Simplificar el proceso de auditoría PCI-DSS aprovechando los controles nativos de AWS
- Escalar automáticamente ante picos de fin de mes sin intervención manual

## Criterios de éxito
- Piloto del módulo de transacciones en producción en AWS en 60 días
- Migración completa en 6 meses
- Reducción de costos operativos demostrable
- Certificación PCI-DSS mantenida post-migración

## Presupuesto aprobado
- Proyecto de migración: hasta USD 120.000
- Costo operativo mensual objetivo en AWS: menor a USD 18.000

## Restricciones y requisitos
- El partner debe tener experiencia comprobada en fintech y PCI-DSS
- No se puede afectar la disponibilidad del servicio durante la migración
- Timeline condicionado por proceso de Serie B (inversores evalúan infraestructura)
