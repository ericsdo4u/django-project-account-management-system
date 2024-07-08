from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('accounts', views.AccountViewSet),
router.register('transactions', views.TransactionViewSet, basename='transactions'),
# router.register('transfer', views.TransferViewSet, basename='transfer')

urlpatterns = [
    path('', include(router.urls)),
    # path('accounts', views.ListAccount.as_view()),
    # for function base
    # path('accounts', views.list_account),
    # path('accounts/<str:pk>/', views.AccountDetail.as_view()),
    # for function base
    # path('accounts/<str:pk>/', views.account_detail),
    path('deposit', views.Deposit.as_view()),
    path('withdraw', views.Withdraw.as_view()),
    path('checkbalance', views.CheckBalance.as_view()),
    # path('create', views.CreateAccount.as_view()),


]
