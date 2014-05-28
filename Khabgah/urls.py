from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'SampleProject.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^signup/$', 'myapp.views.signup',name='signup'),
                       url(r'^login/$', 'myapp.views.login',name='login'),
                       url(r'^home/$','myapp.views.home',name='home'),


                       url(r'^admin/userh/editadminh/([^/]+)/$', 'myapp.views.editadminh',name='editadminh'),








################################################################################################



                       url(r'^test/$', 'myapp.views.test'),





                       )
