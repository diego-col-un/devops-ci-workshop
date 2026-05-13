# Correcciones

**Integrantes:**
- Nombre 1
- Nombre 2

## Error 1
- **Archivo:** app.py
- **Problema:** El puerto estaba en 5001 en vez de 5000
- **Solución:** Cambié `port=5001` por `port=5000`

## Error 2
- **Archivo:** app.py
- **Problema:** endpoint /metric le falta la s  
- **Solución:** /metrics

## Error 3
- **Archivo:** app.py
- **Problema:** endpoint /health le falta el uptime (como lo pide el el README)
- **Solución:** agregar "uptime": round(time.time() - START_TIME, 2)

## Error 4
- **Archivo:** docker-compose.yml
- **Problema:** El mapeo de puerto estaba en 5001 en vez de 5000
- **Solución:** - "5000:5000"

## Error 5
- **Archivo:** prometheus.yml
- **Problema:** target localhost no funciona en docker
- **Solución:** Cambiar el target localhost por api

## Error 6
- **Archivo:** prometheus.yml
- **Problema:**  endpoint /metric le falta la s  
- **Solución:** /metrics

## Error 7
- **Archivo:** app.py
- **Problema:**  falta importar time 
- **Solución:** import time