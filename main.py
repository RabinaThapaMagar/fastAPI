from fastapi import  FastAPI

app = FastAPI() 

@app.get('/')## route banako mathiko app object use garera
def show(): ## show vaney function
    return{'message': 'Hello Guys'}



@app.get('/about')
def about():
    return{'Display':'Broad AI is a education Sector'}