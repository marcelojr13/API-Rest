from flask import Flask, jsonify



app = Flask(__name__)

users = [
    {
        'id': 1,
        'name': 'Robert Marques',
        'books': '[2,4,8]',
    },
    {
        'id': 2,
        'name': 'Robert Hrosher',
        'books': '[1,3]'
    },
    {
        'id': 3,
        'name': 'John Delare',
        'books': '[5,6,7]'
    }
]

books = [

    {
        'id': 1,
        'name': 'O Alquimista',
        'autor': 'Paulo Coelho',
        'id_user': 2,
        'status': 'Reservado',
        'dias_em_atraso': 'Sem atraso',
        'multa': '0%',
        'juros_ao_dia': '0%'
    },
    {
        'id': 2,
        'name': 'O Pequeno Príncipe',
        'autor': 'Antoine de Saint-Exupéry',
        'id_user': 1,
        'status': 'Reservado',
        'dias_em_atraso': 'Até 3 dias',
        'multa': '3%',
        'juros_ao_dia': '0.2%'
    },
    {
        'id': 3,
        'name': 'Uma Breve História do Tempo',
        'autor': 'Stephen Hawking',
        'id_user': 2,
        'status': 'Reservado',
        'dias_em_atraso': 'Sem atraso',
        'multa': '0%',
        'juros_ao_dia': '0%'
    },
    {
        'id': 4,
        'name': 'A Cabana',
        'autor': 'William P. Young',
        'id_user': 1,
        'status': 'Reservado',
        'dias_em_atraso': 'Acima 3 dias',
        'multa': '5%',
        'juros_ao_dia': '0.4%'
    },
    {
        'id': 5,
        'name': 'O Ladrão de Raios',
        'autor': 'Rick Riordan',
        'id_user': 3,
        'status': 'Reservado',
        'dias_em_atraso': 'Acima 5 dias',
        'multa': '7%',
        'juros_ao_dia': '0.6%'
    },
    {
        'id': 6,
        'name': 'Capitães de Areia',
        'autor': 'Jorge Amado',
        'id_user': 3,
        'status': 'Reservado',
        'dias_em_atraso': 'Sem atraso',
        'multa': '0%',
        'juros_ao_dia': '0%'
    },
    {
        'id': 7,
        'name': 'Ulisses',
        'autor': 'James Joyce',
        'id_user': 3,
        'status': 'Reservado',
        'dias_em_atraso': 'Sem atraso',
        'multa': '0%',
        'juros_ao_dia': '0%'
    },
    {
        'id': 8,
        'name': 'Crime e Castigo',
        'autor': 'Fiódor Dostoiévski',
        'id_user': 1,
        'status': 'Reservado',
        'dias_em_atraso': 'Sem atraso',
        'multa': '0%',
        'juros_ao_dia': '0%'
    },
    {
        'id': 9,
        'name': 'Ilíada e Odisseia',
        'autor': 'Homero',
        'id_user': 0,
        'status': 'Disponível',
        'dias_em_atraso': 'Sem atraso',
        'multa': '0%',
        'juros_ao_dia': '0%'
    },
    {
        'id': 10,
        'name': 'Os Lusíadas',
        'autor': 'Luís de Camões',
        'id_user': 0,
        'status': 'Disponível',
        'dias_em_atraso': 'Sem atraso',
        'multa': '0%',
        'juros_ao_dia': '0%'
    },

]

@app.route('/books', methods=['GET'])
def list_books():
    return jsonify(books),200

@app.route('/', methods=['GET'])
def home():
    return jsonify('Hello! Welcome to my API Rest!'),200

@app.route('/client/<int:id>/books', methods=['GET'])
def book_per_client(id):
    book_per_client = {}
    count = 1
    provisory = 'Livro'
    new_provisory = ''
    for book in books:
        if book['id_user'] == id:
            new_provisory = provisory + ' - '  + str(count)
            book_per_client[new_provisory] = book
            count = count + 1

    if len(book_per_client) > 0:
        return jsonify(book_per_client),200
    else:
        return jsonify({'error': 'Not Found'}),404

@app.route('/books/<int:id>/reserve', methods=['GET'])
def book_for_reserve(id):
    for book in books:
        if book['id'] == id:
            return jsonify(book),200


if __name__ == '__main__':
    app.run(debug=True)
