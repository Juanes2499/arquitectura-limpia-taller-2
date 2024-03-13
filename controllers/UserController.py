from flask import Flask, jsonify, request
from repositories.UserRepository import UserRepository
from services.CreateUserUseCase import CreateUserUseCase

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def create_user():

    dataJson = request.json
    name = dataJson.get("name")
    email = dataJson.get("email")
    password = dataJson.get("password")

    useCase = CreateUserUseCase(UserRepository())

    stateCreated = useCase.execute(name, email, password)

    print(stateCreated)

    return jsonify({'status': stateCreated, 'user': dataJson}), 201

if __name__ == '__main__':
    app.run(debug=True)