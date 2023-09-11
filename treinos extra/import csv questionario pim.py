import csv

# Classe para armazenar informações sobre uma obra
class Obra:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

# Classe para armazenar respostas do questionário
class Resposta:
    def __init__(self, nome_visitante, gostou_obra, comentario, aceitou_termos):
        self.nome_visitante = nome_visitante
        self.gostou_obra = gostou_obra
        self.comentario = comentario
        self.aceitou_termos = aceitou_termos

# Função para coletar respostas do questionário
def coletar_respostas(obra, num_respostas):
    respostas = []

    print(f"Informações sobre a obra:\nNome: {obra.nome}\nDescrição: {obra.descricao}\n")

    for i in range(num_respostas):
        print(f"Visitante {i + 1}:")
        nome_visitante = input("Nome do visitante: ")
        gostou_obra = int(input("Gostou da obra? (1 - Sim, 2 - Não): "))
        comentario = input("Comentários (opcional): ")
        aceitou_termos = input("Você aceita os termos da LGPD? (S - Sim, N - Não): ").strip().lower()

        if aceitou_termos == 's':
            aceitou_termos = True
        else:
            aceitou_termos = False

        resposta = Resposta(nome_visitante, gostou_obra, comentario, aceitou_termos)
        respostas.append(resposta)

    return respostas

# Função para salvar respostas em um arquivo CSV
def salvar_respostas_csv(respostas):
    with open('respostas.csv', mode='w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(['Nome do Visitante', 'Gostou da Obra', 'Comentário', 'Aceitou Termos LGPD'])

        for resposta in respostas:
            escritor_csv.writerow([resposta.nome_visitante, resposta.gostou_obra, resposta.comentario, resposta.aceitou_termos])

    print("Respostas salvas em 'respostas.csv'.")

def main():
    obra = Obra("Bis 16 de Santos Dumont", "Uma das primeiras aeronaves construídas por Santos Dumont.")
    
    num_respostas = int(input("Quantos visitantes responderão ao questionário? "))
    
    respostas = coletar_respostas(obra, num_respostas)
    salvar_respostas_csv(respostas)

if __name__ == "__main__":
    main()
