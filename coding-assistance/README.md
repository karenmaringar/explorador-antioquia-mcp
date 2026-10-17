# Registro de desarrollo asistido por IA

## 1. Información del proyecto

**Nombre:** Explorador de Antioquia MCP

**Objetivo:** desarrollar un servidor MCP que permita consultar información turística de Antioquia, recomendar destinos, planificar itinerarios y consultar información externa mediante APIs.

## 2. Agentes y herramientas de inteligencia artificial

### ChatGPT

- **Modelo utilizado:** GPT-6.
- **Uso:** apoyo en la definición de requisitos, planificación de la arquitectura, explicación de conceptos MCP, elaboración y revisión de código Python, solución de errores, integración de APIs, pruebas y documentación.
- **Enfoque:** desarrollo guiado paso a paso, comprensión de las funcionalidades y validación del funcionamiento del servidor.

### Herramientas de desarrollo

- **Python:** lenguaje utilizado para implementar el servidor.
- **FastMCP:** framework utilizado para definir los recursos, herramientas y prompts MCP.
- **HTTPX:** cliente HTTP utilizado para realizar solicitudes a las APIs externas.
- **MCP Inspector:** herramienta utilizada para conectarse al servidor y probar sus funcionalidades.
- **Visual Studio Code:** entorno de desarrollo.
- **Git y GitHub:** control de versiones y almacenamiento del código.
- **Render:** Render: plataforma utilizada para desplegar el servidor MCP públicamente.

## 3. Uso de inteligencia artificial durante el desarrollo

La inteligencia artificial se utilizó como apoyo para:

1. Interpretar los requisitos de la actividad y organizar las funcionalidades.
2. Diseñar la estructura inicial del proyecto.
3. Implementar recursos, herramientas y prompts MCP.
4. Integrar la API meteorológica Open-Meteo y la API de tasas de cambio ExchangeRate-API.
5. Analizar errores y realizar correcciones.
6. Preparar instrucciones de instalación, ejecución y pruebas.
7. Documentar el proyecto y crear una skill para agentes de IA.

El código se revisó y probó progresivamente durante el desarrollo. La asistencia de IA no sustituye la verificación del comportamiento real del software.

## 4. Validaciones realizadas

- Inicio local del servidor MCP mediante HTTP.
- Conexión al servidor mediante MCP Inspector.
- Verificación de los tres recursos, las cinco herramientas y los dos prompts.
- Prueba de la consulta meteorológica mediante Open-Meteo.
- Prueba de la consulta de tasas de cambio mediante ExchangeRate-API.
- Despliegue público en Render y comprobación de la conexión remota mediante MCP Inspector.

## 5. Registro de prompts

El archivo `prompts.jsonl` contiene el registro de las solicitudes realizadas a la IA durante el desarrollo.

Cada entrada debe ser un objeto JSON independiente e incluir:

- `timestamp`: fecha y hora de la solicitud, con zona horaria.
- `agent`: herramienta o agente de IA utilizado.
- `model`: modelo utilizado, cuando se conozca.
- `prompt`: texto de la solicitud.
- `purpose`: propósito de la solicitud.

Se deben registrar los prompts de desarrollo de forma fiel, sin inventar fechas ni solicitudes. No se deben incluir contraseñas, tokens, claves API ni otros datos secretos.

## 6. Skill para agentes

La skill asociada al proyecto se encuentra en:

`skills/explorador-antioquia/SKILL.md`

Esta proporciona instrucciones para utilizar las herramientas y los recursos del servidor MCP de forma adecuada.