from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'humanocr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ver/(?P<tipo>[a-z]+)/(?P<pagina>[0-9]+)', 'humanocr.views.ver', name='ver'),
    url(r'^image/(?P<tipo>[a-z]+)/(?P<orden>[0-9]+)/(?P<columna>[0-9]+)/(?P<pagina>[0-9]+)', 'humanocr.views.getImage', name='getImage'),
    url(r'^text/(?P<tipo>[a-z]+)/(?P<orden>[0-9]+)/(?P<columna>[0-9]+)/(?P<pagina>[0-9]+)', 'humanocr.views.getText', name='getText'),
    url(r'^set$', 'humanocr.views.setText', name='setText'),
    
)