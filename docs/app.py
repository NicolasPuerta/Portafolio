from flask import Flask, render_template, url_for, request,redirect
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='static')

app.config['MAIL_SERVER'] = 'smtp.gmail.com' 
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USE_TLS'] = True 
app.config['MAIL_USERNAME'] = 'nicolas.puerta487@pascualbravo.edu.co' 
app.config['MAIL_PASSWORD'] = os.getenv('PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'nicolas.puerta487@pascualbravo.edu.co'

mail = Mail(app)

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/contacto', methods=['POST'])
def contacto():
    mensaje = Message('Contacto de portafolio', recipients=['nicolas.puerta487@pascualbravo.edu.co'])
    mensaje.body = f"hola soy {request.form['nombre']} mi correo es {request.form['email']}\n te quiero comunicar que {request.form['mensaje']}"
    mail.send(mensaje)
    return redirect(url_for('Home'))

if __name__ == '__main__':
    app.run(debug=True)