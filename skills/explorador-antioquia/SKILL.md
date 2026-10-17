
---
name: explorador-antioquia
description: Ayuda a agentes de IA a consultar información turística de Antioquia, recomendar destinos, planificar itinerarios y consultar clima y tasas de cambio usando el servidor MCP Explorador de Antioquia.
---

# Skill: Explorador de Antioquia

## Objetivo
Ayudar a un agente de IA a utilizar el servidor MCP Explorador de Antioquia para responder preguntas de viaje.

## Herramientas disponibles
- `listar_municipios`: obtiene la lista de municipios incluidos en la guía.
- `recomendar_destino`: recomienda un destino según los intereses del viajero.
- `crear_itinerario`: prepara un itinerario básico de uno a siete días.
- `consultar_clima`: consulta información meteorológica actual mediante Open-Meteo.
- `consultar_tasa_cambio`: consulta tasas de cambio mediante ExchangeRate-API.

## Recursos disponibles
- `antioquia://guia`: guía general de Antioquia.
- `antioquia://municipios`: municipios incluidos en el proyecto.
- `antioquia://recomendaciones`: recomendaciones generales de viaje.

## Instrucciones de uso
1. Identifica qué información necesita el usuario.
2. Para preguntas sobre destinos, utiliza `listar_municipios` o `recomendar_destino`.
3. Para organizar un viaje, utiliza `crear_itinerario`.
4. Si preguntan por el clima, utiliza `consultar_clima` con la ciudad admitida.
5. Si preguntan por tasas de cambio, utiliza `consultar_tasa_cambio` con los códigos de moneda correspondientes.
6. Explica los resultados con claridad y no inventes datos que no devuelvan las herramientas.
7. Informa cuando una API no responda o no tenga datos disponibles.

## Consideraciones
- Las tasas de cambio son informativas y pueden diferir de las aplicadas por bancos o casas de cambio.
- El clima consultado corresponde a los datos disponibles en la API y no garantiza las condiciones futuras.
- Verifica la información de transporte, horarios y condiciones de las vías antes de viajar.
