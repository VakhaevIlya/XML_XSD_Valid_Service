import xmlschema
from flask import Flask, request

schemaResponse = 'Now go to /validate to check your xml\n'
validateResponse = 'You must load xsd schema to /schema\n'
xsd = ''

app = Flask(__name__)

@app.route('/schema', methods=['POST'])
def schema():
    """
    Get xsd schema and say what to do next.
    """
    global xsd
    xsd = request.get_data(as_text=True)
    return schemaResponse

@app.route('/validate', methods=['POST'])
def validate():
    """
    Get xml and validate it if xsd schema was load.
    Return Valid/Invalid.
    """
    if not xsd:
        return validateResponse
    xml = request.get_data(as_text=True)
    schema = xmlschema.XMLSchema(xsd)
    result = schema.is_valid(xml)
    if (result):
        return('Valid')
    else:
        return('Invalid')

app.run(host='0.0.0.0', port=80)

