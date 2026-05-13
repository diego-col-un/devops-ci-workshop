# DevOps CI Workshop — Hackathon 🔧

![CI/CD](https://github.com/diego-col-un/devops-ci-workshop/actions/workflows/ci.yml/badge.svg)

**Trabajen en grupos de 2 personas. Este repositorio tiene errores. Su misión es encontrarlos y corregirlos todos.**

---

## Reglas

1. Hacer **Fork** de este repositorio
2. Encontrar y corregir **TODOS** los errores
3. Lograr que el pipeline de GitHub Actions pase **verde ✅**
4. Hacer push con las correcciones
5. Enviar el link del repositorio con un archivo `CORRECCIONES.md` listando cada error encontrado y qué se cambió

**El taller termina cuando logren pipeline verde con todos los pasos pasando. Documenten cada corrección en `CORRECCIONES.md`.**

---

## La Aplicación

API REST en Python (Flask) con 3 endpoints que DEBEN funcionar:

| Endpoint | Qué debería retornar |
|----------|---------------------|
| `/` | `{"status": "ok", "service": "devops-api"}` |
| `/health` | JSON con CPU, memoria, uptime y status "healthy"/"unhealthy" |
| `/metrics` | Métricas en formato Prometheus |

---

## Archivos

```
├── app.py                    ← API Flask (¿todo bien?)
├── test_app.py               ← Tests unitarios (¿pasarán?)
├── requirements.txt          ← Dependencias (¿está completo?)
├── Dockerfile                ← Contenerización (¿está optimizado?)
├── docker-compose.yml        ← API + Prometheus (¿los puertos cuadran?)
├── prometheus.yml            ← Config Prometheus (¿las rutas son correctas?)
└── .github/workflows/ci.yml  ← Pipeline CI/CD (¿pasará verde?)
```

---

## Pistas

Los errores están en diferentes niveles:

- **Código:** Bugs en app.py y test_app.py
- **Configuración:** Puertos, rutas, dependencias
- **Infraestructura:** Dockerfile, docker-compose, Prometheus
- **Pipeline:** El workflow tiene pasos que van a fallar

**No todos los errores son obvios.** Algunos solo se ven cuando ejecutás el pipeline o levantás el contenedor.

---

## Cómo trabajar

### Localmente (recomendado para debuggear)

```bash
# Clonar tu fork
git clone https://github.com/TU_USUARIO/devops-ci-workshop.git
cd devops-ci-workshop

# Instalar y probar
pip install -r requirements.txt
python app.py

# En otra terminal: correr tests
pytest test_app.py -v

# Probar endpoints
curl http://localhost:5000/
curl http://localhost:5000/health
curl http://localhost:5000/metrics

# Probar con Docker
docker build -t devops-api .
docker run -p 5000:5000 devops-api

# Probar con Docker Compose
docker compose up -d
```

### En GitHub

1. Hacer correcciones
2. Commit + push a `main`
3. Ir a la pestaña **Actions** y ver si el pipeline pasa
4. Si falla: leer los logs, corregir, push nuevamente

---

## Entregable

Crear un archivo `CORRECCIONES.md` en el repositorio con este formato:

```markdown
# Correcciones

**Integrantes:**
- Nombre 1
- Nombre 2

## Error 1
- **Archivo:** app.py
- **Problema:** El puerto estaba en 5001 en vez de 5000
- **Solución:** Cambié `port=5001` por `port=5000`

## Error 2
- **Archivo:** ...
- **Problema:** ...
- **Solución:** ...
```

**Enviar:** Link del repositorio + captura del pipeline verde.

---

## Pipeline que debe pasar

El pipeline hace:

1. ✅ Checkout del código
2. ✅ Setup Python 3.11
3. ✅ Instalar dependencias
4. ✅ Ejecutar tests con pytest
5. ✅ Build de Docker image
6. ✅ Levantar contenedor y testear endpoints
7. ✅ Generar reporte y subir como artefacto

**Cuando los 7 pasos pasen verde, ganaron.**

---

## Pistas extra (si están bloqueados)

<details>
<summary>💡 Pista 1: Endpoints</summary>
Revisá que los endpoints en app.py coincidan con los que testean test_app.py y ci.yml. ¿`/metrics` es lo mismo que `/metric`?
</details>

<details>
<summary>💡 Pista 2: Puertos</summary>
Revisá TODOS los puertos: app.py, Dockerfile, docker-compose.yml, ci.yml. Deben ser consistentes.
</details>

<details>
<summary>💡 Pista 3: Dependencias</summary>
¿pytest está en requirements.txt? ¿Y en el pipeline se puede ejecutar si no está instalado?
</details>

<details>
<summary>💡 Pista 4: Tests</summary>
Revisá las aserciones de test_app.py. ¿El endpoint `/` realmente devuelve `status: "running"`? ¿`/health` tiene campo `uptime_seconds`?
</details>

<details>
<summary>💡 Pista 5: Dockerfile</summary>
¿`python:3.11` es lo mismo que `python:3.11-slim`? Funciona, pero no es lo óptimo. Hay errores más graves primero.
</details>

<details>
<summary>💡 Pista 6: Prometheus</summary>
En docker-compose, los servicios se comunican por nombre de servicio, no por localhost. ¿El target en prometheus.yml es correcto para docker-compose?
</details>

---

*DevOps — Universidad Nacional de Colombia — Sede Manizales — 2026-1*
