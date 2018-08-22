from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        determines get request, defines the endpoint, generates a response
        :return:
        """
        # import pdb; pdb.set_trace() #debug
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query) # DEBUG later

        # set a status code

        # set any headers

        # set body to generate

        # end headers

        if parsed_path.path =="/":
            self.send_response(200)
            self.send_header('Content-Type','text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>Hello World</h1></body></html>')
            return

        elif parsed_path.path == '/banana':
            pass

        self.send_response(404)
        self.send_header('Content-Type', 'text/plain')



    def do_POST(self):
        """
        determines post request, defines the endpoint
        :return:
        """
        pass


def create_server():
    """
    Generate an instance of a server, .env in .gitignore
    """
    return HTTPServer(
        ('127.0.0.1', int(os.environ['PORT'])),
        SimpleHTTPRequestHandler
    )


def run_forever():
    """
    define in this file, executable code, this runs application
    :return:
    """
    server = create_server()

    try:
        server.serve_forever() # on switch to run the application
        print(f'Server running on {os.environ["PORT"]}')
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    run_forever()

