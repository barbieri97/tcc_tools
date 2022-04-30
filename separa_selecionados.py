with open('/home/barbieri/Documents/projetos/tools_tcc/seleção pelo titulo - Página1.tsv', 'r') as file:
    data = file.readlines()
    _ = data.pop(0)

data_list = []    
for item in data:
    article = item.split('\t')
    data_list.append(article)

arq_selecionados = open('/home/barbieri/Documents/projetos/tools_tcc/selecionados.tsv', 'a')
arq_nao_seleceionados = open('/home/barbieri/Documents/projetos/tools_tcc/nao_selecionados.tsv', 'a')
title = 'index\tname\tauthor\tDOI\tbase\n'
arq_nao_seleceionados.write(title)
arq_selecionados.write(title)

incluido = 0
excluido = 0

for item in data_list:
    if item[2] == '0':
        item[0] = str(excluido + 1)
        _ = item.pop(2)
        article_data = '\t'.join(i for i in item)
        arq_nao_seleceionados.write(article_data)
        excluido += 1
    elif item[2] == '1':
        item[0] = str(incluido + 1)
        _ = item.pop(2)
        article_data = '\t'.join(i for i in item)
        arq_selecionados.write(article_data)
        incluido += 1
    else:
        print(f'O artigo {item[1]} não foi avaliado')

arq_nao_seleceionados.close()
arq_selecionados.close()




print(f'o total de artigos selecionados foram: {incluido}\nO total de artigos excluidos foram: {excluido}')