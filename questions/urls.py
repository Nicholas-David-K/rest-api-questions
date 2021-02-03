"""questions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.forms import CustomUserCreationForm

from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import PasswordResetConfirmView


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/register/', RegistrationView.as_view(form_class=CustomUserCreationForm, success_url='/'), name='django_registration_register'),

    # registration via brower urls
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # login via browsable api
    path('api-auth/', include('rest_framework.urls')),

    # login via rest
    path('api/rest-auth/', include('rest_auth.urls')),

    # path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
 

    # registration via rest
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),


    # api
    path('api/', include('users.api.urls')),
    path('api/', include('Userqueries.api.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
