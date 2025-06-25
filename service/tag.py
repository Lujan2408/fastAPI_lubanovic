import datetime
from model.tag import TagIn, TagOut, Tag
import service.tag as tag_service
from fastapi import FastAPI

app = FastAPI()

@app.post("/") 
def create_tag(tag_in: TagIn) -> TagIn: 
  tag: Tag = Tag(tag=tag_in.tag, created_at=datetime.datetime.now(), secret="123")
  tag_service.create_tag(tag)
  return tag_in

@app.get("/{tag_str}")
def get_one(tag_str: str) -> TagOut:
  tag : Tag = tag_service.get_one(tag_str)
  return tag