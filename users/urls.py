from django.urls import path,include
from .views import (
    UserRegister,
    #UserLogin,
    Login,
    #UserLogout,
    #ProfileView,
    AddUserPackage,
    UserPackageViewSet,
    ProfileUpdateView,
    #UserPackagesList,
    AllUserPackageViewSet,
    #UserPackageDetail,
    UserPackageDestroy,
    BlacklistTokenUpdateView
)
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router=routers.DefaultRouter()
router.register(r'alldeals',AllUserPackageViewSet,basename='alldeals')
router.register(r'myjourneys',UserPackageViewSet,basename='profile')
urlpatterns=[
    path('',include(router.urls)),
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/blacklist/',BlacklistTokenUpdateView.as_view(),name='blacklist'),
    path('register',UserRegister.as_view(),name='register'),
    path('login/<str:type>',Login.as_view(),name='login'),
	#path('logout/', UserLogout.as_view(), name='logout'),
    path('profile',ProfileUpdateView.as_view(),name='usersprofile'),
    path('packages/add_plan/<int:package>',AddUserPackage.as_view(),name='add_plan'),
    path('packages/remove_plan/<int:deal_id>',UserPackageDestroy.as_view(),name='delete_plan')
    #path('user/plan/<int:package>',UserPackageDetail.as_view(),'update_delete_plan')
    #path('user/myjourneys/', UserPackagesList.as_view(), name='user-packages-list-create'),
]
