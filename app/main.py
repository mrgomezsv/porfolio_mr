# app/main.py
from app import app

@app.route('/')
def index():
    return '¡Hola! Soy MrGomez'

if __name__ == '__main__':
    app.run(debug=True)
