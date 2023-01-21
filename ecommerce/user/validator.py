from sqlalchemy.orm import Session
from . models import User
from typing import Optional

async def verify_email_exists(email: str, db_session: Session) -> Optional[User]:
    return db_session.query(User).filter(User.email == email).first()