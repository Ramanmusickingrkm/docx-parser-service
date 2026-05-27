import io
import json
import base64
import re
from docx import Document

def parse_docx_to_html(file_buffer):
    """Convert DOCX to plain text and detect fields"""
    try:
        doc = Document(io.BytesIO(file_buffer))
        text_parts = []
        all_fields = []
        seen_fields = set()
        
        # Extract paragraphs and detect fields
        for para in doc.paragraphs:
            if para.text and para.text.strip():
                raw_text = para.text.strip()
                # Clean the text
                raw_text = re.sub(r'<[^>]+>', '', raw_text)
                raw_text = re.sub(r'\s+', ' ', raw_text)
                text_parts.append(raw_text)
                
                # Find placeholders like [Field Name] or {{Field Name}}
                fields = re.findall(r'\[([^\]]+)\]', raw_text)
                fields += re.findall(r'\{\{([^}]+)\}\}', raw_text)
                
                for field in fields:
                    field_clean = field.strip()
                    # Skip if it's a URL or looks like XML
                    if field_clean.startswith('http') or '<' in field_clean:
                        continue
                    if len(field_clean) > 50:  # Skip very long matches
                        continue
                    field_name = field_clean.lower().replace(' ', '_')
                    field_name = re.sub(r'[^a-z0-9_]', '', field_name)
                    if field_name and field_name not in seen_fields:
                        seen_fields.add(field_name)
                        all_fields.append({
                            'name': field_name,
                            'label': field_clean,
                            'type': 'date' if 'date' in field_name or 'date' in field_clean.lower() else 'text',
                            'preview': field_clean
                        })
        
        # Join all text
        plain_text = "\n\n".join(text_parts)
        
        # Return fields separately for selection
        html_content = f'<div class="docx-content" style="font-family: \'Times New Roman\', Times, serif; font-size: 12pt; white-space: pre-wrap; line-height: 1.6; padding: 20px;">{plain_text}</div>'
        
        return {
            'success': True,
            'html': html_content,
            'text': plain_text,
            'fields': all_fields,
            'paragraphs': len(doc.paragraphs),
            'tables': len(doc.tables)
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }