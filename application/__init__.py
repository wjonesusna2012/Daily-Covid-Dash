"""Initialize app."""
from flask import Flask
import dash
import dash_html_components as html
from application.templates.layout import html_layout

def Add_Dash(server):
    """Create a Dash app."""
    external_stylesheets = ['/static/dist/css/styles.css',
                            'https://fonts.googleapis.com/css?family=Lato',
                            'https://use.fontawesome.com/releases/v5.8.1/css/all.css']
    external_scripts = ['/static/dist/js/includes/jquery.min.js',
                        '/static/dist/js/main.js']
    dash_app = dash.Dash(server=server,
                         external_stylesheets=external_stylesheets,
                         external_scripts=external_scripts,
                         routes_pathname_prefix='/dashapp/')

    # Override the underlying HTML template
    dash_app.index_string = html_layout

    # Create Dash Layout comprised of Data Tables
    # dash_app.layout = html.Div(
    #     children=get_datasets(),
    #     id='dash-container'
    #   )

    return dash_app.server
def create_app():
  """Construct the core application."""
  app = Flask(__name__,
              instance_relative_config=False)
  app.config.from_object('config.Config')

  with app.app_context():
    from . import routes
    app.register_blueprint(routes.main_bp)
    
    app = Add_Dash(app)
    
    return app