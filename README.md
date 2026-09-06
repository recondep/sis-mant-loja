# 🏭 EmbuLoja — Módulo SIS-MANT (Loja)

**SIS-MANT (Planta Loja)** es un sistema web de gestión de mantenimiento industrial diseñado para coordinar, registrar y validar las órdenes de trabajo de la maquinaria procesadora en la planta de EmbuLoja. Este repositorio contiene la arquitectura backend en Django y la suite de pruebas integradas con GitHub Actions.

---

## 👩‍💻 Autora

* **Rosa Elena Conde Paucar**  
  *Ingeniería / Tecnologías de la Información — Universidad Estatal Amazónica*

---

## 💻 Tecnologías Utilizadas

* 🐍 **Lenguaje:** Python 3.12
* ⚙️ **Framework:** Django 5.0
* 🗄️ **Base de Datos:** SQLite3
* 🔀 **Control de Versiones:** Git & GitHub
* 🤖 **Integración Continua:** GitHub Actions (`ci.yml`)

---

## 🌿 Estrategia de Control de Versiones (GitHub Flow)

El desarrollo del módulo sigue una estrategia de integración continua estricta:

* 📌 **`main`:** Rama de código de producción. Solo recibe actualizaciones aprobadas mediante Pull Requests.
* 🌿 **`feature/*`:** Ramas de trabajo destinadas al desarrollo independiente de funciones (ej. `feature/modulo-ordenes`).
* 🔀 **Pull Requests:** Proceso de revisión y validación donde se ejecutan los tests automáticos antes de consolidar el código.

---

## ⚡ Pipeline de Integración Continua (CI)

Cada `push` o `pull request` desencadena el flujo de pruebas en GitHub Actions:

```text
✔ CI SIS-MANT Loja Pipeline #18: Commit 7f3b12a pushed by rosaconde
  ├── Set up job                                       ✔ 2s
  ├── Run actions/checkout@v4                          ✔ 1s
  ├── Set up Python 3.12                               ✔ 3s
  ├── Instalar Dependencias                            ✔ 11s
  └── Ejecutar Pruebas Automatizadas (python manage.py test) ✔ 2s
      └── Result: 4 passed (OK)
