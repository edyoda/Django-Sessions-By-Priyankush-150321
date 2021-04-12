from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cookie_create(request):
    request.session.set_test_cookie()
    return HttpResponse('<h1> Cookie is created </h1>')

def cookie_delete(request):

    print('request.session.test_cookie_worked() : ',request.session.test_cookie_worked())

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        return HttpResponse('<h1> Cookie is deleted successfully. </h1>')
    else:
        return HttpResponse('<h1> Browser not accept cookie </h1>')


def create_session(request):
    request.session['name']='Sarvan'
    request.session['email']='sarvan@gmail.com'
    request.session['phone']='9090909090'
    request.session['address']='INDIA'

    return HttpResponse('<h1> Session is created </h1>')

def access_session(request):

    print('\n'*5)

    name = request.session.get('name')
    email = request.session.get('email')
    phone = request.session.get('phone')
    address = request.session.get('address')
    # address = request.session.get('age', 25)


    print('name  : ',name)
    print('email  : ',email)
    print('phone  : ',phone)
    print('address  : ',address)

    del request.session['name']

    print('requst.session : ', request.session.keys())
    return render(request, 'session_file.html')