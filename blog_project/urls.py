from django.contrib import admin
from django.urls import path , include
import blog.views
import pot.views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home , name= "home"),
    path('new/',blog.views.new , name ="new"),
    path('blog/',include('blog.url')),
    path('pot/', pot.views.pot ,name ="pot"),
    path('accounts/',include('accounts.urls')),
    path('getpage/', blog.views.getpage, name = "getpage"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
