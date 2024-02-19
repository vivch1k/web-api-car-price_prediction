from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from models.models import prediction


app = FastAPI(
    title='Сar predition price'
)

templates = Jinja2Templates(directory="venv/frontend")

class CarAttrib(BaseModel):
    Year : int
    Drivetrain : str
    Transmission : str
    FuelType : str
    MaxPower : float
    FuelTankCapacity : float
 

@app.get('/predict/', response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("test.html", {"request" : request})

@app.post('/predict/')
def predict_price(request: Request, year: int = Form(...), drivetrain: str = Form(...),
                   transmission: str = Form(...), fueltype: str = Form(...), 
                   horsepower: int = Form(...), fueltank: int = Form(...)):

    # global pred

    imput_dict = {'Year' : year, 'Drivetrain' : drivetrain,
                   'Transmission' : transmission, 'FuelType' : fueltype,
                     'MaxPower' : horsepower, 'FuelTankCapacity' : fueltank}

    Year = imput_dict['Year']
    Drivetrain = imput_dict['Drivetrain']
    Transmission = imput_dict['Transmission']
    FuelType = imput_dict['FuelType']
    MaxPower = imput_dict['MaxPower']
    FuelTankCapacity = imput_dict['FuelTankCapacity']

    pred = int(prediction([[Year, Drivetrain, Transmission, FuelType, MaxPower, FuelTankCapacity]]))


    return templates.TemplateResponse('test.html', context={'request': request, 'pred': pred})
    



