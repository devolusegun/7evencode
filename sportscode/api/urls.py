from django.urls import path
from .views import (
    BettingCodeListCreate, BettingCodeRetrieveUpdateDestroy,
    MessageListCreate, MessageRetrieveUpdateDestroy,
    LocationListCreate, LocationRetrieveUpdateDestroy
)

urlpatterns = [

    #BettingcodeEndpoints
    path('betting-codes/', BettingCodeListCreate.as_view(), name='betting-code-list-create'),
    path('betting-codes/<int:pk>/', BettingCodeRetrieveUpdateDestroy.as_view(), name='betting-code-retrieve-update-destroy'),

    #MessageEndpoints
    path('messages/', MessageListCreate.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageRetrieveUpdateDestroy.as_view(), name='message-retrieve-update-destroy'),

    #LocationEndpoints
    path('locations/', LocationListCreate.as_view(), name='location-list-create'),
    path('locations/<int:pk>/', LocationRetrieveUpdateDestroy.as_view(), name='location-retrieve-update-destroy'),

]