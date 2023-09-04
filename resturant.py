class Restaurant(Base):
    # ... existing code ...

    def reviews(self):
        return self.reviews

    def customers(self):
        return [review.customer for review in self.reviews]

    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        return [review.full_review() for review in self.reviews]