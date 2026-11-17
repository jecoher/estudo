from aplicacion.excepciones.producto_excepciones import ProductoDuplicadoError

print('inicio programa')

try: 
    raise ProductoDuplicadoError('El producto ya existe')
except ProductoDuplicadoError as error:
    print(error)
print('fin programa')