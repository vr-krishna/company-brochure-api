from pydantic import BaseModel, HttpUrl, Field


class BrochureRequest(BaseModel):
    url: HttpUrl


class RelevantLinks(BaseModel):
    links: list[HttpUrl]


class BrochureResponse(BaseModel):
    title: str
    brochure: str
    pages_used: int