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
