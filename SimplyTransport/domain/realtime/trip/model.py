from litestar.contrib.sqlalchemy.base import BigIntAuditBase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pydantic import BaseModel as _BaseModel


class BaseModel(_BaseModel):
    """Extend Pydantic's BaseModel to enable ORM mode"""

    model_config = {"from_attributes": True}


class RTTripModel(BigIntAuditBase):
    __tablename__ = "rt_trip"


class RTTrip(BaseModel):
    pass
