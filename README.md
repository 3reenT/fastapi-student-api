This is a simple CRUD API built with FastAPI to manage student records.
You can Create, Read, Update, and Delete students easily and test all endpoints in Postman.

🚀 Setup Instructions

⿡ Install Dependencies
pip install fastapi uvicorn

⿢ Run the API
python -m uvicorn myapi:app --reload
✅ The API will be available at http://127.0.0.1:8000/

📖 API Endpoints
🔹 1. Get Student by ID
Method: GET
URL: http://127.0.0.1:8000/get-students/1

🔹 2. Get Student by Name
Method: GET
URL:http://127.0.0.1:8000/get-by-name/?name=Arein&test=1

🔹 3. Create Student
Method: POST
URL: http://127.0.0.1:8000/create-student/3
Body → raw → JSON

🔹 4. Update Student
Method: PUT
URL: http://127.0.0.1:8000/update-student/1
Body → raw → JSON (send only the fields you want to update)

🔹 5. Delete Student
Method: DELETE
URL: http://127.0.0.1:8000/delete-student/1
