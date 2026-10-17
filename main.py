
import os
from fastmcp import FastMCP

mcp = FastMCP(
    name="Explorador de Antioquia",
    instructions="Servidor MCP para explorar destinos, consultar el clima y conocer tasas de cambio."
)


# RECURSOS: información que el cliente puede consultar

@mcp.resource("antioquia://guia")
def guia_antioquia() -> str:
    """Guía básica para explorar Antioquia."""
    return "Antioquia, Colombia, ofrece destinos culturales y naturales. Medellín es su capital."


@mcp.resource("antioquia://municipios")
def municipios_antioquia() -> str:
    """Lista de municipios turísticos de ejemplo."""
    return "Medellín, Guatapé, Santa Fe de Antioquia y Jardín."


@mcp.resource("antioquia://recomendaciones")
def recomendaciones_viaje() -> str:
    """Recomendaciones generales para viajar."""
    return "Consulta el clima antes de viajar y verifica horarios, transporte y condiciones de las vías."


# HERRAMIENTAS: funciones que puede ejecutar el cliente

@mcp.tool()
def listar_municipios() -> list[str]:
    """Lista municipios incluidos en esta guía."""
    return ["Medellín", "Guatapé", "Santa Fe de Antioquia", "Jardín"]


@mcp.tool()
def recomendar_destino(interes: str) -> str:
    """Sugiere un destino según el interés del viajero."""
    interes = interes.lower()

    if "naturaleza" in interes or "paisaje" in interes:
        return "Puedes explorar Guatapé."
    if "cultura" in interes or "historia" in interes:
        return "Puedes explorar Santa Fe de Antioquia."
    if "jardín" in interes or "pueblo" in interes:
        return "Puedes explorar Jardín."
    return "Puedes comenzar explorando Medellín."


@mcp.tool()
def crear_itinerario(dias: int = 1) -> list[str]:
    """Crea una propuesta sencilla de itinerario."""
    if dias < 1 or dias > 7:
        return ["Elige entre 1 y 7 días."]

    destinos = [
        "Día 1: Explorar Medellín.",
        "Día 2: Visitar Guatapé.",
        "Día 3: Conocer Santa Fe de Antioquia.",
        "Día 4: Recorrer Jardín."
    ]
    return destinos[:dias]


@mcp.tool()
async def consultar_clima(ciudad: str = "Medellín") -> dict:
    """Consulta el clima actual usando Open-Meteo."""
    coordenadas = {
        "medellin": (6.2442, -75.5812),
        "guatape": (6.2317, -75.1586),
        "jardin": (5.599, -75.819),
        "santa fe de antioquia": (6.5569, -75.8281)
    }

    import unicodedata

    clave = "".join(
        c for c in unicodedata.normalize("NFD", ciudad.strip().lower())
        if unicodedata.category(c) != "Mn"
    )

    if clave not in coordenadas:
        return {"error": "Ciudad no incluida. Prueba Medellín, Guatapé, Jardín o Santa Fe de Antioquia."}

    latitud, longitud = coordenadas[clave]
    url = "https://api.open-meteo.com/v1/forecast"
    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature",
        "timezone": "America/Bogota"
    }

    import httpx

    async with httpx.AsyncClient(timeout=15) as cliente:
        respuesta = await cliente.get(url, params=parametros)
        respuesta.raise_for_status()
        datos = respuesta.json()

    return {
        "ciudad": ciudad,
        "clima_actual": datos.get("current", {}),
        "fuente": "Open-Meteo"
    }



@mcp.tool()
async def consultar_tasa_cambio(
    moneda_origen: str = "USD",
    moneda_destino: str = "COP"
) -> dict:
    """Consulta tasas de cambio usando ExchangeRate-API."""

    import httpx

    origen = moneda_origen.upper().strip()
    destino = moneda_destino.upper().strip()

    url = f"https://open.er-api.com/v6/latest/{origen}"

    async with httpx.AsyncClient(timeout=20) as cliente:
        respuesta = await cliente.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()

    if datos.get("result") != "success":
        return {"error": "No fue posible consultar la tasa de cambio."}

    tasas = datos.get("rates", {})
    tasa = tasas.get(destino)

    if tasa is None:
        return {
            "error": f"No hay una tasa disponible para {origen} a {destino}."
        }

    return {
        "moneda_origen": origen,
        "moneda_destino": destino,
        "tasa": tasa,
        "fecha_actualizacion": datos.get("time_last_update_utc"),
        "fuente": "ExchangeRate-API"
    }

@mcp.prompt()
def planificar_visita(ciudad: str = "Medellín") -> str:
    """Prepara una consulta del clima antes de visitar un destino."""
    return (
        f"Estoy planeando visitar {ciudad} en Antioquia. "
        "Usa la herramienta consultar_clima para revisar el clima actual. "
        "Resume los datos recibidos y recomienda qué verificar antes de viajar."
    )


@mcp.prompt()
def preparar_presupuesto(
    moneda_origen: str = "USD",
    moneda_destino: str = "COP"
) -> str:
    """Prepara una consulta de tasa de cambio para planificar un presupuesto."""
    return (
        f"Quiero planificar un presupuesto de viaje. "
        f"Consulta la tasa de cambio de {moneda_origen} a {moneda_destino} "
        "con consultar_tasa_cambio. Explica la tasa y su fecha. "
        "Aclara que la tasa informativa puede diferir de la ofrecida por un banco."
    )


if __name__ == "__main__":
    mcp.run(
    transport="http",
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 8000))
)
