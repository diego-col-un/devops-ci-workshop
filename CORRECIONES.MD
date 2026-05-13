# Correcciones

**Integrantes:**
- Diego Fernando Aristizábal Gutierrez
- David Parra Castaño

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

## Error 8
- **Archivo:** test_app.py
- **Problema:**  el programa entrega status=ok y el test está esperando "running" 
- **Solución:** cambiar en test assert data["status"] == "running"
 por
assert data["status"] == "ok"

## Error 9
- **Archivo:** docker-compose.yml
- **Problema:**  no hay una red entre docker compose para los servicios 
- **Solución:** integrar en el archivo networks "monitoring" con driver: bridge

## Error 10
- **Archivo:** app.py
- **Problema:** funcion metrics está devolviendo html, prometheus espera plain   
- **Solución:** corregir funcion e importar Response

    return Response(data, mimetype='text/plain')