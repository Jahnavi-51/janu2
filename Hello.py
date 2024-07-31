from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from Database import engine,Sessionlocal
from Models import Base, User
from schema import UserSchema

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = Sessionlocal()
        yield db
    finally:
        db.close()

@app.post("/adduser")
def add_user(request: UserSchema, db: Session = Depends(get_db)):
    user = User( Name=request.Name, Email=request.Email, Nickname=request.Nickname)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/user/{user_name}")
def get_users(user_name,db: Session= Depends(get_db)):
    users = db.query(User).filter(User.Name == user_name).first()
    return users

# @app.get("/user/{user_id}")
# def get_users(user_id : int,db: Session=Depends(get_db)):
#     users = db.query(User).filter(User.Id == user_id)
#     return users

# @app.put("/user/{user_name}")
# def update(us_id : int , us : Us,db:Session=Depends(get_db)):

    #     if employ_id not in emp:
    #         return {"employee doesn't exist"}
    #     emp[employ_id] = employ
    #     return "updated Successfully!!!"
