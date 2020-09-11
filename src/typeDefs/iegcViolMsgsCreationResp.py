from typing import TypedDict


class IegcViolMsgsCreationResp(TypedDict):
    isSuccess: bool
    status: int
    message: str
