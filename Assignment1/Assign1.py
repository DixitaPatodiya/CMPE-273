#!flask/bin/python
from flask import request, Flask
import os
import json
import rocksdb, uuid
import subprocess

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'app/v1/scripts/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#@app.route('/api/v1/scripts', methods=['POST'])
@app.route('/app/v1/scripts/<scriptid>', methods=['GET'])
def get_script(id):
    db = rocksdb.DB("assign1.db", rocksdb.Options(create_if_missing=True))
    script = db.get(str.encode(id))
    response = subprocess.check_output(['python3.6', str(os.path.join(UPLOAD_FOLDER, script))])
    return response, 200

@app.route('/app/v1/scripts/', methods=['POST'])
def script_post():
    db = rocksdb.DB("assign1.db", rocksdb.Options(create_if_missing=True))
    scriptId = request.files.get("data")
    scriptId.save(os.path.join(UPLOAD_FOLDER, scriptId.filename))
    sc = str(uuid.uuid4())
    db.put(sc.encode(), (str(scriptId.script)).encode());
    resp = json.dumps({'script-id':sc})
    return resp, 201

if __name__ == '__main__':
    app.run(debug=True, port=8000)






