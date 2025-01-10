# Anbessa Bus Backend System
# Features
- User Authentication with password change and reset
- Complaint Submission and retrieval
# Usage
1. Clone the repo
```
git clone https://github.com/abeni-al7/anbessa_project
```
2. Get into the project directory
```
cd anbessa_project
```
3. Create a virtual environment by the name .venv
For Linux and Mac
```
python3 -m venv .venv
```
For Windows
```
python -m venv .venv
```
4. Activate the virtual environment
For Linux and Mac
```
source .venv/bin/activate
```
For Windows
```
.venv\Scripts\activate
```
5. Install the dependencies (ensure virtual environment is activated before this step)
```
pip install -r requirements.txt
```
6. Migrate the database
```
python manage.py migrate
```
7. Create an admin user through the command line:
```
python manage.py createsuperuser
```
Fill in username, email and password for an admin user
8. Run the backend server in a terminal window
```
python manage.py runserver
```
9. Access the API docs
Browse to http://localhost:8000/api/swagger or http://localhost:8000/api/redoc to access the API documentation
10. In your frontend app prefix all API urls with http://localhost:8000 (preferably store it in an environment variable) and use the APIs exactly how they are laid out in the documentation

# API Docs
Use either
- /api/swagger
or
- /api/redoc
for API documentation