from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/webhook")
async def receive_event(payload: dict = Body(...)):
    with open("events.txt", "a") as file:
        file.write(str(payload) + "\n")

    return {"status": "received"}