from fastapi import FastAPI, Query, HTTPException, Request
from user_details_model import UserDetails
import uuid

app = FastAPI()

list_of_users = []
letters = "abcdefghijklmnopqrstuvwxyz"

@app.post("/user")
async def add_user(user_details:UserDetails):
    if (len(user_details.firstName) > 3 and len(user_details.lastName) > 3 ):
        if (user_details.firstName.isalpha() or user_details.lastName.isalpha()):
            full_name = f'{user_details.firstName} {user_details.lastName}'
            list_of_users.append(full_name)
            return {"FullName":f"{user_details.firstName} {user_details.lastName}"}
        else:
            return {"message": "Name cannot contain numeric data"}
    else:
        return {"message": "length of firstname and lastname must be greater than 3"}


@app.get("/details")
async def get_details():
    if len(list_of_users) > 0:
        return {"list_of_users":list_of_users}

@app.get("/getUid")
async def set_uid():
    new_users_list = []
    for i in range(0, len(list_of_users)):
        random_uuid = uuid.uuid4()
        uuid_appended = f'{list_of_users[i]} {random_uuid}'
        new_users_list.append(uuid_appended)
    return {"list_of_users_with_uuid":new_users_list}
    

