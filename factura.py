#" Grupo 3: Gestión de servicios de Restaurante "
#INTEGRANTES:
# ALCIVAR BAZURTO ANA DANIELA
# ANZULES AGUILAR NEICER JOSUE
# LEON SEGURA ANTHONY DAVID(no participa en el trabajo)
# MOREIRA AGUIÑO JARIB JORGE
class Factura:
    '''
        Clase que genera una factura del servicio.
    '''
    def __init__(self, servicio, fecha):
        self.servicio = servicio
        self.fecha = fecha

    def generar_factura(self):
        print("=== FACTURA ===")
        print("Fecha:", self.fecha)
        print("Servicio:", self.servicio.mostrar_info())
        print("Total a pagar:", self.servicio.calcular())

if __name__ == '__main__':
    print("=== PRUEBA DE CLASE FACTURA ===")


    # Creamos un servicio de ejemplo (puedes usar ServicioMesa o ServicioDelivery)
    class ServicioEjemplo:
        """Clase temporal solo para probar Factura."""

        def __init__(self):
            self._descripcion = "Servicio de prueba"

        def mostrar_info(self):
            return self._descripcion

        def calcular(self):
            return 25.50


    servicio = ServicioEjemplo()

    # Crear factura
    factura = Factura(servicio, "10/03/2025")

    # Generar factura
    factura.generar_factura()
