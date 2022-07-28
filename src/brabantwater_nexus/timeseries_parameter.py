import enum


class TimeseriesParameter(enum.Enum):
    GROUNDWATER_HEAD = "groundwater_head_m_msl"
    GROUNDWATER_HEAD_MANUAL = "groundwater_head_manual_m_msl"
    COLLECTOR_REMARK = "collector_remark"
    PH_FIELD = "groundwater_ph_field"
    ELECTRIC_CONDUCTIVITY_FIELD = "groundwater_ec_us_field_cm"
    PH = "groundwater_ph"
    ELECTRIC_CONDUCTIVITY = "groundwater_ec_us_cm"
