from fastapi import APIRouter, HTTPException
from backend.models.course_model import courses_collection

router = APIRouter()

@router.post("/courses/")
def create_course(course: dict):
    if courses_collection.find_one({"code": course["code"]}):
        raise HTTPException(status_code=400, detail="Course already exists")
    courses_collection.insert_one(course)
    return {"message": "Course added successfully"}

@router.get("/courses/")
def get_courses():
    courses = list(courses_collection.find({}, {"_id": 0}))
    return {"courses": courses}
