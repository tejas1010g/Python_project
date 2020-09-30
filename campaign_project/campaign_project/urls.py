
from django.conf.urls import include, url
from django.contrib import admin

from c_app import views

admin.autodiscover()

urlpatterns = [
url(r'^admin/', include(admin.site.urls)),

url(r'^users/', views.UserList.as_view()),

url(r'^index/(?P<partner_id>.*)/$', views.UserDetail.as_view()),]

