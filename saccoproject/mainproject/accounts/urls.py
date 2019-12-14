from django.conf.urls import url
from django.urls import include

from . import views
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView, PasswordResetDoneView,PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    url(r'^logout/$', LogoutView.as_view(template_name='accounts/logout.html'), name="login"),
    url(r'^register/$', views.register, name='register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate,
        name='activate'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change_password/$', views.change_password, name='change_password'),

    # passwordreset
    # url('accounts/', include('django.contrib.auth.urls')),

    url(r'^password_reset/$', PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset'),
    url(r'^password_reset/done/$', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/done/$', PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    url(r'^delete/(?P<username>[\W| \W.-]+)/$', views.delete_user, name= 'delete-user'),
]