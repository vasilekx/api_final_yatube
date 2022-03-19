# api/viewsets.py

from rest_framework import mixins
from rest_framework import viewsets

from .permissions import IsOwnerOrReadOnly, ReadOnly


class IsAuthOrReadOnly(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin ,
                        viewsets.GenericViewSet):
    pass
