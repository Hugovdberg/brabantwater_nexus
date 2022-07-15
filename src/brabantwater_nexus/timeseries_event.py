import datetime
from typing import List, Optional

import pydantic

from brabantwater_nexus.data_connection import DataConnection
from brabantwater_nexus.feature_type import FeatureType
from brabantwater_nexus.hashable import HashableModel
from brabantwater_nexus.timeseries_missing_value_reason import MissingValueReason
from brabantwater_nexus.timeseries_parameter import TimeseriesParameter


class TimeseriesEvent(HashableModel):
    dc_id: DataConnection = pydantic.Field(description="ID van de data connection.")
    feature_type: FeatureType = pydantic.Field(
        description="Type meetpunt waaraan de meting gekoppeld moet worden."
    )
    feature_id: int = pydantic.Field(
        description=(
            "ID van het meetpunt binnen Nexus, aangemaakt door Nexus. "
            "Bij bulkleveringen aangeleverd met ID -1."
        ),
        ge=-1,
    )
    feature_id_src: str = pydantic.Field(
        description=("ID van het meetpunt binnen het bron systeem."),
    )
    parameter: TimeseriesParameter = pydantic.Field(description="Parameter")
    timestamp: datetime.datetime = pydantic.Field(description="Tijdstip van de meting")
    value: Optional[float] = pydantic.Field(description="Meting")
    missing_value_reason: Optional[MissingValueReason] = pydantic.Field(
        description="Reden voor afwezigheid meting, alleen gevuld bij afwezigheid meting."
    )


class TimeseriesEventSet(pydantic.BaseModel):
    """Set van TimeseriesEvent objecten, niet per se van een enkele time series"""

    start_date: datetime.datetime = pydantic.Field(
        "Startdatum van de metingen in de set."
    )
    end_date: datetime.datetime = pydantic.Field(
        description="Einddatum van de metingen in de set."
    )
    events: List[TimeseriesEvent] = pydantic.Field(description="Events in de set")
