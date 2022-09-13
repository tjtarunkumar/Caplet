from django.http import HttpResponse
from django.shortcuts import redirect

# class SimpleMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.

#     def __call__(self, request,id):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.

#         response = self.get_response(request,id)

#         # Code to be executed for each request/response after
#         # the view is called.

#         return response

#     def process_view(request, view_func, view_args, view_kwargs):
#         print(view_args)


def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request,id):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not request.session.get('mobile_number'):
           return redirect('/login')


        response = get_response(request,id)

        # Code to be executed for each request/response after
        # the view is called.

        return response
        
    return middleware