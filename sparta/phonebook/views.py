from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse





#-------------------------------------------------------------------------------
def phonebook(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('authorization'))

    # else:
    #     return HttpResponseRedirect(reverse('index'))



#-------------------------------------------------------------------------------
def errors(data):
    data = list(dict(data).values())
    return [i for j in data for i in j]



#-------------------------------------------------------------------------------
def authorization(request):
    data = {'auth': AuthenticationForm(), 'user': UserCreationForm()}
    data.update({'name': 'Spartan phonebook'})
    data.update({'uDisplay': 'block'})
    data.update({'aDisplay': 'none'})
    data.update({'errors': ''})

    if request.method == 'POST':
        if len(request.POST) == 4:
            auth = AuthenticationForm(request, data=request.POST)
            if auth.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                login(request, user)

                return redirect('index')

            else:
                print(auth.errors)
                data['errors'] = errors(auth.errors)
                data['aDisplay'] = 'block'
                data['uDisplay'] = 'none'

        else:
            user = UserCreationForm(request.POST)
            if user.is_valid():
                return redirect('index')

            else:
                print(user.errors)
                data['errors'] = errors(user.errors)
                data['aDisplay'] = 'none'
                data['uDisplay'] = 'block'

    return render(request, 'login.html', data)



#-------------------------------------------------------------------------------
def index(request):
    return render(request, 'index.html')
