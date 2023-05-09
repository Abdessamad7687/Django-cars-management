
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.shortcuts import render


# def handler404(request, exception):
#     if request.user.is_authenticated:
#         print('True')
#         return render(request, '404.html')
#     else:
#         print('Fail')
#         return render(request, '1404.html')


urlpatterns = [
  path('', include('crud.urls')),
  path('admin/', admin.site.urls),
  path('', TemplateView.as_view(template_name='home.html'), name='home'),
  path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),
  path('password/reset/', auth_views.LoginView.as_view(template_name='login.html'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler404 = handler404
