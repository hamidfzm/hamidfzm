# import python
from htmlmin.main import minify

# import flask
from flask import Flask

# import project
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.template_folder = '../templates'
    app.static_folder = '../static'

    # Registering blue prints
    from main import mod
    app.register_blueprint(mod)

    def response_minify(response):
            """
            minify response html to decrease traffic
            """
            if response.content_type == u'text/html; charset=utf-8':
                response.set_data(
                    minify(response.get_data(as_text=True),
                           remove_comments=True,
                           remove_empty_space=True,
                           remove_all_empty_space=True)
                )

                return response
            return response

    if app.config['MINIFY_PAGE']:
        app.after_request(response_minify)

    # attach routes and custom error pages here
    return app