def gravar_arquivo(nome_do_arquivo, valor):
    with open(f'{nome_do_arquivo}.txt', 'w') as handler:
        handler.write(f'{valor}')


if __name__ == '__main__':
    teste = 'mais um teste'
    gravar_arquivo('teste', teste)