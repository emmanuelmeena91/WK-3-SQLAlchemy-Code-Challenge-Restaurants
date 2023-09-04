class Customer(Base):
    # ... existing code ...

    def reviews(self):
        return self.reviews

    def restaurants(self):
        return [review.restaurant for review in self.reviews]

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def favorite_restaurant(self):
        reviews_by_rating = sorted(self.reviews, key=lambda review: review.star_rating, reverse=True)
        if reviews_by_rating:
            return reviews_by_rating[0].restaurant
        else:
            return None

    def add_review(self, restaurant, rating):
        review = Review(star_rating=rating, restaurant=restaurant, customer=self)
        self.reviews.append(review)
        session.add(review)
        session.commit()

    def delete_reviews(self, restaurant):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            self.reviews.remove(review)
            session.delete(review)
        session.commit()