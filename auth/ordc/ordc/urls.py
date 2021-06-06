"""ordc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name="landing_page"),
    path('auth/web/', include("apps.authentication.urls.web_urls")),
    path('auth/api/', include("apps.authentication.urls.api_urls")),
    path('referral/web/', include("apps.referral.urls.web_urls")),
    path('ecommerce/api/', include("apps.ecommerce.urls.api_urls")),
]

try:
    auction_urls = [path("api/tenders/", include("apps.tender.urls.api_urls")),
                    path("api/bidding/", include("apps.bidding.urls.api_urls")),
                    path("api/transport/", include("apps.transport.urls.api_urls")),
                    ]
    urlpatterns += auction_urls
except Exception as e:
    print("ERROR>>>>", "Auction Project Not Register: {}".format(e))


try:
    notification_urls = [path("api/notification/", include("apps.notification.urls.api_urls")),
                    ]
    urlpatterns += notification_urls
except Exception as e:
    print("ERROR>>>>", "Notification Project Not Register: {}".format(e))


try:
    customer_urls = [path("api/clients/", include("apps.client.urls.api_urls")),
                    ]
    urlpatterns += customer_urls
except Exception as e:
    print("ERROR>>>>", "Customer Project Not Register: {}".format(e))
try:
    integration_urls = [path("api/service/", include("apps.integration.urls.api_urls")),
                    ]
    urlpatterns += integration_urls
except Exception as e:
    print("ERROR>>>>", "Integration Project Not Register: {}".format(e))

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
