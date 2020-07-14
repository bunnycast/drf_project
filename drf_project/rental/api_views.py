from rest_framework import viewsets, permissions

from rental.models import Friend, Belonging, Borrowed
from rental.permissions import IsOwner
from rental.serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer


class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsOwner]


class BelongingViewSet(viewsets.ModelViewSet):
    queryset = Belonging.objects.all()
    serializer_class = BelongingSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class BorrowedViewSet(viewsets.ModelViewSet):
    queryset = Borrowed.objects.all()
    serializer_class = BorrowedSerializer
    permission_classes = [permissions.DjangoModelPermissions]
