def wsgi_application(environ, start_response): 
     status = '200 OK' 
     headers = [('Content-type', 'text/plain')] 
     body = environ['QUERY_STRING'].split('&') 
     start_response(status, headers) 
     resp = '' 
     for elem in body: 
         resp += (elem + '\n') 
     return resp 


