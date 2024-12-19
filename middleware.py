def simple_middleware(app):
    def middleware(environ, start_response):
        # Example middleware logic
        print("Middleware executed!")
        return app(environ, start_response)
    return middleware
