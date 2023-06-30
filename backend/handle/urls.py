from rest_framework import routers
from django.urls import path

from . import views

router = routers.DefaultRouter()
router.register('train',views.TrainsViewSet)
router.register('test',views.TestsViewSet)

urlpatterns = router.urls

urlpatterns += [
    # path('test/',
    #     views.TestsViewSet.as_view({
    #         "get": "list",
    #         "post": "create"
    #     })),
    path('result/',views.HandleResult.as_view())
]