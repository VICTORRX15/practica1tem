from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inscripcion_curso', methods=['GET', 'POST'])
def inscripcion_curso():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        curso = request.form.get('curso')
        flash('Formulario de inscripción enviado con éxito!')
        return redirect(url_for('index'))
    return render_template('inscripcion_curso.html')

@app.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        correo = request.form.get('correo')
        contrasena = request.form.get('contrasena')
        flash('Usuario registrado con éxito!')
        return redirect(url_for('index'))
    return render_template('registro_usuario.html')

@app.route('/registro_productos', methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'POST':
        producto = request.form.get('producto')
        categoria = request.form.get('categoria')
        existencia = request.form.get('existencia')
        precio = request.form.get('precio')
        flash('Producto registrado con éxito!')
        return redirect(url_for('index'))
    return render_template('registro_productos.html')

@app.route('/registro_libros', methods=['GET', 'POST'])
def registro_libros():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        resumen = request.form.get('resumen')
        medio = request.form.get('medio')
        flash('Libro registrado con éxito!')
        return redirect(url_for('index'))
    return render_template('registro_libros.html')

if __name__ == '__main__':
    app.run(debug=True)