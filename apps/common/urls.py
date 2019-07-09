from .jwt.urls import urlpatterns as jwt_urls
from .swagger.urls import urlpatterns as swagger_urls
from .silk.urls import urlpatterns as silk_urls

urlpatterns_common = []
urlpatterns_common += jwt_urls
urlpatterns_common += swagger_urls
urlpatterns_common += silk_urls
