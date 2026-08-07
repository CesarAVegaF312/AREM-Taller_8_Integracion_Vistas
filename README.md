# 🛠️ Taller 8: Integración de Vistas de Arquitectura

## 🎯 Objetivo

Integrar todas las vistas arquitectónicas desarrolladas a lo largo del curso (negocio, información, aplicaciones, infraestructura y seguridad) en una narrativa visual coherente, identificando cómo se relacionan y soportan los objetivos del cliente. Con el cliente real, la integración debe incluir tanto el estado actual (AS-IS) como la arquitectura objetivo (TO-BE) propuesta en el Taller 7 (Opportunities & Solutions).

---

## 📘 Guía paso a paso

Antes de armar el tablero, revise la [**Guía Paso a Paso: Integración de Vistas de Arquitectura**](clase/guia_paso_a_paso_integracion.md). Incluye la metodología de 5 pasos para pasar de un inventario de vistas sueltas a un tablero conectado con narrativa, un ejemplo completo construido paso a paso sobre el caso de FarmApp (incluyendo una tabla para verificar que ningún elemento quede huérfano), y una tabla de errores comunes.

## 💊 Caso base de referencia: FarmApp (Cadena de Farmacias con E-Commerce)

FarmApp es una cadena nacional de farmacias que ha incorporado un sistema de e-commerce integrado a su red de puntos físicos. La plataforma permite a los clientes realizar pedidos de medicamentos, consultar disponibilidad, recibir recomendaciones personalizadas y hacer pagos digitales. Internamente se sincronizan sistemas como el POS, el CRM, el inventario y el sistema de logística de entrega. Integrar todas las vistas arquitectónicas de FarmApp permite visualizar cómo interactúan los diferentes niveles (negocio, datos, aplicaciones, infraestructura y seguridad) y cómo se alinean para brindar un servicio consistente y seguro.

**Contexto:**
- FarmApp es una cadena de farmacias físicas que ofrece pedidos en línea por app/web, integrados con el sistema de inventario y el CRM de clientes.
- Dispone de servicios como rastreo de entregas, pagos electrónicos, promociones personalizadas y registro de historiales de compra.

**Vistas a integrar:**

1. **Negocio:** procesos de compra, prescripción, despacho
2. **Información:** entidades como Producto, Cliente, Pedido, Descuento
3. **Aplicaciones:** App móvil, plataforma e-commerce, sistema POS, CRM
4. **Infraestructura:** servidores regionales, nube híbrida, base de datos replicada
5. **Seguridad:** control de accesos por rol, cifrado de datos personales, monitoreo de fraude

---

## 🧪 Parte 1: Trabajo en Clase

Durante la clase se espera que el equipo:

Siga la metodología de 5 pasos de la [guía paso a paso](clase/guia_paso_a_paso_integracion.md) para armar el tablero integrado de FarmApp:

1. Organice las 5 vistas como capas del tablero.
2. Ubique los elementos de cada vista dentro de su capa, sin conectar todavía.
3. Trace las relaciones verticales entre capas para un proceso de negocio a la vez.
4. Redacte la narrativa que explique el porqué de esas conexiones.
5. Revise que ningún elemento quede huérfano, con la [checklist de autoevaluación](clase/guia_paso_a_paso_integracion.md#4-checklist-de-autoevaluación-antes-de-entregar).

- Use papel, Miro o draw.io para el tablero visual.
- Reciba retroalimentación del docente y registre avances en `clase/notas.md` (use la [plantilla de notas](plantillas/plantilla_notas.md)).

---

## 🧠 Parte 2: Aplicación al Cliente Real

Después de la clase, el equipo debe:

- Realizar la misma integración para su cliente real, combinando todos los entregables previos —incluyendo el TO-BE de Aplicaciones y Tecnología del Taller 7—, siguiendo los mismos 5 pasos de la metodología.
- Documentar cómo estas vistas se articulan entre sí y qué decisiones fueron clave.
- Redactar el informe en `entrega/informe.md` usando la [plantilla de informe del taller](plantillas/plantilla_informe_taller.md), con una reflexión crítica sobre la coherencia de la arquitectura.
- Investigar ejemplos reales de documentación de vistas en empresas similares, y registrar las fuentes en `entrega/referencias.md` con la [plantilla de referencias](plantillas/plantilla_referencias.md).

---

## 📁 Estructura esperada del repositorio

```text
taller-08-integracion-vistas/
├── README.md
├── clase/
│   ├── guia_paso_a_paso_integracion.md   # Metodología de 5 pasos y ejemplo guiado
│   ├── tablero-farmapp.drawio
│   └── notas.md                          # Ver plantillas/plantilla_notas.md
├── entrega/
│   ├── tablero-integrado-cliente.drawio
│   ├── informe.md                        # Ver plantillas/plantilla_informe_taller.md
│   └── referencias.md                    # Ver plantillas/plantilla_referencias.md
└── plantillas/
    ├── plantilla_informe_taller.md
    ├── plantilla_notas.md
    └── plantilla_referencias.md
```

---

## ⚠️ Errores comunes

Antes de entregar, compare su tablero contra los errores más frecuentes (vistas sin conectar, seguridad omitida, narrativa que solo describe el diagrama) documentados en la [sección 3 de la guía paso a paso](clase/guia_paso_a_paso_integracion.md#3-errores-comunes-a-evitar).

## 📤 Entregables

- Tablero de vistas integradas del cliente
- Informe narrativo que explique la coherencia de la arquitectura
- Referencias o ejemplos usados para integrar

---

## 📊 Rúbrica de Evaluación

| Criterio                            | Excelente (5)                                                          | Aceptable (3) / Insuficiente (1–2)                    |
|-------------------------------------|------------------------------------------------------------------------|---------------------------------------------------------|
| Integración de vistas (caso base)   | Relación clara entre vistas, completa y visualmente conectada         | Fragmentado o poco consistente                         |
| Aplicación al cliente real          | Arquitectura bien articulada, reflejando decisiones previas           | Conexión débil o confusa entre vistas                  |
| Análisis y narrativa                | Informe bien redactado que explica el porqué de la arquitectura       | Documento desordenado o superficial                    |
| Investigación complementaria        | Referencias reales o buenas prácticas de documentación arquitectónica | Investigación escasa o sin aporte técnico              |

---

## ✅ Licencia

Este taller hace parte del curso de Arquitectura Empresarial - Universidad de La Sabana. Uso académico bajo licencia MIT.
