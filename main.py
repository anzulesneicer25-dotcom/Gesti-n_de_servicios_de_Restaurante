#" Grupo 3: Gestión de servicios de Restaurante "
#INTEGRANTES:
# ALCIVAR BAZURTO ANA DANIELA
# ANZULES AGUILAR NEICER JOSUE
# LEON SEGURA ANTHONY DAVID(no participa en el trabajo)
# MOREIRA AGUIÑO JARIB JORGE
from servicio_restaurante import ServicioRestaurante
from servicio_mesa import ServicioMesa
from servicio_delivery import ServicioDelivery
from empleado import Empleado
from factura import Factura


if __name__ == '__main__':
    print("=== SISTEMA DE GESTIÓN DE SERVICIOS DE RESTAURANTE ===\n")

    print(">>> Demostrando uso de la SUPERCLASE ServicioRestaurante...\n")

    servicio_base = ServicioRestaurante("S000", "Cliente Base", 10.0)
    print("Servicio Base creado desde la superclase:")
    print(servicio_base.mostrar_info())
    print("Total calculado:", servicio_base.calcular(), "\n")

    # -------------------------------------------------------------
    # 1. Crear empleados
    # -------------------------------------------------------------
    print(">>> Creando empleados...")
    mesero = Empleado("Carlos López", "Mesero")
    repartidor = Empleado("Ana Torres", "Repartidora")

    print(f"Empleado creado: {mesero.nombre} - {mesero.cargo}")
    print(f"Empleado creado: {repartidor.nombre} - {repartidor.cargo}\n")

    # -------------------------------------------------------------
    # 2. Crear servicios (SUBCLASES)
    # -------------------------------------------------------------
    print(">>> Creando servicios...")

    servicio_mesa = ServicioMesa("S001", "Juan Pérez", 20.0, 3, 5.0)
    servicio_delivery = ServicioDelivery("S002", "María Gómez", 18.0, "Av. Central 123", 3.5)

    print("Servicios creados.\n")

    # -------------------------------------------------------------
    # 3. Lista polimórfica (NO SE PREGUNTA EL TIPO)
    # -------------------------------------------------------------
    print(">>> Lista polimórfica de servicios:")

    servicios = [servicio_mesa, servicio_delivery]

    for s in servicios:
        print("•", s.mostrar_info())
        print("  Total:", s.calcular())
        print()

    # -------------------------------------------------------------
    # 4. Crear Facturas
    # -------------------------------------------------------------
    print(">>> Generando facturas...\n")

    factura1 = Factura(servicio_mesa, "10/03/2025")
    factura2 = Factura(servicio_delivery, "10/03/2025")

    factura1.generar_factura()
    print()
    factura2.generar_factura()
    print()

    # -------------------------------------------------------------
    # 5. Polimorfismo real: sumar totales sin preguntar tipo
    # -------------------------------------------------------------
    print(">>> Calculando total general de ingresos del día...\n")

    total_general = sum(s.calcular() for s in servicios)

    print(f"Total recaudado con todos los servicios: ${total_general:.2f}")
    print("\n=== FIN DEL SISTEMA ===")
