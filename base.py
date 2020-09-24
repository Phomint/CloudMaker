import First as f
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfile

def fonte():
    try:
        Tk().withdraw()
        df = pd.read_excel(askopenfile(filetypes=[("Excel files", ".xlsx .xls")]).name)
        print('Sucesso na leitura do arquivo')
    except Exception as a:
        print('Erro ao salvar arquivo\n'+a)

    print(df.columns)
    col = input('Qual das colunas abaixo é sua principal fonte: ')

    return df[col]

if __name__ == '__main__':
    msg = '''Programa para criar nuvem de palavras de forma simplificada \n[Pressione ENTER] para continuar ...'''

    input(msg)
    dados = fonte()
    Tk().withdraw()
    opt = input('Deseja inserir imagem de fundo[S/n]: ')
    if opt.lower() == 's':
        try:
            image = askopenfile(filetypes=["Image Files", ".jpeg .jpg .png"]).name
            print('Imagem Coletada com sucesso!')
        except Exception as a:
            print('Erro ao pegar a imagem\n'+a)

    opt = input('Deseja confirgura tamanho da imagem[S/n]: ')
    if opt.lower() == 's':
        x = int(input('Tamanho eixo X: '))
        y = int(input('Tamanho eixo Y: '))

        tamanho = [x, y]

    try:
        nuvem = f.cria_cloud(fonte=dados, image=image, tamanho=tamanho, stopwords=None)
        print('Nuvem criada')
    except Exception as a:
        print('Erro na criação do nuvem\n'+a)

    opt = input('Deseja visualizar antes de salvar[s/N]: ')
    if opt.lower() == 's':
        try:
            f.visualizar(nuvem)
        except Exception as a:
            print('Erro na função de visualizar\n'+a)

    opt = input('Deseja salvar[S/n]: ')
    if opt.lower() == 's':
        try:
            f.salvar(nuvem)
            print('Salvo com sucesso!')
        except Exception as a:
            print('Erro ao salvar\n'+a)
    print('Encerramento . . .')
