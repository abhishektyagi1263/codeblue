from django.shortcuts import render
#from codeblueapp.models import users
from codeblueapp.forms import NewUser
# Create your views here.

def index(request):
    return render(request,'codeblueapp/index.html')

def use(request):
    form = NewUser()

    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form invalid')
    return render(request,'codeblueapp/users.html',{'form':form})
