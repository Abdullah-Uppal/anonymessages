from django.urls import path
from .views import *

urlpatterns = [
  path('', home, name='home'),
  path('new/', newview, name='new'),
  path('send_message/<uuid:id>/', CreateMessageView.as_view(), name='send_message'),
  path('create_link/', URLCreateView.as_view(), name='create_link'),
  path('links/', URLListView.as_view(), name='links'),
  path('messages/<uuid:id>/', AnonymousMessageListView.as_view(), name='messages'),
  path('message/<int:id>/delete/', delete_message, name='delete_message'),
  path('links/<uuid:id>/delete/', delete_link, name='delete_link'),
  path('send_message/success/', message_sent, name="message_sent"),
]