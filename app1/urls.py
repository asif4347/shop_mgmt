from django.urls import path, re_path
from .views import *
from django.conf.urls import url


urlpatterns= [
    path('', loginView, name='login'),
    path('logout/', logout, name='logout'),

    path('display_salesman/', DisplaySalesmanView, name='display_salesman'),
    path('add_salesman/', AddSalesmanView, name='add_salesman'),
    path('edit_salesman/<int:pk>/', EditSalesmanView, name='edit_salesman'),
    path('delete_salesman/<int:pk>/', delete_salesman, name='delete_salesman'),

    path('display_shops/', DisplayShopView, name='display_shops'),
    path('add_shop/', AddShopView, name='add_shop'),
    path('edit_shop/<int:pk>/', EditShop, name='edit_shop'),
    path('delete_shop/<int:pk>/', delete_shop, name='delete_shop'),

    path('display_orders/', indexView, name='display_orders'),
    path('add_order/', ProfileFamilyMemberCreate.as_view(), name='add_order'),
    url(r'profile/(?P<pk>[0-9]+)/$', ProfileFamilyMemberUpdate.as_view(), name='edit_order'),
    # path('edit_order/<int:pk>/', ProfileFamilyMemberUpdate.as_view(), name='edit_order'),
    path('delete_order/<int:pk>/', delete_order, name='delete_order'),

    path('salesman_order/<int:pk>/', SalesmanOrderView, name='salesman_order'),

    path('order_amounts/<int:pk>/', OrderAmountView, name='order_amounts'),
    path('add_amount/<int:pk>/', AddAmountView, name='add_amount'),
    path('edit_amount/<int:pk>/', EditAmount, name='edit_amount'),
    path('delete_amount/<int:pk>/', AddAmountView, name='delete_amount'),



    path('index/', indexView, name='index'),
    path('filter-order/', filterView, name='filter-order'),
    # path('add_order', , name='index')
    path('export/orders',export_orders_xls , name="export-orders")
]
