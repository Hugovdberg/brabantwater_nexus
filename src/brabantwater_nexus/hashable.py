import pydantic


class HashableModel(pydantic.BaseModel):
    def __hash__(self) -> int:  # type: ignore
        return hash((type(self),) + tuple(self.__dict__.values()))
