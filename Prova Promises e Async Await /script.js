async function fetchBreeds() {
    try {
        const response = await fetch('https://api.example.com/breeds');
        if (!response.ok) throw new Error('Network response was not ok.');
        const data = await response.json();
        populateSelect(data.breeds);
    } catch (error) {
        document.querySelector('#loadingMessage').textContent = `Erro: ${error.message}`;
    }
}

function populateSelect(breeds) {
    const select = document.querySelector('#breedSelect');
    breeds.forEach(breed => {
        const option = document.createElement('option');
        option.value = breed.id;
        option.textContent = breed.name;
        select.appendChild(option);
    });
}

async function fetchBreedImages(breedId) {
    document.querySelector('#loadingMessage').textContent = 'Carregando...';
    try {
        const response = await fetch(`https://api.example.com/breeds/${breedId}/images`);
        if (!response.ok) throw new Error('Network response was not ok.');
        const data = await response.json();
        displayImages(data.images);
        document.querySelector('#loadingMessage').style.display = 'none';
    } catch (error) {
        document.querySelector('#loadingMessage').textContent = `Erro: ${error.message}`;
    }
}

function displayImages(images) {
    const gallery = document.querySelector('#gallery');
    gallery.innerHTML = '';
    images.forEach(image => {
        const container = document.createElement('div');
        container.className = 'image-container';
        const img = document.createElement('img');
        img.src = image.url;
        img.alt = image.alt;
        img.className = 'dog-image';
        container.appendChild(img);
        gallery.appendChild(container);
    });
}

document.querySelector('#breedSelect').addEventListener('change', (event) => {
    const breedId = event.target.value;
    if (breedId) {
        fetchBreedImages(breedId);
    }
});

fetchBreeds();
