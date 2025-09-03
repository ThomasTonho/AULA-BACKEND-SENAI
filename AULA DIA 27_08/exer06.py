class Aluno:
    def __init__(self, nome_aluno, curso, nota_final):
        self.nome_aluno = nome_aluno
        self.curso = curso
        self.nota_final = nota_final

    def status(self):
        print(f"Nome do(a) Aluno(a): {self.nome_aluno}")
        print(f"Curso: {self.curso}")
        print(f"Nota final: {self.nota_final}")
        if self.nota_final > 7:
            print(f"Você foi: APROVADO(A)!")
        else:
            print(f"Você foi: REPROVADO(A)!")

aluno1 = Aluno("Thomás Veloso", "SQL Avançado", 10)
aluno2 = Aluno("Nicolas Pereira", "Python", 8)
aluno3 = Aluno("Mariam Pirela", "Sistemas operacionais", 4)

aluno1.status()
aluno2.status()
aluno3.status()