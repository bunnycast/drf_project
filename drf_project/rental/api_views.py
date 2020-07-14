from rest_framework import viewsets

from rental.models import Friend, Belonging, Borrowed
from rental.serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer


class FriendviewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class BelongingViewSet(viewsets.ModelViewSet):
    queryset = Belonging.objects.all()
    serializer_class = BelongingSerializer


class BorrowedViewSet(viewsets.ModelViewSet):
    queryset = Borrowed.objects.all()
    serializer_class = BorrowedSerializer