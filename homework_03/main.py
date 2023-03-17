from fastapi import FastAPI


app = FastAPI ()

@app.get('/')
def read_root():
    return {'Hello':'world!'}


@app.get('/ping/')
def ping():
    return  {"message": "pong"}
