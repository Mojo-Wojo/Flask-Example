def simple_middleware(app):
    def middleware(environ, start_response):
        # Example middleware logic
        print("Middleware executed!")
        return app(environ, start_response)
    return middleware

def validator(input_string):
    # Check if the string contains any numbers
    return any(char.isdigit() for char in input_string)
