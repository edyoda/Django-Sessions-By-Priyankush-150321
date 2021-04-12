from django.shortcuts import render
from .forms import ContactForm
from .models import ContactModel

from django.views import View

class HOMEView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
    
    def post(self, request):
        pass
    
    def delete(self, request):
        pass

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name_var = request.POST['name']
            email_var = request.POST['email']
            message_var = request.POST['message']
            ContactModel.objects.create(name=name_var, email = email_var, message=message_var)
            print('data is saved in DB.')
            pass  # does nothing, just trigger the validation
    if request.method == 'GET':
        # fetch all data of model with ORM pass that varibale to HTMl, user django tempalte language to work further
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_form(request):

    print('\n\n\n')
    print('inside contact from ', request.method)

    return render(request, 'contact_form.html')

