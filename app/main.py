from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
from app.schemas.error import ValidationError
from app.core.config import settings
from app.db.redis import redisFeed, stream_messages

app = FastAPI(
    title=settings.TITLE,
    responses={422: {"description": "Validation Error", "model": ValidationError}},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, e):
    errors = []
    for error in e.errors():
        error_obj = {"path": error["loc"][1], "msg": error["msg"]}
        errors.append(error_obj)
    return JSONResponse(content={"errors": errors}, status_code=422)


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse("/docs")


@app.get("/subscribe/{channel}")
async def subscribe_to_event(channel):
    print(f"Connection established on {channel}")
    response = EventSourceResponse(stream_messages(channel))
    response.headers.update(
        {
            "Content-Type": "text/event-stream",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )

    return response
