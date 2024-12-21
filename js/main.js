async function loadWars() {
    try {
        const url = 'https://swapi.dev/api/people/';
        const response = await fetch(url); 
        const data = await response.json(); 

        const people = data.results; // Acessa o array de personagens
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

            // Adiciona o evento de clique para carregar os detalhes do personagem
            accordionItem.querySelector('.accordion-button').addEventListener('click', () => {
                const detailsElement = document.getElementById(`people-details-${index}`);
                if (!detailsElement.classList.contains('loaded')) {
                    loadPeopleDetails(person.url, index); // Usa a url do personagem
                }
            });
        });

    } catch (error) {
        console.error('Erro ao buscar os personagens:', error);
        alert('Não foi possível carregar os personagens.');
    }
}

async function loadPeopleDetails(personId, index) {
    try {
        const response = await fetch(personId);
        const person = await response.json();

        const peopleDetails = document.getElementById(`people-details-${index}`);
        peopleDetails.innerHTML = `
            <p><strong>Nome:</strong> ${person.name}</p>
            <p><strong>Altura:</strong> ${person.height} cm</p>
            <p><strong>Peso:</strong> ${person.mass} kg</p>
            <p><strong>Cor do Cabelo:</strong> ${person.hair_color}</p>
            <p><strong>Cor dos Olhos:</strong> ${person.eye_color}</p>
        `;
        peopleDetails.classList.add('loaded'); 

    } catch (error) {
        console.error('Erro ao carregar os detalhes do personagem:', error);
        alert('Não foi possível carregar os detalhes do personagem.');
    }
}

document.getElementById('load-people-btn').addEventListener('click', loadWars);