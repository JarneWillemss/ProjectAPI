# Fitness Supplementen API

## Overzicht

Dit project bevat een RESTful API voor het beheren van informatie over fitnesssupplementen.
De API stelt gebruikers in staat om informatie over supplementbedrijven en details van de supplementen
te raadplegen, maken, bij te werken en te verwijderen.

## API Endpoints

De API heeft verschillende endpoints voor het beheren van de gegevens:

- `GET /companies`: Haal een lijst van alle geregistreerde supplementbedrijven op.
- `POST /companies`: Voeg een nieuw supplementbedrijf toe.

- `GET /supplements`: Haal een lijst van alle geregistreerde fitnesssupplementen op.
- `POST /supplements`: Voeg een nieuw fitnesssupplement toe.
- `DELETE /supplements/{supplement_id}`: Verwijder een supplementbedrijf.

## Thema
Omdat er zoveel verschillende fitnessuplementen en supplementbedrijven bestaan leek het mij interessant om een API te creeëren
die alle supplementbedrijven en de supplementen zelf laat zien. De gebruiker kan bijvoorbeeld een bedrijf opzoeken en zo alle
supplementen vinden die verkocht worden door dat bedrijf. Dit idee stamt voort uit mijn persoonlijke interesse voor fitness.

## OpenAPI Docs







