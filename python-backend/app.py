from flask import Flask, jsonify, request
from flask_cors import CORS
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configure CORS to allow all origins
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "expose_headers": ["Content-Type", "Authorization"],
        "max_age": 3600
    }
})

@app.route('/api/hello')
def hello():
    client_ip = request.remote_addr
    forwarded_for = request.headers.get('X-Forwarded-For')
    real_ip = request.headers.get('X-Real-IP')
    
    logger.info(f"Hello endpoint called from:")
    logger.info(f"Remote Addr: {client_ip}")
    logger.info(f"X-Forwarded-For: {forwarded_for}")
    logger.info(f"X-Real-IP: {real_ip}")
    
    return jsonify({
        "message": "Hello from Python Backend!",
        "status": "success",
        "client_info": {
            "remote_addr": client_ip,
            "forwarded_for": forwarded_for,
            "real_ip": real_ip
        }
    })

@app.route('/api/test')
def test():
    client_ip = request.remote_addr
    forwarded_for = request.headers.get('X-Forwarded-For')
    real_ip = request.headers.get('X-Real-IP')
    
    logger.info(f"Test endpoint called from:")
    logger.info(f"Remote Addr: {client_ip}")
    logger.info(f"X-Forwarded-For: {forwarded_for}")
    logger.info(f"X-Real-IP: {real_ip}")
    
    return jsonify({
        "message": "Backend connection successful!",
        "status": "success",
        "client_info": {
            "remote_addr": client_ip,
            "forwarded_for": forwarded_for,
            "real_ip": real_ip
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 