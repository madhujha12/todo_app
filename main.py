# uvicorn main:blog --reload
from fastapi import FastAPI,status,HTTPException
from sqlalchemy import create_engine, Column, Integer, String,text
from sqlalchemy.ext.declarative import declarative_base
import mysql.connector
from mysql.connector import errorcode

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import List



todo_api = FastAPI()

security = HTTPBasic()

todos = []
username = "madhu"
password = "2005"


# CREATE,UPDATE AND DELETE_OPERATION_USING_Fast API:

#CREATE DATA USING POST:
cnx = mysql.connector.connect(user='madhu',password='2005',host='localhost',database='my_todo')

class User(BaseModel):
    task:str
    due_date:str
    status:str


@todo_api.post("/create/todo")
# def create_todo(todo: TodoCreate, credentials: HTTPBasicCredentials = Depends(security)):
async def create_data(user: User,credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username == username and credentials.password == password:
        cursor = cnx.cursor()
        query = "INSERT INTO todo (task,due_date,status) VALUES (%s,%s, %s)"
        values = (user.task, user.due_date,user.status)
        cursor.execute(query, values)
        cnx.commit()
        return {"message": "todo created successfully"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")





# #UPDATE DATA USING PUT METHOD:

mydb=mysql.connector.connect(user='madhu',password='2005',host='localhost',database='my_todo')
# class TodoUpdate(BaseModel):
#     task: str
#     due_date: str
#     status: str

@todo_api.put("/api/todo/update/{id}")
# def update_todo(todo_id: int, todo: TodoUpdate, credentials: HTTPBasicCredentials = Depends(security)):
async def update_data(id: int, task:str,credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username == username and credentials.password == password:
        table_name = "todo"  # Replace with the actual table name
        query = f"SELECT COUNT(*) FROM {table_name}"
        cursor=mydb.cursor()
        cursor.execute(query)

        result = cursor.fetchone()
        table_length = result[0]
        print(table_length)
        if 0 <= id <=table_length:
            cursor = mydb.cursor()
            sql = "UPDATE todo SET task = %s WHERE id = %s"
            val = (task, id)
            cursor.execute(sql, val)
            mydb.commit()
            return {"message": "todo_data updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Todo not found")
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")



# #DELETE DATA USING DELETE METHOD:

mydb=mysql.connector.connect(user='madhu',password='2005',host='localhost',database='my_todo')
@todo_api.delete("/delete_data/{id}")
async def delete_data(id: int):
    cursor = mydb.cursor()
    sql = "DELETE FROM todo WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    mydb.commit()
    return {"message": "todo_Data deleted successfully"}
