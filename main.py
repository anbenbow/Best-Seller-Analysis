from book import Book
from data import data_list

def data_list_creator(data_list):
    final_data_list = []
    for data in data_list:
        new_data= Book (data)
        final_data_list.append(new_data)
    return final_data_list    

new_data_list = data_list_creator(data_list)
#five_moons_or_less = list(filter(lambda book: book.moons ,= 5, new_data_list))
# for book in five_moons_or_less:
#     print(f'The planet {book.name} has {str(book.moons)} moons!')

# sorted_data = sorted(new_data_list,key=lambda book: book.name)
# for data in sorted_data:
#      print(data.name)
#             OR
sorted_data = sorted(new_data_list,key=lambda book: book.name, reverse=True)
for data in sorted_data:
    print(data.name)