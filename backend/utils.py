# -*- coding: utf-8 -*-
from fastapi import Request


async def get_body(req: Request):
    body = await req.body()

    async def receive():
        return {'type': 'http.request', 'body': body}

    req._receive = receive
    return body
