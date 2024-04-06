import os

from domain.archive import Archive
from model.transparence import Transparence

if __name__ == '__main__':
    file_name = "dados_transparencia.csv"
    arquivo = Archive(file_name)
    data = []
    if os.path.exists(file_name):
        data = arquivo.file_read()

        # Edita o segundo registro
        novo_registro = Transparence(
            "123456",
            "Novo nome órgão superior",
            "1234",
            "Novo nome órgão",
            "5678",
            "Nova nome unidade gestora",
            "Nova categoria econômica",
            "Nova origem receita",
            "Nova espécie receita",
            "Novo detalhamento",
            "1000.00",
            "900.00",
            "800.00",
            "80.00",
            "2023-03-10",
            "2024",
        )
        arquivo.edit_file(data, 1, novo_registro)

        arquivo.delete_data(data, 2)

        arquivo.file_write(data)
        
    else:
        arquivo.create_archive()

        # Edita o segundo registro
        novo_registro = Transparence(
            "123456",
            "Novo nome órgão superior",
            "1234",
            "Novo nome órgão",
            "5678",
            "Nova nome unidade gestora",
            "Nova categoria econômica",
            "Nova origem receita",
            "Nova espécie receita",
            "Novo detalhamento",
            "1000.00",
            "900.00",
            "800.00",
            "80.00",
            "2023-03-10",
            "2024",
        )
        arquivo.edit_file(data, 1, novo_registro)

        arquivo.file_write(data)
        