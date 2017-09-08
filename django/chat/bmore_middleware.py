class BmoreMiddleware(object):
    def __init__(self, app):
        print("In BmoreMiddleware init...")
        self.app = app


    def __call__(self, environ, start_response):
        print("In BmoreMiddleware call...")
        return self.app(environ, start_response)


