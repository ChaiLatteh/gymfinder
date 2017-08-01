from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^user_register$', views.user_register),
    url(r'^user_login$', views.user_login),

    url(r'^business_register$', views.business_register),
    url(r'^business_login$', views.business_login),

    url(r'^landing$',views.landing),

    url(r'^users/(?P<user_id>\d+)$', views.show_user),
    url(r'^uploadpicture$', views.upload_picture),
    url(r'^update$', views.upload_picture_process),
    url(r'^removepicture$', views.remove_picture_process),

    url(r'^businesses/(?P<business_id>\d+)$', views.show_business),

    url(r'^meetups$', views.meetups),
    url(r'^meetups/new$', views.new_meetup),
    url(r'^meetups/new/process$', views.new_meetup_process),
    url(r'^meetups/(?P<meetup_id>\d+)$', views.show_meetup),
    url(r'^meetups/search$', views.search_meetup),

    url(r'^deals$', views.deals),
    url(r'^createdeal$', views.createdeal),
    url(r'^getting$', views.getting),
    url(r'^pickbusiness$',views.pickbusiness),
    url(r'^form$',views.form),

    url(r'^messageboard/$', views.messageboard),
    url(r'^messageboard/new$', views.new_message),
    url(r'^messageboard/new/process$', views.new_message_process),
    url(r'^messageboard/(?P<message_id>\d+)$', views.show_message),
    url(r'^messageboard/(?P<message_id>\d+)/like_process$', views.like_message_process),
    url(r'^messageboard/(?P<message_id>\d+)/unlike_process$', views.unlike_message_process),
    url(r'^messageboard/(?P<message_id>\d+)/comment/process$', views.new_comment_process),
    url(r'^messageboard/(?P<message_id>\d+)/bookmark_process$', views.bookmark_message_process),
    url(r'^messageboard/(?P<message_id>\d+)/unbookmark_process$', views.unbookmark_message_process),

    url(r'^logout$', views.logout),

    #no longer in use
    # url(r'^messageboard/$', views.messageboard),
    # url(r'^messageboard/message/add_message$', views.new_message_process),
    # url(r'^messageboard/message/(?P<message_id>\d+)/like$', views.like_message),
    # url(r'^messageboard/message/(?P<message_id>\d+)/unlike$', views.unlike_message),
    # url(r'^messageboard/message/(?P<message_id>\d+)/add_comment$', views.new_comment_process),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
