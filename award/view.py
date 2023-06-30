from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from award.models import Award
from award.serializer import AwardSerializer


class AwardViewSet(ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if(request.user):
            awards = Award.objects.filter(user=request.user)
            serializer = self.get_serializer(awards, many=True)
            return Response(serializer.data)

        return Response(status=status.HTTP_404_NOT_FOUND)
