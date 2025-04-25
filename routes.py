#Program routing
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas

router = APIRouter()

# DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def root():
    return {"message": "The Health System is running!"}

@router.post("/programs/", response_model=schemas.Program)
def create_program(program: schemas.ProgramBase, db: Session = Depends(get_db)):
    return crud.create_program(db, program)

@router.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientBase, db: Session = Depends(get_db)):
    return crud.create_client(db, client)

@router.post(
    "/clients/{client_id}/enroll/{program_id}",
    response_model=schemas.Client
)
def enroll_client(client_id: int, program_id: int, db: Session = Depends(get_db)):
    client = crud.enroll_client(db, client_id, program_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client or Program not found")
    return client

@router.get("/clients/", response_model=list[schemas.Client])
def read_clients(db: Session = Depends(get_db)):
    clients = crud.get_clients(db)
    for client in clients:
        score = crud.calculate_risk_score(client)
        client.risk_score = score
        client.risk_level = crud.get_risk_label(score)
    return clients

@router.get("/clients/{client_id}", response_model=schemas.Client)
def read_client(client_id: int, db: Session = Depends(get_db)):
    client = crud.get_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    score = crud.calculate_risk_score(client)
    client.risk_score = score
    client.risk_level = crud.get_risk_label(score)
    return client