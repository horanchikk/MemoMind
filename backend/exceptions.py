# -*- coding: utf-8 -*-
from fastapi.responses import JSONResponse
from fastapi import status


def error(message: dict, status_code: int = status.HTTP_404_NOT_FOUND) -> JSONResponse:
    return JSONResponse(content={
        'message': message,
        'code': status_code
    }, status_code=status_code)


class Error:
    EmailWasUsed = error("This email is used", status.HTTP_403_FORBIDDEN)
