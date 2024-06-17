function searchBooks() {
    const query = document.getElementById('book-search-input').value;
    fetch(`https://www.googleapis.com/books/v1/volumes?q=${query}`)
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById('book-results');
            resultsDiv.innerHTML = '';
            data.items.forEach(item => {
                const book = item.volumeInfo;
                const bookDiv = document.createElement('div');
                bookDiv.classList.add('book');
                bookDiv.innerHTML = `
                    <h3>${book.title}</h3>
                    <p>${book.authors ? book.authors.join(', ') : 'Autor no disponible'}</p>
                    <p>${book.publishedDate ? book.publishedDate : 'Fecha de publicación no disponible'}</p>
                    <p>${book.description ? book.description : 'Descripción no disponible'}</p>
                    <img src="${book.imageLinks ? book.imageLinks.thumbnail : 'Imagen no disponible'}" alt="Portada del libro">
                `;
                resultsDiv.appendChild(bookDiv);
            });
        })
        .catch(error => {
            console.error('Error al buscar libros:', error);
        });
}
