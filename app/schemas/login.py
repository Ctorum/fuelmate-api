from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserMetadata(BaseModel):
    provider: str
    providers: List[str]

class UserIdentity(BaseModel):
    pass

class UserDetails(BaseModel):
    id: str
    app_metadata: UserMetadata
    user_metadata: dict
    aud: str
    confirmation_sent_at: Optional[datetime]
    recovery_sent_at: Optional[datetime]
    email_change_sent_at: Optional[datetime]
    new_email: Optional[str]
    invited_at: Optional[datetime]
    action_link: Optional[str]
    email: EmailStr
    phone: str
    created_at: datetime
    confirmed_at: datetime
    email_confirmed_at: datetime
    phone_confirmed_at: Optional[datetime]
    last_sign_in_at: datetime
    role: str
    updated_at: datetime
    identities: List[UserIdentity]
    factors: Optional[dict]
    is_anonymous: bool

class Session(BaseModel):
    provider_token: Optional[str]
    provider_refresh_token: Optional[str]
    access_token: str
    refresh_token: str
    expires_in: int
    expires_at: int
    token_type: str
    user: UserDetails

class UserLoginResponse(BaseModel):
    user: UserDetails
    session: Session