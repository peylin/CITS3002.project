import http.server
import cgitb

cgitb.enable()  # This line enables CGI error reporting, and I have no idea what that means

server = http.server.HTTPServer # creating a server object
handler = http.server.CGIHTTPRequestHandler # create the CGI handler
server_address = ("", 8000) # connect via "localhost:8000" or "IpOfHostComputer:8000"
handler.cgi_directories = ["/cgi-bin"] # directory of cgi-bin

# Then start server

httpd = server(server_address, handler)
httpd.serve_forever()