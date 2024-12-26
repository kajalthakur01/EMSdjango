from django.contrib import admin
from django.urls import path
from EMSapp import views

urlpatterns =[
    path('home/<int:num>' , views.home),
    path('' , views.index),
    path('get/',views.getData,name='getData'),
    path('d/',views.Department),
    path('about/',views.about),
    path('addData/',views.addData ,name='addData'),
    path('updatedata/<int:id>', views.updateData ,name='updatedata'),
    path('fetch/',views.fetch,name='fetch'),
    path('add/',views.addStudent,name='addStudent'),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>/',views.deletestu,name='delete'),
    path('contact/', views.contactview , name='contact'),
    path('register/',views.register),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout')

]