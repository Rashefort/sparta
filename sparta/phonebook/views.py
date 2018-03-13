from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
from .models import Memo




#-------------------------------------------------------------------------------
def phonebook(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('authorization'))
    else:
        return HttpResponseRedirect(reverse('index'))



#-------------------------------------------------------------------------------
def errors(data):
    data = list(dict(data).values())
    return [i for j in data for i in j]



#-------------------------------------------------------------------------------
def authorization(request):
    data = {'auth': AuthenticationForm(), 'user': UserCreationForm()}
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
                data['errors'] = errors(auth.errors)
                data['aDisplay'] = 'block'
                data['uDisplay'] = 'none'

        else:
            user = UserCreationForm(request.POST)
            if user.is_valid():
                user.save()
                username = user.cleaned_data.get('username')
                password = user.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)

                return redirect('index')

            else:
                data['errors'] = errors(user.errors)

    return render(request, 'login.html', data)



#-------------------------------------------------------------------------------
def index(request):
    user =  User.objects.get(username=request.user)
    memos = Memo.objects.filter(user=user).order_by('-id')

    return render(request, 'index.html', {'memos': memos})



#-------------------------------------------------------------------------------
def get_ip(request):
    xff = request.META.get('HTTP_X_FORWARDED_FOR')

    return xff.split(',')[0] if xff else request.META.get('REMOTE_ADDR')



#-------------------------------------------------------------------------------
def ajax(request):
    if len(request.POST) == 4:
        memo = Memo()
        memo.user = request.user
        memo.phone = request.POST.get('phone')
        memo.note = request.POST.get('note')
        memo.date = request.POST.get('date')
        memo.ip = get_ip(request)
        memo.save()

    else:
        memo = Memo.objects.get(id=request.POST.get('id'))
        memo.delete()

    return JsonResponse({'id': memo.pk})
