import io
import json
import base64
import re
from docx import Document

def parse_docx_to_html(file_buffer):
    """Convert DOCX to plain text (no HTML tags)"""
    try:
        doc = Document(io.BytesIO(file_buffer))
        text_parts = []
        all_fields = []
        seen_fields = set()
        
        # Extract paragraphs
        for para in doc.paragraphs:
            if para.text and para.text.strip():
                raw_text = para.text.strip()
                # Clean the text
                raw_text = re.sub(r'<[^>]+>', '', raw_text)
                raw_text = re.sub(r'\s+', ' ', raw_text)
                text_parts.append(raw_text)
                
                # Find placeholders
                fields = re.findall(r'\[([^\]]+)\]', raw_text)
                fields += re.findall(r'\{\{([^}]+)\}\}', raw_text)
                
                for field in fields:
                    field_clean = field.strip()
                    if field_clean.startswith('http') or '<' in field_clean:
                        continue
                    field_name = field_clean.lower().replace(' ', '_')
                    field_name = re.sub(r'[^a-z0-9_]', '', field_name)
                    if field_name and field_name not in seen_fields:
                        seen_fields.add(field_name)
                        all_fields.append({
                            'name': field_name,
                            'label': field_clean,
                            'type': 'text'
                        })
        
        # Extract tables
        for table in doc.tables:
            text_parts.append("")
            for row in table.rows:
                row_text = []
                for cell in row.cells:
                    cell_text = cell.text.strip()
                    cell_text = re.sub(r'<[^>]+>', '', cell_text)
                    if cell_text:
                        row_text.append(cell_text)
                if row_text:
                    text_parts.append(" | ".join(row_text))
            text_parts.append("")
        
        # Join all text
        plain_text = "\n\n".join(text_parts)
        
        # Final cleanup
        plain_text = re.sub(r'\n\s*\n', '\n\n', plain_text)
        plain_text = re.sub(r' +', ' ', plain_text)
        
        # Return plain text wrapped in div with white-space pre-wrap
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