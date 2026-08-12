from flask import Flask

meu_site = Flask(__name__)

@meu_site.route('/')
def root():
    return 'Olá, turma. É minha 1ª página com flask!'

@meu_site.route('/contato')
def contato():
    return 'e-mail:rodolfo.viana@estudante.ifro.edu.br'

def saudacoes(nome):
    return f'Olá, {nome}. Seja bem-vindo(a) ao meu site!'

if __name__ == '__main__':
    meu_site.run(port=7000)

meu_site.run(port=6000)