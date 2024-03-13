from entities.User import User

class CreateUserUseCase:
    def __init__(self, userRepository):
        self.userRepository = userRepository

    def execute(self, name, email, password):
        user = User(name, email, password)
        userCreated = self.userRepository.saveUser(user)
        return userCreated