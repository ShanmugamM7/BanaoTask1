from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('patient_page/', views.patient_page, name='patient_page'),
    path('doctor_page/', views.doctor_page, name='doctor_page'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)