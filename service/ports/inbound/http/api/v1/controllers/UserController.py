from fastapi import APIRouter, Body, Depends
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

class UserController:
    def __init__(self, inboundUserAdapter):
        self.inboundUserAdapter = inboundUserAdapter

    def login(self, login_request: LoginRequest = Body(...)):
        username = login_request.username
        password = login_request.password
        
        return self.inboundUserAdapter.login(username, password, 'traceId')

def get_user_controller(inboundUserAdapter):
    return UserController(inboundUserAdapter)

@router.post("/login")
def login(login_request: LoginRequest = Body(...), user_controller: UserController = Depends(get_user_controller)):
    return user_controller.login(login_request)