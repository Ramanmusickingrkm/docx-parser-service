import io
import re
from docx import Document

def parse_docx_to_html(file_buffer):
    """Convert DOCX buffer to HTML with placeholders"""
    try:
        doc = Document(io.BytesIO(file_buffer))
        html_parts = []
        all_fields = []
        seen_fields = set()
        
        # Process paragraphs
        for para in doc.paragraphs:
            if para.text.strip():
                style = para.style.name if para.style else ''
                
                if 'Heading 1' in style:
                    html_parts.append(f'<h1>{para.text}</h1>')
                elif 'Heading 2' in style:
                    html_parts.append(f'<h2>{para.text}</h2>')
                elif 'Heading 3' in style:
                    html_parts.append(f'<h3>{para.text}</h3>')
                else:
                    html_parts.append(f'<p>{para.text}</p>')
                    
                    # Find placeholders
                    fields = re.findall(r'\[([^\]]+)\]', para.text)
                    fields += re.findall(r'\{\{([^}]+)\}\}', para.text)
                    
                    for field in fields:
                        field_clean = field.strip()
                        field_name = field_clean.lower().replace(' ', '_')
                        if field_name not in seen_fields:
                            seen_fields.add(field_name)
                            all_fields.append({
                                'name': field_name,
                                'label': field_clean,
                                'type': 'text'
                            })
        
        # Process tables
        for table in doc.tables:
            html_parts.append('<table border="1" style="border-collapse:collapse; width:100%;">')
            for i, row in enumerate(table.rows):
                tag = 'th' if i == 0 else 'td'
                html_parts.append('<td>')
                for cell in row.cells:
                    html_parts.append(f'<{tag} style="border:1px solid #ccc; padding:8px;">{cell.text}</{tag}>')
                html_parts.append('</tr>')
            html_parts.append('<tr>')
        
        html = ''.join(html_parts)
        
        # Replace placeholders with input fields
        for field in all_fields:
            input_html = f'<input type="text" class="doc-field" data-field="{field["name"]}" placeholder="{field["label"]}">'
            html = html.replace(f'[{field["label"]}]', input_html)
            html = html.replace(f'{{{{{field["label"]}}}}}', input_html)
        
        return {
            'success': True,
            'html': html,
            'fields': all_fields,
            'paragraphs': len(doc.paragraphs),
            'tables': len(doc.tables)
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }