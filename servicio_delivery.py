#" Grupo 3: Gestión de servicios de Restaurante "
#INTEGRANTES:
# ALCIVAR BAZURTO ANA DANIELA
# ANZULES AGUILAR NEICER JOSUE
# LEON SEGURA ANTHONY DAVID(no participa en el trabajo)
# MOREIRA AGUIÑO JARIB JORGE
from servicio_restaurante import ServicioRestaurante


class ServicioDelivery(ServicioRestaurante):
    '''
          Clase que representa un servicio de entrega a domicilio.
          Hereda de ServicioRestaurante.
    '''
    def __init__(self, id_servicio: str, cliente: str, costo_base: float,
                 direccion: str, tarifa_envio: float):
        ServicioRestaurante.__init__(self,id_servicio,cliente,costo_base)
        self.direccion = direccion
        self.tarifa_envio = tarifa_envio

        @property
        def direccion(self):
            return self._direccion

        @direccion.setter
        def direccion(self, valor):
            if valor.strip() == "":
                raise ValueError("La dirección no puede estar vacía.")
            self._direccion = valor

        @property
        def tarifa_envio(self):
            return self._tarifa_envio

        @tarifa_envio.setter
        def tarifa_envio(self, valor):
            try:
                valor = float(valor)
            except:
                raise ValueError("La tarifa de envío debe ser un número.")

            if valor < 0:
                raise ValueError("La tarifa de envío no puede ser negativa.")

            self._tarifa_envio = valor
# Métodos polimórficos
    # ================================

    def calcular(self):
        '''Calcula el total sumando costo base + tarifa de envío'''
        return self.costo_base + self.tarifa_envio

    def mostrar_info(self):
        '''Muestra la información del servicio delivery'''
        return (f"[Delivery] ID:{self.id_servicio} - Cliente:{self.cliente} "
                f"- Dirección:{self.direccion} - Total:${self.calcular():.2f}")

if __name__ == '__main__':
    print("=== PRUEBA DE SERVICIO DELIVERY ===")

    try:
        delivery1 = ServicioDelivery("D001", "María López", 18.0,
                                     "Calle Principal 123", 2.5)
        print(delivery1.mostrar_info())

        # Prueba: dirección vacía
        print("\nIntentando crear delivery con dirección vacía...")
        delivery2 = ServicioDelivery("D002", "Carlos", 12.0, "", 3.0)

    except Exception as e:
        print("Error detectado:", e)

    try:
        # Prueba: tarifa negativa
        print("\nIntentando crear delivery con tarifa negativa...")
        delivery3 = ServicioDelivery("D003", "Ana", 10.0, "Av. Quito", -1.5)

    except Exception as e:
        print("Error detectado:", e)

    print("\n=== FIN DE LA PRUEBA ===")
