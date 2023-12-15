import re
import pandas as pd
from utils import extract_info

def preprocess(input_string):
    # Get the data
    data = extract_info(input_string)
        
    # Convert dict to DataFrame
    df = pd.DataFrame(data)
    
    df.user = df.user.apply(lambda x: "~" if x == "" else x)  
    
    df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d, %H:%M:%S") 
    df["month"] = df.date.dt.month_name()
    df["day_of_the_month"] = df.date.dt.day
    df["hour"] = df.date.dt.hour
    df["minute"] = df.date.dt.minute
    return df