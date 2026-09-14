from fastapi import APIRouter

from schema.login_schema import (
    RegRequest,
    LoginRequest,
    ChangePasswordRequest
)

from database.mongo import users_collection

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(data: RegRequest):

    existing_user = users_collection.find_one(
        {"email": data.email}
    )

    if existing_user:
        return {
            "msg": "User already exists"
        }

    users_collection.insert_one(
        {
            "student_id": data.student_id,
            "username": data.username,
            "email": data.email,
            "password": data.password
        }
    )

    return {
        "msg": "Registration successful"
    }


@router.post("/login")
def login(data: LoginRequest):

    exist_user = users_collection.find_one(
        {"email": data.email}
    )

    if not exist_user:
        return {
            "msg": "Invalid email"
        }

    if data.password != exist_user["password"]:
        return {
            "msg": "Password is wrong"
        }

    return {
        "msg": "Login successful",
        "student_id": exist_user["student_id"],
        "username": exist_user["username"],
        "email": exist_user["email"]
    }


@router.get("/user/{email}")
def get_user(email: str):

    exist_user = users_collection.find_one(
        {"email": email}
    )

    if not exist_user:
        return {
            "msg": "Invalid email"
        }

    return {
        "student_id": exist_user["student_id"],
        "username": exist_user["username"],
        "email": exist_user["email"]
    }


@router.put("/changepass")
def change_password(
    email: str,
    data: ChangePasswordRequest
):

    exist_user = users_collection.find_one(
        {"email": email}
    )

    if not exist_user:
        return {
            "msg": "Account does not exist"
        }

    users_collection.update_one(
        {"email": email},
        {
            "$set": {
                "password": data.new_password
            }
        }
    )

    return {
        "msg": "Password changed successfully"
    }