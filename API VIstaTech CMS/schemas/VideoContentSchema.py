from typing import Optional

from pydantic import BaseModel as SCBaseModel

class VideoContentSchema(SCBaseModel):
    id: Optional[int]
    video_content_titulo: str
    video_content_video_link: str


    class Config:
        orm_mode = True