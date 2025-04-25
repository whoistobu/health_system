# crud.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
import models, schemas

# Main program
def create_program(db: Session, program: schemas.ProgramBase):

    # Check any existing/similar program
    existing = db.query(models.Program)\
                 .filter(models.Program.name == program.name)\
                 .first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail=f"Program '{program.name}' already exists."
        )

    # Create a new program
    db_program = models.Program(**program.dict())
    db.add(db_program)
    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e.orig))
    db.refresh(db_program)
    return db_program

# Client program
def create_client(db: Session, client: schemas.ClientBase):
    # New client
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_client(db: Session, client_id: int):
    #Get a client by their ID
    return db.query(models.Client).filter(models.Client.id == client_id).first()

def get_clients(db: Session):
    #Get all clents
    return db.query(models.Client).all()

# Enrolling a client
def enroll_client(db: Session, client_id: int, program_id: int):
    client = get_client(db, client_id)
    program = db.query(models.Program).filter(models.Program.id == program_id).first()
    if not client or not program:
        return None

    client.programs.append(program)
    db.commit()
    db.refresh(client)
    return client

# Calculate the risk
def calculate_risk_score(client) -> int:
    """
    Calculate a simple rule-based health risk score using various factors such as age gender and program:
    Age ≥ 60: +3 points
    Age 40-59: +2 points
    Female: +1 point
    HIV: +4 points
    TB: +3 points
    Malaria: +2 points
    Other: +1 point
    """
    score = 0
    # Age scoring
    if client.age >= 60:
        score += 3
    elif client.age >= 40:
        score += 2
    # Gender scoring
    if client.gender.lower() == "female":
        score += 1
    # Program scoring
    for prog in client.programs:
        name = prog.name.lower()
        if "hiv" in name:
            score += 4
        elif "tb" in name:
            score += 3
        elif "malaria" in name:
            score += 2
        else:
            score += 1
    return score

def get_risk_label(score: int) -> str:
    if score <= 3:
        return "🟢 Low Risk"
    elif score <= 6:
        return "🟡 Moderate Risk"
    else:
        return "🔴 High Risk"
