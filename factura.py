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

    @property
    def servicio(self):
        return self._servicio

    @servicio.setter
    def servicio(self, valor):
        if valor is None:
            raise ValueError("El servicio no puede ser None.")
        self._servicio = valor
    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        if valor.strip() == "":
            raise ValueError("La fecha no puede estar vacía.")
        self._fecha = valor

    def generar_factura(self):
        print("=== FACTURA ===")
        print("Fecha:", self.fecha)
        print("Servicio:", self.servicio.mostrar_info())
        print("Total a pagar:", self.servicio.calcular())

    def __str__(self):
        return f"Factura del {self.fecha} - Total: ${self.servicio.calcular():.2f}"

if __name__ == "__main__":

    class ServicioEjemplo:
        def mostrar_info(self):
            return "Servicio de prueba"

        def calcular(self):
            return 25.50

    servicio = ServicioEjemplo()
    factura = Factura(servicio, "10/03/2025")
    factura.generar_factura()


