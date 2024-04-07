from sqlalchemy.orm import Session
import models, schemas

def create_user(db: Session,
                user: schemas.UserCreate
                ) -> models.User:
    fake_hash_password = user.password[::-1]
    db_user = models.User(
        name=user.name,
        email=user.email,
        hash_password=fake_hash_password,
        is_active = True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user