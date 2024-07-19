import os
import json
import pdfkit
from flask import Flask, request, send_file, render_template_string
from pybars import Compiler
from gevent.pywsgi import WSGIServer


app = Flask(__name__)

# Define the Handlebars template
template_source = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Report</title>
    <style>
        body { font-family: Arial, sans-serif; }
        h1 { text-align: center; }
        table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
        th, td { border: 1px solid black; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .section { margin-bottom: 40px; }
        .section h2 { border-bottom: 2px solid #000; padding-bottom: 5px; }
    </style>
</head>
<body>
    <h1>{{#each data.summary}}   
        {{#if 'data.summary.this==data.summary.Basic Company Information'}}  
        {{{[Company Name]}}}{{/if}}{{/each}}  Report</h1>
    
    <div class="section">
        <h2>Basic Information</h2>
        {{#each data.summary}}    
        {{#if 'data.summary.this==data.summary.Basic Company Information'}}
        <p><strong>Website URL:</strong> <a href="{{{[Website URL]}}}">{{{[Website URL]}}}</a></p>
        <p><strong>LinkedIn URL:</strong> <a href="{{{[LinkedIn URL]}}}">{{{[LinkedIn URL]}}}</a></p>
        <p><strong>Logo:</strong> <img src=" {{{[Logo]}}}" alt="Company Logo"></p>
        {{/if}}
        {{/each}}     
    </div>
   
    <div class="section">
        <h2>Company Overview</h2>
        {{#each data.summary}}
        {{#if 'data.summary.this==data.summary.Company Overview'}}
        <p><strong>Description:</strong> {{{[Description]}}}</p>
        <p><strong>Mission Statement:</strong> {{{[Mission Statement]}}} </p>
        <p><strong>Founding Date:</strong>{{{[Founding Date]}}}</p>
        <p><strong>Founders:</strong> {{{[Founders]}}}</p>
        <p><strong>Headquarters:</strong> {{{[Headquarters]}}}</p>
        <p><strong>Industry:</strong> {{{[ Industry ]}}}</p>
        {{/if}}
        {{/each}}
    </div>

    <div class="section">
        <h2>Products and Services</h2>
        <h3>Products</h3>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Description</th>
                    <th>Category</th>
                    <th>Features</th>
                </tr>
            </thead>
            <tbody>
                {{#each data.summary}}
                {{#each this.Products}}
                <tr>
                    <td>{{{[Product Name]}}}</td>
                    <td>{{Description}}</td>
                    <td>{{Category}} </td>
                    <td>{{Features}}</td>
                </tr>
                {{/each}} 
                {{/each}}
            </tbody>
        </table>
        <h3>Services</h3>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Description</th>
                    <th>Category</th>
                    <th>Features</th>
                </tr>
            </thead>
            <tbody>
                {{#each data.summary}}
                {{#each this.Services}}
                <tr>
                    <td>{{{[Service Name]}}}</td>
                    <td>{{Description}}</td>
                    <td>{{Category}} </td>
                    <td>{{Features}}</td>
                </tr>
                {{/each}} 
                {{/each}}
            </tbody>
        </table>
    </div>
    


    <div class="section">
        <h2>Technologies</h2>
         {{#each data.summary.Technologies}}
        {{#each this}}
        <p><strong>{{{[Technology Name]}}} :</strong> {{{[Application]}}}</p>
        <p><strong>Partnerships:</strong>{{{[Partnerships]}}}</p>
        {{/each}}
        {{/each}}                   
    
    </div>
    <div class="section">
        <h2>Leadership and Team</h2>
        {{#each data.summary}}
        {{#if 'data.summary.this==data.summary.Leadership and Team'}}
    
        <p><strong>CEO:</strong> {{CEO}}</p>
        <p><strong>Leadership Team:</strong> {{{[Leadership Team]}}}</p>
        <p><strong>Employee Count:</strong> {{{[Employee Count]}}}</p>
        <p><strong>Company Culture:</strong> {{{[Company Culture]}}}</p>

        {{/if}}
        {{/each}}                   
    
    </div>
    <div class="section">
        <h2>Social Media Presence</h2>
        {{#each data.summary}}
        {{#if 'data.summary.this==data.summary.Social Media Presence'}}
    
        <p><strong>LinkedIn:</strong> <a href="{{LinkedIn}}">{{LinkedIn}}</a></p>
        <p><strong>Twitter:</strong> <a href="{{Twitter}}">{{Twitter}}</a></p>
        <p><strong>Facebook:</strong> <a href="{{Facebook}}">{{Facebook}}</a></p>
        <p><strong>Instagram:</strong> <a href="{{Instagram}}">{{Instagram}}</a></p>

        {{/if}}
        {{/each}}                   
    
    </div>

    <div class="section">
        <h2>News and Updates</h2>
        {{#each data.summary}}
        {{#if 'data.summary.this==data.summary.News and Updates'}}
        {{#each this}}
        <p><strong>Title:</strong> <a href="{{Title}}">{{Title}}</a></p>
        <p><strong>Date:</strong> {{Date}}</p>
        <p><strong>Source:</strong> {{Source}}</p>
        <p><strong>Summary:</strong> {{Summary}}</p>

        {{/each}}
        {{/if}}                   
        {{/each}}
    </div> 

</body>
</html>
'''

# Compile the Handlebars template
compiler = Compiler()
template = compiler.compile(template_source)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Get JSON data from request
    #request.accept_mimetypes.accept_json
    
    data = request.get_json

    with open('company_data.json', 'r') as f:
        data = json.load(f)

    # Create HTML content
    #html_content = create_html(data)


    # Create HTML content
    #html_content = create_html(data)

    # Generate HTML content from template and data
    html_content = template(data)

    # Define the output PDF file
    pdf_file = 'E:\\company_report.pdf'

    #file_name = 'invoice.pdf'
    #wkhtmltopdftemp="C:\\Program Files\\wkhtmltopdf\\bin\\"
    #pdf_path = os.path.join(wkhtmltopdftemp, 'static', 'pdf', file_name)

    # Convert HTML to PDF using pdfkit
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")


    pdfkit.from_string(html_content, pdf_file, configuration=config)

    return send_file(pdf_file)

if __name__ == '__main__':
    # Ensure wkhtmltopdf is in PATH
    #os.environ['PATH'] += os.pathsep + '/usr/local/bin'
    # Debug/Development
    #app.run(debug=True, host="127.0.0.1", port="5000")
    # Production
    #os.environ['PATH'] += os.pathsep + '/usr/local/bin'
    http_server = WSGIServer(('127.0.0.1', 5000), app)
    http_server.serve_forever()
    #headers = {'accept': 'application/json'}
    app.run(debug=True)