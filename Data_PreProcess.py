import pandas as pd
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


def preprocessing():
    num_features = ["mileage","tax","mpg","enginesize","year"]
    cat_features = ["model","transmission","fueltype"]

    num_pipeline = Pipeline([
        ("scaler",StandardScaler())
    ])
    cat_pipeline = Pipeline([
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer([
        ("num",num_pipeline,num_features),
        ("cat",cat_pipeline,cat_features)
    ])

    return preprocessor

