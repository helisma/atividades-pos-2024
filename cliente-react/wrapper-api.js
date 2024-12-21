// pessoas
export async function fetchPeople() {
    const url = 'https://swapi.dev/api/people/';
    const response = await fetch(url);
    const data = await response.json();
    return data.results; // lista de personagens
}

export async function fetchPersonDetails(personUrl) {
    const response = await fetch(personUrl);
    return await response.json(); // detalhes do personagem
}

// planetas
export async function fetchPlanets() {
    const url = 'https://swapi.dev/api/planets/';
    const response = await fetch(url);
    const data = await response.json();
    return data.results; // lista de planetas
}

export async function fetchPlanetsDetails (planetUrl) {
    const response = await fetch(planetUrl);
    return await response.json(); // detalhes do planetas
}


// naves estelares
export async function fetchShips() {
    const url = 'https://swapi.dev/api/starships/';
    const response = await fetch(url);
    const data = await response.json();
    return data.results; // lista de naves estelares
}

export async function fetchShipsDetails (shipUrl) {
    const response = await fetch(shipUrl);
    return await response.json(); // detalhes da nave
}