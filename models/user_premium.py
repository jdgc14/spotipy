from .user import User


class UserPremium(User):
    def __init__(self, username, password, email, subscription=True, **kwargs):
        super().__init__(username, password, email, subscription, **kwargs)