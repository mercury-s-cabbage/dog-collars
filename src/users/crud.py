from sqlalchemy.orm import Session
import src.users.models as models
import src.users.schemas as schemas
import uuid


def create_user(db: Session,
                user: schemas.User
                ) -> models.Users:
    fake_hash_password = user.password[::-1]
    db_user = models.Users(
        name=user.nickname,
        number=user.number,
        hash_password=fake_hash_password,
        is_active=True,
        is_superuser=user.superuser
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_user_session(db: Session,
                        id: int,
                        token: str
                        ) -> models.UsersSessions:
    db_user_session = models.UsersSessions(
        id=id,
        token=token
    )
    db.add(db_user_session)
    db.commit()
    db.refresh(db_user_session)
    return db_user_session