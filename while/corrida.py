import random
import time
import os

def limpar_tela():
    # Limpa o terminal dependendo do sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')

# Definição do design do carro em arte ASCII (lateral)
# Ele tem 3 linhas de altura
DESIGN_CARRO = [
    "  ______",
    " /|_||_\`.__",
    "(   _    _ _\ ",
    "=`-(_)--(_)-' "
]

LARGURA_CARRO = max(len(linha) for linha in DESIGN_CARRO)

def desenhar_pista(pos1, pos2, chegada):
    limpar_tela()
    
    # Define a largura total da tela com base na chegada e tamanho do carro
    largura_total = chegada + LARGURA_CARRO + 5
    print("=" * largura_total)
    print("      GRANDE PRÊMIO ASCII      ")
    print("=" * largura_total)
    print("\n")

    # Desenha o Carrinho 1
    print(f"--- JOGADOR 1 ---")
    for linha in DESIGN_CARRO:
        print(" " * pos1 + linha)
    print("-" * largura_total) # Linha divisória da pista

    print("\n") # Espaço entre as pistas

    # Desenha o Carrinho 2
    print(f"--- JOGADOR 2 ---")
    for linha in DESIGN_CARRO:
        print(" " * pos2 + linha)
    print("-" * largura_total) # Linha divisória da pista

    # Desenha a linha de chegada
    print("\n" + " " * chegada + "| CHEGADA |")
    print(" " * chegada + "|_________|")

def comemorar(vencedor):
    moldura = "*" * 50
    print(f"\n\n{moldura}")
    print(f"      🏆🏆🏆 FIM DE PROVA! 🏆🏆🏆      ")
    print(f"         O JOGADOR {vencedor} É O VENCEDOR!         ")
    print(f"{moldura}")
    
    print("\nDesenho do Carro Campeão:")
    for linha in DESIGN_CARRO:
        print("      " + linha)
        
    print("\n      PARABÉNS PELA VITÓRIA! 🏁")
    print("\n" + "="*50 + "\n")

def iniciar_corrida():
    pos1 = 0
    pos2 = 0
    # Ajustei a chegada para 60 para a corrida durar um pouco mais, 
    # já que o carro é maior.
    chegada = 60 
    
    limpar_tela()
    print("Preparem seus motores!")
    print("O design dos carros é:")
    for linha in DESIGN_CARRO:
        print(linha)
    print("\n")
    
    input("Pressione ENTER para dar a largada!...")
    
    while pos1 < chegada and pos2 < chegada:
        # Cada carro avança entre 1 e 4 espaços aleatoriamente
        # Aumentei um pouco a velocidade para compensar o tamanho
        pos1 += random.randint(1, 4)
        pos2 += random.randint(1, 4)
        
        desenhar_pista(pos1, pos2, chegada)
        
        # Um pequeno delay para a animação
        # Se achar muito lento, diminua este número (ex: 0.05)
        time.sleep(0.9) 
    
    # Verifica quem cruzou a linha primeiro (ou mais longe)
    if pos1 >= chegada and pos2 >= chegada:
        # Empate técnico na mesma rodada, ganha quem foi mais longe
        if pos1 > pos2:
            comemorar("1")
        elif pos2 > pos1:
            comemorar("2")
        else:
            comemorar("1 (por sorteio no empate exacto!)")
    elif pos1 >= chegada:
        comemorar("1")
    else:
        comemorar("2")

if __name__ == "__main__":
    iniciar_corrida()