from flask import Flask, render_template

meu_site = Flask(__name__, template_folder='templates')  #cria uma instância do Flask, que é a aplicação web, e define a pasta de templates

@meu_site.route('/index')  #decorador que vincula a função abaixo à rota /ola
def indice():
    return render_template('index.html')  #renderiza o template index.html localizado na pasta templates

@meu_site.route('/')
#@meu_site.route('/ola')
def homepage():   #esta função está vinculada a rota raiz e a rota /ola
    return render_template('homepage.html')

@meu_site.route('/contato')
def contato():
    return render_template('contato.html')

@meu_site.route('/usuario')
def dados_usuario():
    nome_usuario = "Rodolfo"
    dados_usu = {"profissão": "Supervisor de recepção", "disciplina": "Desenvolvimento Web III"}
    return render_template('usuario.html', nome=nome_usuario, dados=dados_usu)

@meu_site.route('/rota2')
def rota2():
    resposta = "<H3>Olá, Turma 2026! </H3>" 
    resposta += "<H4> sou a rota 2 </H4>"  #concatena string com o operador += montando uma resposta em HTML
    return resposta


#esta função não está vinculado a rota, mas pode ser usada dentro de uma rota ou outra função ou invocada de fora
def saudacoes(nome): 
    return f"Boa noite, {nome}!. Tudo bem?"

#maiores detalhes nos slides que estão no AVA.
if __name__ == '__main__':  #verifica se o arquivo está sendo executado diretamente, e não importado
    meu_site.run(port=7000)

meu_site.run( port=6000)    #executa caso o o arquivo seja importado, mas não é uma boa prática, pois pode gerar conflito de portas