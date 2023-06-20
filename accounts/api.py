from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import status

class SignUpAPI(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def create(self, request):
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            return Response(
                {'user': user_serializer.data},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {'message': 'Invalid data'},
                status=status.HTTP_400_BAD_REQUEST
            )
