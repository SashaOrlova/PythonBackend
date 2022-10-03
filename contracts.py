from pydantic import BaseModel


class CreateCommentModel(BaseModel):
    topic_id: int
    text: str


class CreateTopicModel(BaseModel):
    text: str
