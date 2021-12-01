import requests, json

url = 'https://www.googleapis.com/books/v1/volumes?q='

def searchBooks(q):
    books = []

    q = '+'.join(q.split()) # eg. harry+potter

    full_url = url + q

    res = requests.get(full_url)

    json_data = json.loads(res.text)
    for book in json_data['items']:
        
        try:
            title = book['volumeInfo']['title']
        except(KeyError):
            releaseDate = '?'

        try:
            authors = ', '.join(book['volumeInfo']['authors'])
        except(KeyError):
            releaseDate = '?'

        try:
            desc = book['volumeInfo']['description']
        except(KeyError):
            releaseDate = '?'

        try:
            releaseDate = book['volumeInfo']['publishedDate']
        except(KeyError):
            releaseDate = '?'

        books.append((title, authors, desc, releaseDate))
        #books.append(f'Title: {title}\n\nAuthor(s): {authors}\n\nDescription: {desc}\n\nRelease Date: {releaseDate}\n\n\n')
    return books