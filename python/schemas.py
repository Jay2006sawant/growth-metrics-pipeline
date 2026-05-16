from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class CustomerRow(BaseModel):
    customer_id: int = Field(gt=0)
    signup_date: date
    country: str = Field(min_length=2, max_length=2)


class OrderRow(BaseModel):
    order_id: int = Field(gt=0)
    customer_id: int = Field(gt=0)
    order_date: date
    channel: str = Field(min_length=1, max_length=32)
    campaign: str = Field(min_length=1, max_length=64)
    net_revenue: float

    @field_validator("net_revenue")
    @classmethod
    def non_negative_revenue(cls, value: float) -> float:
        if value < 0:
            raise ValueError("net_revenue cannot be negative")
        return value


class SessionRow(BaseModel):
    session_id: int = Field(gt=0)
    session_date: date
    channel: str
    campaign: str


class SpendRow(BaseModel):
    spend_date: date
    channel: str
    campaign: str
    spend_usd: float

    @field_validator("spend_usd")
    @classmethod
    def non_negative_spend(cls, value: float) -> float:
        if value < 0:
            raise ValueError("spend_usd cannot be negative")
        return value


class FxRow(BaseModel):
    rate_date: date
    base_currency: str
    quote_currency: str
    exchange_rate: float
    source: Optional[str] = None
