from decouple import config
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from flask_recaptcha import ReCaptcha


app = Flask(__name__)
recaptcha = ReCaptcha(app=app)

app.config.update(dict(
    RECAPTCHA_ENABLED=True,
    RECAPTCHA_SITE_KEY=config('RECAPTCHA_SITE_KEY'),
    RECAPTCHA_SECRET_KEY=config('RECAPTCHA_SECRET_KEY'),
))

recaptcha = ReCaptcha()
recaptcha.init_app(app)

app.config['SECRET_KEY'] = config('SECRET_KEY')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = config('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = config('MAIL_PASSWORD')


@app.errorhandler(404)
@app.route('/404')
def page_not_found(e):
    title = 'Página No Encontrada'
    return render_template('404.html', title=title), 404


# Inicio
@app.route('/')
def home():
    title = 'CielTechno SAS'
    return render_template('homepage.html', title=title)


# Contacto
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        if recaptcha.verify():
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            message = request.form.get('message')
            subject = 'Solicitud de Cotizacion'
            product = request.form.get('product')

            mail = Mail(app)
            msg = Message(subject=subject,
                          body=f'Nombre cliente: {name}\nE-mail: {email}\nTelefóno: {phone}\n\n\n{message},\n{product}',
                          sender=config('MAIL_USERNAME'),
                          recipients=['ciel.techno@gmail.com']
                          )
            mail.send(msg)
            flash(
                'Mensaje se ha enviado satisfactoriamente, uno de nuestros representantes se comunicará con usted',
                'info')
            render_template('contact.html', success=True)
        else:
            flash('Error: Confirmar ReCaptcha!!', 'danger')
            return redirect(url_for('contact'))
    title = 'Contáctenos'
    return render_template('contact.html', title=title)


# Acerca de nosotros
@app.route('/about')
def about():
    title = 'Acerca de Nosotros'
    return render_template('about.html', title=title)


# Calentadores de líquidos
@app.route('/calentador_liquidos')
def warm():
    title = 'Calentadores de Líquidos'
    return render_template('warm_fluid.html', title=title)


# Servicio de Telemetria
@app.route('/telemetria')
def telemetry():
    title = 'Sistema de Telemetría - CielTechno SAS'
    return render_template('telemetry.html', title=title)


# Software BPMPRO
@app.route('/bpmpro')
def bpmpro():
    title = 'BPMPRO Sistema de Calidad'
    return render_template('bpmpro.html', title=title)


# Terminos y Condiciones
@app.route('/terms_conditions')
def bpmpro():
    title = 'Terminos y Condiciones'
    return render_template('terms_and_conditions.html', title=title)


# Terminos y Condiciones
@app.route('/privacy_policy')
def bpmpro():
    title = 'Política de Privacidad'
    return render_template('privacy_policy.html', title=title)


if __name__ == '__main__':
    app.run()
