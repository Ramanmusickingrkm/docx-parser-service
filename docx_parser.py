import io
import json
import base64
import re
from docx import Document
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def extract_plain_text(doc):
    """Extract plain text exactly as in DOCX"""
    text_parts = []
    
    for para in doc.paragraphs:
        if para.text.strip():
            text_parts.append(para.text)
    
    for table in doc.tables:
        text_parts.append("")
        for row in table.rows:
            row_text = []
            for cell in row.cells:
                row_text.append(cell.text.strip())
            text_parts.append(" | ".join(row_text))
        text_parts.append("")
    
    return "\n\n".join(text_parts)

def find_placeholders(text):
    """Find placeholders like [Field Name]"""
    placeholders = []
    seen = set()
    
    bracket = re.findall(r'\[([^\]]+)\]', text)
    curly = re.findall(r'\{\{([^}]+)\}\}', text)
    
    for field in bracket + curly:
        field_clean = field.strip()
        field_name = field_clean.lower().replace(' ', '_')
        if field_name not in seen:
            seen.add(field_name)
            placeholders.append({
                'name': field_name,
                'label': field_clean,
                'type': 'text'
            })
    
    return placeholders

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/parse-docx', methods=['POST'])
def parse_docx():
    try:
        data = request.get_json()
        if not data or 'file' not in data:
            return jsonify({'success': False, 'error': 'No file provided'}), 400
        
        file_buffer = base64.b64decode(data['file'])
        doc = Document(io.BytesIO(file_buffer))
        
        # Extract plain text (no HTML tags)
        plain_text = extract_plain_text(doc)
        
        # Find placeholders
        placeholders = find_placeholders(plain_text)
        
        # Wrap in pre tag to preserve formatting
        html_content = f'<div class="docx-content" style="font-family: Times New Roman, serif; font-size: 12pt; white-space: pre-wrap; line-height: 1.6;">{plain_text}</div>'
        
        return jsonify({
            'success': True,
            'html': html_content,
            'text': plain_text,
            'fields': placeholders
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)