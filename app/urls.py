"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
<<<<<<< HEAD
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Car Auction API',
        description='...',
        default_version='v1',
    ),
    public=True
)
=======
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view




schema_view = get_schema_view(
    openapi.Info(
        title="Car Auction API",
        description="...",
        default_version="v1",
        
    ),
    public=True
)



>>>>>>> c4d5f43f4811c8b547f105067cd86ac4dac50055

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('docs/', schema_view.with_ui('swagger')),
    path('', include('auction.urls')),
]
