from bottle import route, run, request


#mento send é disparado quando ocorre uma requisição na raiz
@route('/', method='POST')

#função para caputrar dados do formulário e enfileirar as mensagens
def send():
    assunto = request.forms.get('assunto')
    mensagem = request.forms.get('mensagem')
    return 'Mensagem enfileirada! Assunto: {} Mensagem: {}'.format(assunto, mensagem
    )


# teste para saber se este aquivo é o principal
# serviço
if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)