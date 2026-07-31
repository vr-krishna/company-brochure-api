from pydantic import BaseModel, HttpUrl, Field


class WebsiteLink(BaseModel):
    text: str = Field(..., description="Anchor text")
    url: HttpUrl = Field(..., description="Absolute URL")


class Website(BaseModel):
    url: HttpUrl
    title: str
    text: str
    links: list[WebsiteLink] = Field(default_factory=list)