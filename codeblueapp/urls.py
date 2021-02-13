from django.conf.urls import url
from codeblueapp import views

urlpatterns = [
    url(r'^$',views.use,name='use'),
]
