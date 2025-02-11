from flask import Flask, render_template

def create_app():
    app =  Flask(__name__)
    # Configuracion del proyecto
    app.config.from_mapping(
        DEBUG = True, 
        SECRETE_KEY = 'dev'
    )
    # Registrar Blueprint
    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    return app