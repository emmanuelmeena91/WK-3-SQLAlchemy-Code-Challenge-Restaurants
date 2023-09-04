# WK-3-SQLAlchemy-Code-Challenge-Restaurants

In this code challenge, we'll be working with a restaurant review domain and implementing various methods in the Restaurant, Review, and Customer classes. These methods will involve relationships, aggregations, and other functionalities specific to the domain.

# Topics
SQLAlchemy Migrations
SQLAlchemy Relationships
Class and Instance Methods
SQLAlchemy Querying

# Instructions
Start by creating the necessary SQLAlchemy migrations for the initial Restaurant and Customer models. Ensure that the migrations include the required columns for establishing relationships.

After setting up the migrations, create a Review model that belongs to both a Restaurant and a Customer. Include a star_rating column to store the rating for each review.

Use the seeds.py file to create instances of Restaurant and Customer for testing purposes.

Implement the following methods in the respective classes:

# Review

customer(): Returns the Customer instance associated with this review.
restaurant(): Returns the Restaurant instance associated with this review.
Restaurant

reviews(): Returns a collection of all the reviews for the restaurant.
customers(): Returns a collection of all the customers who reviewed the restaurant.
Customer

reviews(): Returns a collection of all the reviews left by the customer.
restaurants(): Returns a collection of all the restaurants reviewed by the customer.
Test the implemented methods in the console to ensure they are functioning as expected. Verify that you can retrieve the necessary relationships and collections of objects.

Implement additional methods in the classes:

# Customer

full_name(): Returns the full name of the customer, concatenating the first name and last name in Western style.
favorite_restaurant(): Returns the restaurant instance with the highest star rating from this customer.
add_review(restaurant, rating): Creates a new review for the given restaurant with the specified rating.
delete_reviews(restaurant): Removes all reviews by the customer for the specified restaurant.
Review

full_review(): Returns a formatted string representing the review, including the restaurant name, customer's full name, and star rating.
# Restaurant

fanciest() (class method): Returns a restaurant instance with the highest price.
all_reviews(): Returns a list of strings representing all the reviews for the restaurant, including the restaurant name, customer's full name, and star rating.
Continuously test the implemented methods in the console and ensure they are working correctly.

Once your code is functioning as expected, you can consider refactoring and optimizing your code if you have time. Prioritize getting things working correctly before focusing on code cleanliness.

Remember to save and run your code to verify that everything works as expected. Test each method and relationship in the console to ensure they return the desired results.