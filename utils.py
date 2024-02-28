import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def load_saved_artifacts():
    global __data_columns
    global __locations

    try:
        with open("vitu\model\columns.json", "r") as f:
            data = json.load(f)
            __data_columns = data.get('data_columns', [])
            __locations = __data_columns[3:] if __data_columns else []
    except Exception as e:
        print("Error loading data columns:", e)

    global __model
    if __model is None:
        try:
            with open('vitu\model\\banglore_home_prices_model.pickle', 'rb') as f:
                __model = pickle.load(f)
        except Exception as e:
            print("Error loading model:", e)

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

# Load artifacts
load_saved_artifacts()

# Retrieve and print location names
# locations = get_location_names()
# print(locations)
print(get_estimated_price('Indira Nagar',1000,2,3))
a="Indira Nagar"
print(__data_columns.index(a.lower()))