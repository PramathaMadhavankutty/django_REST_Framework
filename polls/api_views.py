from rest_framework import generics
from .models import Poll, Vote, Thread, PollSubject
from serializers import PollSerializer, VoteSerializer

class PollViewSet(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class= PollSerializer

class PollInstanceView(generics.RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer