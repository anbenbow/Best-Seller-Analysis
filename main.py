from book import Book
from data import data_list
from collections import Counter

def data_list_creator(data_list):
    final_data_list = []
    for data in data_list:
        new_data= Book (data)
        final_data_list.append(new_data)
    return final_data_list    

new_data_list = data_list_creator(data_list)

# top_fifty_most_years = list(filter(lambda data: data.id <= 50, new_data_list))
# for data in top_fifty_most_years:
#     print(f'The book {data.name} has been in the top 50 for {str(data.years)} years!')


sorted_by_user_rating = sorted(new_data_list,key=lambda book: book.user_rating, reverse=True)
sorted_by_rating_and_review = sorted(sorted_by_user_rating, key=lambda book: book.number_of_reviews, reverse=True)

c = Counter
# for data in sorted_by_user_rating:
#     print(sorted_by_user_rating['name']['year'])
most_by_rating_and_review = c(sorted_by_rating_and_review.name).most_common()[0]
print(most_by_rating_and_review)
# most_common = counter(data_list).most_common()
# print(data for data in data_list.most_common for data in ['years'])


book_for_most_years = lambda : print('This book has been in the top 50s list for the most years: ')
# result
genre_the_most = lambda : print('This genre has appeared the most in the top 50s list: ')
#result
author_the_most = lambda : print('This author has shown up on the top 50s list the most:')
#result
books_for_each_year = lambda : print('These are the top books for each year:')
#result