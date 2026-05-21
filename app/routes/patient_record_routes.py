from fastapi import APIRouter
from app.database.mongodb import patient_records_collection

router = APIRouter()

@router.post("/records")
def create_patient_record(record: dict):
    result = patient_records_collection.insert_one(record)

    return {
        "message": "Patient record created",
        "id": str(result.inserted_id)
    }

@router.get("/records")
def get_patient_records():
    records = []

    for record in patient_records_collection.find():
        record["_id"] = str(record["_id"])
        records.append(record)

    return records