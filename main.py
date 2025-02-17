from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi_versioning import VersionedFastAPI, version
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from pydantic import BaseModel
import redis
import uvicorn
import services

app = FastAPI(
    title="Alias Generator",
    description="Boilerplate setup with CORS, Rate Limiting, and API Versioning",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://alias-generator-e636b.web.app"],  # Use specific domains in prod
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    print("Registered routes:")
    for route in app.routes:
        print(f"{route.path} ({route.methods})")

class AliasRequest(BaseModel):
    first_name: str
    last_name: str

class AliasResponse(BaseModel):
    first_name: str
    last_name: str
    alias: str

@app.post("/get-random-alias")
@version(1)
async def get_random_alias(alias_request: AliasRequest):
    try:
        first_name = alias_request.first_name
        last_name = alias_request.last_name
        
        alias = services.generate_random_alias(first_name, last_name)
        
        return {
            "success": True,
            "firstName": first_name,
            "lastName": last_name,
            "alias": alias
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            "success": False,
            "message": str(e)
        }        

# app = VersionedFastAPI(app, version_format="{major}", prefix_format="/v{major}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
