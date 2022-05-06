from subprocess import run

AZUL = '\033[1;94m'
VERDE = '\033[1;32m'
RESET = '\033[0;0m'
VERMELHO = '\033[1;31m'
AMARELO = '\033[1;33m'
VERMELHO_CLARO = '\033[1;91m'

def googlar(nome):
    base_url = 'https://www.google.com/search?q=' + nome
    # o comando abaixo também poderia ser utilizado
    # run(['firefox', '--search', nome])
    run(['firefox', base_url])



if __name__ == '__main__':
    inicio = int(input('deseja iniciar de qual index? '))
    with open('/home/barbieri/Documents/projetos/tools_tcc/meus_artigos.tsv', 'r') as f:
        arq = f.readlines()
        _ = arq.pop(0)
    
    for item in arq:
        index, nome, autor, doi, base, yn = item.split('\t')
        if int(index) < inicio:
            pass
        else:
            print(AZUL + nome + RESET)
            secur = 0
            while True:
                command = input('>> ').strip()
                if command == 'name':
                    googlar(nome)
                elif command == 'doi':
                    googlar(doi)
                elif command == 'incluir':
                    selected = open('resumo_selecionado.tsv', 'a')
                    selected.write(item.replace('\n', '1\n'))
                    selected.close()
                    secur = 1
                    print(VERDE + f'O artigo {nome} foi selecionado' + RESET)
                    break
                elif command == 'excluir':
                    selected = open('resumo_excluido.tsv', 'a')
                    selected.write(item.replace('\n', '0\n'))
                    selected.close()
                    secur = 1
                    print(VERMELHO + f'O artigo {nome} foi excluido' + RESET)
                    break
                elif command == 'next':
                    if secur == 0:
                        print(AMARELO + 'você ainda não decidiu se o artigo foi selecionado ou não...' + RESET)
                    else:
                        break
                elif command == 'base':
                    print(base)
                else:
                    print(VERMELHO_CLARO + 'comando não encontrado' + RESET)




                
            
            


        

