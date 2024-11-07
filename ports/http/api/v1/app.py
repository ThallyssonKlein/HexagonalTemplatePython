from fastapi import FastAPI
from .controllers.UserController import router as user_router, get_user_controller
from .controllers.PingController import router as ping_router

from adapters.inbound.http.api.v1.InboundUserAdapter import InboundUserAdapter

app = FastAPI()

app.dependency_overrides[get_user_controller] = lambda: get_user_controller(InboundUserAdapter())

app.include_router(user_router)
app.include_router(ping_router)