# -*- coding: utf-8 -*-
from fastapi.responses import JSONResponse
from fastapi import status


def error(message: dict, status_code: int = status.HTTP_404_NOT_FOUND) -> JSONResponse:
    return JSONResponse(content={
        'message': message,
        'code': status_code
    }, status_code=status_code)


class Error:
    NoteIsNotExists = error("This note is not exists", status.HTTP_204_NO_CONTENT)
    UserIsNotExists = error("This user is not exists", status.HTTP_204_NO_CONTENT)
    EmailWasUsed = error("This email is used", status.HTTP_409_CONFLICT)
    LoginWasUsed = error("This login is used", status.HTTP_409_CONFLICT)
    AccessDenied = error("Access denied", status.HTTP_403_FORBIDDEN)
