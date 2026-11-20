from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/summarize")
async def summarize(input: TextInput) -> Dict[str, int]:
    """
    Returns the word count of the input text.
    """
    word_count = len(input.text.split())
    return {"word_count": word_count}

@app.post("/summarize/strict")
async def summarize_strict(input: TextInput) -> Dict[str, int]:
    """
    Returns the word count, raising 422 if text is empty or whitespace-only.
    """
    if not input.text.strip():
        raise HTTPException(status_code=422, detail="text must not be empty or whitespace")
    word_count = len(input.text.split())
    return {"word_count": word_count}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
