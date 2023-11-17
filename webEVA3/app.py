from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'ejercicio1' in request.form:
            return redirect(url_for('ejercicio1'))
        elif 'ejercicio2' in request.form:
            return redirect(url_for('ejercicio2'))
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    # Renderiza la plantilla para el Ejercicio 1
    return render_template('formulario_ejercicio1.html')

@app.route('/ejercicio2')
def ejercicio2():
    # Renderiza la plantilla para el Ejercicio 2
    return render_template('formulario_ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
