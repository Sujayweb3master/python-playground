def main():
    book, author, release_year, goodreads_rating = 'Dracula', 'Bram Stoker', 1897, 4.01

    # print(book + ' is a novel by ' + author + ', published in ' + str(release_year) + '. It has a rating of ' + str(goodreads_rating) + ' on goodreads.')
    print(f'{book} is a novel by {author}, published in {release_year}. It has a rating of {goodreads_rating}')

if __name__ == '__main__':
    main()
