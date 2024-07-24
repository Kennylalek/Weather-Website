// script.js
document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.querySelector('#city-input');
    const suggestionsList = document.querySelector('#suggestions');

    let records = [];

    fetch('/get_cities')
        .then(response => response.json())
        .then(data => {
            records = data.RECORDS;
        })
        .catch(error => console.error('Error fetching suggestions: ', error));

    searchInput.addEventListener('input', function () {
        const query = this.value.toLowerCase();
        suggestionsList.innerHTML = '';
        
        if (query) {
            const Suggestions = records
            .filter(record => record.owm_city_name.toLowerCase().includes(query));

            if (Suggestions.length > 0 && query.length >= 2) {
                Suggestions.forEach(record => {
                    const listItem = document.createElement('li');
                    const content = `${record.owm_city_name}, ${record.country_short}`
                    listItem.textContent = content;
                    suggestionsList.appendChild(listItem);

                    listItem.addEventListener('click', function () {
                        searchInput.value = content;
                        suggestionsList.innerHTML = '';
                        suggestionsList.style.display = 'none';
                    });
                });

                suggestionsList.style.display = 'block';
            } 
            else {
                suggestionsList.style.display = 'none';
            }
        } 
        else {
            suggestionsList.style.display = 'none';
        }
    });

    document.addEventListener('click', function (event) {
        if (!event.target.closest('.autocomplete')) {
            suggestionsList.innerHTML = '';
            suggestionsList.style.display = 'none';
        }
    });
});
