from flask import Blueprint, jsonify, request

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():
    try:
        email, password, _session = (request.json.get(key) for key in ('email', 'password', '_session'))

        # keys = ['email', 'password', '_session']
        values = []

        for key in ('email', 'password', '_session'):
            values.append(request.json.get(key))

        print(values)

        email, password, _session = values

        return jsonify({
                "access_token": email,
                "user": password
            }), 200
        # user = User.authenticate_user(username, password)
        # if user:
        #     access_token = create_access_token(identity=username)
        #     return jsonify({
        #         "access_token": access_token,
        #         "user": user.to_dict()
        #     })
        # return jsonify({"message": "Credenciais inválidas!"}), 401
    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro ao realizar login.\nDescrição: {e}'}), 500