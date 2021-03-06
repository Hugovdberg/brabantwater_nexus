import dataclasses
from typing import List

import pydantic
from shapely import geometry

from brabantwater_nexus.hashable import HashableModel


@dataclasses.dataclass(frozen=True)
class GroundwaterMonitoringTubeLocation:
    dawaco_filters_recnum: int
    x: float
    y: float
    elevation_top: float
    screen_top: float
    screen_bottom: float


class GroundwaterMonitoringTube(HashableModel):
    """Peilbuis, onderdeel van een MonitoringStation"""

    id_src: str = pydantic.Field(
        description="ID van de peilbuis binnen het bron systeem."
    )
    monitoring_station_id_src: str = pydantic.Field(
        description=(
            "ID van de bovenliggende monitoring station binnen het bron systeem."
        ),
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
