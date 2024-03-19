class Transparence:
    def __init__(self, codigo_orgao_superior, nome_orgao_superior,
                 codigo_orgao, nome_orgao, codigo_unidade_gestora,
                 nome_unidade_gestora, categoria_economica,
                 origem_receita, especie_receita, detalhamento,
                 valor_previsto_atualizado, valor_lancado,
                 valor_realizado, percentual_realizado,
                 data_lancamento, ano_exercicio):
        self.codigo_orgao_superior = codigo_orgao_superior
        self.nome_orgao_superior = nome_orgao_superior
        self.codigo_orgao = codigo_orgao
        self.nome_orgao = nome_orgao
        self.codigo_unidade_gestora = codigo_unidade_gestora
        self.nome_unidade_gestora = nome_unidade_gestora
        self.categoria_economica = categoria_economica
        self.origem_receita = origem_receita
        self.especie_receita = especie_receita
        self.detalhamento = detalhamento
        self.valor_previsto_atualizado = valor_previsto_atualizado
        self.valor_lancado = valor_lancado
        self.valor_realizado = valor_realizado
        self.percentual_realizado = percentual_realizado
        self.data_lancamento = data_lancamento
        self.ano_exercicio = ano_exercicio
