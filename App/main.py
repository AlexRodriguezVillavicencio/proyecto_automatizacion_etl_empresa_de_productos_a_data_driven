import os
from flask import Flask, render_template, jsonify, request

from pathlib import Path
from ETL.extract import carga_archivo

# instancia del objeto Flask
app = Flask(__name__)

#app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'database')
CURRENT_DIRECTORY = os.getcwd() + "/database/"


@app.route("/")
def upload_file():
 return render_template('formulario.html')

@app.route("/upload", methods=['POST'])
def uploader():
  try:
    f = request.files.getlist("mi_base_de_datos")
    for file in f:
      directory_file = file.filename.split("/")
      print(file)
      print(file.filename)
      file_d = directory_file.pop()
      if os.path.exists(CURRENT_DIRECTORY) == False:
        os.mkdir(path=CURRENT_DIRECTORY)
        file.save(CURRENT_DIRECTORY + file_d)
      else:
        file.save(CURRENT_DIRECTORY + file_d)
    return jsonify({"message":"ok"})
  except FileNotFoundError:
    return jsonify({"message":"FileNotFoundError"})

for ruta in list(Path('database').iterdir()):
    ruta = os.path.join(os.getcwd(), ruta)
    print(ruta)
    carga_archivo(ruta)

if __name__ == '__main__':
  app.run(debug=True)
