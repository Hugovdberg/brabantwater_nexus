import dataclasses
from typing import List

import pydantic
from shapely import geometry

from brabantwater_nexus.data_connection import DataConnection


@dataclasses.dataclass(frozen=True)
class GroundwaterMonitoringTubeMetadata:
    dawaco_filters_recnum: int
    putcode_dawaco: str
    filternummer: int
    label: str
    id_src: str
    monitoring_station_id_src: str


@dataclasses.dataclass(frozen=True)
class GroundwaterMonitoringTubeLocation:
    dawaco_filters_recnum: int
    x: float
    y: float
    elevation_top: float
    screen_top: float
    screen_bottom: float


class GroundwaterMonitoringTube(pydantic.BaseModel):
    """Peilbuis, onderdeel van een MonitoringStation"""

    id: int = pydantic.Field(
        description=(
            "ID van de peilbuis binnen Nexus, aangemaakt door Nexus. "
            "Nieuwe buizen worden aangeleverd met ID -1."
        ),
        ge=-1,
    )
    dc_id: DataConnection = pydantic.Field(description="ID van de data connection.")
    id_src: str = pydantic.Field(
        description="ID van de peilbuis binnen het bron systeem."
    )
    monitoring_station_id: int = pydantic.Field(
        description=(
            "ID van de bovenliggende monitoring station binnen Nexus, "
            "aangemaakt door Nexus. "
            "Nieuwe buizen worden aangeleverd met ID -1."
        ),
        ge=-1,
    )
    monitoring_station_id_src: str = pydantic.Field(
        description=(
            "ID van de bovenliggende monitoring station binnen het bron systeem."
        ),
        ge=-1,
    )
    x: float = pydantic.Field(
        description=(
            "X coordinaat van de peilbuis in het Rijksdriehoekstelsel (EPSG:28992)."
        ),
        ge=-7000,
        le=300000,
    )
    y: float = pydantic.Field(
        description=(
            "Y coordinaat van de peilbuis in het Rijksdriehoekstelsel (EPSG:28992)."
        ),
        ge=289000,
        le=629000,
    )
    label: str = pydantic.Field(description="Weergavenaam van de peilbuis.")
    screen_no: int = pydantic.Field(description="Nummer van de peilbuis")
    elevation_top: float = pydantic.Field(
        description="Bovenkant van de peilbuis in m. t.o.v. NAP"
    )
    screen_top: float = pydantic.Field(
        description="Bovenkant van het peilfilter in m. t.o.v. NAP"
    )
    screen_bottom: float = pydantic.Field(
        description="Onderkant van het peilfilter in m. t.o.v. NAP"
    )

    @property
    def centroid(self) -> geometry.Point:
        return geometry.Point(self.x, self.y)


class GroundwaterMonitoringTubeList(pydantic.BaseModel):
    __root__: List[GroundwaterMonitoringTube]
