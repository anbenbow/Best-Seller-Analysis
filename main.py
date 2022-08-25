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
    books_that_are_fiction = [book for book in books if book.genre == 'Fiction']
    books_that_are_non_fiction = [book for book in books if book.genre == 'Non Fiction']

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
    distinct_books = []
    
    for book in books:
        current_book_names_in_list = [dist_book.name for dist_book in distinct_books]
        if book.name not in current_book_names_in_list:
            distinct_books.append(book)

    author_names = [dist_book.author for dist_book in distinct_books]
    distinct_author_names = set(author_names)

    top_author = {'name':'','count':0}

    for distinct_author in distinct_author_names:
        list_of_author_duplicates = [author for author in author_names if author == distinct_author]
        if top_author['count'] < len(list_of_author_duplicates):
            top_author['name'] = distinct_author
            top_author['count'] = len(list_of_author_duplicates)
    print(f"Here is the result for the author that appears the most in the top 50 list:\nAuthor Name: {top_author['name']}\nNumber of Books: {top_author['count']}")              
    print('')

def books_for_each_year (books):
    # oh_nine_books = []
    # top_of_oh_nine = {'number_of_reviews':'','count':0}
    for book in books:
        book_years = [book.year for book in books]
        book_reviews = [book.number_of_reviews for book in books]
        
        
        books_sorted_by_year = sorted(book_years, book_reviews,reverse=True)
    #     
    #     books_sorted_by_reviews = sorted(book_reviews, reverse=True)
    # #books_sorted_by_year_and_review=
    print(books_sorted_by_year)
  #  for book in books_sorted_by_year:
     
  






def run():
    
    books = []
    
    for book_dictionary in data_list:
        new_book = Book(book_dictionary)
        books.append(new_book)

    book_for_most_years(books)
    genre_most_appeared(books)
    author_the_most(books)
    books_for_each_year(books)


















run()