import datetime
from typing import List, Optional

import pydantic

from brabantwater_nexus.feature_type import FeatureType
from brabantwater_nexus.hashable import HashableModel
from brabantwater_nexus.timeseries_missing_value_reason import MissingValueReason
from brabantwater_nexus.timeseries_parameter import TimeseriesParameter


class TimeseriesEvent(HashableModel):
    feature_type: FeatureType = pydantic.Field(
        description="Type meetpunt waaraan de meting gekoppeld moet worden."
    )
    feature_id_src: str = pydantic.Field(
        description=("ID van het meetpunt binnen het bron systeem."),
    )
    parameter: TimeseriesParameter = pydantic.Field(description="Parameter")
    timestamp: datetime.datetime = pydantic.Field(description="Tijdstip van de meting")
    value: Optional[float] = pydantic.Field(description="Meting (numerieke waarde)")
    text_value: Optional[str] = pydantic.Field(description="Meting (tekstwaarde)")
    missing_value_reason: Optional[MissingValueReason] = pydantic.Field(
        description="Reden voor afwezigheid meting, alleen gevuld bij afwezigheid meting."
    )


class TimeseriesEventList(pydantic.BaseModel):
    """Lijst van TimeseriesEvent objecten, niet per se van een enkele time series"""

    __root__: List[TimeseriesEvent]
