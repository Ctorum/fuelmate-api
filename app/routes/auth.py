from fastapi import APIRouter, HTTPException, Depends
from app.schemas.login import UserLogin, UserLoginResponse
from app.schemas.register import UserRegister, UserRegisterResponse
from app.auth.service import AuthService
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/login", response_model=UserLoginResponse)
async def login(credentials: UserLogin):
    try:
        response = await AuthService.login(credentials)
        return response
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
    
@router.post("/register", response_model=UserRegisterResponse)
async def register(user_data: UserRegister):
    try:
        response = await AuthService.register(user_data)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/protected")
async def protected_route(user = Depends(get_current_user)):
    return {
        "message": "This is a protected route",
        "user_id": user.user.id,
        "user_email": user.user.email
    }