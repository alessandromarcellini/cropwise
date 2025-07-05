from models.routes.users import NonAdminUser

class LoginController:
    def __init__(self):
        pass

    def login(self, email: str, password: str):
        pass

    def logout(self):
        pass

    def deactivate_account(self, user_id: str):
        pass

class SignUpController:
    def __init__(self):
        pass

    def sign_up(self, user: NonAdminUser):
        # TODO probably will use the strategy pattern to signup different types of users
        pass