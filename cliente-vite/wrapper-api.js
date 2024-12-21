// responsável por realizar as requisições à API e retornar os dados.

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