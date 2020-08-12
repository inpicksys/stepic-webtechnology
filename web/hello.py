def wsgi_app(environ, start_response):
    """simple wsgi app, returns GET parameters separated by a newline"""
    if environ['REQUEST_METHOD'] != "GET":
     	raise NotImplementedError
    url_query_string = environ['QUERY_STRING']
    newline_separated_query_string = url_query_string.replace("&","\n")
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [str.encode(newline_separated_query_string)]
