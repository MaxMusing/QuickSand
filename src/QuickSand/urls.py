from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import QuickSandA.views

urlpatterns = [
    url(r'^$', QuickSandA.views.landing_page, name='landing_page'),
	url(r'^admin/', admin.site.urls),
	url(r'^home/', QuickSandA.views.home, name='home'),
	url(r'^login_request/', QuickSandA.views.login_request, name='login_request'),
	url(r'^logout_request/', QuickSandA.views.logout_request, name='logout_request'),
	url(r'^add_meal/', QuickSandA.views.add_meal, name='add_meal'),
	url(r'^add_meal_request/', QuickSandA.views.add_meal_request, name='add_meal_request'),
	url(r'^user_profile_request/', QuickSandA.views.user_profile_request, name='user_profile_request'),
	url(r'^(?P<meal_id>[0-9]+)/$', QuickSandA.views.page_meal, name='page_meal'),
	url(r'^(?P<meal_id>[0-9]+)/([-\w]+)/$', QuickSandA.views.page_meal, name='page_meal'),
	url(r'^(?P<meal_id>[0-9]+)/request/$', QuickSandA.views.page_meal_request, name='page_meal_request'),
	url(r'^(?P<meal_id>[0-9]+)/([-\w]+)/request/$', QuickSandA.views.page_meal_request, name='page_meal_request'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
