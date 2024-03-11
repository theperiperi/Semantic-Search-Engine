const form = document.getElementById('searchForm');
const searchInput = document.getElementById('searchInput');
const resultsContainer = document.getElementById('results');

form.addEventListener('submit', async function(event) {
    event.preventDefault();
    
    // Clear previous results
    resultsContainer.innerHTML = '';
    
    const query = searchInput.value.trim();
    
    if (query === '') {
        return;
    }
    
    try {
        const response = await fetch('/api/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query })
        });
        const data = await response.json();
        
        if (data.error) {
            throw new Error(data.error);
        }
        
        displayResults(data.results);
    } catch (error) {
        console.error('Error fetching data:', error.message);
    }
});

function displayResults(results) {
    results.forEach(result => {
        const resultElement = document.createElement('div');
        resultElement.classList.add('result');
        
        const titleElement = document.createElement('h3');
        titleElement.textContent = result[0];
        
        const descriptionElement = document.createElement('p');
        descriptionElement.textContent = result[1];
        
        const linkElement = document.createElement('a');
        linkElement.textContent = 'Watch Video';
        linkElement.href = `https://www.youtube.com/watch?v=${result[2]}`;
        linkElement.target = '_blank'; // Open link in new tab
        
        resultElement.appendChild(titleElement);
        resultElement.appendChild(descriptionElement);
        resultElement.appendChild(linkElement);
        
        resultsContainer.appendChild(resultElement);
    });
}
