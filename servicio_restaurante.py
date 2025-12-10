#" Grupo 3: Gestión de servicios de Restaurante "
#INTEGRANTES:
# ALCIVAR BAZURTO ANA DANIELA
# ANZULES AGUILAR NEICER JOSUE
# LEON SEGURA ANTHONY DAVID(no participa en el trabajo)
# MOREIRA AGUIÑO JARIB JORGE
class ServicioRestaurante:
    """
    Superclase base para todos los servicios del restaurante.
    """

    def __init__(self, id_servicio: str, cliente: str, costo_base: float):
        self.id_servicio = id_servicio
        self.cliente = cliente
        self.costo_base = costo_base

    @property
    def id_servicio(self):
        return self._id_servicio

    @id_servicio.setter
    def id_servicio(self, valor):
        if valor.strip() == "":
            raise ValueError("El ID del servicio no puede estar vacío.")
        self._id_servicio = valor

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, valor):
        if valor.strip() == "":
            raise ValueError("El nombre del cliente no puede estar vacío.")
        self._cliente = valor

    @property
    def costo_base(self):
        return self._costo_base

    @costo_base.setter
    def costo_base(self, valor):
        if valor < 0:
            raise ValueError("El costo base no puede ser negativo.")
        self._costo_base = valor

    # ======= MÉTODO BASE POLIMÓRFICO =======
    def calcular(self):
        return self.costo_base
    # ======= MÉTODO BASE DE INFORMACIÓN =======
    def mostrar_info(self):
        return f"Servicio {self.id_servicio} para {self.cliente} - Costo base: {self.costo_base}"
if __name__ == '__main__':
    print("=== PRUEBA DE SERVICIO RESTAURANTE ===")

    try:
        # Crear un servicio válido
        servicio1 = ServicioRestaurante("SR001", "Juan Pérez", 15.50)
        print("Servicio creado correctamente:")
        print("ID:", servicio1.id_servicio)
        print("Cliente:", servicio1.cliente)
        print("Costo base:", servicio1.costo_base)

        # Intentar crear un servicio con costo negativo
        print("\nIntentando crear servicio con costo negativo...")
        servicio2 = ServicioRestaurante("SR002", "Ana", -10)

    except Exception as e:
        print("Error detectado:", e)

    try:
        # Intentar crear un servicio con cliente vacío
        print("\nIntentando crear servicio con cliente vacío...")
        servicio3 = ServicioRestaurante("SR003", "", 20)  # debe fallar

    except Exception as e:
        print("Error detectado:", e)


