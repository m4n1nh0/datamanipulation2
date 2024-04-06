import csv

from model.transparence import Transparence


class Archive:

    def __init__(self, path_file):
        self.path_file = path_file

    def create_archive(self):
        with open(self.path_file, "w", encoding="utf-8") as file:
            csv.writer(file, delimiter=";")

    def file_read(self):
        with open(self.path_file, "r", encoding="latin-1") as file:
            leitor = csv.reader(file, delimiter=";")

            next(leitor, None)
            datas = []
            for line in leitor:
                transparence = Transparence(
                    line[0],
                    line[1],
                    line[2],
                    line[3],
                    line[4],
                    line[5],
                    line[6],
                    line[7],
                    line[8],
                    line[9],
                    line[10],
                    line[11],
                    line[12],
                    line[13],
                    line[14],
                    line[15])
                datas.append(transparence)

        return datas

    def file_write(self, dados):
        with open(self.path_file, "w", encoding="latin-1") as file:
            gravador = csv.writer(file, delimiter=";")

            # Escreve cabeçalho
            gravador.writerow([
                "CODIGO_ORGAO_SUPERIOR",
                "NOME_ORGAO_SUPERIOR",
                "CODIGO_ORGAO",
                "NOME_ORGAO",
                "CODIGO_UNIDADE_GESTORA",
                "NOME_UNIDADE_GESTORA",
                "CATEGORIA_ECONOMICA",
                "ORIGEM_RECEITA",
                "ESPECIE_RECEITA",
                "DETALHAMENTO",
                "VALOR_PREVISTO_ATUALIZADO",
                "VALOR_LANCADO",
                "VALOR_REALIZADO",
                "PERCENTUAL_REALIZADO",
                "DATA_LANCAMENTO",
                "ANO_EXERCICIO",
            ])

            # Escreve os dados
            for registro in dados:
                gravador.writerow([
                    registro.codigo_orgao_superior,
                    registro.nome_orgao_superior,
                    registro.codigo_orgao,
                    registro.nome_orgao,
                    registro.codigo_unidade_gestora,
                    registro.nome_unidade_gestora,
                    registro.categoria_economica,
                    registro.origem_receita,
                    registro.especie_receita,
                    registro.detalhamento,
                    registro.valor_previsto_atualizado,
                    registro.valor_lancado,
                    registro.valor_realizado,
                    registro.percentual_realizado,
                    registro.data_lancamento,
                    registro.ano_exercicio,
                ])

    @staticmethod
    def edit_file(dados, position, new_register):
        """
        Edit position register from list.

        :parameter:
            dados (list): A lista a ser modificada.
            position (int): A posição do elemento a ser editado.
            new_register (list): A lista de registros a ser modificada.

        :exception:
            IndexError: Se a posição estiver fora da faixa da lista.

        :return:
            None: O método não retorna nenhum valor.
        """
        dados[position] = new_register

    @staticmethod
    def delete_data(dados, position):
        """
        Exclude element register from list.

        :parameter:
            dados (list): A lista a ser modificada.
            position (int): A posição do elemento a ser excluído.

        :exception:
            IndexError: Se a posição estiver fora da faixa da lista.

        :return:
            None: O método não retorna nenhum valor.
        """
        del dados[position]
        