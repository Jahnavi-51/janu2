import asyncio
from fastapi import FastAPI,Path,BackgroundTasks

app = FastAPI()
users = {
    1:{
        "Name ":"Jaanu",
        "Role ":"Student"
    },
    2:{
        "Name ":"Sruthi",
        "Role ":"Student"
    }
}
async def task_1():
    await asyncio.sleep(10)
    print("Task 1 is completed")
async def task_2():
    await asyncio.sleep(10)
    print("Task 2 is completed")
@app.get("/run_tasks")
async def run_tasks(b_task:BackgroundTasks):
    b_task.add_task(task_1)
    b_task.add_task(task_2)
    return "Task was scheduled!!!"
@app.get("/Users/{user_id}")
async def get_user(user_id:int):
    if user_id in users:
        return users[user_id]
    return "User not found"




