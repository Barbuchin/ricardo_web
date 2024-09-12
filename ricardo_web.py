from flask import Flask, render_template

# Crear una instancia de Flask
app = Flask(__name__)

# Definir las rutas
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bio')
def bio():
    return render_template('bio.html')

@app.route('/media')
def media():
    return render_template('media.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/store')
def store():
    return render_template('store.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Ejecutar la aplicación en modo de desarrollo
if __name__ == '__main__':
    app.run(debug=True)
