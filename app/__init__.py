from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")  # optional

    # Register blueprints
    from .routes import main, diet, exercise, chatbot, auth
    app.register_blueprint(main.bp)
    app.register_blueprint(diet.bp)
    app.register_blueprint(exercise.bp)
    app.register_blueprint(chatbot.bp)
    app.register_blueprint(auth.bp)


    return app