from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    title = 'CielTechno SAS'
    return render_template('homepage.html', title=title)


@app.route('/contact')
def contact():
    title = 'Contáctenos'
    return render_template('contact.html', title=title)


@app.route('/about')
def about():
    title = 'Quienes Somos'
    return render_template('about.html', title=title)


@app.route('/calentador_liquidos')
def warm():
    title = 'Calentadores de Líquidos'
    return render_template('warm_fluid.html', title=title)


@app.route('/telemetria')
def telemetry():
    title = 'Sistema de Telemetría - CielTechno SAS'
    return render_template('telemetry.html', title=title)


@app.route('/tubos_colorimetricos')
def tubes():
    title = 'Tubos Colorimetricos - CielTechno SAS'
    return render_template('tubes_colorimetric.html', title=title)


@app.route('/bpmpro')
def bpmpro():
    title = 'BPMPRO Sistema de Calidad'
    return render_template('bpmpro.html', title=title)


if __name__ == '__main__':
    app.run()
