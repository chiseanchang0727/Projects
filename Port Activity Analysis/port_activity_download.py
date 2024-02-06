import pandas as pd
import requests
from datetime import datetime
from sqlalchemy import create_engine


def load_data(start_year, end_year):
    url = 'https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Trade_Data/FeatureServer/0/query?where=year%20%3E%3D%20'+str(start_year)+'%20AND%20year%20%3C%3D%20'+str(end_year)+'&outFields=*&outSR=&f=json'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        features = data.get('features', [])
        
        attribute_list = [feature['attributes'] for feature in features]
        
        df = pd.DataFrame(attribute_list)
        
        df['date'] = pd.to_datetime(df['date'], unit='ms')
        
    else:
        print('no response.')
        
    return df


def export_data(df, connection_str, table_name, method):

    engine = create_engine(connection_str)
    
    df.to_sql(name=table_name, con=engine, if_exists=method, index=False)
    
    
if __name__ == '__main__':
    
    start_year = 2019
    end_year = datetime.today().year
    
    df_concat = pd.DataFrame()
    for i in range(start_year, end_year, 2):
        df_temp = load_data(i, i+1)
        df_concat = pd.concat([df_concat, df_temp], axis=0)
        
    df_concat['import_time'] = datetime.now()
    
    username = 'seanc'
    password = '!QAZ2wsx'
    hostname = '127.0.0.1'
    database_name = 'generaldb'
    connection_string = f'mysql+pymysql://{username}:{password}@{hostname}/{database_name}'
    export_data(df_concat, connection_string, 'port_activity', 'replace')