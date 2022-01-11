from flaskblog import app

# Funcion para poder correr desde terminal,y se actualize automaticamente
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

