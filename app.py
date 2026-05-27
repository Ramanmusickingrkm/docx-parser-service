import base64
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from docx_parser import parse_docx_to_html

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'status': 'ok',
        'message': 'DOCX Parser Service is running',
        'endpoints': {
            'POST /parse-docx': 'Parse DOCX file to HTML',
            'GET /health': 'Health check'
        }
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/parse-docx', methods=['POST'])
def parse_docx():
    try:
        # Get request data
        data = request.get_json()
        
        if not data or 'file' not in data:
            return jsonify({
                'success': False,
                'error': 'No file provided'
            }), 400
        
        # Decode base64 file
        file_buffer = base64.b64decode(data['file'])
        
        # Parse DOCX
        result = parse_docx_to_html(file_buffer)
        
        if result['success']:
            return jsonify({
                'success': True,
                'html': result['html'],
                'fields': result['fields'],
                'stats': {
                    'paragraphs': result.get('paragraphs', 0),
                    'tables': result.get('tables', 0),
                    'fields_count': len(result['fields'])
                }
            })
        else:
            return jsonify({
                'success': False,
                'error': result.get('error', 'Unknown error')
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)