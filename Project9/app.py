from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    # System info like IP, port, environment
    ip = request.host.split(':')[0]
    port = request.host.split(':')[1] if ':' in request.host else '8000'
    environment = 'Debug' if app.debug else 'Production'
    return {
        "IP": ip,
        "Port": port,
        "Environment": environment
    }

@app.route('/status')
def status():
    if app.debug:
        return "Running in Debug Mode"
    else:
        return "Running in Production Mode"

if __name__ == '__main__':
    # Run on port 8000 (change from default 5000)
    app.run(host='0.0.0.0', port=8000)
