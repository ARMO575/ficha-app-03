"""Ficha técnica de una aplicación móvil antes de publicarla en la tienda."""

from decimal import Decimal, ROUND_HALF_UP
import platform
from typing import Final

# ---------------------------------------------------------------------------
# Datos de la aplicación. Sustituid los del ejemplo APP-00 por los vuestros.
# ---------------------------------------------------------------------------
CODIGO: Final[str] = "APP-03"
NOMBRE: Final[str] = "Horario de Bus"
PAQUETE: Final[str] = "es.transporte.horariobus"
VERSION_MAYOR, VERSION_MENOR, VERSION_PARCHE = 2, 1, 0
TAMANO_APK: Final[int] = 25_165_824          # bytes
DESCARGAS: Final[int] = 41_000
PRECIO: Final[float] = 0.99                  # euros, IVA incluido
VALORACIONES: Final[int] = 2_000
ESTRELLAS: Final[int] = 8_300                # suma de todas las valoraciones
PERMISOS: Final[int] = 0b0001011
COLOR_ICONO: Final[int] = 0xFF1565C0         # ARGB

# ---------------------------------------------------------------------------
# Datos del programa. Solo hay que cambiar AUTORES.
# ---------------------------------------------------------------------------
VERSION_PROGRAMA: Final[str] = "1.0.0"
AUTORES: Final[str] = "ARMO575 · alejandromoreno"
PENDIENTE: Final[str] = "  (opción pendiente de implementar)"

# ---------------------------------------------------------------------------
# Constantes de la pareja. Todo valor fijo del programa va aquí, con nombre.
# ---------------------------------------------------------------------------
ANCHO: Final[int] = 44
ANCHO_ETIQUETA: Final[int] = 18
ANCHO_NUMERO: Final[int] = 8
ANCHO_CANAL: Final[int] = 3
ANCHO_TIPO: Final[int] = 16

BYTES_POR_MB: Final[int] = 1_000_000
BYTES_POR_MIB: Final[int] = 1_048_576
PORCENTAJE: Final[int] = 100
COMISION_TIENDA: Final[float] = 0.15

DESPL_MAYOR: Final[int] = 16
DESPL_MENOR: Final[int] = 8
DESPL_ALFA: Final[int] = 24
DESPL_ROJO: Final[int] = 16
DESPL_VERDE: Final[int] = 8
MASCARA_BYTE: Final[int] = 0xFF
MAX_CANAL: Final[int] = 255

PERMISO_INTERNET: Final[int] = 0b0000001
PERMISO_NOTIFICACIONES: Final[int] = 0b0000010
PERMISO_CAMARA: Final[int] = 0b0000100
PERMISO_UBICACION: Final[int] = 0b0001000
PERMISO_CONTACTOS: Final[int] = 0b0010000
PERMISO_MICROFONO: Final[int] = 0b0100000
PERMISO_ALMACENAMIENTO: Final[int] = 0b1000000

DECIMALES_1: Final[int] = 1
DECIMALES_2: Final[int] = 2
PRECISION_1_DEC: Final[str] = "0.1"
PRECISION_2_DEC: Final[str] = "0.01"

CARACTER_CABECERA: Final[str] = "="
CARACTER_SEPARADOR: Final[str] = "-"
TITULO_FICHA: Final[str] = "FICHA DE LA APLICACIÓN"


# ---------------------------------------------------------------------------
# Funciones auxiliares de la pareja. Al menos una, usada en varias opciones.
# ---------------------------------------------------------------------------
def fila(etiqueta: str, valor: object) -> str:
    """Devuelve una fila con la etiqueta alineada y su valor al lado."""
    return f"{etiqueta:<{ANCHO_ETIQUETA}}{valor}"


def linea_separadora(caracter: str) -> str:
    """Genera una línea horizontal repitiendo el carácter indicado."""
    return caracter * ANCHO


# ---------------------------------------------------------------------------
# Las diez opciones. Sustituid el docstring y el print(PENDIENTE).
# ---------------------------------------------------------------------------
def opcion_1_identificacion() -> None:
    """Muestra los datos básicos de identificación y la versión de la app."""
    version_texto = f"{VERSION_MAYOR}.{VERSION_MENOR}.{VERSION_PARCHE}"

    print(fila("Código:", CODIGO))
    print(fila("Nombre:", NOMBRE))
    print(fila("Paquete:", PAQUETE))
    print(fila("Versión:", version_texto))


def opcion_2_tamano() -> None:
    """Calcula el tamaño del APK en MB y MiB y su diferencia porcentual."""
    # Dividimos entre 10^6 para la tienda y entre 2^20 para el móvil
    tamano_mb = TAMANO_APK / BYTES_POR_MB
    tamano_mib = TAMANO_APK / BYTES_POR_MIB
    diferencia = ((tamano_mb - tamano_mib) / tamano_mb) * PORCENTAJE

    print("TAMAÑO DEL APK")
    print(fila("Bytes:", f"{TAMANO_APK:>{ANCHO_NUMERO}} B"))
    print(fila("En la tienda:", f"{tamano_mb:>{ANCHO_NUMERO}.2f} MB"))
    print(fila("En el móvil:", f"{tamano_mib:>{ANCHO_NUMERO}.2f} MiB"))
    print(fila("Diferencia:", f"{diferencia:>{ANCHO_NUMERO}.1f} %"))


def opcion_3_ingresos() -> None:
    """Calcula los ingresos brutos, la comisión de la tienda y el neto."""
    ingresos_brutos = DESCARGAS * PRECIO
    importe_comision = ingresos_brutos * COMISION_TIENDA
    ingresos_netos = ingresos_brutos - importe_comision

    print("INGRESOS")
    print(fila("Descargas:", f"{DESCARGAS:>{ANCHO_NUMERO}} uds."))
    print(fila("Precio:", f"{PRECIO:>{ANCHO_NUMERO}.2f} €"))
    print(fila("Ingresos brutos:", f"{ingresos_brutos:>{ANCHO_NUMERO}.2f} €"))
    print(fila("Comisión tienda:", f"{importe_comision:>{ANCHO_NUMERO}.2f} €"))
    print(fila("Ingresos netos:", f"{ingresos_netos:>{ANCHO_NUMERO}.2f} €"))


def opcion_4_version() -> None:
    """Empaqueta y desempaqueta la versión en un entero usando bits."""
    version_original = f"{VERSION_MAYOR}.{VERSION_MENOR}.{VERSION_PARCHE}"

    # Movemos cada parte a su hueco de 8 bits y las juntamos con OR (|)
    parte_mayor = VERSION_MAYOR << DESPL_MAYOR
    parte_menor = VERSION_MENOR << DESPL_MENOR
    version_code = parte_mayor | parte_menor | VERSION_PARCHE

    # Sacamos cada parte moviendo a la derecha y filtrando con 0xFF
    mayor_recup = (version_code >> DESPL_MAYOR) & MASCARA_BYTE
    menor_recup = (version_code >> DESPL_MENOR) & MASCARA_BYTE
    parche_recup = version_code & MASCARA_BYTE
    desempaquetado = f"{mayor_recup}.{menor_recup}.{parche_recup}"

    print("VERSIONCODE")
    print(fila("Versión:", version_original))
    print(fila("versionCode:", version_code))
    print(fila("En hexadecimal:", f"0x{version_code:06X}"))
    print(fila("Desempaquetado:", desempaquetado))


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
