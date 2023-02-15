# -*- coding: utf-8 -*-
from os import path

import aiofiles
from fastapi import FastAPI, status
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from .mounts import user_app, note_app, desk_app
from .docs.autodocs import AutoDocs
from .config import DOCS_EXCEPTIONS, DOCS_ROOT, DOCS_TITLE, DOCS_MOUNTS, DOCS_MODELS


app = FastAPI(redoc_url=None, docs_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_headers=['*'],
    allow_origins=['*'],
    allow_methods=['*'],
    allow_credentials=True
)
DOCS_FILE = f'{DOCS_ROOT}/index.html'

app.mount('/user', user_app)
app.mount('/note', note_app)
app.mount('/desk', desk_app)

AutoDocs.generate(
    root=f'{DOCS_ROOT}/',
    title=DOCS_TITLE,
    models=DOCS_MODELS,
    methods=DOCS_MOUNTS,
    exceptions=DOCS_EXCEPTIONS
)


@app.get('/docs')
async def get_api_doc():
    if path.exists(DOCS_FILE) and path.isfile(DOCS_FILE):
        async with aiofiles.open(DOCS_FILE, 'r', encoding='utf-8') as f:
            content = await f.read()
        return HTMLResponse(content=content)
    return JSONResponse(
        content={'error': 'not found'},
        status_code=status.HTTP_404_NOT_FOUND
    )


@app.get('/backend/docs/{file:path}')
async def get_api_doc(file: str):
    file = f'{DOCS_ROOT}/{file}'
    print(file)
    if path.exists(file) and path.isfile(file):
        return FileResponse(path=file)
    return JSONResponse(
        content={'error': 'not found'},
        status_code=status.HTTP_404_NOT_FOUND
    )
