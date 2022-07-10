import enum


class MonitoringStationType(enum.Enum):
    """Type meetlocatie"""

    GROUNDWATER = "Grondwater"
    SURFACE_WATER = "Oppervlaktewater"
    COMBINED = "Grondwater en Oppervlaktewater"
    SOIL_MOISTURE = "Bodemvocht"
