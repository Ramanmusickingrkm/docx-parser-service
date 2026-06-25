import os  # ✅ Add this at top
import base64
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from docx_parser import parse_docx_to_html

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": [
    "https://docsssign.vercel.app"
]}}, supports_credentials=True)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'https://docsssign.vercel.app'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'status': 'ok',
        'message': 'DOCX Parser Service is running'
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/parse-docx', methods=['POST', 'OPTIONS'])  # ✅ Add OPTIONS for CORS
def parse_docx():
    # Handle preflight request
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        file_buffer = None
        
        print(f"📥 Request method: {request.method}")
        print(f"📥 Content-Type: {request.content_type}")
        print(f"📥 Files: {request.files}")
        print(f"📥 Is JSON: {request.is_json}")
        
        # Case 1: multipart/form-data (for frontend FormData)
        if 'file' in request.files:
            file = request.files['file']
            file_buffer = file.read()
            print(f"📁 Received file via multipart/form-data: {file.filename}")
        
        # Case 2: JSON with base64 (for Node.js backend)
        elif request.is_json:
            data = request.get_json()
            if data and 'file' in data:
                file_buffer = base64.b64decode(data['file'])
                print("📁 Received file via JSON base64")
        
        if not file_buffer:
            return jsonify({'success': False, 'error': 'No file provided'}), 400
        
        result = parse_docx_to_html(file_buffer)
        print(f"✅ Parse result success: {result['success']}")
        print(f"✅ Fields found: {len(result.get('fields', []))}")
        
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
    # ✅ Railway uses PORT environment variable, default is 8080
    port = int(os.environ.get('PORT', 8080))
    print(f"🚀 Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
























DocSign
🔔
❓
⚙️
rr

✉️
Send an Envelope
Manage
🏠
Dashboard
📥
Action Required
⏳
Waiting for Others
✅
Completed
⏰
Expiring Soon
📝
Drafts
📁
All Documents
Create
📋
Templates
🚀
Send New
Manage
👥
Contacts
📊
Reports
⚙️
Settings
rr
r r
Administrator
◀
All Documents
✉️ New Envelope
Name	Type	Recipient(s)	Status	Sent	Actions
test9991212
Document
Template	Raman Kumar	✓ Completed	Jun 1, 2026	View Download
jdkqskjgsa
Document
Template	Raman Kumar	✓ Completed	Jun 1, 2026	View Download
nddd
Document
Template	Raman Kumar	✓ Completed	Jun 1, 2026	View Download
ss
Document
Template	Raman Kumar	✓ Completed	Jun 1, 2026	View Download
ndddyutdy
Document
Template	Raman Kumar	📤 Sent	May 28, 2026	View
testtttt
Document
Template	Raman Kumar	📤 Sent	May 28, 2026	View
aa
Document
Template	Raman Kumar	✓ Completed	May 28, 2026	View Download
test999
Document
Template	Raman Kumar	✓ Completed	May 28, 2026	View Download
fwq
Document
Template	Raman Kumar	✓ Completed	May 28, 2026	View Download
hiiiiiii
Document
Template	Raman Kumar	📤 Sent	May 28, 2026	View
ndaaaa
Document
Template	Raman Kumar	✓ Completed	May 28, 2026	View Download
sd
Document
Template	Raman Kumar	📤 Sent	May 28, 2026	View
test999
Document
Template	Raman Kumar	📤 Sent	May 28, 2026	View
mmsdf
Document
Template	Raman Kumar	📤 Sent	May 28, 2026	View
bnnbm
Document
Template	Raman Kumar	📤 Sent	May 28, 2026	View
fdfed
Document
Template	Raman Kumar	📤 Sent	May 28, 2026	View
tes
Document
Template	Raman Kumar	📤 Sent	May 27, 2026	View
eewewr
Document
Template	Raman Kumar	📤 Sent	May 27, 2026	View
nnbbvn
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
mbn
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
nbmbb
Document
Template	Raman Kumar	📤 Sent	May 27, 2026	View
mnmnmnll
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
bnnbmlkkllj
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
nnn
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
m
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
mm
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
n nm
Document
Template	Raman Kumar	📤 Sent	May 27, 2026	View
mmwem
Document
Template	Raman Kumar	📤 Sent	May 27, 2026	View
qwes
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
mmcvaca
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
142dwea
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
m,3wq
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
htjuy
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
wedf
Document
Template	Raman Kumar	📤 Sent	May 27, 2026	View
qwq
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
qqqqqqqq
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
nm,wenm
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
we
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
waaa
Document
Template	Raman Kumar	✓ Completed	May 27, 2026	View Download
we
Document
Template	Raman Kumar	📤 Sent	May 27, 2026	View
dfs
Document
Template	Raman Kumar	📤 Sent	May 27, 2026	View
nn
Document
Template	Raman Kumar	✓ Completed	May 26, 2026	View Download
hgj
Document
Template	Raman Kumar	✓ Completed	May 26, 2026	View Download
hkfc
Document
Template	Raman Kumar	📤 Sent	May 26, 2026	View
hiiiiiii
Document
Template	Raman Kumar	📤 Sent	May 26, 2026	View
test1
test1.html
text/html	Raman Kumar	✓ Completed	May 22, 2026	View Download
n cgre
n cgre.html
text/html	Raman Kumar	✓ Completed	May 22, 2026	View Download
mm
mm.html
text/html	Raman Kumar	✓ Completed	May 22, 2026	View Download
ljlj
ljlj.html
text/html	Raman Kumar	✓ Completed	May 22, 2026	View Download
mnnnnnnnnnnnnnnnn
mnnnnnnnnnnnnnnnn.html
text/html	Raman Kumar	✓ Completed	May 22, 2026	View Download
rt
rt.html
text/html	Raman Kumar	✓ Completed	May 22, 2026	View Download
add
add.html
text/html	Raman Kumar	✓ Completed	May 22, 2026	View Download
asdrrr
asdrrr.html
text/html	Raman Kumar	✓ Completed	May 22, 2026	View Download
cgg
cgg.html
text/html	Raman Kumar	✓ Completed	May 22, 2026	View Download
vnb
vnb.html
text/html	Raman Kumar	✓ Completed	May 22, 2026	View Download
asd
asd.html
text/html	Raman Kumar	📤 Sent	May 22, 2026	View
dsf
dsf.html
text/html	Raman Kumar	📤 Sent	May 22, 2026	View
fdfd
fdfd.html
text/html	Raman Kumar	📤 Sent	May 21, 2026	View
wefe
wefe.html
text/html	Raman Kumarwefe	📤 Sent	May 21, 2026	View
wsa
wsa.html
text/html	Raman Kumar	📤 Sent	May 21, 2026	View
Test Subject 2
Test Subject 2.html
text/html	Sagar Keim	✓ Completed	May 21, 2026	View Download
Test Subject 1
Test Subject 1.html
text/html	Sagar Keim	📤 Sent	May 21, 2026	View
Test Subject
Test Subject.html
text/html	Sagar Keim	✓ Completed	May 21, 2026	View Download
v
v.html
text/html	Raman Kumar	✓ Completed	May 21, 2026	View Download
nnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnn.html
text/html	Raman Kumar	📤 Sent	May 21, 2026	View
wq
wq.html
text/html	Raman Kumar	✓ Completed	May 21, 2026	View Download
kb
kb.html
text/html	Raman Kumar	✓ Completed	May 21, 2026	View Download
bv
bv.html
text/html	Raman Kumar	✓ Completed	May 21, 2026	View Download
sdgdsg
sdgdsg.html
text/html	Raman Kumar	✓ Completed	May 21, 2026	View Download
enmklwe
enmklwe.html
text/html	Raman Kumar	✓ Completed	May 21, 2026	View Download
uyury
uyury.html
text/html	Raman Kumar	✓ Completed	May 21, 2026	View Download
dfew
dfew.html
text/html	Raman Kumar	📤 Sent	May 21, 2026	View
sdfjkdsfkj
sdfjkdsfkj.html
text/html	Raman Kumar	📤 Sent	May 21, 2026	View
testerrrr
testerrrr.html
text/html	Raman Kumar	📤 Sent	May 21, 2026	View
nda test
nda test.html
text/html	Raman Kumar	✓ Completed	May 20, 2026	View Download
gaurav
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	gaurav	✓ Completed	May 20, 2026	View Download
test2443
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	✓ Completed	May 20, 2026	View Download
nmvbnvb
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	✓ Completed	May 20, 2026	View Download
smnsn
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	✓ Completed	May 20, 2026	View Download
grmmm
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	✓ Completed	May 20, 2026	View Download
qweewer
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	✓ Completed	May 20, 2026	View Download
qwrew
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	✓ Completed	May 20, 2026	View Download
bvmnvc
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	✓ Completed	May 20, 2026	View Download
vnbv
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 20, 2026	View
jknss
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 20, 2026	View
mnnm
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	✓ Completed	May 20, 2026	View Download
mmmmmmmmmmmmmmmmmmmmmm
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 20, 2026	View
qqre
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 20, 2026	View
sdfsd
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 20, 2026	View
aksldnsaj
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 20, 2026	View
tsttt
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 20, 2026	View
vvbvbbvb
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 19, 2026	View
lmkl
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 19, 2026	View
asdada
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 19, 2026	View
asd
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 19, 2026	View
mmnm
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 19, 2026	View
mmmm
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 19, 2026	View
tio
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 19, 2026	View
sss
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 19, 2026	View
tstt
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 19, 2026	View
ds
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 18, 2026	View
sddsf
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	📤 Sent	May 18, 2026	View
final_test
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	✓ Completed	May 18, 2026	View Download
hllooo
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	✓ Completed	May 18, 2026	View Download
dsfs
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	✓ Completed	May 18, 2026	View Download
asdsda
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	✓ Completed	May 18, 2026	View Download
dsgfsdfg
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	✓ Completed	May 18, 2026	View Download
asdsad
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	✓ Completed	May 18, 2026	View Download
kljasdljkls
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	✓ Completed	May 18, 2026	View Download
testtt
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	✓ Completed	May 18, 2026	View Download
nda twsp
Non Disclosure Agreement.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document	Raman Kumar	✓ Completed	May 18, 2026	View Download
Guarav Temp
2021.1.14-ILPA-Model-NDA.pdf
application/pdf	Gaurav	✓ Completed	May 18, 2026	View Download
test999
2021.1.14-ILPA-Model-NDA.pdf
application/pdf	Raman Kumar	✓ Completed	May 18, 2026	View Download
jjhjh
2021.1.14-ILPA-Model-NDA.pdf
application/pdf	Raman Kumar	✓ Completed	May 18, 2026	View Download
jhjh
2021.1.14-ILPA-Model-NDA.pdf
application/pdf	Raman Kumar	✓ Completed	May 18, 2026	View Download
bnnbm
2021.1.14-ILPA-Model-NDA.pdf
application/pdf	Raman Kumar	✓ Completed	May 18, 2026	View Download
hiiiiiii
2021.1.14-ILPA-Model-NDA.pdf
application/pdf	Raman Kumar	✓ Completed	May 18, 2026	View Download
test1
Pocket_Tanks_Java_Project_-_Fortify_Security_Report.pdf
application/pdf	Raman Kumar	✓ Completed	May 18, 2026	View Download
h
Pocket_Tanks_Java_Project_-_Fortify_Security_Report.pdf
application/pdf	Raman Kumar	✓ Completed	May 18, 2026	View Download
sdf
Pocket_Tanks_Java_Project_-_Fortify_Security_Report.pdf
application/pdf	Raman Kumar	✓ Completed	May 18, 2026	View Download
hklds
Pocket_Tanks_Java_Project_-_Fortify_Security_Report.pdf
application/pdf	Raman Kumar	✓ Completed	May 18, 2026	View Download
hii
Pocket_Tanks_Java_Project_-_Fortify_Security_Report.pdf
application/pdf	Raman Kumar	✓ Completed	May 18, 2026	View Download
fdsd
Pocket_Tanks_Java_Project_-_Fortify_Security_Report.pdf
application/pdf	Raman Kumar	✓ Completed	May 18, 2026	View Download
sc
Pocket_Tanks_Java_Project_-_Fortify_Security_Report.pdf
application/pdf	Raman Kumar	✓ Completed	May 14, 2026	View Download
ugsdfyydsyus
Pocket_Tanks_Java_Project_-_Fortify_Security_Report.pdf
application/pdf	Raman Kumar	✓ Completed	May 14, 2026	View Download
gddhdh
Pocket_Tanks_Java_Project_-_Fortify_Security_Report.pdf
application/pdf	Raman Kumar	📤 Sent	May 14, 2026	View
tsssssssssssss
1778745335445-556632899.pdf
application/pdf	Raman Kumar	📤 Sent	May 14, 2026	View
test99
nps_ios_report.pdf
application/pdf	Raman Kumar	✓ Completed	May 14, 2026	View Download
test999
nps_ios_report.pdf
application/pdf	Raman Kumar	📤 Sent	May 14, 2026	View
teste5
Pocket_Tanks_Java_Project_-_Fortify_Security_Report.pdf
application/pdf	Raman Kumar	✓ Completed	May 14, 2026	View Download
test222
document.pdf
application/pdf	Raman Kumar	✓ Completed	May 14, 2026	View Download
test1
document.pdf
application/pdf	Raman Kumar	📤 Sent	May 14, 2026	View
test
document.pdf
application/pdf	Raman Kumar	📤 Sent	May 14, 2026	View
Download failed: <!DOCTYPE html> <html> <head> <meta charset="UTF-8"> <title>test9991212 - Signed Document</title> <style> body { font-family: 'Times New Roman', Times, serif; margin: 0; padding: 40px; background: #f5f5f5; } .container { max-width: 900px; margin: 0 auto; background: white; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); overflow: hidden; } .header { background: #1e2d4a; color: white; padding: 20px; text-align: center; } .header h1 { margin: 0 0 10px; font-size: 24px; } .content { padding: 30px; } .message-box { background: #e8f0fd; padding: 15px; border-radius: 8px; margin-bottom: 25px; border-left: 4px solid #2e6fea; } .template-content { margin-bottom: 30px; padding-bottom: 20px; border-bottom: 1px solid #e2e8f0; } .fields-table { width: 100%; border-collapse: collapse; margin: 20px 0; border: 1px solid #e2e8f0; } .fields-table td { border: 1px solid #e2e8f0; vertical-align: top; } .signature-box { margin-top: 30px; padding: 20px; background: #f8fafc; border-radius: 8px; border-left: 4px solid #10b981; } .signature-value { font-family: 'Dancing Script', cursive; font-size: 28px; color: #1e2d4a; margin: 10px 0; } .footer { background: #f1f5f9; padding: 15px; text-align: center; font-size: 11px; color: #64748b; border-top: 1px solid #e2e8f0; } .print-btn { position: fixed; bottom: 20px; right: 20px; background: #2e6fea; color: white; border: none; padding: 10px 20px; border-radius: 8px; cursor: pointer; } @media print { .print-btn { display: none; } body { background: white; padding: 0; } .container { box-shadow: none; } } </style> </head> <body> <div class="container"> <div class="header"> <h1>test9991212</h1> <p>Document ID: 6a1d3437f26c20f3bce84b04 | COMPLETED</p> <p>From: r r</p> </div> <div class="content"> <div class="message-box"> <strong>📝 Message from Sender:</strong><br> Please review and sign. </div> <div class="template-content"> <h1><strong>NON-DISCLOSURE AGREEMENT<br> &amp; <br>AUTHORIZATION &amp; VERIFICATION AGREEMENT</strong></h1><p>(Between CERT-In Empanelled Auditor &amp; Auditee)</p><p>THIS NON-DISCLOSURE AGREEMENT is made on _________</p><p>By and between</p><p><strong><span class="receiver-field" contenteditable="true" data-field="organisation_name">a2dgc</span> </strong>incorporated /registered under the Companies Act, <span class="receiver-field" contenteditable="true" data-field="act">_______________________* </strong>(hereinafter referred to as Auditee which expression shall unless repugnant to the context or meaning thereof, includes its successors, administrators and permitted assigns) of the first part.</p><p><strong>And</strong></p><p><strong>HiTrust Infotech Solution Private Limited </strong>incorporated/registered under the <strong>Companies Act, 2013</strong> having its corporate office at <strong>Kh. No 187, Ist Floor, Near Mahaveer Bhawan, Rithala, Pocket-11, Sector 5, Rohini, New Delhi, Delhi 110085 </strong>(herein referred to as Auditor which expression shall unless repugnant to the context or meaning thereof, includes its successors, assigns, administrators, liquidators and receivers) of the second part </p><p><strong>WHEREAS</strong></p><ol><li>Auditor is a services organization Empanelled by the Indian Computer Emergency Response Team (hereinafter CERT-IN) under Department of Electronics &amp; IT, for auditing, including vulnerability assessment and penetration testing of computer systems, networks, computer resources &amp; applications of various agencies or departments of the Government, critical infrastructure organizations and those in other sectors of Indian economy.</li><li>Auditor as an Empanelled Information Security Auditing organization has agreed to fully comply the Guidelines for CERT-In Empaneled Information Security Auditing</li></ol><p>Organizations, Terms &amp; conditions of empanelment and Policy guidelines for handling audit related data while conducting audits.</p><ol><li>Auditee is also aware of the aforesaid Guidelines along with guidelines for Auditee Organizations published by CERT-In.</li><li>Both Auditor and Auditee have given their irrevocable consent to fully comply the aforesaid Guidelines and any amendments thereof without any reservations.</li></ol><p><strong>NOW, THEREFORE</strong>, in consideration of the foregoing and the covenants and agreements contained herein, the parties agree as follows:</p><h1>Definitions.:</h1><ul><li><ul><li><ol><li>The term Confidential Information shall include, without limitation, all information and materials, furnished by either Party to the other in connection with Auditee products and services including information transmitted in writing, orally, visually, (e.g. video terminal display) or on magnetic media, and including all proprietary information, customer &amp; prospect lists, trade secrets, trade names or proposed trade names, methods and procedures of operation, business or marketing plans, licensed document know-how, ideas, concepts, designs, drawings, flow charts, diagrams, quality manuals, checklists, guidelines, processes, formulae, source code materials, specifications, programs, software packages, codes and other intellectual property relating to Auditee products and services. Results of any information security audits, tests, analysis, extracts or usages carried out by the Auditor in connection with the Auditees products and/or services, IT infrastructure, etc. shall also be considered Confidential Information.</li><li>The term Auditee products shall include all such products, goods, services, deliverables, which are subject to audit by the empaneled auditor under the Agreement.</li></ol></li></ul></li></ul><p><strong>2 Protection of Confidential Information. </strong>With respect to any Confidential Information disclosed to it or to which it has access, Auditor affirms that it shall:</p><ol><li>Use the Confidential Information as necessary only in connection with scope of audit and in accordance with the terms and conditions contained herein;</li><li>Maintain the Confidential Information in strict confidence and take all reasonable steps to enforce the confidentiality obligations imposed hereunder, but in no event take less care with the Confidential Information that the parties take to protect the confidentiality of its own proprietary and confidential information and that of its other clients;</li><li>Not to make or retain copy of any details of products and/or services, prototypes, business or marketing plans, Client lists, Proposals developed by or originating from Auditee or any of the prospective clients of Auditee.</li><li>Not to make or retain copy of any details of results of any information security audits, tests, analysis, extracts or usages carried out by the Auditor in connection with the Auditees products and/or services, IT infrastructure, etc. without the express written consent of Auditee.</li><li>Not disclose or in any way assist or permit the disclosure of any Confidential Information to any other person or entity without the express written consent of the auditee; and</li><li>Return to the auditee, or destroy, at auditees discretion, any and all Confidential Information disclosed in a printed form or other permanent record, or in any other tangible form (including without limitation, all copies, notes, extracts, analyses, studies, summaries, records and reproductions thereof) immediately on (i) expiration or termination of this agreement, or (ii) the request of Auditee therefor.</li><li>Not to send Auditees audit information or data and/or any such Confidential Information at any time outside India for the purpose of storage, processing, analysis or handling without the express written consent of the Auditee.</li><li>The auditor shall use only the best possible secure methodology to avoid confidentiality breach, while handling audit related data for the purpose of storage, processing, transit or analysis including sharing of information with auditee.</li><li>Not to engage or appoint any non-resident/foreigner to undertake any activity related to Information Security Audit. In case of information security audits for Government/ critical sector organization, only the man power declared to CERT-In shall be deployed to carry out such audit related activities.</li><li>Not to discuss with any member of public, media, press, any or any other person about the nature of arrangement entered between the Auditor and the Auditee or the nature of services to be provided by Auditor to the Auditee.</li><li>Make sure that all the employees and/or consultants engaged to undertake any audit on its behalf have signed the mandatory non-disclosure agreement.</li><li><strong>Onus. </strong>Auditor shall have the burden of proving that any disclosure or use inconsistent with the terms and conditions hereof falls within any of the foregoing exceptions.</li></ol><h1>Permitted disclosure of audit related information:</h1><p>The auditor may share audit information with CERT-In or similar Government entities mandated under the law as and when called upon to do so by such agencies with prior written information to the auditee.</p><ol><li><strong>Exceptions. </strong>The Confidentiality obligations as enumerated in Article 2of this Agreement shall not apply in following cases:<ol><li>Which is independently developed by Auditor or lawfully received from another source free of restriction and without breach of this Agreement; or</li><li>After it has become generally available to the public without breach of this Agreement by Auditor; or</li><li>Which at the time of disclosure to Auditor was known to such party free of restriction and evidenced by documents in the possession of such party; or</li><li>Which Auditee agrees in writing is free of such restrictions.</li><li>Which is received from a third party not subject to the obligation of confidentiality with respect to such Information;</li></ol></li><li><strong>Remedies. </strong>Auditor acknowledges that any actual or threatened disclosure or use of the Confidential Information by Auditor would be a breach of this agreement and may cause immediate and irreparable harm to Auditee or to its clients; Auditor affirms that damages from such disclosure or use by it may be impossible to measure accurately; and injury sustained by Auditee / its clients may be impossible to calculate and compensate fully. Therefore, Auditor acknowledges that in the event of such a breach, Auditee shall be entitled to specific performance by Auditor of its obligations contained in this Agreement. In addition, Auditor shall compensate the Auditee for the loss or damages caused to the auditee actual and liquidated damages which may be demanded by Auditee. Liquidated damages not to exceed the Contract value. Moreover, Auditee shall be entitled to recover all costs of litigation including reasonable attorneys fees which it or they may incur in connection with defending its interests and enforcement of contractual rights arising due to a breach of this agreement by Auditor. All rights and remedies hereunder are cumulative and in addition to any other rights or remedies under any applicable law, at equity, or under this Agreement, subject only to any limitations stated herein.</li><li><strong>Need to Know</strong>. Auditor shall restrict disclosure of such Confidential Information to its employees and/or consultants with a need to know (and advise such employees and/or consultants of the obligations assumed herein), shall use the Confidential Information only for the purposes set forth in the Agreement, and shall not disclose such Confidential Information to any affiliates, subsidiaries, associates and/or third party without prior written approval of the Auditee. No information relating to auditee shall be hosted or taken outside the country in any circumstances.</li><li><strong>Intellectual Property Rights Protection. </strong>No license to a party, under any trademark, patent, copyright, design right, mask work protection right, or any other intellectual property right is either granted or implied by the conveying of Confidential Information to such party.</li><li><strong>No Conflict</strong>. The parties represent and warrant that the performance of its obligations hereunder do not and shall not conflict with any other agreement or obligation of the respective parties to which they are a party or by which the respective parties are bound.</li><li><strong>Authority. </strong>The parties represent and warrant that they have all necessary authority and power to enter into this Agreement and perform their obligations hereunder.</li><li><strong>Governing Law. </strong>This Agreement shall be interpreted in accordance with and governed by the substantive and procedural laws of India and the parties hereby consent to the jurisdiction of Courts and/or Forums situated at &lt; Name of the city&gt;</li><li><strong>Entire Agreement. </strong>This Agreement constitutes the entire understanding and agreement between the parties, and supersedes all previous or contemporaneous agreement or communications, both oral and written, representations and under standings among the parties with respect to the subject matter hereof.</li><li><strong>Amendments. </strong>No amendment, modification and/or discharge of this Agreement shall be valid or binding on the parties unless made in writing and signed on behalf of each of the parties by their respective duly authorized officers or representatives.</li><li><strong>Binding Agreement. </strong>This Agreement shall be binding upon and inure to the benefit of the parties hereto and their respective successors and permitted assigns.</li><li><strong>Severability</strong>. It is the intent of the parties that in case any one or more of the provisions contained in this Agreement shall be held to be invalid or unenforceable in any respect, such provision shall be modified to the extent necessary to render it, as modified, valid and enforceable under applicable laws, and such invalidity or unenforceability shall not affect the other provisions of this Agreement.</li><li><strong>Waiver. </strong>Waiver by either party of a breach of any provision of this Agreement, shall not be deemed to be waiver of any preceding or succeeding breach of the same or any other provision hereof.</li><li><strong>Survival. </strong>Both parties agree that all of their obligations undertaken herein with respect to Confidential Information received pursuant to this Agreement shall survive till perpetuity even after expiration or termination of this Agreement.</li><li><strong>Non-solicitation. </strong>During the term of this Agreement and thereafter for a further period of two (2) years Auditor shall not solicit or attempt to solicit Auditees employees and/or consultants, for the purpose of hiring/contract or to proceed to conduct business similar to Auditee with any employee and/or consultant of the Auditee who has knowledge of the Confidential Information, without the prior written consent of Auditee.</li><li>This Agreement is governed by and shall be construed in accordance with the laws of India. In the event of dispute arises between the parties in connection with the validity, interpretation, implementation or alleged breach of any provision of this Agreement, the parties shall attempt to resolve the dispute in good faith by senior level negotiations. In case, any such difference or dispute is not amicably resolved within forty-five (45) days of such referral for negotiations, it shall be resolved through arbitration process, wherein both the parties will appoint one arbitrator each and the third one will be appointed by the two arbitrators in accordance with the Arbitration and Conciliation Act, 1996. The venue of arbitration in India shall be (please choose the venue of dispute resolution as the city) or where the services are provided. The proceedings of arbitration shall be conducted in English language and the arbitration award shall be substantiated in writing and binding on the parties. The arbitration proceedings shall be completed within a period of one hundred and eighty (180) days from the date of reference of the dispute to arbitration.</li><li><strong>Term. </strong>This Agreement shall come into force on the date of its signing by both the parties and shall be valid up to 365 Days.</li></ol><p>IN WITNESS HEREOF, and intending to be legally bound, the parties have executed this Agreement to make it effective from the date and year first written above.</p><p><strong>AUTHORIZATION &amp; VERIFICATION AGREEMENT</strong></p><p><strong>1. PURPOSE</strong></p><p>The Client hereby authorizes HiTrust Infotech Solution Private Limited to conduct the security, audit, testing, compliance, or consulting activities as mutually agreed between the Parties for the purpose of evaluating, improving, and maintaining the Clients cybersecurity and information security posture.</p><p>Such activities may include but are not limited to:</p><ul><li>Application Vulnerability Assessment and Penetration Testing (VAPT) </li></ul><p>(collectively, the <strong>Authorized Activities</strong>).</p><p><strong>2. AUTHORIZATION</strong></p><p>The Client hereby grants HiTrust and its authorized employees, contractors, or representatives the right to:<br>a. Access, analyze, and test the Clients systems, applications, networks, and related infrastructure as identified and approved in writing by the Client;<br>b. Use ethical hacking, penetration testing, or similar security evaluation techniques solely for the purpose of identifying vulnerabilities and improving security;<br>c. Collect, review, and analyze information necessary to provide findings, reports, and recommendations; and<br>d. Perform such activities within the timeframe and boundaries mutually agreed upon in writing.</p><p>This authorization confirms that HiTrust is legally permitted by the Client to perform the above-mentioned activities in accordance with applicable laws and professional standards.</p><p><strong>3. CLIENT ACKNOWLEDGEMENT</strong></p><p>The Client acknowledges and agrees that:</p><ul><li>All activities will be performed <strong>only within the agreed and authorized scope</strong> (listed in Annexure A).</li><li>The Client has obtained all necessary internal and third-party approvals (e.g., from hosting providers, ISPs, or cloud services) for such testing.</li><li>HiTrust shall not be held liable for any unintentional or incidental service interruptions that may occur during controlled testing within the approved scope.</li><li>The Client will ensure coordination and communication with relevant IT and security teams before commencement of testing.</li></ul><p><strong>4. CONFIDENTIALITY</strong></p><p>All information shared, discovered, or generated during the course of the engagement shall be treated as <strong>Confidential Information</strong> under the separate <strong>Non-Disclosure Agreement (NDA)</strong> executed between the Parties.<br>HiTrust shall maintain confidentiality and use such information solely for the purpose of the authorized engagement.</p><p><strong>5. LIMITATION OF LIABILITY</strong></p><p>HiTrust shall take all reasonable measures to minimize risk and avoid system disruption. However, HiTrust shall not be responsible for:<br>a. Any incidental or indirect losses (e.g., downtime, loss of business, data corruption) arising from authorized testing;<br>b. Any pre-existing vulnerabilities or system weaknesses found during assessment;<br>c. Any security incident caused by unauthorized third-party interference during testing. HiTrusts total liability under this Agreement shall not exceed the amount paid for the engagement.</p><p><strong>6. COMPLIANCE AND ETHICAL CONDUCT</strong></p><p>HiTrust shall perform all activities:</p><ul><li>In accordance with applicable laws and regulations (including the Information Technology Act, 2000 and related rules in India);</li><li>Following global ethical hacking and cybersecurity testing standards (OWASP, NIST, ISO 27001 guidelines, CERT-IN guidelines);</li><li>With professional integrity and due care.</li></ul><p><strong>7. TERM AND VALIDITY</strong></p><p>This Agreement shall be effective from the date of signing and remain valid until completion of the authorized engagement or until revoked in writing by either Party.<br>All confidentiality, limitation of liability, and data protection obligations shall survive termination.</p><p><strong>8. GOVERNING LAW AND JURISDICTION</strong></p><p>This Agreement shall be governed by and construed in accordance with the laws of <strong>India</strong>.<br>The courts of <strong>New Delhi, India</strong>, shall have exclusive jurisdiction over all disputes arising out of or relating to this Agreement.</p><p><strong>9. ENTIRE AGREEMENT</strong></p><p>This Agreement, along with any annexures and the NDA, constitutes the entire understanding between the Parties and supersedes all prior communications regarding the subject matter.</p><p><strong>For Hitrust Infotech Solution Private Limited</strong></p><p><strong><br>Authorised Signatory: Trupti<br>Designation: LA &amp; LI</strong></p><p><strong>HiTrust Infotech Solution Private Limited<br></strong></p><p><strong><span class="receiver-field" contenteditable="true" data-field="for_organisation_name">_____________________________________</strong></p><p><strong><span class="receiver-field" contenteditable="true" data-field="organisation_name">a2dgc</span></strong></p><h1><strong><span class="receiver-field" contenteditable="true" data-field="organisation_name">a2dgc</span></strong> </h1><p><strong>Provide the mandatory details*</strong></p><p><strong>Annexure-A</strong></p><p><strong>Scope Defined by Organization Name</strong></p><p><strong>For Organization Name, </strong></p><p><strong>Designation </strong></p><p><strong>Duly authorized vide board resolution</strong></p><p><strong>by Board of Directors of </strong></p><p><strong>Organisation Name</strong></p><h1><strong>Organisation Name*</strong> </h1><p><strong>Provide the mandatory details*</strong></p> </div> <h3>📋 Document Details</h3> <table class="fields-table"> <tr> <td style="padding: 8px; background: #f8fafc; width: 180px;"><strong>Organisation_name:</strong></td> <td style="padding: 8px;">a2dgc</td> </tr> </table> <div class="signature-box"> <h3>🔒 Electronic Signature Certificate</h3> <div class="signature-value">✍️ Handwritten Signature (Image)</div> <div><strong>Signed by:</strong> Raman Kumar</div> <div><strong>Email:</strong> ramanmahawar839@gmail.com</div> <div><strong>IP Address:</strong> 38.254.167.145</div> <div><strong>Date & Time:</strong> 1/6/2026, 9:10:26 am</div> <div><strong>Verification ID:</strong> 6a1d3437f26c20f3bce84b04</div> </div> </div> <div class="footer"> This document was signed electronically via DocSign and is legally binding. </div> </div> <button class="print-btn" onclick="window.print()">🖨️ Save as PDF / Print</button> <script>setTimeout(function() { window.print(); }, 500);</script> </body> </html>
