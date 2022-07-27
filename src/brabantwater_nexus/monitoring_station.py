import dataclasses
from typing import List, Optional

import pydantic
from shapely import geometry

from brabantwater_nexus.hashable import HashableModel
from brabantwater_nexus.monitoring_station_type import MonitoringStationType
from brabantwater_nexus.owner import Owner


@dataclasses.dataclass(frozen=True)
class MonitoringStationLocation:
    dawaco_mp_recnum: int
    x: float
    y: float
    surface_elevation: float
    sensor_elevation: Optional[float]


class MonitoringStation(HashableModel):
    """Fysieke meetlocatie waar een of meer metingen aan gekoppeld zijn"""

    id_src: str = pydantic.Field(
        description="ID van de meetlocatie binnen het bron systeem."
    )
    x: float = pydantic.Field(
        description=(
            "X coordinaat van de meetlocatie "
            "in het Rijksdriehoekstelsel (EPSG:28992)."
        ),
        ge=-7000,
        le=300000,
    )
    y: float = pydantic.Field(
        description=(
            "Y coordinaat van de meetlocatie "
            "in het Rijksdriehoekstelsel (EPSG:28992)."
        ),
        ge=289000,
        le=629000,
    )
    label: str = pydantic.Field(description="Weergavenaam van de meetlocatie.")
    surface_elevation: float = pydantic.Field(description="Maaiveld hoogte in m+NAP.")
    owner: Owner = pydantic.Field(description="Eigenaar van de meetlocatie.")
    group: MonitoringStationType = pydantic.Field(
        description="Type van de meetlocatie."
    )
    sensor_elevation: Optional[float] = pydantic.Field(
        description=(
            "Hoogte van gekoppelde sensor in m+NAP. "
            "Alleen relevant voor bodemvocht metingen"
        )
    )

    @property
    def centroid(self) -> geometry.Point:
        return geometry.Point(self.x, self.y)


class MonitoringStationList(pydantic.BaseModel):
    __root__: List[MonitoringStation]
