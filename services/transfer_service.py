
class Transferencia:
    # Estados de la transferencia
    SOLICITADA = 'SOLICITADA'
    APROBADA = 'APROBADA'
    SEPARANDO = 'SEPARANDO'
    EN_TRANSITO = 'EN_TRANSITO'
    RECIBIDA = 'RECIBIDA'
    COMPLETADA = 'COMPLETADA'
    CON_DIFERENCIA = 'CON_DIFERENCIA'
    CANCELADA = 'CANCELADA'

    def __init__(self, codigo, pedido_venta, sku, cantidad, origen, destino):
        self.codigo = codigo
        self.pedido_venta = pedido_venta
        self.sku = sku
        self.cantidad = cantidad
        self.origen = origen
        self.destino = destino

        # Cantidades registradas durante el proceso
        self.cantidad_enviada = 0
        self.cantidad_recibida = 0

        self.estado = self.SEPARANDO

    # Validación genérica de cantidades
    def validar_cantidad(self, cantidad):
        return (
            isinstance(cantidad, (int, float))
            and not isinstance(cantidad, bool)
            and cantidad > 0
        )

    # Aprobar transferencia
    def aprobar(self):
        if self.estado == self.SOLICITADA:
            self.estado = self.APROBADA
            return True
        return False

    # Iniciar separación
    def iniciar_separacion(self):
        if self.estado == self.APROBADA:
            self.estado = self.SEPARANDO
            return True
        return False

    # Confirmar salida desde el origen
    def confirmar_salida(self, cantidad):
        if (
            self.estado == self.SEPARANDO
            and self.validar_cantidad(cantidad)
        ):
            self.cantidad_enviada = cantidad
            self.estado = self.EN_TRANSITO
            return True
        return False

    # Calcular diferencia entre lo solicitado y enviado
    def diferencia_solicitud(self):
        return self.cantidad - self.cantidad_enviada

    # Calcular diferencia entre lo enviado y recibido
    def diferencia_transporte(self):
        return self.cantidad_enviada - self.cantidad_recibida

    # Confirmar recepción en destino
    def confirmar_recepcion(self, cantidad):
        if (
            self.estado != self.EN_TRANSITO
            or not self.validar_cantidad(cantidad)
        ):
            return False

        self.cantidad_recibida = cantidad

        if self.diferencia_transporte() != 0:
            self.estado = self.CON_DIFERENCIA
        elif self.diferencia_solicitud() != 0:
            self.estado = self.CON_DIFERENCIA
        else:
            self.estado = self.COMPLETADA

        return True
trans = Transferencia(1,1001, 'cimento', 50, 'ventas', 'deposito' )
print(trans.confirmar_salida(100))
print(trans.diferencia_solicitud())