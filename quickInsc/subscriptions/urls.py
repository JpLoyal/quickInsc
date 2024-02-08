from django.urls import path
from quickInsc.subscriptions.views import SubscriptionPerson, SubscriptionEvent, subscription_person_sucess, subscription_event_sucess


urlpatterns = [
    path('person/', SubscriptionPerson.as_view(), name='pessoa'),
    path('person/sucess/<int:pk>', subscription_person_sucess, name='person_sucess'),
    path('event/', SubscriptionEvent.as_view()),
    path('event/sucess/<int:pk>', subscription_event_sucess, name='event_sucess'),
]