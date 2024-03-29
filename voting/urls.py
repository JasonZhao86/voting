"""voting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from voting.views import index
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^polls/', include(('polls.urls', 'polls'), namespace='polls')),
    url(r'^books/', include(('books.urls', 'books'), namespace='books')),
    url(r'^blog/', include(('blog.urls', 'blog'), namespace='blog')),
    url(r'^app/', include(('blog.urls', 'blog'), namespace='blog')),
    url(r'^media/(?P<path>.*/$)', serve, {"document_root": settings.MEDIA_ROOT}),
    url(r'^api/books/', include(('books.api_urls', 'books'), namespace='api_books')),
]
