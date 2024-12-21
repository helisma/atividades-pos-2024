import { useState, useEffect } from 'react';
import { fetchPeople, fetchPlanets } from '../wrapper-api';

function App() {
  const [view, setView] = useState('people'); // Controle de navegação
  const [people, setPeople] = useState([]);
  const [planets, setPlanets] = useState([]);
  const [loading, setLoading] = useState(false);

  const loadPeople = async () => {
    setLoading(true);
    try {
      const peopleData = await fetchPeople();
      setPeople(peopleData);
    } catch (error) {
      alert('Erro ao carregar os personagens.');
    } finally {
      setLoading(false);
    }
  };

  const loadPlanets = async () => {
    setLoading(true);
    try {
      const planetsData = await fetchPlanets();
      setPlanets(planetsData);
    } catch (error) {
      alert('Erro ao carregar os planetas.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (view === 'people') loadPeople();
    if (view === 'planets') loadPlanets();
  }, [view]);

  return (
    <div className="container-fluid">
      {/* Navegação */}
      <nav className="navbar navbar-expand-lg bg-body-tertiary">
        <div className="container-fluid">
          <a className="navbar-brand" href="index.html">APISW</a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <a className="nav-link active" href="#" onClick={() => setView('people')}>Pessoas</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#" onClick={() => setView('planets')}>Planetas</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <h1 className="text-center">Bem-vindo(a) a API do Star Wars</h1>

      {/* Carregar Personagens ou Planetas */}
      {loading ? (
        <div className="d-flex justify-content-center">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Carregando...</span>
          </div>
        </div>
      ) : (
        <>
          {/* Exibir Personagens */}
          {view === 'people' && (
            
            <div className="accordion mt-4" id="people-accordion">
              {people.map((person, index) => (
                <div className="accordion-item" key={index}>
                  <h2 className="accordion-header" id={`heading-${index}`}>
                    <button
                      className="accordion-button collapsed"
                      type="button"
                      data-bs-toggle="collapse"
                      data-bs-target={`#collapse-${index}`}
                      aria-expanded="false"
                      aria-controls={`collapse-${index}`}
                    >
                      {person.name}
                    </button>
                  </h2>
                  <div
                    id={`collapse-${index}`}
                    className="accordion-collapse collapse"
                    aria-labelledby={`heading-${index}`}
                    data-bs-parent="#people-accordion"
                  >
                    <div className="accordion-body">
                      <p><strong>Nome:</strong> {person.name}</p>
                      <p><strong>Altura:</strong> {person.height} cm</p>
                      <p><strong>Peso:</strong> {person.mass} kg</p>
                      <p><strong>Cor do Cabelo:</strong> {person.hair_color}</p>
                      <p><strong>Cor dos Olhos:</strong> {person.eye_color}</p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}

          {/* Exibir Planetas */}
          {view === 'planets' && (
            <div className="accordion mt-4" id="planets-accordion">
              {planets.map((planet, index) => (
                <div className="accordion-item" key={index}>
                  <h2 className="accordion-header" id={`heading-planet-${index}`}>
                    <button
                      className="accordion-button collapsed"
                      type="button"
                      data-bs-toggle="collapse"
                      data-bs-target={`#collapse-planet-${index}`}
                      aria-expanded="false"
                      aria-controls={`collapse-planet-${index}`}
                    >
                      {planet.name}
                    </button>
                  </h2>
                  <div
                    id={`collapse-planet-${index}`}
                    className="accordion-collapse collapse"
                    aria-labelledby={`heading-planet-${index}`}
                    data-bs-parent="#planets-accordion"
                  >
                    <div className="accordion-body">
                      <p><strong>Clima:</strong> {planet.climate}</p>
                      <p><strong>Terreno:</strong> {planet.terrain}</p>
                      <p><strong>População:</strong> {planet.population}</p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </>
      )}
    </div>
  );
}

export default App;