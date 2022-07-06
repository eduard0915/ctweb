from flask import Flask, render_template

app = Flask(__name__)


# Inicio
@app.route('/')
def home():
    title = 'CielTechno SAS'
    return render_template('homepage.html', title=title)


# Contacto
@app.route('/contact')
def contact():
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


if __name__ == '__main__':
    app.run()
