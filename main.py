from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
async def serve(action: str, email: str):
    sequence_number = 10
    return Response(content=f"{sequence_number} OK\n{action} {email}")
