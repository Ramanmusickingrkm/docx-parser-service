import base64
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from docx_parser import parse_docx_to_html

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'status': 'ok',
        'message': 'DOCX Parser Service is running'
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/parse-docx', methods=['POST'])
def parse_docx():
    try:
        file_buffer = None
        
        # Case 1: multipart/form-data (for frontend FormData)
        if 'file' in request.files:
            file = request.files['file']
            file_buffer = file.read()
            print("📁 Received file via multipart/form-data")
        
        # Case 2: JSON with base64 (for Node.js backend)
        elif request.is_json:
            data = request.get_json()
            if data and 'file' in data:
                file_buffer = base64.b64decode(data['file'])
                print("📁 Received file via JSON base64")
        
        if not file_buffer:
            return jsonify({'success': False, 'error': 'No file provided'}), 400
        
        result = parse_docx_to_html(file_buffer)
        
        if result['success']:
            return jsonify({
                'success': True,
                'html': result['html'],
                'text': result['text'],
                'fields': result['fields'],
                'paragraphs': result.get('paragraphs', 0),
                'tables': result.get('tables', 0)
            })
        else:
            return jsonify({'success': False, 'error': result.get('error')}), 500
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)