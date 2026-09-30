from decimal import Decimal

typeDicc = {
    "Ingreso": {
        "Familia": 1,
        "Other":2
    },
    "Alimento": {
        "Snack":8,
        "FastFood": 7
    },
    "Transporte":{
        "Ride":10,
        "SUBE":9
    },
    "Salud": 11,
    "Supermercado": 26,
    "Comisión": 25,
    "Servicios":{
        "Youtube Music": 20,
        "Internet": 21,
        "Gas": 22,
        "Luz": 23,
        "Agua": 24
    },
    "Entretenimiento":{
        "Cine": 12,
        "Drink": 14,
        "Fair": 7
    },
    "API": 19,
    "Material":{
        "Universidad": 15,
        "CD": 16,
        "Tech": 17,
        "Ropa": 18,
        "Regalo": 27,
        "Varios": 28
    }
}

## Transporte puede ser Didi o Subte, es Didi si es mayor a $2400
## En el CSV solo exite la terapia como salud
## Solo uso DeepSeek API xd ((Por ahora))
## Nunca fui a un restaurante que no sea de comida rápida :(
## La idea es poder elegir entre tipos por el front


## Casos de Variables

def resolveIngreso (description:str):
    if "mamá" in description.lower() or "hermana" in description.lower():
        return typeDicc["Ingreso"]["Snack"]
    else:
        return typeDicc["Ingreso"]["Other"]

def resolveFood (amount:Decimal):
    if(amount<5000):
        return typeDicc["Alimento"]["Snack"]
    else:
        return typeDicc["Alimento"]["FastFood"]

def resolveTransporte(amount:Decimal):
    if(amount<2000):
        return typeDicc["Transporte"]["SUBE"]
    else:
        return typeDicc["Transporte"]["Ride"]
    
def resolveServices(description:str):
    if "gas" in description.lower():
        return typeDicc["Servicios"]["Gas"]
    if "edesur" in description.lower():
        return typeDicc["Servicios"]["Luz"]
    if "aysa" in description.lower():
        return typeDicc["Servicios"]["Agua"]
    if "youtube" in description.lower():
        return typeDicc["Servicios"]["Youtube Music"]
    else:
        return typeDicc["Servicios"]["Internet"]
    
def resolveEntertaiment(description:str):
    if "fernet" in description.lower():
        return typeDicc["Entretenimiento"]["Drink"]
    if "cine" in description.lower():
        return typeDicc["Entretenimiento"]["Cine"]
    else:
        return typeDicc["Entretenimiento"]["Fair"]
    
def resolveMaterial(description:str):
    if "regalo" in description.lower():
        return typeDicc["Material"]["Regalo"]
    if "album" in description.lower():
        return typeDicc["Material"]["CD"]
    else:
        return typeDicc["Material"]["Varios"]


## Funcion principal

def convertTypeToID (amount:Decimal, description:str, type: str):
    if(type == "Ingreso"):
        return resolveIngreso(description)
    if(type == "Alimento"):
        return resolveFood(amount)
    if(type == "Transporte"):
        return resolveTransporte(amount)
    if(type == "Servicios"):
        return resolveServices(description)
    if(type == "Entretenimiento"):
        return resolveEntertaiment(description)
    if(type == "Material"):
        return resolveMaterial(description)
    try:
        return typeDicc[type]
    except:
        return 0