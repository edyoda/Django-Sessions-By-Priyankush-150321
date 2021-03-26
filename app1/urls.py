from django.urls import path


from app1.views import blogs, home, sale, order

urlpatterns = [   
    path('blogs/', blogs),
    path('home_application1/', home),
    path('sale_app1/', sale, name='sale_url'),
    path('order_application1/', order, name='order_url_name'),
]
