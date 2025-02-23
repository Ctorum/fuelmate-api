from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr


class IdentityData(BaseModel):
    email: Optional[EmailStr]
    sub: Optional[str]

class Identity(BaseModel):
    id: Optional[UUID]
    user_id: Optional[UUID]
    identity_data: Optional[IdentityData]
    provider: Optional[str]
    created_at: Optional[datetime]
    last_sign_in_at: Optional[datetime]
    updated_at: Optional[datetime]

class AppMetadata(BaseModel):
    provider: Optional[str]
    providers: Optional[List[str]]

class UserData(BaseModel):
    id: Optional[UUID]
    app_metadata: Optional[AppMetadata]
    user_metadata: Optional[dict]
    aud: Optional[str]
    confirmation_sent_at: Optional[datetime]
    recovery_sent_at: Optional[datetime]
    email_change_sent_at: Optional[datetime]
    new_email: Optional[str]
    invited_at: Optional[datetime]
    action_link: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]
    created_at: Optional[datetime]
    confirmed_at: Optional[datetime]
    email_confirmed_at: Optional[datetime]
    phone_confirmed_at: Optional[datetime]
    last_sign_in_at: Optional[datetime]
    role: Optional[str]
    updated_at: Optional[datetime]
    identities: Optional[List[Identity]]
    factors: Optional[str]

class Session(BaseModel):
    provider_token: Optional[str]
    provider_refresh_token: Optional[str]
    access_token: Optional[str]
    refresh_token: Optional[str]
    expires_in: Optional[int]
    expires_at: Optional[int]
    token_type: Optional[str]
    user: Optional[UserData]

class UserRegisterResponse(BaseModel):
    user: Optional[UserData]
    session: Optional[Session]

class UserRegister(BaseModel):
    email: Optional[EmailStr]
    password: Optional[str]