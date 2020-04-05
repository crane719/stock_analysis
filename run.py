from app import create_app

application = create_app()
jinja_options = application.jinja_options.copy()
jinja_options.update({
    "variable_start_string": "<<",
    "variable_end_string": ">>",
    })
application.jinja_options = jinja_options

application.run(debug=True)
