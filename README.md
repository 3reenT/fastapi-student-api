# 📚 Student Management API – FastAPI + Postman
This is a simple CRUD API built with FastAPI to manage student records.
You can Create, Read, Update, and Delete students easily and test all endpoints in Postman.


## 🚀 Setup Instructions
### 1️⃣ Install Dependencies
```
pip install fastapi uvicorn
```
### 2️⃣ Run the API
```
python -m uvicorn myapi:app --reload
```
✅ The API will be available at: http://127.0.0.1:8000/


## 📖 API Endpoints
### 🔹 1. Get Student by ID
Method: GET

URL: http://127.0.0.1:8000/get-students/1

✅ Example Response:

```
{
  "name": "Arein",
  "age": 22,
  "year": "year 4"
}
```
### 🔹 2. Get Student by Name
Method: GET

URL:http://127.0.0.1:8000/get-by-name/?name=Arein&test=1

✅ Example Response:
```
{
  "name": "Arein",
  "age": 22,
  "year": "year 4"
}
```
### 🔹 3. Create Student
Method: POST

URL: http://127.0.0.1:8000/create-student/3

Body → raw → JSON:
```
{
  "name": "Deema",
  "age": 21,
  "year": "year 2"
}
```
✅ Example Response:
```
{
  "name": "Teema",
  "age": 21,
  "year": "year 2"
}
```
### 🔹 4. Update Student
Method: PUT

URL: http://127.0.0.1:8000/update-student/1

Body → raw → JSON (send only the fields you want to update):
```
{
  "age": 25
}
```
✅ Example Response:
```
{
  "name": "Arein",
  "age": 25,
  "year": "year 4"
}
```
### 🔹 5. Delete Student
Method: DELETE

URL: http://127.0.0.1:8000/delete-student/1

✅ Example Response:
```
{
  "Message": "Student deleted successfully"
}
```
