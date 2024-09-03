import json

def calcular_faturamento(vetor):
    if not vetor:
        return "O vetor está vazio."

    faturamento_filtrado = [valor for valor in vetor if valor > 0]

    menor_faturamento = min(faturamento_filtrado)
    maior_faturamento = max(faturamento_filtrado)

    media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)
    dias_acima_da_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)

    return {
        'menor_faturamento': menor_faturamento,
        'maior_faturamento': maior_faturamento,
        'dias_acima_da_media': dias_acima_da_media
    }

def ler_dados_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados


caminho_arquivo = 'C:\\Users\\guilherme.sil\\PycharmProjects\\pythonProject\\Python-Meu\\dados.json'




dados = ler_dados_json(caminho_arquivo)


faturamento_diario = [dia['valor'] for dia in dados]


resultado = calcular_faturamento(faturamento_diario)

print("Menor faturamento:", resultado['menor_faturamento'])
print("Maior faturamento:", resultado['maior_faturamento'])
print("Número de dias acima da média:", resultado['dias_acima_da_media'])

#rodei o comandos pelo PyChar, e coloquei ele em VsCode para subi pro GITHUB, ali em caminho_arquivo preciei colocar o caminho raix para rodar o json. 