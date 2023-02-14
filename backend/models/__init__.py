# -*- coding: utf-8 -*-
from pydantic import BaseModel


class SignUpUser:
    email: str
    login: str
    password: str
