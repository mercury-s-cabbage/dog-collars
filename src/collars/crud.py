from sqlalchemy.orm import Session
import src.collars.models as models
import src.collars.schemas as schemas


def create_collar(db: Session,
                mac=str
                ) -> models.Collars:
    db_collar = models.Collars(
        mac=mac,
        is_active=True
    )
    db.add(db_collar)
    db.commit()
    db.refresh(db_collar)
    return db_collar

def add_me_collar(db: Session,
                user_id: int,
                collar_id: int
                ) -> models.Owners:
    db_collar_user = models.Owners(
        user_id=user_id,
        collar_id=collar_id
    )
    db.add(db_collar_user)
    db.commit()
    db.refresh(db_collar_user)
    return db_collar_user

def remove_collar(db: Session,
                user_id: int,
                collar_id: int
                ):
    db_collar_user = db.query(models.Owners).filter_by(user_id=user_id, collar_id=collar_id).one()
    db.delete(db_collar_user)
    db.commit()
    return {}

def collar_group(db: Session, user_id: int):
    db_pets = [x.collar_id for x in db.query(models.Owners).filter_by(user_id=user_id).distinct()]
    is_active = []
    for i in db_pets:
        collar_n = db.query(models.Collars).filter_by(id=i).one()
        if (collar_n.is_active == True):
            is_active.append(i)
    return {"owner_id": user_id,
            "collars_id": is_active}

def unactivate_collar(db: Session, collar_id: int):
    db_collar_active = db.query(models.Collars).filter_by(id=collar_id).one()
    db_collar_active.is_active = False
    db.commit()
    db.refresh(db_collar_active)
    return {"active_status": False}


