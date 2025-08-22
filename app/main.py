from fastapi import FastAPI

__version__ = "0.2.0"

app = FastAPI(title="GitFlow Example API", version=__version__)

@app.get("/")
def root():
    return {"message": f"Hello world! This is version {__version__}."}

@app.get("/version")
def get_version():
    return {"version": __version__}
