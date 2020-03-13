from django.urls import path
from user.views import PersonView

urlpatterns = [
    path('', PersonView.as_view(), name='persons'),
]
