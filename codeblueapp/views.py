from django.shortcuts import render
from codeblueapp.models import users
# Create your views here.

def index(request):
    return render(request,'codeblueapp/index.html')

def use(request):
    use_list = users.objects.order_by('first_name')
    use_dict = {'usem':use_list}
    return render(request,'codeblueapp/users.html',context=use_dict,)
