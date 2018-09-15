"""yerbamat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from yerba_mat.views import IndexView, CategoryView, CategoryAddView, ProductAddView, ProductDetailsView, BasketView
from yerba_mat.views import LoginView, LogoutView, ClientCreateView, AddProductToBasketView, ModifyInsideBasketView
from yerba_mat.views import OrderCreateView, OrderToSendView, CategoryDeleteView, ProductDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/$', IndexView.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^category_view/(?P<id>(\d)+)/$', CategoryView.as_view(), name='category-view'),
    url(r'^category_add/$', CategoryAddView.as_view(), name='category-add'),
    url(r'^product_add/$', ProductAddView.as_view(), name='product-add'),
    url(r'^product_details/(?P<id>(\d)+)/$', ProductDetailsView.as_view(), name='product-details'),
    url(r'^basket/$', BasketView.as_view(), name='basket'),
    url(r'^client_create/$', ClientCreateView.as_view(), name='client-create'),
    url(r'^add_product_to_basket/(?P<id>(\d)+)/$', AddProductToBasketView.as_view(), name='add-product-to-basket'),
    url(r'^modify_inside_basket/$', ModifyInsideBasketView.as_view(), name='modify-inside-basket'),
    url(r'^order_create/$', OrderCreateView.as_view(), name='order-create'),
    url(r'^order_to_send/$', OrderToSendView.as_view(), name='order-to-send'),
    url(r'^category_delete/$', CategoryDeleteView.as_view(), name='category-delete'),
    url(r'^product_delete/$', ProductDeleteView.as_view(), name='product-delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
