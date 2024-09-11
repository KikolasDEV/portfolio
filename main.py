from flask import Flask, render_template, flash
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Configuración de Flask-Mail para enviar correos
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
mail = Mail(app)

class ContactForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Correo Electrónico', validators=[DataRequired(), Email()])
    mensaje = TextAreaField('Mensaje', validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        email = form.email.data
        mensaje = form.mensaje.data
        msg = Message('Nuevo mensaje de tu portafolio',
                      sender=os.getenv('MAIL_USERNAME'),
                      recipients=[os.getenv('MAIL_RECIPIENT')])  # Cambiado para usar el entorno de variable
        msg.body = f"Nombre: {nombre}\nCorreo: {email}\nMensaje: {mensaje}"
        mail.send(msg)
        flash('Mensaje enviado. ¡Gracias por contactarme!', 'success')
    return render_template('contact.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
