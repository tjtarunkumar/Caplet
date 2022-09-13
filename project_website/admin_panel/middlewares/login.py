from django.http import HttpResponse
from django.shortcuts import redirect

def test_middleware(get_response):

    def middleware(request):

        if not request.session.get('email'):
            print('workibng')
            return redirect('login_page')
        response = get_response(request)

        return response

    return middleware