# Algoritmo genético capaz de encontar uma senha de n digitos

import random

# Parâmetros
alvo = "0000000000000000"
populacao_tamanho = 2
mutacao_taxa = 0.01
geracoes = 1000


# Inicialização
def criar_populacao():
    """"
        Inicializa uma nova população com indivíduos aleátorios.
    """

    populacao = []
    for x in range(populacao_tamanho):
        individual = []
        for x in alvo:
            gene = random.choice("1234567890")
            individual.append(gene)
        populacao.append(individual)
    return populacao

def fitness(individual):
    """
        Calcula o fitness de um indivíduo
    """

    pontos = 0

    for x in range(len(alvo)):
        if individual[x] == alvo[x]:
            pontos+= 1
    return pontos


def selecionar(populacao: list[list[str]]):
    """
        Seleciona dos melhores indivíduos da população
    """

    populacao.sort(key= lambda x: fitness(x), reverse=True)
    top_20_porcent = max(2, int(0.2 * populacao_tamanho))
    return populacao[:top_20_porcent]

def crossover(parent1, parent2):
    """
        Realiza o crossover entre dois pais para criar dois novos filhos
    """
    crossover_point = random.randint(1, len(alvo) - 2)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual):
    """
        Realizar mutação aleatória em um individuo
    """

    for x in range(len(individual)):
        if random.random() < mutacao_taxa:
            individual[x] = random.choice("1234567890")

# Main Loop
def main():
    nova_populacao = criar_populacao()

    # Loop Iterativo
    for geracao in range(geracoes):
        selecionado = selecionar(nova_populacao)

        # Realizar crossover e a mutação para criar uma nova geranção
        descendencia = []
        while len(descendencia) < populacao_tamanho:
            parent1, parent2 = random.sample(selecionado, 2)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            descendencia.extend([child1, child2])
        
        nova_populacao = descendencia[:populacao_tamanho]

        # Melhor indivíduo da geração atual
        melhor_individuo = max(nova_populacao, key=fitness)
        melhor_individuo_string = "".join(melhor_individuo)
        print(f"Geração: {geracao} Melhor indivíduo: {melhor_individuo_string} com fitness {fitness(melhor_individuo)}")

        # Verificar se o melhor individuo atingiu o objetivo
        if melhor_individuo_string == alvo:
            print(f"Objetivo {alvo} atingido! Geração: {geracao}")
            break

if __name__ == "__main__":
    main()