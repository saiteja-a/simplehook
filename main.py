from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def receive_event(request: Request):
    payload = await request.json()

    with open("events.txt", "a") as file:
        file.write(str(payload) + "\n")

    return {"status": "received"}

