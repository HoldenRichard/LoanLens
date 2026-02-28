from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import db
from typing import Annotated
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(
        "login.jinja",
        {"request": request,}
    )

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(
    request: Request,
    # The 'get_current_user' function extracts the Kinde ID from the token
    current_user: Annotated[dict, Depends(get_current_user)]
):
    # 1. Access the user's unique ID from the Kinde token
    kinde_id = current_user.get("id")

    # 2. Query your DB using ONLY this ID
    # example: user_data = db.query(User).filter(User.kinde_id == kinde_id).first()
    
    return templates.TemplateResponse(
        "dashboard.jinja", 
        {
            "request": request, 
            "user": current_user  # Pass the Kinde info to the frontend
        }
    )

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
