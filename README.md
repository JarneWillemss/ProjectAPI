# Fitness Supplementen API

## Overzicht

Dit project bevat een RESTful API voor het beheren van informatie over fitnesssupplementen.
De API stelt gebruikers in staat om informatie over supplementbedrijven en details van de supplementen
te raadplegen, maken, bij te werken en te verwijderen.

## API Endpoints

De API heeft verschillende endpoints voor het beheren van de gegevens:

- `GET /supplement_companies`: Haal een lijst van alle geregistreerde supplementbedrijven op.
- `POST /supplement_companies`: Voeg een nieuw supplementbedrijf toe.

- `GET /items`: Haal een lijst van alle geregistreerde fitnesssupplementen op.
- `POST /items`: Voeg een nieuw fitnesssupplement toe.

- `DELETE /items/{item_id}`: Verwijder een supplement.

## Thema
Omdat er zoveel verschillende fitnessuplementen en supplementbedrijven bestaan leek het mij interessant om een API te creeëren
die alle supplementbedrijven en de supplementen zelf laat zien. De gebruiker kan bijvoorbeeld een bedrijf opzoeken en zo alle
supplementen vinden die verkocht worden door dat bedrijf. Dit idee stamt voort uit mijn persoonlijke interesse voor fitness.

## OpenAPI Docs
![Get supplement_companies screen 1](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/6276de7d-3170-4712-b325-02963d86406a)
![Get supplement_companies screen 2](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/c6ef6b15-0bf6-4b07-aa72-8d0cf73534d0)
![Post supplement_companies screen 1](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/53f50e5d-f498-4767-be6d-a3987cf525b4)
![Post supplement_companies screen 2](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/1d81f234-b14d-45a8-a9f6-4bdf6a98e19a)
![Get items screen 1](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/84dccf29-bbbb-4047-a3d8-73f97c90f7e2)
![Get items screen 2](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/3f03b2dd-31db-4801-9e57-0c8d5807e67a)
![Post items screen 1](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/e9b99b34-f49e-4f83-9531-a00ff23933bd)
![Post items screen 2](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/603c6543-10c6-45f4-b0bb-08a0015bbcd3)
![Delete items screen 1](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/154e44dd-024a-43b6-bdee-ea79035767d7)
![Delete items screen 2](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/fbbeb58f-f3ff-4f86-a780-f024816fa080)

## Postman
![Get supplement_companies Postman](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/ff29741a-cb00-4e27-8baa-a17c713f0f3b)
![Post supplement_companies Postman](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/92fed69e-f1ae-4169-bdcc-c77736aa5370)
![Get items postman](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/ab2999a2-ca20-4a8b-a01d-6e964042ccfb)
![Post items postman](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/3831231c-346b-40f5-8d17-1fb6f3a3dd6e)
![Delete item postman](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/96c79f56-7934-41be-8ad7-8470a1ea7685)

## Link Hosted API
https://useritem-api-service-jarnewillemss.cloud.okteto.net/




















