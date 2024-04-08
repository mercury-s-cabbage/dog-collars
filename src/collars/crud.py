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
