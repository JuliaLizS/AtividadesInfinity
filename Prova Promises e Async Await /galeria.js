
const breedSelect = document.getElementById('breedSelect');
const gallery = document.getElementById('gallery');
const loadingMessage = document.getElementById('loadingMessage');


async function fetchData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Erro: ${response.status} - ${response.statusText}`);
        }
        return await response.json();
    } catch (error) {
        throw new Error(`Erro ao buscar dados: ${error.message}`);
    }
}


async function loadBreeds() {
    try {
        const data = await fetchData('https://dog.ceo/api/breeds/list/all');
        populateBreedSelect(data.message);
    } catch (error) {
        displayError(`Falha ao carregar raças. ${error.message}`);
    }
}


function populateBreedSelect(breeds) {
    breedSelect.innerHTML = '<option value="">Selecione uma raça</option>';
    Object.keys(breeds).forEach(breed => {
        const option = document.createElement('option');
        option.value = breed;
        option.textContent = capitalize(breed);
        breedSelect.appendChild(option);
    });
}


function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}


async function loadBreedImages(breed) {
    try {
        showLoading(); 
        const data = await fetchData(`https://dog.ceo/api/breed/${breed}/images`);
        displayImages(data.message);
    } catch (error) {
        displayError(`Falha ao carregar imagens. ${error.message}`);
    } finally {
        hideLoading();
    }
}


function displayImages(images) {
    gallery.innerHTML = images.map(imageUrl => `
        <div class="image-container">
            <img src="${imageUrl}" alt="Imagem de um cachorro" class="dog-image" />
        </div>
    `).join('');
}


function showLoading() {
    loadingMessage.textContent = 'Carregando imagens...';
    loadingMessage.style.display = 'block';
}


function hideLoading() {
    loadingMessage.style.display = 'none';
}


function displayError(message) {
    gallery.innerHTML = `<p class="error">${message}</p>`;
}


breedSelect.addEventListener('change', (event) => {
    const selectedBreed = event.target.value;
    if (selectedBreed) {
        loadBreedImages(selectedBreed);
    } else {
        gallery.innerHTML = ''; 
    }
});


loadBreeds();
