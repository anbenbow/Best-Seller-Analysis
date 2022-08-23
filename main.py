from asyncio import current_task
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



def run():
    
    books = []
    
    for book_dictionary in data_list:
        new_book = Book(book_dictionary)
        books.append(new_book)

    book_for_most_years(books)
 



    
#    = list(filter(lambda data: data.id <= 50, new_data_list))
# # for data in top_fifty_most_years:
# #     print(f'The book {data.name} has been in the top 50 for {str(data.years)} years!')


# sorted_by_user_rating = sorted(new_data_list,key=lambda book: book.user_rating, reverse=True)
# sorted_by_rating_and_review = sorted(sorted_by_user_rating, key=lambda book: book.number_of_reviews, reverse=True)

# print(sorted_by_user_rating)

# c = Counter
# # for data in sorted_by_user_rating:
# #     print(sorted_by_user_rating['name']['year'])
# most_by_rating_and_review = c(sorted_by_rating_and_review.name).most_common()[0]
# print(most_by_rating_and_review)
# # most_common = counter(data_list).most_common()
# # print(data for data in data_list.most_common for data in ['years'])


# book_for_most_years = lambda : print('This book has been in the top 50s list for the most years: ')

# # times in top 50: ...
# genre_the_most = lambda : print('This genre has appeared the most in the top 50s list: ')
# #genre:
# # number of appearances:
# author_the_most = lambda : print('This author has shown up on the top 50s list the most:')
# #author:
# #times in top 50:
# books_for_each_year = lambda : print('These are the top books for each year:')
# #year:
#name:
#author


















run()