class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def num_reviews(self):
        return len([review for review in Review.all() if review.customer() == self])

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all_customers if customer.given_name == name]

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        return review

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self._name = name
        Restaurant.all_restaurants.append(self)

    @property
    def name(self):
        return self._name

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def reviews(self):
        return [review for review in Review.all() if review.restaurant == self]

    def customers(self):
        return list(set([review.customer for review in self.reviews()]))

    def average_star_rating(self):
        ratings = [review.rating() for review in self.reviews()]
        if ratings:
            return sum(ratings) / len(ratings)
        else:
            return 0

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating_value = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating_value

    @classmethod
    def all(cls):
        return cls.all_reviews

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    def __str__(self):
        return f"Review by {self.customer.full_name()}: {self.restaurant.name}: Ratings: {self.rating_value}.0 Star"

customer1 = Customer("John", "Doe")
restaurant1 = Restaurant("Awesomely Great Restaurant")
customer1.add_review(restaurant1, 5) # Adding a review

print(customer1.full_name())  # John Doe
for review in restaurant1.reviews(): # Show customer review
    print(review)
print(restaurant1.average_star_rating()) # Calculate average star rating for the restaurant
