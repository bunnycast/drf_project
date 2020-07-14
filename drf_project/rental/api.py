from rest_framework import routers
from rental import api_views as rental_views

router = routers.DefaultRouter()
router.register(r'friends', rental_views.FriendViewSet)
router.register(r'Belongings', rental_views.BelongingViewSet)
router.register(r'Borrowings', rental_views.BorrowedViewSet)
