from book import Book
from data import data_list
from collections import Counter


def book_for_most_years (books):
    current_top_book = {'name':'','count':0}
    book_names = [book.name for book in books]
    book_names_distinct = set(book_names)
    for distinct_book_name in book_names_distinct:
        list_of_specific_book = [book_name for book_name in book_names if book_name == distinct_book_name]
        if current_top_book['count'] < len(list_of_specific_book):
            current_top_book['name'] = distinct_book_name
            current_top_book['count'] = len(list_of_specific_book)

    print('This book has been in the top 50s list for the most years: ')
    print(f"Name: {current_top_book['name']}")
    print(f"Times in Top 50: {current_top_book['count']}")
    print('')

def genre_most_appeared (books):
    top_genre = {'genre':'','count':0}
    books_that_are_fiction = [book for book in books if book.genre == 'Fiction']
    books_that_are_non_fiction = [book for book in books if book.genre == 'Non-Fiction']

    fiction_count = len(books_that_are_fiction)
    non_fiction_count = len(books_that_are_non_fiction)

    if fiction_count > non_fiction_count:
        print(f"Based on my findings there are more Fiction books in the top 50 list than Non-Fiction.\nFiction Count: {fiction_count}\nNon-Fiction Count: {non_fiction_count}")
    elif fiction_count == non_fiction_count:
        print('There are the same amount of Fiction and Non-Fiction books in the top 50 list.')
    else:
        print(f"Based on my findings there are more Non-Fiction books in the top 50 list than Fiction.\nFiction Count: {fiction_count}\nNon-Fiction Count: {non_fiction_count}") 
    
    print('')

def author_the_most (books):
    top_author = {'author':'','count':0}
    book_authors = [book.author for book in books]   
    author_count = Counter(book_authors) 
    print(author_count)

  








def run():
    
    books = []
    
    for book_dictionary in data_list:
        new_book = Book(book_dictionary)
        books.append(new_book)

    book_for_most_years(books)
    genre_most_appeared(books)
    author_the_most(books)
 


















run()