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
        data = request.get_json()
        
        if not data or 'file' not in data:
            return jsonify({'success': False, 'error': 'No file provided'}), 400
        
        # Decode base64 file
        file_buffer = base64.b64decode(data['file'])
        
        # Parse DOCX
        result = parse_docx_to_html(file_buffer)
        
        if result['success']:
            # Wrap with styles
            final_html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: 'Times New Roman', Times, serif; font-size: 12pt; padding: 40px; max-width: 900px; margin: 0 auto; }}
        h1 {{ font-size: 18pt; text-align: center; color: #1e2d4a; }}
        h2 {{ font-size: 16pt; color: #1e2d4a; margin-top: 20px; }}
        h3 {{ font-size: 14pt; color: #1e2d4a; }}
        p {{ margin-bottom: 10px; line-height: 1.6; }}
        table {{ border-collapse: collapse; width: 100%; margin: 15px 0; }}
        th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
        .doc-field {{
            display: inline-block;
            min-width: 150px;
            padding: 4px 8px;
            background: #fefce8;
            border: none;
            border-bottom: 2px solid #fbbf24;
            outline: none;
        }}
        .doc-field:focus {{ background: #eff6ff; border-bottom-color: #2e6fea; }}
    </style>
</head>
<body>
{result['html']}
</body>
</html>'''
            
            return jsonify({
                'success': True,
                'html': final_html,
                'fields': result['fields'],
                'paragraphs': result.get('paragraphs', 0),
                'tables': result.get('tables', 0)
            })
        else:
            return jsonify({'success': False, 'error': result.get('error')}), 500
            
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)