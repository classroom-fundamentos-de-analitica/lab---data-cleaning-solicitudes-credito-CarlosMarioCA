"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd
import re
from datetime import *

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)
    df = df.dropna()
    df.drop_duplicates(inplace=True)

    columns = df.columns.tolist()
    columns_to_format = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'línea_credito']

    for i in columns_to_format:
        df[i] = df[i].str.lower()
        df[i] = df[i].str.replace('-', ' ')
        df[i] = df[i].str.replace('_', ' ')

    df["barrio"] = df["barrio"].str.replace(". ",".")

    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype('int64')

    df["fecha_de_beneficio"] = [datetime.strptime(date, "%d/%m/%Y") if bool(re.search(r"\d{1,2}/\d{2}/\d{4}", date))
                             else datetime.strptime(date, "%Y/%m/%d")
                             for date in df.fecha_de_beneficio]
    
    df['monto_del_credito'] = df['monto_del_credito'].apply(lambda x: 
                int(x.replace('$', '').replace(',', '').replace(".0","")))

    return df

print(clean_data())
