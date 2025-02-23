from app.config.supabase import supabase_client
from app.schemas.login import UserLogin
from app.schemas.register import UserRegister

class AuthService:
    @staticmethod
    async def login(credentials: UserLogin):
        try:
            response = supabase_client.auth.sign_in_with_password({
                "email": credentials.email,
                "password": credentials.password
            })
            return response
        except Exception as e:
            raise Exception(f"Authentication failed: {str(e)}")
        
    @staticmethod
    async def register(user_data: UserRegister):
        try:
            response = supabase_client.auth.sign_up({
                "email": user_data.email,
                "password": user_data.password
            })
            return response
        except Exception as e:
            raise Exception(f"Registration failed: {str(e)}")
