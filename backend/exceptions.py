# -*- coding: utf-8 -*-
from fastapi.responses import JSONResponse
from fastapi import status


def error(message: dict, status_code: int = status.HTTP_404_NOT_FOUND) -> JSONResponse:
    return JSONResponse(content={
        'message': message,
        'code': status_code
    }, status_code=status_code)


class Error:
    NoteIsNotExists = error("This note is not exists", status.HTTP_404_NOT_FOUND)
    UserIsNotExists = error("This user is not exists", status.HTTP_404_NOT_FOUND)
    DeskIsNotExists = error("This desk is not exists", status.HTTP_404_NOT_FOUND)
    EmailWasUsed = error("This email is used", status.HTTP_409_CONFLICT)
    LoginWasUsed = error("This login is used", status.HTTP_409_CONFLICT)
    NoteNameIsExits = error("This note name already is used", status.HTTP_409_CONFLICT)
    DeskNameIsExits = error("This desk name already is used", status.HTTP_409_CONFLICT)
    AccessDenied = error("Access denied", status.HTTP_403_FORBIDDEN)
    LoginOrPasswordIsNotCorrect = error("Login or password is not correct.", status.HTTP_400_BAD_REQUEST)
    PasswordIsNotCorrect = error("Password is not correct", status.HTTP_400_BAD_REQUEST)
    IndexError = error("Index error", status.HTTP_400_BAD_REQUEST)
    TitleIsEmpty = error("Title is empty", status.HTTP_400_BAD_REQUEST)
    NoteCantStartsWithId = error("Note name can not starts with 'id'.", status.HTTP_400_BAD_REQUEST)
    DeskCantStartsWithId = error("Desk name can not starts with 'id'.", status.HTTP_400_BAD_REQUEST)
