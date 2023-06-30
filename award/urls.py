from rest_framework import routers

from award.view import AwardViewSet

router = routers.DefaultRouter()

router.register('award', AwardViewSet, basename="award")
