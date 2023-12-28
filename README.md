# Fitness Supplementen API

## Overzicht

Dit project bevat een RESTful API voor het beheren van informatie over fitnesssupplementen.
De API stelt gebruikers in staat om informatie over supplementbedrijven en details van de supplementen
te raadplegen, maken, bij te werken en te verwijderen.

## API Endpoints

De API heeft verschillende endpoints voor het beheren van de gegevens:

- `POST /users`: Voeg een nieuwe user toe.

- `GET /supplement_companies`: Haal een lijst van alle geregistreerde supplementbedrijven op.
- `POST /supplement_companies`: Voeg een nieuw supplementbedrijf toe.

- `GET /items`: Haal een lijst van alle geregistreerde fitnesssupplementen op.
- `GET /items/{item_id}`: Haal één specifiek fitnesssupplement op.
- `POST /items`: Voeg een nieuw fitnesssupplement toe.
- `PUT /items/{item_id}`: Update één specifiek fitnesssupplement.

- `DELETE /items/{item_id}`: Verwijder een supplement.

## Thema
Omdat er zoveel verschillende fitnessuplementen en supplementbedrijven bestaan leek het mij interessant om een API te creeëren
die alle supplementbedrijven en de supplementen zelf laat zien. De gebruiker kan bijvoorbeeld een bedrijf opzoeken en zo alle
supplementen vinden die verkocht worden door dat bedrijf. Dit idee stamt voort uit mijn persoonlijke interesse voor fitness.

## OpenAPI Docs
![Post User screen 1](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/7711077d-162c-4f9e-b163-bc549a93ae57)
![Get supplement_companies screen 1](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/6276de7d-3170-4712-b325-02963d86406a)
![Get supplement_companies screen 2](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/c6ef6b15-0bf6-4b07-aa72-8d0cf73534d0)
![Post supplement_companies screen 1](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/53f50e5d-f498-4767-be6d-a3987cf525b4)
![Post supplement_companies screen 2](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/1d81f234-b14d-45a8-a9f6-4bdf6a98e19a)
![Get items screen 1](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/84dccf29-bbbb-4047-a3d8-73f97c90f7e2)
![Get items by ID screen 1](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/f74bc5ed-e3bb-42e3-93d8-c969cf4b0200)
![Get items screen 2](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/3f03b2dd-31db-4801-9e57-0c8d5807e67a)
![Post items screen 1](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/e9b99b34-f49e-4f83-9531-a00ff23933bd)
![Post items screen 2](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/603c6543-10c6-45f4-b0bb-08a0015bbcd3)
![PUT item By ID screen 1](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/8ecaead5-4d5a-4e4a-ba8b-5e3a95cb70e3)
![PUT item By ID screen 1](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/2ef1d9bd-bfae-493a-9ba0-7b75e9dca7f4")
![Delete items screen 1](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/154e44dd-024a-43b6-bdee-ea79035767d7)
![Delete items screen 2](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/fbbeb58f-f3ff-4f86-a780-f024816fa080)

## Postman
![Post User Postman](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/a49faa31-d798-4aac-9961-46374e46278e)
![Get supplement_companies Postman](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/ff29741a-cb00-4e27-8baa-a17c713f0f3b)
![Post supplement_companies Postman](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/92fed69e-f1ae-4169-bdcc-c77736aa5370)
![Get items postman](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/ab2999a2-ca20-4a8b-a01d-6e964042ccfb)
![Get items postman](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/41eda15e-8840-451b-bb45-36e227ec21d1)
![Post items postman](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/3831231c-346b-40f5-8d17-1fb6f3a3dd6e)
![PUT item by ID postman](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/8b1e4f1f-1485-401a-b552-8ef44c36e740)
![Delete item postman](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/96c79f56-7934-41be-8ad7-8470a1ea7685)

## Implementatie Oauth
De implementatie van Oauth is helaas niet gelukt. De gebruikte code is niet aanwezig in deze repository omdat
het mijn containers deed crashen. Voor implementatie heb ik de volgende code gebruikt:

![Oauth](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/771d6fa9-00e6-4f7a-b5ee-d4686763ba7a)
![Oauth2](https://github.com/JarneWillemss/ProjectAPI/assets/113974853/6c8eab5a-211d-4789-85f8-a4e97dc64fbf)

## Afgewerkte nummers
1 - Algemene Eisen & Documentatie
2 - Aanvullingen Functie
2.1 - Test alle niet-Get Endpoints. +5%
2.2 - Zorg ervoor dat de testfile ook tijdens de GitHub Actions gerund wordt. +5%

## Link Hosted API
https://useritem-api-service-jarnewillemss.cloud.okteto.net/




















