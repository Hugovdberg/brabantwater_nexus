import datetime
from typing import List, Optional, Tuple

import pydantic

from brabantwater_nexus.feature_type import FeatureType
from brabantwater_nexus.hashable import HashableModel
from brabantwater_nexus.timeseries_missing_value_reason import MissingValueReason
from brabantwater_nexus.timeseries_parameter import TimeseriesParameter


class Timeseries(HashableModel):
    feature_type: FeatureType = pydantic.Field(
        description="Type meetpunt waaraan de meting gekoppeld moet worden."
    )
    feature_id_src: str = pydantic.Field(
        description=("ID van het meetpunt binnen het bron systeem."),
    )
    parameter: TimeseriesParameter = pydantic.Field(description="Parameter")
    values: List[
        Tuple[
            datetime.datetime,
            Optional[float],
            Optional[str],
            Optional[MissingValueReason],
        ]
    ] = pydantic.Field(description="Metingen")


class TimeseriesList(pydantic.BaseModel):
    """Lijst van TimeseriesEvent objecten, niet per se van een enkele time series"""

    __root__: List[Timeseries]
