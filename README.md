# DevOps CI Workshop

![CI/CD](https://github.com/cesarpalacios/devops-ci-workshop/actions/workflows/ci.yml/badge.svg)

Taller de CI/CD con GitHub Actions + Observabilidad — DevOps UNAL 2026-1

---

## Objetivo

Construir un pipeline CI/CD completo usando **GitHub Actions** que compile, pruebe, despliegue y monitoree una aplicación, integrando los conceptos de artefactos, contenerización y observabilidad.

---

## La Aplicación

Un API REST en Python (Flask) con 3 endpoints:

| Endpoint | Descripción |
|----------|-------------|
| `/` | Status del servicio |
| `/health` | Health check con métricas de sistema (CPU, memoria, uptime) |
| `/metrics` | Métricas en formato Prometheus |

---

## Requisitos

- Cuenta de GitHub (activa, verificada)
- Navegador con acceso a github.com

---

## Actividad 1: Fork y Exploración (10 min)

1. Hacer **Fork** de este repositorio a su cuenta personal
2. Clonar el fork localmente
3. Explorar la estructura:
   ```
   ├── app.py              ← API Flask
   ├── test_app.py         ← Tests unitarios
   ├── requirements.txt    ← Dependencias Python
   ├── Dockerfile          ← Contenerización
   ├── docker-compose.yml  ← API + Prometheus
   ├── prometheus.yml      ← Config Prometheus
   └── .github/
       └── workflows/
           └── ci.yml      ← CREAR ESTE ARCHIVO
   ```

---

## Actividad 2: Crear el Pipeline CI (30 min)

Crear el archivo `.github/workflows/ci.yml` en su fork:

### Paso 1: Trigger y Checkout

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout código
      uses: actions/checkout@v4
```

**Pregunta:** ¿Qué significa `on: push: branches: [main]`? ¿Cuándo se ejecuta este pipeline?

### Paso 2: Setup Python + Tests

```yaml
    - name: Configurar Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    
    - name: Instalar dependencias
      run: pip install -r requirements.txt
    
    - name: Ejecutar tests
      run: pytest test_app.py -v
```

**Pregunta:** ¿Qué pasa si un test falla? ¿El pipeline continúa?

### Paso 3: Build de Docker Image

```yaml
    - name: Build Docker image
      run: docker build -t devops-api:${{ github.sha }} .
    
    - name: Verificar imagen
      run: docker images | grep devops-api
```

**Pregunta:** ¿Qué es `${{ github.sha }}`? ¿Por qué usarlo como tag?

### Paso 4: Test de contenedor

```yaml
    - name: Levantar contenedor
      run: |
        docker run -d -p 5000:5000 --name test-api devops-api:${{ github.sha }}
        sleep 5
    
    - name: Test endpoint health
      run: |
        curl -s http://localhost:5000/health | grep healthy
    
    - name: Test endpoint metrics
      run: |
        curl -s http://localhost:5000/metrics | grep app_cpu_percent
    
    - name: Detener contenedor
      if: always()
      run: docker rm -f test-api
```

**Pregunta:** ¿Para qué sirve `if: always()`? ¿Qué pasaría sin él?

### Paso 5: Artefacto

```yaml
    - name: Generar reporte
      if: always()
      run: |
        echo "## Pipeline Report" > report.md
        echo "- Commit: ${{ github.sha }}" >> report.md
        echo "- Branch: ${{ github.ref_name }}" >> report.md
        echo "- Status: ${{ job.status }}" >> report.md
    
    - name: Subir artefacto
      uses: actions/upload-artifact@v4
      with:
        name: pipeline-report
        path: report.md
```

**Pregunta:** ¿Qué es un artefacto en el contexto de CI/CD? ¿Cuándo se usaría en un proyecto real?

---

## Actividad 3: Commit, Push y Observar (15 min)

1. Hacer commit del archivo `ci.yml`
2. Push a `main`
3. Ir a la pestaña **Actions** en GitHub
4. Observar la ejecución del pipeline en tiempo real
5. Verificar que todos los pasos pasan (verde ✅)

**Si falla:** Leer el log del paso que falló, identificar el error, corregir, hacer push nuevamente.

---

## Actividad 4: Agregar Monitoreo con Prometheus (25 min)

Agregar un paso al pipeline para validar las métricas con Prometheus:

```yaml
    - name: Levantar con Docker Compose
      run: |
        docker compose up -d
        sleep 10
    
    - name: Verificar Prometheus targets
      run: |
        curl -s http://localhost:9090/api/v1/targets | grep up
    
    - name: Consultar métricas
      run: |
        curl -s "http://localhost:9090/api/v1/query?query=app_cpu_percent" | head -20
```

**Pregunta:** ¿Qué hace Prometheus con el endpoint `/metrics`? ¿Qué es un `scrape`?

---

## Actividad 5: Agregar Badges (5 min)

Modificar el `README.md` de su fork y cambiar `TU_USUARIO` por su usuario de GitHub:

```markdown
![CI/CD](https://github.com/TU_USUARIO/devops-ci-workshop/actions/workflows/ci.yml/badge.svg)
```

Esto muestra un badge verde/rojo según el estado del último pipeline.

---

## Entregable

Al finalizar la clase, cada grupo debe tener:

1. ✅ Repositorio fork con pipeline funcional (verde en Actions)
2. ✅ Pipeline que: ejecuta tests → buildea Docker → testa contenedor → genera artefacto
3. ✅ Métricas expuestas en `/metrics` (formato Prometheus)
4. ✅ Badge en el README
5. ✅ Captura de pantalla del pipeline ejecutado

**Enviar:** Link del repositorio al correo del docente antes de las 8:00 PM.

---

## Pipeline Final Completo

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Configurar Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    
    - name: Instalar dependencias
      run: pip install -r requirements.txt
    
    - name: Ejecutar tests
      run: pytest test_app.py -v
    
    - name: Build Docker image
      run: docker build -t devops-api:${{ github.sha }} .
    
    - name: Levantar contenedor
      run: |
        docker run -d -p 5000:5000 --name test-api devops-api:${{ github.sha }}
        sleep 5
    
    - name: Test endpoints
      run: |
        curl -s http://localhost:5000/health | grep healthy
        curl -s http://localhost:5000/metrics | grep app_cpu_percent
    
    - name: Detener contenedor
      if: always()
      run: docker rm -f test-api
    
    - name: Generar reporte
      if: always()
      run: |
        echo "## Pipeline Report" > report.md
        echo "- Commit: ${{ github.sha }}" >> report.md
        echo "- Branch: ${{ github.ref_name }}" >> report.md
        echo "- Status: ${{ job.status }}" >> report.md
    
    - name: Subir artefacto
      uses: actions/upload-artifact@v4
      with:
        name: pipeline-report
        path: report.md
```

---

## Ejecutar localmente

```bash
# Sin Docker
pip install -r requirements.txt
python app.py

# Con Docker
docker build -t devops-api .
docker run -p 5000:5000 devops-api

# Con Docker Compose (API + Prometheus)
docker compose up -d
# API: http://localhost:5000
# Prometheus: http://localhost:9090

# Tests
pytest test_app.py -v
```

---

## Conceptos Cubiertos

| Tema | Actividad |
|------|-----------|
| Git/GitHub | Fork, branches, commits |
| Pipelines CI/CD | GitHub Actions workflow |
| Docker | Build + run container |
| Artefactos | Upload artifact |
| Observabilidad | Prometheus + métricas + /health |

---

*DevOps — Universidad Nacional de Colombia — Sede Manizales — 2026-1*
