from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_list),
    path('add/',views.add_student),
    path('edit/<int:id>/', views.edit_student),
    path('delete/<int:id>/', views.delete_student),
    path('signup/', views.signup),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    

]

