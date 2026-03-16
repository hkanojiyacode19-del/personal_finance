from django.urls import path
from finance_app.views import home, taskDisplay, taskUpdate, taskDelete, registration, login_view

urlpatterns = [
    path('home', home, name='home'),
    path('task', taskDisplay, name='task'),
    path('taskupdate/<int:id>', taskUpdate, name = 'taskup'),
    path('del/<int:id>', taskDelete, name = 'delete'),
    
    path('', registration, name = 'reg'),
    path('login', login_view, name ='login'),
]