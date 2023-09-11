"""
def main():
    # Pergunta quantos semestres o aluno cursou
    num_semestres = int(input("Quantos semestres você cursou? "))
    
    # Verifica o número de semestres e executa o código correspondente
    if 4 <= num_semestres <= 10:
        gastos_por_semestre = []
        for semestre in range(1, num_semestres + 1):
            gasto = float(input(f"Quanto você gastou no {semestre}° semestre? "))
            gastos_por_semestre.append(gasto)
        
        # Agora você tem uma lista de gastos por semestre para cálculos posteriores
        # Você pode realizar cálculos ou armazenar esses valores conforme necessário
        print("Gastos por semestre:", gastos_por_semestre)
    else:
        print("Número de semestres fora do intervalo permitido.")

if __name__ == "__main__":
    main()
"""
def main():
    print("Bem-vindo ao CGF - Calculadora de Gastos com Faculdade")
    
    # Pergunta quantos semestres o aluno cursou
    num_semestres = int(input("Quantos semestres você cursou? "))
    
    if 4 <= num_semestres <= 10:
        mensalidades_por_semestre = []
        for semestre in range(1, num_semestres + 1):
            mensalidade = float(input(f"Digite o valor da mensalidade do {semestre}° semestre: "))
            mensalidades_por_semestre.extend([mensalidade] * 6)  # 6 meses por semestre
        
        aulas_por_mes = int(input("Quantos meses de aula tinha em cada semestre? "))
        dias_de_aula_por_semana = int(input("Quantos dias de aula por semana? "))
        
        # Realiza os cálculos necessários
        total_gasto = sum(mensalidades_por_semestre)
        valor_por_dia_de_aula = total_gasto / (num_semestres * aulas_por_mes * dias_de_aula_por_semana)
        valor_por_dia_sem_aula = total_gasto / (num_semestres * (12 - aulas_por_mes) * 7)
        valor_pago_por_ano = total_gasto / (num_semestres / 2)
        valor_por_semana_media = total_gasto / ((num_semestres * 12 * 7) + (num_semestres * (12 - aulas_por_mes) * 7 / 2))
        valor_medio_por_dia = total_gasto / (num_semestres * 12 * 7)
        valor_gasto_ferias = valor_por_dia_sem_aula * (num_semestres * (12 - aulas_por_mes) * 7 / 2)

        
        # Exibe os resultados
        print(f"\nValor total gasto no curso: R${total_gasto:.2f}")
        print(f"Valor pago por dia de aula: R${valor_por_dia_de_aula:.2f}")
        print(f"Valor pago nos dias sem aula: R${valor_por_dia_sem_aula:.2f}")
        print(f"Valor pago por ano de faculdade: R${valor_pago_por_ano:.2f}")
        print(f"Valor gasto por semana em média: R${valor_por_semana_media:.2f}")
        print(f"Valor médio de cada dia de aula: R${valor_medio_por_dia:.2f}")
        print(f"Valor gasto nas férias: R${valor_gasto_ferias:.2f}")
    else:
        print("Número de semestres fora do intervalo permitido.")

if __name__ == "__main__":
    main()

