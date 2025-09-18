from django.contrib import admin
from django.urls import path, include
from movie import views as movieViews
from django.conf.urls.static import static
from django.conf import settings
from movie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movieViews.home, name='home'),
    path('about/', movieViews.about, name='about'),
    path('news/', include('news.urls')),
    path('statistics/', movieViews.statistics_view, name='statistics'),
    path('signup/', movieViews.signup, name='signup'),
    path("recommend/", views.recommend_view, name="recommend"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

