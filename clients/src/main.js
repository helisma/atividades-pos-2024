import { fetchAlbuns, fetchAlbunsDetails, fetchArtistas, fetchArtistasDetails, fetchMusicas, fetchMusicasDetails } from "./wrapper";

// Carrega a lista de artistas e popula o acordeão
export async function loadArtistas() {
    try {
        const artistas = await fetchArtistas();
        const artistasAccordion = document.getElementById('artistas-accordion');
        artistasAccordion.innerHTML = ''; // Limpa o acordeão

        artistas.forEach((artista, index) => {
            const accordionItem = document.createElement('div');
            accordionItem.className = 'accordion-item';

            accordionItem.innerHTML = `
                <h2 class="accordion-header" id="heading-${index}">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-${index}" aria-expanded="false" aria-controls="collapse-${index}">
                        ${artista.nome}
                    </button>
                </h2>
                <div id="collapse-${index}" class="accordion-collapse collapse" aria-labelledby="heading-${index}" data-bs-parent="#artistas-accordion">
                    <div class="accordion-body" id="artista-details-${index}">
                        <div class="text-center">Carregando detalhes...</div>
                    </div>
                </div>
            `;

            artistasAccordion.appendChild(accordionItem);

            // Adiciona evento para carregar detalhes ao expandir
            accordionItem.querySelector('.accordion-button').addEventListener('click', () => {
                const detailsElement = document.getElementById(`artista-details-${index}`);
                if (!detailsElement.classList.contains('loaded')) {
                    loadArtistaDetails(artista.id, index);
                }
            });
        });
    } catch (error) {
        console.error('Erro ao buscar os artistas:', error);
        alert('Não foi possível carregar os artistas.');
    }
}

// // Carrega os detalhes de um artista
// async function loadArtistaDetails(artista_id, index) {
//     try {
//         const artista = await fetchArtistasDetails(artista_id);
//         const detailsElement = document.getElementById(`artista-details-${index}`);

//         detailsElement.innerHTML = `
//             <p><strong>Nome:</strong> ${artista.nome}</p>
//             <p><strong>Local:</strong> ${artista.local}</p>
//             <p><strong>Ano de Criação:</strong> ${artista.ano_criacao}</p>
    
//         `;
//         detailsElement.classList.add('loaded');

//     } catch (error) {
//         console.error('Erro ao carregar os detalhes do artista:', error);
//         alert('Não foi possível carregar os detalhes do artista.');
//     }
// }

// Carrega os detalhes de um artista
async function loadArtistaDetails(artista_id, index) {
    try {
        const artista = await fetchArtistasDetails(artista_id);
        const detailsElement = document.getElementById(`artista-details-${index}`);

        detailsElement.innerHTML = `
            <p><strong>Nome:</strong> ${artista.nome}</p>
            <p><strong>Local:</strong> ${artista.local}</p>
            <p><strong>Ano de Criação:</strong> ${artista.ano_criacao}</p>
            <button id="view-albuns-${artista.id, index}" class="btn btn-secondary mt-2">Ver Álbuns</button>
        `;
        detailsElement.classList.add('loaded');
        
        // Adiciona evento para carregar os álbuns
        detailsElement.querySelector(`#view-albuns-${artista.id,index}`).addEventListener('click', () => {
            loadAlbuns(artista.id, index);
        });

    } catch (error) {
        console.error('Erro ao carregar os detalhes do artista:', error);
        alert('Não foi possível carregar os detalhes do artista.');
    }
}

// Carrega os álbuns de um artista
async function loadAlbuns(artista_id, index) {
    try {
        const albuns = await fetchAlbuns(artista_id);

        const albumsElement = document.getElementById(`artista-details-${index}`);
        albumsElement.innerHTML += '<div class="row">'; // Adiciona uma nova linha para os cards

        albuns.forEach(album => {
            albumsElement.innerHTML += `
                <div class="col-md-4 col-sm-6 mb-3">
                    <div class="card">
                        <img src="${album.capa ? album.capa : 'default-image.jpg'}" class="card-img-top" alt="${album.nome}">
                        <div class="card-body">
                            <h5 class="card-title">${album.nome}</h5>
                            <p class="card-text"><strong>Ano:</strong> ${album.ano}</p>
                            <button id="view-musicas-${artista_id}_${album.id}" class="btn btn-primary mt-2">Ver Músicas</button>
                        </div>
                    </div>
                </div>
            `;
        });

        albumsElement.innerHTML += '</div>'; // Fecha a linha de cards

        // Adiciona evento para abrir o modal de músicas
        albuns.forEach(album => {
            albumsElement.querySelector(`#view-musicas-${artista_id}_${album.id}`).addEventListener('click', () => {
                loadMusicas(artista_id, album.id, index);
            });
        });

    } catch (error) {
        console.error('Erro ao carregar os álbuns do artista:', error);
        alert('Não foi possível carregar os álbuns do artista.');
    }
}

// Carrega as músicas de um artista e álbum em um modal
async function loadMusicas(artista_id, album_id, index) {
    try {
        const musicas = await fetchMusicasDetails(album_id, artista_id);

        // Cria o modal de músicas
        const modalId = `modal-musicas-${artista_id}_${album_id}_${index}`;
        let modal = document.getElementById(modalId);

        if (!modal) {
            modal = document.createElement('div');
            modal.id = modalId;
            modal.className = 'modal fade';
            modal.setAttribute('tabindex', '-1');
            modal.setAttribute('aria-labelledby', `modal-musicas-label-${index}`);
            modal.setAttribute('aria-hidden', 'true');
            modal.innerHTML = `
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="modal-musicas-label-${index}">Lista de músicas</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body" id="modal-musicas-body-${index}">
                             <hr>
                            <div class="text-center">Carregando músicas...</div>
                        </div>
                       
                       
                    </div>
                </div>
            `;
            document.body.appendChild(modal);

            // Adiciona evento de ocultar o modal quando o botão de fechar é clicado
            modal.querySelector('.btn-close').addEventListener('click', () => {
                new bootstrap.Modal(modal).hide();
            });
        }

        // Popula o modal com as músicas
        const modalBody = document.getElementById(`modal-musicas-body-${index}`);
        modalBody.innerHTML = '';

        musicas.forEach(musica => {
            modalBody.innerHTML += `
                <p><strong>Nome:</strong> ${musica.nome}</p>
                <p><strong>Álbum:</strong> ${musica.album}</p>
                <p><strong>Duração:</strong> ${musica.segundos} segundos</p>
            `;
        });

        // Exibe o modal
        new bootstrap.Modal(modal).show();

    } catch (error) {
        console.error('Erro ao carregar as músicas do artista:', error);
        alert('Não foi possível carregar as músicas do artista.');
    }
}

// Adicione os elementos do DOM
document.querySelector('#app').innerHTML = `
    <div class="d-grid gap-2 col-6 mx-auto">
        <button id="load-artistas-btn" class="btn btn-primary btn-lg">Carregar Artistas</button>
    </div>
    <div class="accordion mt-4" id="artistas-accordion"></div>
    ;`

// Adicione os eventos de clique para carregar os dados
document.getElementById('load-artistas-btn').addEventListener('click',loadArtistas);