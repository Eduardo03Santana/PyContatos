from Contatos import Contato
from Conexao import BD
from time import sleep


def Run():
    ativo = True
    tela = 0
    mensagem = ''
    while ativo:
        bd = BD()
        bd.abrirConexao()
        if tela == 0:
            print('\n'*100,f"""------------------------------- MENU INICIAL -------------------------------
{mensagem}
Por Gentileza, Escolha uma das ações:

1) Listar Contatos
2) Inserir Contato
3) Editar Contato
4) Deletar Contato
5) Detalhar Contato
0) Encerrar

""")
            mensagem = ''
            try:
                escolha = int(input("Sua Escolha:\n").strip())
                if escolha > 5 or escolha < 0:
                    raise Exception("Numero Escolhido fora do alcance das opcoes")
                tela = escolha
            except:
                mensagem = """ --------------- Por Informe Um Numero Valido ---------------"""
            if escolha == 0:
                bd.fecharConexao()
                print("------------------------- Encerrando, volte sempre -------------------------")
                ativo = False
                sleep(10)

        elif tela == 1:
            print(f"""------------------------------- LISTANDO CONTATOS -------------------------------""")
            print("ID ------ NOME ---------------------------------- Numero --------- Email")
            for contato in bd.readAllContatos():
                print(f"{contato.id} {'-' * (8 - len(contato.id)) if 8 - len(contato.id) > 0 else '-'} ", end='')
                print(f"""{contato.nome if len(contato.nome) < 40 else f"{contato.nome[0:34]}..."} {'-' * (38 - len(contato.nome)) if 38 - len(contato.nome) > 0 else '-' } """, end='')
                print(f"""{contato.numero if len(contato.numero) < 15 else f"{contato.numero[0:10]}... "} {'-' * (15 - len(contato.numero)) if 15 - len(contato.numero) > 0 else '-'} """, end = '')
                print(f"{contato.email}")
            input("Aperte enter para voltar ")
            tela = 0

        elif tela == 2:
            info = []
            print("------------------------- Criando Contato -------------------------")
            if bd.criarContato(Contato(input("Insira o nome completo do Contato: \n").strip(), input("Insira o Numero de Telefone/Celular do Contato: \n").strip(),
                               input("Insira o Email do Contato: (Enter Para deixar em Branco) \n").strip())):
                mensagem = '------------------------- Contato Criado com Sucesso -------------------------'
                tela = 0
            else:
                print('------------------------- Ops, Não foi possivel inserir o contato, tente novamente! -------------------------')

        elif tela == 3:
            print(f"------------------------- Editando Contato ------------------------- \n------ {mensagem} ------")
            mensagem = ''
            contato = bd.readContatoById(input("Insira o ID do Contato que deseja editar: \n"))
            if contato:
                contatoNovo = Contato('','','')
                contatoNovo.nome = input(f"Nome Atual: {contato.nome}\nNovo nome (Enter para manter Nome):\n")
                contatoNovo.numero = input(f"Numero Atual: {contato.numero}\nNovo numero (Enter para manter Numero):\n")
                contatoNovo.email = input(f"Email Atual: {contato.email}\nNovo email (Enter para manter Email):\n")
                if contatoNovo.nome != '': contato.nome = contatoNovo.nome
                if contatoNovo.numero != '': contato.numero = contatoNovo.numero
                if contatoNovo.email != '': contato.email = contatoNovo.email

                if bd.updateContato(contato):
                    mensagem = '------------------------- Contato Editado com Sucesso -------------------------'
                    tela = 0
                else:
                    print('------------------------- Ops, Não foi possivel editar o contato, tente novamente! -------------------------')
                del contatoNovo
            else:
                mensagem = 'Este contato nao foi encotrado'
            del contato
        elif tela == 4:
            print(f"------------------------- Deletando Contato ------------------------- \n------ {mensagem} ------")
            mensagem = ''
            inp = input("Insira o ID do Contato que deseja Deletar (Zero para cancelar): \n")
            if inp == 0: tela = 0
            contato = bd.readContatoById(inp)
            del inp
            if contato:
                if bd.deleteContato(contato):
                    mensagem = '------------------------- O Contado contato.nome foi Deletado com Sucesso -------------------------'
                    tela = 0
                else:
                    print('------------------------- Ops, Não foi possivel deletar o contato, tente novamente! -------------------------')
                
            else:
                mensagem = 'Este contato nao foi encotrado'

        elif tela == 5:
            print(f"------------------------- Detalhando Contato ------------------------- \n------ {mensagem} ------")
            mensagem = ''
            contato = bd.readContatoById(input("Insira o ID do Contato que deseja ver detalhadamente: \n"))
            if contato:
                print(contato)
                tela = 0
                input("Aperte Enter Para Continuar")
            else: mensagem = 'Este contato nao foi encotrado'
            del contato

