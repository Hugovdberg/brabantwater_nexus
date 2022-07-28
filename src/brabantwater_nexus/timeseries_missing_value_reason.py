import enum


class MissingValueReason(enum.Enum):
    NO_MEASUREMENT = "no_measurement"
    NO_WATER = "no_water"
    FROZEN = "frozen"
    UNREACHABLE = "location_unreachable"
    BROKEN = "location_broken"
