from fastapi import FastAPI
from controllers.ItemController import router as items_router
from controllers.PingController import router as ping_router

app = FastAPI()

app.include_router(items_router)
app.include_router(ping_router)