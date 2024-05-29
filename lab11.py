def ex111():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating
        def describe_restaurant(self):
            print("Restaurant name:", self.restaurant_name)
            print("Cuisine type:", self.cuisine_type)
            print("Rating:", self.rating)
        def open_restaurant(self):
            print("The restaurant", self.restaurant_name, "is now open!")

        def update_rating(self, new_rating):
            self.rating = new_rating

    newRestaurant = Restaurant("Teremok", "Russian", 4.8)
    newRestaurant.update_rating(3.7)
    restaurant1 = Restaurant("a", "Japanese", 3.2)
    newRestaurant.update_rating(4.0)
    restaurant2 = Restaurant("b", "Italian", 4.1)
    newRestaurant.update_rating(4.7)
    restaurant3 = Restaurant("c", "Georgian", 4.0)
    newRestaurant.update_rating(4.2)



    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()
ex111()
