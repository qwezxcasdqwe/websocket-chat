import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings") #указываем основной файл с настройками

application = ProtocolTypeRouter({
   "http": get_asgi_application(), #http запросы бросаем на django
   "websocket": AuthMiddlewareStack(  #прослойка для получения request.user
       URLRouter(
           chat.routing.websocket_urlpatterns
       )
   ),
})
