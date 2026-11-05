"""[Docstring del módulo: una sola línea que diga qué hace el programa.]"""

from typing import Final

# Añadid aquí las importaciones que necesitéis.

# ---------------------------------------------------------------------------
# Datos de la aplicación. Sustituid los del ejemplo APP-00 por los vuestros.
# ---------------------------------------------------------------------------
CODIGO: Final[str] = "APP-00"
NOMBRE: Final[str] = "Agenda Escolar"
PAQUETE: Final[str] = "es.ieseuropa.agenda"
VERSION_MAYOR, VERSION_MENOR, VERSION_PARCHE = 2, 5, 13
TAMANO_APK: Final[int] = 48_734_208          # bytes
DESCARGAS: Final[int] = 12_500
PRECIO: Final[float] = 1.99                  # euros, IVA incluido
VALORACIONES: Final[int] = 400
ESTRELLAS: Final[int] = 1_700                # suma de todas las valoraciones
PERMISOS: Final[int] = 0b0001011
COLOR_ICONO: Final[int] = 0xFF3A7BD5         # ARGB

# ---------------------------------------------------------------------------
# Datos del programa. Solo hay que cambiar AUTORES.
# ---------------------------------------------------------------------------
VERSION_PROGRAMA: Final[str] = "1.0.0"
AUTORES: Final[str] = "[usuario] · [usuario]"
PENDIENTE: Final[str] = "  (opción pendiente de implementar)"

# ---------------------------------------------------------------------------
# Constantes de la pareja. Todo valor fijo del programa va aquí, con nombre.
# ---------------------------------------------------------------------------
ANCHO: Final[int] = 44


# ---------------------------------------------------------------------------
# Funciones auxiliares de la pareja. Al menos una, usada en varias opciones.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Las diez opciones. Sustituid el docstring y el print(PENDIENTE).
# ---------------------------------------------------------------------------
def opcion_1_identificacion() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_2_tamano() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_3_ingresos() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_4_version() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_5_permisos() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_6_color() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_7_tipos() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_8_redondeo() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_9_ficha() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_10_acerca_de() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


# ---------------------------------------------------------------------------
# Función principal y punto de entrada. Vienen hechos: no los modifiquéis.
# ---------------------------------------------------------------------------
def main() -> None:
    """Ejecuta las diez opciones, una detrás de otra."""
    print("--- Opción 1. Identificación de la app ---")
    opcion_1_identificacion()
    print("\n--- Opción 2. Tamaño del APK ---")
    opcion_2_tamano()
    print("\n--- Opción 3. Ingresos ---")
    opcion_3_ingresos()
    print("\n--- Opción 4. versionCode ---")
    opcion_4_version()
    print("\n--- Opción 5. Permisos ---")
    opcion_5_permisos()
    print("\n--- Opción 6. Color del icono ---")
    opcion_6_color()
    print("\n--- Opción 7. Tipos de datos ---")
    opcion_7_tipos()
    print("\n--- Opción 8. Redondeo de la valoración ---")
    opcion_8_redondeo()
    print("\n--- Opción 9. Ficha completa ---")
    opcion_9_ficha()
    print("\n--- Opción 10. Acerca de ---")
    opcion_10_acerca_de()


if __name__ == "__main__":
    main()
