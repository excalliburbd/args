from django.conf.urls import include, url
from django.views.generic import ListView
from home.models import Person

urlpatterns = [
    # Examples:
    #url(r'^$', 'views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'', 'home.views.index', name='index'),
    url(r'', ListView.as_view(template_name="home/home.html", model=Person)),
]
