from sqlalchemy.orm import Session
from src.users.models import Users
from src.users.schemas import User


def create_user(db: Session,
                user: User
                ) -> Users:
    fake_hash_password = user.password[::-1]
    db_user = Users(
        name=user.name,
        email=user.email,
        hash_password=fake_hash_password,
        is_active=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user