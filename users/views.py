from rest_framework.generics import ListAPIView,RetrieveAPIView
from users.serializer import PaySerializer, CustomUserProfileSerializer
from users.models import Pay, CustomUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class PayViewSet(ListAPIView):
    queryset = Pay.objects.all()
    serializer_class = PaySerializer
    #filter_backends = [DjangoFilterBackend]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields  = ['user','paid_course','paid_lesson','payment_method']
    #ordering_fields = ['data_at']


class ProfileViewSet(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserProfileSerializer