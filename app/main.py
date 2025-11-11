from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import generator

app = FastAPI(title="Blog Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

posts_cache = []

app.mount("/static", StaticFiles(directory="../static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    return "<html><body><a href='/static/blog.html'>Open Blog</a></body></html>"

@app.post("/api/generate")
async def generate_posts(payload: dict):
    """
    Payload format:
    { "items": [ {"title":"...","details":"optional short description"}, ... ] }
    Returns generated posts with bodies.
    """
    items = payload.get("items")
    if not items or not isinstance(items, list):
        raise HTTPException(400, "items must be a non-empty list")

    results = []
    for item in items:
        title = item.get("title")
        if not title:
            continue
        details = item.get("details", "")
        prompt = generator.compose_prompt(title, details)
        body = generator.call_gemini(prompt)
        summary = generator.summarize_short(body)
        
        post = {
            "title": title,
            "summary": summary,
            "body": body
        }
        results.append(post)
        posts_cache.append(post)
    
    return results

@app.get("/api/posts")
async def get_posts():
    return posts_cache