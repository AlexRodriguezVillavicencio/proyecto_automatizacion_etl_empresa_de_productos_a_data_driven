from models import imputacion_outliers_Precio 
from models import imputacion_nulos_precio_capa1
from models import imputacion_nulos_precio_capa2 
from models import imputacion_nulos_precio_capa3
from models import imputacion_nulos_precio_capa4
from models import imputacion_nulos_str_clientes

from models import imputacion_outliers_Monto
from models import imputacion_nulos_monto_capa1
from models import imputacion_nulos_monto_capa2

from models import imputacion_nulos_precio_capa5
from models import imputacion_nulos_precio_capa6

#limpieza de los datos
def transform_compra(df):
    df.drop_duplicates(inplace=True)
    imputacion_outliers_Precio(df)
    imputacion_nulos_precio_capa1(df)
    imputacion_nulos_precio_capa2(df)
    imputacion_nulos_precio_capa3(df)
    imputacion_nulos_precio_capa4(df)
    return df 

def transform_gasto(df):
    df.drop_duplicates(inplace=True)
    imputacion_outliers_Monto(df)
    imputacion_nulos_monto_capa1(df)
    imputacion_nulos_monto_capa2(df)
    return df

def transform_venta(df):
    df.drop_duplicates(inplace=True)
    imputacion_outliers_Precio(df)
    imputacion_nulos_precio_capa5(df)
    imputacion_nulos_precio_capa6(df)
    return df

def transform_clientes(df):
    df.drop_duplicates(inplace=True)
    imputacion_nulos_str_clientes(df)
    df['Provincia'] = df['Provincia'].str.title()
    df['Nombre_Apellido'] = df['Nombre_Apellido'].str.title()
    df['Domicilio'] = df['Domicilio'].str.capitalize()
    df['Localidad'] = df['Localidad'].str.title()
    df['Provincia'] = df['Provincia'].str.replace("Ciudad De Buenos Aires", "Buenos Aires")
    df['Longitud'] = df['Longitud'].str.replace(",", ".")
    df['Latitud'] = df['Latitud'].str.replace(",", ".")
    return df

def transform_canal_venta(df):
    df.drop_duplicates(inplace=True)
    return df

def transform_tipo_gasto(df):
    df.drop_duplicates(inplace=True)
    return df

def transform_proveedores(df):
    df.drop_duplicates(inplace=True)
    df.fillna({'Nombre':'Sin Dato', 'Address':'Sin Dato',
                'City':'sin Dato', 'State':'Sin Dato',
                'Country':'Sin dato', 'departamen':'Sindato'}, inplace=True)
    df['Nombre'] = df['Nombre'].str.title()
    df['Address'] = df['Address'].str.capitalize()
    df['City'] = df['City'].str.title()
    df['State'] = df['State'].str.title()
    df['Country'] = df['Country'].str.title()
    df['departamen'] = df['departamen'].str.title()
    return df

def transform_sucursales(df):
    df.drop_duplicates(inplace=True)
    df.fillna({'Sucursal':'Sin Dato', 'Direccion':'Sin Dato',
                'Localidad':'sin Dato', 'Provincia':'Sin Dato',
                'Longitud':'0', 'Latitud':'0'}, inplace=True)
    df['Longitud'] = df['Longitud'].str.replace(",", ".")
    df['Latitud'] = df['Latitud'].str.replace(",", ".")
    return df

def transform_localidades(df):
    df.drop_duplicates(inplace=True)
    return df
    
#Normalizacion de los datos en curso...