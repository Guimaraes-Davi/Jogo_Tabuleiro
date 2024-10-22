import pygame
import random

# Inicializando o Pygame
pygame.init()

# Configurações de tela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jogo de Educação Financeira')

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARK_GRAY = (50, 50, 50)

# Configurações do Tabuleiro
TOTAL_CASAS = 15
HOUSE_WIDTH = SCREEN_WIDTH // TOTAL_CASAS
HOUSE_HEIGHT = 100

# Classe do Jogador
class Jogador:
    def __init__(self):
        self.posicao = 0  # Posição no tabuleiro
        self.renda = 1000  # Renda inicial
        self.dividas = 0   # Dívidas
        self.faturamento = 0  # Faturamento acumulado
    
    def mover(self):
        if self.posicao < TOTAL_CASAS - 1:
            self.posicao += 1

    def pagar_contas(self, valor):
        if self.renda >= valor:
            self.renda -= valor
        else:
            self.dividas += valor

# Função para desenhar o tabuleiro
def desenhar_tabuleiro():
    for i in range(TOTAL_CASAS):
        x = i * HOUSE_WIDTH
        y = SCREEN_HEIGHT // 2 - HOUSE_HEIGHT // 2
        if i % 5 == 0:
            pygame.draw.rect(screen, BLUE, (x, y, HOUSE_WIDTH, HOUSE_HEIGHT))  # Casas especiais de contas
        else:
            pygame.draw.rect(screen, GREEN, (x, y, HOUSE_WIDTH, HOUSE_HEIGHT))  # Casas normais
        pygame.draw.rect(screen, BLACK, (x, y, HOUSE_WIDTH, HOUSE_HEIGHT), 2)

# Função para mostrar o jogador no tabuleiro
def desenhar_jogador(jogador):
    x = jogador.posicao * HOUSE_WIDTH + HOUSE_WIDTH // 2
    y = SCREEN_HEIGHT // 2
    pygame.draw.circle(screen, RED, (x, y), 20)

# Função para exibir as informações financeiras do jogador
def mostrar_informacoes(jogador):
    font = pygame.font.Font(None, 36)
    renda_text = font.render(f"Renda: R${jogador.renda}", True, BLACK)
    divida_text = font.render(f"Dívidas: R${jogador.dividas}", True, BLACK)
    faturamento_text = font.render(f"Faturamento: R${jogador.faturamento}", True, BLACK)
    
    screen.blit(renda_text, (50, 50))
    screen.blit(divida_text, (50, 100))
    screen.blit(faturamento_text, (50, 150))

# Função para pop-up de eventos no canto superior direito
def pop_up(text):
    font = pygame.font.Font(None, 26)
    
    # Definir tamanho e posição do pop-up
    pop_width, pop_height = 300, 100
    x = SCREEN_WIDTH - pop_width - 20  # 20 pixels de margem do lado direito
    y = 20  # 20 pixels de margem do topo

    # Desenhar o retângulo do pop-up
    pygame.draw.rect(screen, YELLOW, (x, y, pop_width, pop_height))
    pygame.draw.rect(screen, DARK_GRAY, (x, y, pop_width, pop_height), 3)  # Borda escura

    # Renderizar o texto centralizado no pop-up
    pop_text = font.render(text, True, BLACK)
    text_rect = pop_text.get_rect(center=(x + pop_width // 2, y + pop_height // 2))
    screen.blit(pop_text, text_rect)

    pygame.display.update()
    pygame.time.delay(2000)  # Exibe o pop-up por 2 segundos

# Função para gerenciar os desafios financeiros
def desafio_financeiro(jogador):
    chance = random.randint(1, 3)
    if chance == 1:
        jogador.faturamento += 200
        pop_up("Você recebeu um bônus! +200")
    elif chance == 2:
        jogador.dividas += 100
        pop_up("Gasto inesperado! +100 em dívidas")
    else:
        jogador.renda += 150
        pop_up("Investimento feito! +150 de renda")

# Loop principal do jogo
jogador = Jogador()
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    desenhar_tabuleiro()
    desenhar_jogador(jogador)
    mostrar_informacoes(jogador)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                jogador.mover()
                desafio_financeiro(jogador)
                if jogador.posicao % 5 == 0:  # Se estiver em uma casa de contas
                    jogador.pagar_contas(200)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
