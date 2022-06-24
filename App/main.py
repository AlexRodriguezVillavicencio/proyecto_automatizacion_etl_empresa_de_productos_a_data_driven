# Importamos todo lo necesario
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from ETL.extract import carga_archivo

# instancia del objeto Flask
app = Flask(__name__)
# Carpeta de subida
app.config['UPLOAD_FOLDER'] = "../Datasets"


@app.route("/")
def upload_file():
 # renderisamos la plantilla "formulario.html"
 return render_template('formulario.html')

@app.route("/upload", methods=['POST'])
def uploader():
  if request.method == 'POST':
    # obtenemos el archivo del input "archivo"
    f = request.files['archivo']
    filename = secure_filename(f.filename)
    # Guardamos el archivo en el directorio "Archivos PDF"
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    sep =request.form['sep']
    encoding =request.form['encoding']

    carga_archivo(filename, sep, encoding)

    # Retornamos una respuesta satisfactoria
    return 'respuesta exitosa'


if __name__ == '__main__':
  # Iniciamos la aplicación
  app.run(debug=True)
