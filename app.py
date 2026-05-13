from flask import Flask, jsonify, Response
import psutil
import time

app = Flask(__name__)
START_TIME = time.time()

@app.route('/')
def home():
    return jsonify({"status": "ok", "service": "devops-api"})

@app.route('/health')
def health():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    return jsonify({
        "cpu_percent": cpu,
        "memory_percent": mem,
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "status": "healthy" if cpu < 80 and mem < 80 else "unhealthy"
    })

@app.route('/metrics')
def metrics():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    data = f"""# HELP app_cpu_percent CPU usage percentage
# TYPE app_cpu_percent gauge
app_cpu_percent {cpu}
# HELP app_memory_percent Memory usage percentage
# TYPE app_memory_percent gauge
app_memory_percent {mem}
"""
    return Response(data, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
