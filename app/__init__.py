from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'votre_cle_secrete'  # Nécessaire pour les formulaires Flask-WTF

    from app.routes import main
    app.register_blueprint(main)

    return app