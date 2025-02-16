from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import api_router  # Assuming this is where your `books` routes are included

app = FastAPI()

# Add middleware for CORS if necessary
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router with the '/api/v1' prefix
app.include_router(api_router, prefix="/api/v1")

@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}
