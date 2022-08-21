class Book:
    def __init__(self, data_list):
        self.id = data_list ['id']
        self.name = data_list ['name']
        self.author = data_list ['author']
        self.user_rating = data_list ['user_rating']
        self.number_of_reviews = data_list ['number_of_reviews']
        self.price = data_list ['price']
        self.year = data_list ['year']
        self.genre = data_list ['genre']

