from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs, urlunparse, urlencode
import ssl

host = 'localhost'
port = 3000
redirect_uri = f'https://{host}:{port}/'

code = None

class HandleRequests(BaseHTTPRequestHandler):

    keep_running = True

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        global code

        self._set_headers()

        path = urlparse(self.path)

        if not path.query:
            # If there's no auth code, keep serving the web page.
            request_payload = {
                    "client_id": client_id,
                    "force_verify": 'false',
                    "redirect_uri": redirect_uri,
                    "response_type": 'code',
                    "scope": 'chat:edit chat:read'
                    }
            encoded_payload = urlencode(request_payload)
            url = 'https://id.twitch.tv/oauth2/authorize?' + encoded_payload
            self.wfile.write(f'<html><head><body><a href="{url}">Click here to auth with Twitch</a></body></head>'.encode('utf-8'))
        else:
            # If Twitch has provided a code, store it and stop the web server.
            code = parse_qs(path.query)['code'][0]
            print(f'Code: {code}')
            HandleRequests.keep_running = False

 # Authorisation Code Flow
# Launch HTTP Server, listen for request, direct user to Twitch,
# listen for response.
def auth_code_flow():

    httpd = HTTPServer((host, port), HandleRequests)
    httpd.socket = ssl.wrap_socket (httpd.socket,
        keyfile="key.pem",
        certfile='cert.pem', server_side=True)

    print(f'Please open your browser at {redirect_uri}')

    # Keep listening until we handle a post request
    while HandleRequests.keep_running:
         httpd.handle_request()