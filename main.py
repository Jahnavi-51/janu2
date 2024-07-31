from typing import Union,Optional
from fastapi import FastAPI, Path ,HTTPException
from pydantic import BaseModel
app = FastAPI()

# class Emp(BaseModel):
#     name: str
#     role: str
# # class Employee(BaseModel):
# #     name: Optional[str] = None
# #     role: Optional[str] = None
# emp = {
#     1:{
#         "name": "jaanu",
#         "role": "tester"
#     },
#     2:{
#         "name": "vasu",
#         "role": "wastefellow"
#     },
#     3:{
#         "name": "likki",
#         "role": "developer"
#     },
#     4:{
#         "name": "sai",
#         "role": "admin"
#     }
# }
# @app.get("/basic")
# def test():
#     return {"Test": "Manual input"}
# @app.get("/test/{emp_id}")
# def test(emp_id:int):
#      if emp_id in emp:
#          return emp[emp_id]
#      return "Data Not found"
# @app.get("/query/{empl_id}")
# def get_by_query(empl_id:int, name:str):
#     for empl_id in emp:
#         if emp[empl_id]["name"] == name:
#             return emp[empl_id]
#         return " name not found"
#     return "data not found"
#
# @app.post("/post/{employ_id}")
# def create(employ_id:int,employ:Emp):
#     if employ_id in emp:
#         return "employee is already exits!!!"
#     emp[employ_id] = employ
#     return emp
#
# @app.put("/update/{employ_id}")
# def update(employ_id:int,employ:Emp):
#     if employ_id not in emp:
#         return {"employee doesn't exist"}
#     emp[employ_id] = employ
#     return "updated Successfully!!!"
# # @app.put("/update1/{empl_id}")
# # def update(empl_id:int,empl:Employee):
# #     if empl_id not in emp:
# #         return "Employee Doesn't exist!!!"
# #     emp[empl_id] = empl
# #     return "updated succesfully"
# @app.delete("/delete/{emp_id}")
# def delete_emp(emp_id:int):
#     if emp_id not in emp:
#         return "Employee Doesn't existed"
#     del emp[emp_id]
#     return "emp Deleted"

class Student(BaseModel):
    name : str
    branch : str
class Student1(BaseModel):
    name : Optional[str] == None
    branch : Optional[str] == None
stu = {
    1:{
        "name":"janu",
        "branch":"IT"
    },
    2:{
        "name":"vasu",
        "branch":"IT"
    },
    3:{
        "name":"likki",
        "branch":"CSE"
    }
}
# running
@app.get("/test1/{stu_id}")
def test1(stu_id:int):
    if stu_id in stu:
        return f"Data Found!!!{stu[stu_id]}"
    return "Data Not Found"

@app.get("/test2/{stu_id}")
def test2(stu_id:int, name:str):
    if stu_id in stu:
        if stu[stu_id]["name"] == name:
            return stu[stu_id]
        return "name not found"
    return "data not found"
# @app.get("/test3/{stu_id}")
# def test3(stu_id: int, name: str):
#     try:
#         if not isinstance(stu, dict):
#             raise HTTPException(status_code=500, detail="Internal Error: 'stu' is not a dictionary")
#
#         if stu_id in stu:
#             student = stu[stu_id]
#             if not isinstance(student, dict):
#                 raise HTTPException(status_code=500, detail="Internal Error: 'student' is not a dictionary")
#             if student["name"] == name:
#                 return student
#             raise HTTPException(status_code=404, detail="name not found")
#         raise HTTPException(status_code=404, detail="data not found")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
@app.post("/post/{stud_id}")
def create(stud_id:int,stud:Student):
    if stud_id in stu:
        return "Student is already exits!!!"
    stu[stud_id] = stud
    return stu

@app.put("/change/{stud_id}")
def change(stud_id:int,stud:Student):
    if stud_id in stu:
        stu[stud_id] = stud
        return stu
    return "Student not exist"
@app.put("/update/{stud_id}")
def update(stud_id:int,stud:Student1):
    if stud_id in stu:
        stu[stud_id] = stud
        return stu
    return "Student not exist"

@app.delete("/delete/{stud_id")
def delete(stud_id):
    if stud_id in stu:
        del stu[stud_id]
        return stu
    return "student not exist"
