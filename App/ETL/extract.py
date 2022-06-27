import pandas as pd
from utils import sep_detected, encoding_detected


def carga_archivo(filename):

    sep = sep_detected(filename)
    encoding= encoding_detected(filename)

    df = pd.read_csv(filename, sep=sep, encoding=encoding)
    #eliminando las columnas vacias
    column_drop = [column for column in df if df[column].isna().sum() == df.shape[0]]
    df.drop(column_drop, axis=1, inplace=True)
    
    compra = ['IdCompra', 'Fecha', 'Fecha_Año', 'Fecha_Mes', 'Fecha_Periodo',
       'IdProducto', 'Cantidad', 'Precio', 'IdProveedor']
    gasto = ['IdGasto', 'IdSucursal', 'IdTipoGasto', 'Fecha', 'Monto']
    localidades = ['categoria', 'centroide_lat', 'centroide_lon', 'departamento_id',
       'departamento_nombre', 'fuente', 'id', 'localidad_censal_id',
       'localidad_censal_nombre', 'municipio_id', 'municipio_nombre', 'nombre',
       'provincia_id', 'provincia_nombre']
    proveedores = ['IDProveedor', 'Nombre', 'Address', 'City', 'State', 'Country',
       'departamen']
    sucursales = ['ID', 'Sucursal', 'Direccion', 'Localidad', 'Provincia', 'Latitud',
       'Longitud']
    venta = ['IdVenta', 'Fecha', 'Fecha_Entrega', 'IdCanal', 'IdCliente',
       'IdSucursal', 'IdEmpleado', 'IdProducto', 'Precio', 'Cantidad']
    clientes = ['ID', 'Provincia', 'Nombre_y_Apellido', 'Domicilio', 'Telefono', 'Edad',
       'Localidad', 'X', 'Y']
    canal_venta = ['CODIGO','DESCRIPCION'] 
    tipo_gasto = ['IdTipoGasto', 'Descripcion', 'Monto_Aproximado']

    if list(df.columns) == gasto :
        df.drop(['IdGasto'], axis=1,inplace=True)
        print('es una tabla de gasto')
        return df
    elif list(df.columns) == compra :
        df.drop(['IdCompra'], axis=1,inplace=True)
        print('es una tabla de compra')
        return df
    elif list(df.columns) == localidades :
        df.drop(['id'], axis=1,inplace=True)
        print('es una tabla de localidades')
        return df
    elif list(df.columns) == proveedores :
        df.drop(['IDProveedor'], axis=1,inplace=True)
        print('es una tabla de proveedores')
        return df
    elif list(df.columns) == sucursales :
        df.drop(['ID'], axis=1,inplace=True)
        print('es una tabla de sucursales')
        return df
    elif list(df.columns) == venta :
        df.drop(['IdVenta'], axis=1,inplace=True)
        print('es una tabla de venta')
        return df
    elif list(df.columns) == clientes :
        df.drop(['ID'], axis=1,inplace=True)
        print('es una tabla de clientes')
        return df
    elif list(df.columns) == canal_venta :
        print('es una tabla de canal_venta')
        return df
    elif list(df.columns) == tipo_gasto :
        print('es una tabla de tipo_gasto')
        return df
    else:
        print('no encontrtado')
        return "archivo no concuerda con ninguna especificación"
