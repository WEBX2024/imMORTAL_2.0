from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')  # replace with your connection string if different

# Select the database
db = client.immortals

# Create (or select) the doctor_time collection
doctor_time_collection = db.doctor_time

# Example data to insert
doctor_time_data = [
    {
        "doctor_id": "D123",
        "date": "2024-06-01",
        "time_slot": "09:00-09:30",
        "status": "available"
    },
    {
        "doctor_id": "D123",
        "date": "2024-06-01",
        "time_slot": "09:30-10:00",
        "status": "booked",
        "appointment_id": "A789"
    },
    {
        "doctor_id": "D124",
        "date": "2024-06-01",
        "time_slot": "10:00-10:30",
        "status": "available"
    }
]

# Insert the data into the collection
doctor_time_collection.insert_many(doctor_time_data)

# Verify insertion by printing out the documents
for doc in doctor_time_collection.find():
    print(doc)
