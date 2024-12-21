const API_BASE_URL = 'http://127.0.0.1:8000'; 

// Busca lista de artistas
export async function fetchArtistas() {
    const response = await fetch(`${API_BASE_URL}/artistas/`);
    if (!response.ok) {
        throw new Error(`Erro ao buscar artistas: ${response.statusText}`);
    }
    return await response.json();
}

// Busca detalhes de um artista
export async function fetchArtistasDetails(artista_id) {
    const response = await fetch(`${API_BASE_URL}/artistas/${artista_id}/`);
    if (!response.ok) {
        throw new Error(`Erro ao buscar detalhes do artista ${artista_id}: ${response.statusText}`);
    }
    return await response.json();
}

// Busca álbuns de um artista
export async function fetchAlbuns(artista_id) {
    const response = await fetch(`${API_BASE_URL}/artistas/${artista_id}/albuns/`);
    if (!response.ok) {
        throw new Error(`Erro ao buscar álbuns do artista ${artista_id}: ${response.statusText}`);
    }
    return await response.json();
}

// Busca detalhes de um álbum
export async function fetchAlbunsDetails(album_id) {
    const response = await fetch(`${API_BASE_URL}/albuns/${album_id}/`);
    if (!response.ok) {
        throw new Error(`Erro ao buscar detalhes do álbum ${album_id}: ${response.statusText}`);
    }
    return await response.json();
}

// Busca músicas de um álbum
export async function fetchMusicas(album_id) {
    const response = await fetch(`${API_BASE_URL}/albuns/${album_id}/musicas/`);
    if (!response.ok) {
        throw new Error(`Erro ao buscar músicas do álbum ${album_id}: ${response.statusText}`);
    }
    return await response.json();
}

export async function fetchMusicasDetails(album_id, artista_id) {
    const response = await fetch(`${API_BASE_URL}/artistas/${artista_id}/albuns/${album_id}/musicas`);
    if (!response.ok) {
        throw new Error(`Erro ao buscar detalhes do álbum ${album_id}: ${response.statusText}`);
    }
    return await response.json();
}