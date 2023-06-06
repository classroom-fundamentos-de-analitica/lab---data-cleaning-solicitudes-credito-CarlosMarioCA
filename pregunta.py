"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df = df.dropna()

    columns = df.columns.tolist()
    columns_to_format = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'línea_credito']

    for i in columns_to_format:
        df[i] = df[i].str.lower()
        df[i] = df[i].str.replace('-', ' ')
        df[i] = df[i].str.replace('_', ' ')

    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype('int64')

    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'],
                            infer_datetime_format=True,
                            errors='ignore',
                            dayfirst=True)
    
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].dt.strftime("%Y/%m/%d")
    df['monto_del_credito'] = df['monto_del_credito'].str.strip('$')
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',', '')
    df['monto_del_credito'] = df['monto_del_credito'].astype('float64')

    ind=df.columns.values.tolist()
    ind.remove('Unnamed: 0')
    df.drop_duplicates(subset=ind, inplace=True)
    return df

print(clean_data())