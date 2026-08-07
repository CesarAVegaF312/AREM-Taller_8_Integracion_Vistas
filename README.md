# 🛠️ Taller 7: Integración de Vistas de Arquitectura

## 🎯 Objetivo

Integrar todas las vistas arquitectónicas desarrolladas a lo largo del curso (negocio, información, aplicaciones, infraestructura y seguridad) en una narrativa visual coherente, identificando cómo se relacionan y soportan los objetivos del cliente.

---

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

- Organice todas las vistas del caso base de FarmApp en un tablero visual (papel, Miro, draw.io).
- Analice cómo se conectan entre sí y qué relaciones hay entre capas (negocio → aplicaciones → infraestructura).
- Reciba retroalimentación del docente.

---

## 🧠 Parte 2: Aplicación al Cliente Real

Después de la clase, el equipo debe:

- Realizar la misma integración para su cliente real, combinando todos los entregables previos.
- Documentar cómo estas vistas se articulan entre sí y qué decisiones fueron clave.
- Realizar una reflexión crítica sobre la coherencia de la arquitectura.
- Investigar ejemplos reales de documentación de vistas en empresas similares.

---

## 📁 Estructura esperada del repositorio

```
taller-07-integracion-vistas/
├── README.md
├── clase/
│   ├── tablero-farmapp.drawio
│   └── notas.md
├── entrega/
│   ├── tablero-integrado-cliente.drawio
│   ├── informe.md
│   └── referencias.md
```

---

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
