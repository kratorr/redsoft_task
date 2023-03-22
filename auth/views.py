from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny


from api.serializers import SignUpSerializer


class SignUpView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = SignUpSerializer
