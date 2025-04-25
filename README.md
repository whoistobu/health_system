# health_system
A simple program that stimulates basic health information for managing clients and health programs
It is built with FastAPI and SQLite to help doctors manage clients and enroll them into health programs. It includes also a health risk scoring and risk level labeling feature for patient care.

Features

1. Program Management
  - Create health programs (TB, HIV, Malaria)
     
2. Client Management  
  - Register new clients (name, age, gender)  
  - Enroll clients into one or more programs  
  - List all clients.

3. Client Profile
  - View a single client’s full profile

4. Error Handling
  - checks for duplication on program creation  
  - Clear 400 responses for validation or integrity errors  
  - Clean 404 when resources are not found

5. Tech Stack

- Language & Framework: Python, FastAPI  
- ORM: SQLAlchemy  
- Validation & Serialization: Pydantic  
- Database:SQLite (file `health.db`)  
- Server: Uvicorn (ASGI)  
- Testing:`pytest` (basic smoke tests)  

6. Running

 create virtual enviroment - venv\Scripts\activate (windows)
 Install dependacies - pip install -r requirements.txt
 Start the server - uvicorn main:app --reload
 on the browser open - http://127.0.0.1:8000/docs (or whichever port you are using)
 run the program

 7. Example Workflows
 
- Create a Program
   curl -X POST http://127.0.0.1:8000/programs/ \
      -H "Content-Type: application/json" \
      -d '{"name":"Malaria","description":"Check for Malaria"}'
- Register a Client
   curl -X POST http://127.0.0.1:8000/clients/ \
      -H "Content-Type: application/json" \
      -d '{"name":"Keith","age":20,"gender":"male"}'
- Enroll the Client
   curl -X POST http://127.0.0.1:8000/clients/1/enroll/3
- View Client Profile
   curl http://127.0.0.1:8000/clients/1

 8. Added Inovation

 I have added a rule-based health risk scoring program that automatically adds points for age, gender, and programs so it would provide a general summary of the clients health and help the doctor take care of the patient

 Build by Keith Gitonga as an Intern task
 /whoistobu  
