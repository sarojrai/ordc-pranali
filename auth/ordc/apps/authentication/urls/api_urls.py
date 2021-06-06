# -*- coding: utf-8 -*-
__author__ = "Anil Kumar  Gupta"
__copyright__ = "Copyright (©) 2017. ORDC. All rights reserved."
__credits__ = ["ORDC"]

# Django related dependencies
from django.conf.urls import url

# Project Related dependencies
from  apps.authentication.views import api_views as views


web_urls = [
    # User won't be allowed to register by themselves.
    # url(r'^user-registration$', views.user_registration, name="user-registration"),
    url(r'^login$', views.login_user, name="login"),
    url(r'^logout$', views.logout_user, name="logout"),
    url(r'^get-user-detail/$', views.user_detail, name="get-user-detail"),
    url(r'^update-user-status/$', views.update_user_status, name="update-user-status"),
    url(r'^update-profile/$', views.update_profile, name="update-profile"),
    url(r'^reset-password$', views.change_password, name="change-password"),
    url(r'^api-token-auth/', views.CustomAuthToken.as_view()),
    url(r'^invite-user/', views.invite_user, name="invite-user"),
    url(r'^complete-invitation/', views.complete_invitation, name="complete-invitation")



]
location_urls = [
    url(r'^organisations/', views.OrganisationView.as_view({"get": "get_organisation"}, name="get_organisation")),
    url(r'^get-organisation-groups', views.get_organisation_groups, name="get-organisation-groups"),
    url(r'^client-onboarding', views.client_onboarding, name="client-onboarding"),
    url(r'^sc/', views.get_service_centre),
    url(r'^cities/', views.get_cities),
]
# Main URL
# urlpatterns = web_urls + app_urls
urlpatterns = web_urls+location_urls
