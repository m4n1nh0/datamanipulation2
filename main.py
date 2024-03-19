import os

from domain.archive import Archive

if __name__ == '__main__':
    file_name = "dados_transparencia.csv"
    arquivo = Archive(file_name)
    if os.path.exists(file_name):
        print(arquivo.file_read())
    else:
        arquivo.create_archive()
