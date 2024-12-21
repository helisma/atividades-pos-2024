import { fetchPeople, fetchPersonDetails } from "./wrapper-api";

export async function loadPeople() {
    try {
        const people = await fetchPeople(); 
        const peopleAccordion = document.getElementById('people-accordion');
        peopleAccordion.innerHTML = '';

        people.forEach((person, index) => {
            const accordionItem = document.createElement('div');
            accordionItem.className = 'accordion-item';

            accordionItem.innerHTML = `
                <h2 class="accordion-header" id="heading-${index}">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-${index}" aria-expanded="false" aria-controls="collapse-${index}">
                        ${person.name}
                    </button>
                </h2>
                <div id="collapse-${index}" class="accordion-collapse collapse" aria-labelledby="heading-${index}" data-bs-parent="#people-accordion">
                    <div class="accordion-body" id="people-details-${index}">
                        <div class="text-center">Carregando detalhes...</div>
                    </div>
                </div>
            `;

            peopleAccordion.appendChild(accordionItem);

            // evento para carregar os detalhes do personagem 
            accordionItem.querySelector('.accordion-button').addEventListener('click', () => {
                const detailsElement = document.getElementById(`people-details-${index}`);
                if (!detailsElement.classList.contains('loaded')) {
                    loadPersonDetails(person.url, index);
                }
            });
        });

    } catch (error) {
        console.error('Erro ao buscar os personagens:', error);
        alert('Não foi possível carregar os personagens.');
    }
}

async function loadPersonDetails(personUrl, index) {
    try {
        const person = await fetchPersonDetails(personUrl);
        const detailsElement = document.getElementById(`people-details-${index}`);

        detailsElement.innerHTML = `
            <p><strong>Nome:</strong> ${person.name}</p>
            <p><strong>Altura:</strong> ${person.height} cm</p>
            <p><strong>Peso:</strong> ${person.mass} kg</p>
            <p><strong>Cor do Cabelo:</strong> ${person.hair_color}</p>
            <p><strong>Cor dos Olhos:</strong> ${person.eye_color}</p>
        `;
        detailsElement.classList.add('loaded');
    } catch (error) {
        console.error('Erro ao carregar os detalhes do personagem:', error);
        alert('Não foi possível carregar os detalhes do personagem.');
    }
}


document.querySelector('#app').innerHTML = `
  <div class="d-grid gap-2 col-6 mx-auto">
      <button id="load-people-btn" class="btn btn-primary btn-lg">Carregar..</button>
  </div>
  <div class="accordion mt-4" id="people-accordion"></div>
`;

document.getElementById('load-people-btn').addEventListener('click', loadPeople);

