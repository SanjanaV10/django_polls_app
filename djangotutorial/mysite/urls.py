from django.contrib import admin
from django.urls import include, path   # include added

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),   # add this line
]