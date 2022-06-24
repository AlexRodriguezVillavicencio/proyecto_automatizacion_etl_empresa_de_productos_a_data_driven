import numpy as np

def imputacion_outliers_Precio(df):
    df_drop = df.drop_duplicates(df.columns[df.columns.isin(['IdProducto'])])
    for id in list(df_drop['IdProducto']):
        df_id = df[df.IdProducto == id]
        Q1 = df_id['Precio'].quantile(.25)
        Q3 = df_id['Precio'].quantile(.75)
        IQR = Q3 -Q1
        minimo = Q1 - 1.5 * IQR
        maximo = Q3 + 1.5 * IQR

        #capturamos las filas con outliers
        ubicacion_outliers = (df_id.Precio < minimo) | (df_id.Precio > maximo)

        #calculamos la media, descartando los outliers
        outlier = list(df_id[ubicacion_outliers].Precio)
        #descartamos los valores nulos en el calculo
        nulos = list(df_id[df_id.Precio.isna()].index)
        #calculo de la media sin nulos ni outliers
        media = (df_id.Precio.sum() - sum(outlier)) / (len(df_id) - len(outlier) -len(nulos))

        #reemplazando valores atipicos en el dataframe principal
        df.loc[list(df_id[ubicacion_outliers].index)] = round(media, 2)
    return df

def imputacion_nulos_precio_capa1(df):
    #imputación de valores faltantes de columna precio por columnas: IdProducto, IdProveedor, Fecha_Año
    for i in list(zip(*np.where(df['Precio'].isna()))):
        ii = i[0]
        pr = tuple(df.loc[ii,['IdProducto']])[0]
        po = tuple(df.loc[ii,['IdProveedor']])[0]
        fa = tuple(df.loc[ii,['Fecha_Año']])[0]
        media =df.loc[(df['IdProducto'] == pr) & 
                        (df['IdProveedor'] == po) & 
                        (df['Fecha_Año'] == fa)]
        df.loc[ii, ['Precio']] = media['Precio'].mean()
    return df

def imputacion_nulos_precio_capa2(df):
    #imputación de valores faltantes de columna precio por columnas: IdProducto, Fecha_Mes, Fecha_Año
    for i in list(zip(*np.where(df['Precio'].isna()))):
        ii = i[0]
        pr = tuple(df.loc[ii,['IdProducto']])[0]
        po = tuple(df.loc[ii,['Fecha_Mes']])[0]
        fa = tuple(df.loc[ii,['Fecha_Año']])[0]
        media =df.loc[(df['IdProducto'] == pr) & 
                        (df['Fecha_Mes'] == po) & 
                        (df['Fecha_Año'] == fa)]
        df.loc[ii, ['Precio']] = media['Precio'].mean()
    return df

def imputacion_nulos_precio_capa3(df):
    #imputación de valores faltantes de columna precio por columnas: IdProducto, IdProveedor, Fecha_Año
    for i in list(zip(*np.where(df['Precio'].isna()))):
        ii = i[0]
        pr = tuple(df.loc[ii,['IdProducto']])[0]
        po = tuple(df.loc[ii,['IdProveedor']])[0]
        media =df.loc[(df['IdProducto'] == pr) & 
                        (df['IdProveedor'] == po)]
        df.loc[ii, ['Precio']] = media['Precio'].mean()
    return df

def imputacion_nulos_precio_capa4(df):
    #imputación de valores faltantes de columna precio por columnas: IdProducto, Fecha_Año
    for i in list(zip(*np.where(df['Precio'].isna()))):
        ii = i[0]
        pr = tuple(df.loc[ii,['IdProducto']])[0]
        po = tuple(df.loc[ii,['Fecha_Año']])[0]
        media =df.loc[(df['IdProducto'] == pr) & 
                        (df['Fecha_Año'] == po)]
        df.loc[ii, ['Precio']] = media['Precio'].mean()
    return df

def imputacion_nulos_cantidad(df):
    #imputación de valores faltantes de columna precio por columnas: IdProducto, Fecha_Año
    for i in list(zip(*np.where(df['Precio'].isna()))):
        ii = i[0]
        pr = tuple(df.loc[ii,['IdProducto']])[0]
        po = tuple(df.loc[ii,['Fecha_Año']])[0]
        media =df.loc[(df['IdProducto'] == pr) & 
                        (df['Fecha_Año'] == po)]
        df.loc[ii, ['Precio']] = media['Precio'].mean()
    return df



def imputacion_nulos_str_clientes(df):
    #Reemplazamos los valores nulos
    df.fillna({'Provincia':'Sin Dato', 'Nombre_Apellido':'Sin Dato',
                    'Domicilio':'sin Dato', 'Telefono':'Sin Dato',
                    'Localidad':'Sin dato', 'Longitud':'0', 'Latitud':'0'}, inplace=True)
    return df



def imputacion_outliers_Monto(df):
    df_drop = df.drop_duplicates(df.columns[df.columns.isin(['IdTipoGasto'])])
    for id in list(df_drop['IdTipoGasto']):
        df_id = df[df.IdTipoGasto == id]
        Q1 = df_id['Monto'].quantile(.25)
        Q3 = df_id['Monto'].quantile(.75)
        IQR = Q3 -Q1
        minimo = Q1 - 1.5 * IQR
        maximo = Q3 + 1.5 * IQR

        #capturamos las filas con outliers
        ubicacion_outliers = (df_id.Monto < minimo) | (df_id.Monto > maximo)

        #calculamos la media, descartando los outliers
        outlier = list(df_id[ubicacion_outliers].Monto)
        #descartamos los valores nulos en el calculo
        nulos = list(df_id[df_id.Monto.isna()].index)
        #calculo de la media sin nulos ni outliers
        media = (df_id.Monto.sum() - sum(outlier)) / (len(df_id) - len(outlier) -len(nulos))

        #reemplazando valores atipicos en el dataframe principal
        df.loc[list(df_id[ubicacion_outliers].index)] = round(media, 2)
    return df

def imputacion_nulos_monto_capa1(df):
    for i in list(zip(*np.where(df['Monto'].isna()))):
        ii = i[0]
        pr = tuple(df.loc[ii,['IdSucursal']])[0]
        po = tuple(df.loc[ii,['Fecha']])[0]
        media =df.loc[(df['IdSucursal'] == pr) & 
                        (df['Fecha'] == po) ]
        df.loc[ii, ['Monto']] = media['Monto'].mean()
    return df

def imputacion_nulos_monto_capa2(df):
    for i in list(zip(*np.where(df['Monto'].isna()))):
        ii = i[0]
        pr = tuple(df.loc[ii,['IdSucursal']])[0]
        media =df.loc[(df['IdSucursal'] == pr)]
        df.loc[ii, ['Monto']] = media['Monto'].mean()
    return df



def imputacion_nulos_precio_capa5(df):
    for i in list(zip(*np.where(df['Precio'].isna()))):
        ii = i[0]
        pr = tuple(df.loc[ii,['IdProducto']])[0]
        po = tuple(df.loc[ii,['IdSucursal']])[0]
        media =df.loc[(df['IdProducto'] == pr) & 
                        (df['IdSucursal'] == po)]
        df.loc[ii, ['Precio']] = media['Precio'].mean()
    return df

def imputacion_nulos_precio_capa6(df):
    #imputación de valores faltantes de columna precio por columnas: IdProducto, Fecha_Mes, Fecha_Año
    for i in list(zip(*np.where(df['Precio'].isna()))):
        ii = i[0]
        pr = tuple(df.loc[ii,['IdProducto']])[0]
        media =df.loc[(df['IdProducto'] == pr)]
        df.loc[ii, ['Precio']] = media['Precio'].mean()
    return df
