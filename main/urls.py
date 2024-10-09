from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, create_account, user_login, user_logout, update_product, delete_product, create_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('create_account/', create_account, name='create_account'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('update-product/<uuid:id>', update_product, name='update_product'),
    path('delete-product/<uuid:id>', delete_product, name='delete_product'),
    path('create-ajax', create_product_ajax, name='create_product_ajax'),
]