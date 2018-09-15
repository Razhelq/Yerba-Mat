from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from yerba_mat.views import IndexView, CategoryView, CategoryAddView, ProductAddView, ProductDetailsView, BasketView
from yerba_mat.views import LoginView, LogoutView, ClientCreateView, AddProductToBasketView, ModifyInsideBasketView
from yerba_mat.views import OrderCreateView, OrderToSendView, CategoryDeleteView, ProductDeleteView
from yerba_mat.views import CategoryModifyView, ProductModifyView


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
    url(r'^category_delete/$', CategoryDeleteView.as_view(), name='category-del'),
    url(r'^product_delete/$', ProductDeleteView.as_view(), name='product-del'),
    url(r'^category_modify/$', CategoryModifyView.as_view(), name='category-mod'),
    url(r'^product_modify/$', ProductModifyView.as_view(), name='product-mod')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
