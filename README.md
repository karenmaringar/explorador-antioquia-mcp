# Explorador de Antioquia MCP

## Descripción

Explorador de Antioquia MCP es un servidor basado en el Model Context Protocol (MCP) que permite a agentes de inteligencia artificial consultar información turística sobre Antioquia, recomendar destinos y planificar itinerarios.

El proyecto también integra APIs externas para consultar el clima actual y las tasas de cambio de monedas.

## Objetivo

Facilitar la consulta de información turística de Antioquia mediante herramientas y recursos que puedan utilizarse desde clientes compatibles con MCP.

## Funcionalidades

### Recursos MCP

El servidor cuenta con tres recursos:

- `antioquia://guia`: guía general sobre Antioquia.
- `antioquia://municipios`: información de municipios.
- `antioquia://recomendaciones`: recomendaciones turísticas.

### Herramientas MCP

El servidor incluye cinco herramientas:

1. `listar_municipios`: permite consultar la lista de municipios disponibles.
2. `recomendar_destino`: recomienda destinos según los intereses del usuario.
3. `crear_itinerario`: ayuda a organizar un itinerario turístico.
4. `consultar_clima`: consulta información meteorológica mediante la API de Open-Meteo.
5. `consultar_tasa_cambio`: consulta tasas de cambio mediante ExchangeRate-API.

### Prompts MCP

- `planificar_visita`: ayuda a organizar una visita turística.
- `preparar_presupuesto`: ayuda a preparar un presupuesto de viaje.

## Tecnologías utilizadas

- Python
- FastMCP
- HTTPX
- Model Context Protocol (MCP)
- Open-Meteo API
- ExchangeRate-API
- MCP Inspector
- Git y GitHub
- Render para el despliegue público del servidor MCP

## Requisitos

- Python instalado.
- Acceso a internet para consultar las APIs externas.
- Dependencias definidas en `requirements.txt`.

## Instalación y ejecución local

1. Clona el repositorio o descarga el código.
2. Abre una terminal en la carpeta del proyecto.
3. Crea un entorno virtual:

   ```bash
   python -m venv .venv
   ```

4. Activa el entorno virtual en Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

5. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

6. Ejecuta el servidor:

   ```bash
   python main.py
   ```

El endpoint MCP local es:

`http://127.0.0.1:8000/mcp`

El puerto puede cambiar si se configura la variable de entorno `PORT`.

## Estructura del proyecto

```text
mcp-antioquia/
├── coding-assistance/
│   ├── README.md
│   └── prompts.jsonl
├── skills/
│   └── explorador-antioquia/
│       └── SKILL.md
├── .gitignore
├── main.py
├── render.yaml
└── requirements.txt
```

## Pruebas

El servidor y las herramientas de consulta del clima y de tasas de cambio se probaron localmente mediante MCP Inspector.

El servidor se desplegó públicamente en Render y se verificó la conexión remota mediante MCP Inspector. Se comprobó la disponibilidad de los tres recursos, las cinco herramientas y los dos prompts, y se probó la consulta del clima.

## Desarrollo asistido por IA

Durante el desarrollo se utilizaron herramientas de inteligencia artificial como apoyo para planificar la arquitectura, escribir y revisar código, resolver errores y preparar pruebas y documentación.

El registro de este proceso se encuentra en `coding-assistance/README.md` y `coding-assistance/prompts.jsonl`.

## Skill para agentes

El proyecto incluye una skill en:

`skills/explorador-antioquia/SKILL.md`

Esta contiene instrucciones para orientar a agentes de IA en el uso de las funcionalidades del servidor.

## Licencia

La licencia del proyecto está pendiente de definir.