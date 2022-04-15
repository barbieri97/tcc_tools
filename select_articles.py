import pandas as pd


articles = pd.read_csv('all_articles.csv',)

articles.drop_duplicates()



for item in articles['Title']:
    print(item)
    include = input('incluir arquivo? ')
    if include == 'n':
        index = articles[articles['Title']==item].index.tolist()
        articles = articles.drop(index[0])
        print(f'voce deletou esse artigo com index {index}')
    if include == 'stop':
        break

name_arq = input('escolha o nome do novo arquivo csv: ')

articles.to_csv(name_arq, index=False)