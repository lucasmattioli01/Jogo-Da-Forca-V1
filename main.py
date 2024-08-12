import random as rd

lista_frutas = [
    "ABACAXI", "MELÃO", "BANANA", "MELANCIA", "MAÇÃ", "CAJU", "MORANGO", 
    "LARANJA", "PERA", "MANGA", "ABACATE", "AÇAÍ", "ACEROLA", "AMORA", 
    "CACAU", "TOMATE", "UVA", "KIWI", "LIMÃO", "GOIABA", "MARACUJÁ", 
    "FIGO", "PÊSSEGO", "PITAYA", "GRAVIOLA", "TANGERINA", "JACA", 
    "FRAMBOESA", "ROMÃ", "JABUTICABA", "LICHIA", "SERIGUELA", "GUARANÁ"
]

lista_animais = [
    "CACHORRO", "GATO", "ELEFANTE", "LEÃO", "TIGRE", "GIRAFA", "MACACO",
    "PAPAGAIO", "ZEBRA", "HIPOPÓTAMO", "PANDA", "URSO", "COELHO", "GOLFINHO",
    "PEIXE", "CABRA", "PINGUIM", "CAVALO", "VACA", "GALINHA", "TARTARUGA",
    "RATO", "CORUJA", "ARARA", "RINOCERONTE", "CAMELO", "LHAMA", "JACARÉ",
    "CANGURU", "BÚFALO", "FALCÃO", "AVESTRUZ", "BALEIA"
]

lista_carros = [
    "UNO", "GOL", "LANCER", "CIVIC", "EVOQUE", "GALLARDO", "MAREA", "URUS",
    "CAMARO", "VENENO", "HURACAN", "MCLAREN", "CYBERTRUCK", "FUSCA",
    "MUSTANG", "CORVETTE", "TESLA", "FERRARI", "PORSCHE", "BMW", "AUDI",
    "JEEP", "PAGANI", "ALFA", "CHEVROLET", "BUGATTI", "MASERATI"
]

lista_profissoes = [
    "MÉDICO", "ENGENHEIRO", "ADVOGADO", "PROFESSOR", "ARQUITETO", 
    "ENFERMEIRO", "DESENVOLVEDOR", "JORNALISTA", "DESIGNER", 
    "FOTÓGRAFO", "CHEF", "FISIOTERAPEUTA", "MECÂNICO", "PILOTO", 
    "DENTISTA", "PSICÓLOGO", "FARMACÊUTICO", "CONTADOR", "ELETRICISTA", 
    "CARPINTEIRO", "BOMBEIRO", "POLICIAL", "VETERINÁRIO", "BIÓLOGO", 
    "QUÍMICO", "ASTRÔNOMO", "GEÓLOGO", "SOCIOLOGO", "NUTRICIONISTA", 
    "TRADUTOR", "MARKETING", "VENDEDOR", "AGRICULTOR", "JUIZ", 
    "MOTORISTA", "TAXISTA", "MAQUIADOR", "COREÓGRAFO", "PESQUISADOR", 
    "COSTUREIRO", "RELOJOEIRO", "ARTESÃO", "SAPATEIRO", "LANTERNEIRO",       
    "FERREIRO", "VIDRACEIRO", "PEDREIRO"
]

lista_cores = [
    "VERMELHO", "AZUL", "VERDE", "AMARELO", "ROXO", "LARANJA", 
    "MARROM", "PRETO", "BRANCO", "CINZA", "ROSA", "VIOLETA", 
    "TURQUESA", "DOURADO", "PRATEADO", "BEGE", "MAGENTA", "CARAMELO", 
    "SALMÃO", "LILÁS", "VERDE-ÁGUA", "VINHO", "OLIVA", "AZUL-CLARO", 
    "AZUL-ESCURO", "LIMÃO", "BRANCO-NEVE", "ÂMBAR", "GRAFITE", 
    "CREME", "PÚRPURA", "TERRA-QUEIMADA", "ROSA-CHOCK", "AZUL-TURQUESA"
]

lista_esportes = [
    "FUTEBOL", "BASQUETE", "VÔLEI", "TÊNIS", "NATAÇÃO", "ATLETISMO", 
    "GOLFE", "RUGBY", "BEISEBOL", "HANDEBOL", "CICLISMO", "SURFE", 
    "SKATE", "ESGRIMA", "JUDÔ", "LUTA LIVRE", "BOXE", "TAEKWONDO", 
    "GINÁSTICA", "HÓQUEI", "CORRIDAS", "ESCALADA", "PATINAÇÃO", 
    "KARATE", "PING-PONG", "BADMINTON", "FUTSAL", "CANOAGEM", "CAPOEIRA"
]

lista_paises = [
    "BRASIL", "EUA", "CANADÁ", "ALEMANHA", "FRANÇA", "JAPÃO", 
    "CHINA", "AUSTRÁLIA", "ITÁLIA", "ESPANHA", "RÚSSIA", 
    "ÍNDIA", "MÉXICO", "ARGENTINA", "ÁFRICA DO SUL", "INGLATERRA", 
    "PAÍSES BAIXOS", "SUIÇA", "SUECIA", "NORUEGA", "DINAMARCA", 
    "ÁRABIA SAUDITA", "TURQUIA", "ISRAEL", "NIGÉRIA", "PAQUISTÃO", 
    "TAILÂNDIA", "MALÁSIA", "CINGAPURA", "FILIPINAS", "VIETNÃ", 
    "COLOMBIA", "CHILE", "PERU", "URUGUAI", "PARAGUAI"
]

lista_objetos = [
    "SOFÁ", "CAMA", "CADEIRA", "ESCRIVANINHA", "ESTANTE", "GUARDA-ROUPA",
    "MESA", "LÂMPADA", "TV", "FRIGOBAR", "ARMÁRIO", "TAPETE", "RELÓGIO",
    "VENTILADOR", "MICRO-ONDAS", "CAFETEIRA", "ADESIVO", "CANETA", "CADERNO",
    "MOUSE", "TECLADO", "CARTEIRA", "ÓCULOS", "CELULAR", "CARREGADOR",
    "MAQUIAGEM", "TRAVESSEIRO", "MANTAS", "MESA DE JANTAR", "APARELHO DE SOM",
    "PENTE", "ESCOVA", "SABONETE", "TOALHA", "CHAVE", "LIVRO", "ROUPA",
    "SAPATO", "COPO", "PRATO", "TALHERES", "GARFO", "COLHER"
]

def inicio():
  if rodadas < 1:
    print("=============== Jogo Da Forca ===============")
    print()
  if rodadas % 5 == 0 and rodadas != 0:
    print()
    print("Vitórias: ", vitorias)
    print("Derrotas: ", derrotas)
    print("Pontuação: ", pontos)

def removeAcentos(s):
  replaces = (
    ("á", "a"), ("à", "a"), ("ã", "a"), ("â", "a"),
    ("é", "e"), ("ê", "e"), ("í", "i"), ("ó", "o"),
    ("ô", "o"), ("õ", "o"), ("ú", "u"), ("ç", "c"),
    ("Á", "A"), ("À", "A"), ("Ã", "A"), ("Â", "A"),
    ("É", "E"), ("Ê", "E"), ("Í", "I"), ("Ó", "O"),
    ("Ô", "O"), ("Õ", "O"), ("Ú", "U"), ("Ç", "C"),
  )
  for a, b in replaces: # (a, b) a é a letra e b é ela substituída
      s = s.replace(a, b)
  return s

def tema(): 
  global palavra_parcial
  global tema_sort
  global resposta_sort
  global tamanho_resposta
  temas = [lista_frutas, lista_animais, lista_carros, 
           lista_profissoes, lista_cores, lista_esportes,
           lista_paises, lista_objetos]
  
  tema_sort = rd.choice(temas)
  resposta_sort = rd.choice(tema_sort)
  tamanho_resposta = len(resposta_sort)  # Após o random escolher a palavra
  palavra_parcial = "_ " * tamanho_resposta
  
  return tema_sort, resposta_sort, palavra_parcial

def imprimirTema():
  if tema_sort == lista_frutas:
    print("TEMA: Frutas")
  elif tema_sort == lista_animais:
    print("TEMA: Animais")
  elif tema_sort == lista_carros:
    print("TEMA: Carros")
  elif tema_sort == lista_profissoes:
    print("TEMA: Profissões")
  elif tema_sort == lista_cores:
    print("TEMA: Cores")
  elif tema_sort == lista_esportes:
    print("TEMA: Esportes")
  elif tema_sort == lista_paises:
    print("TEMA: Países")
  elif tema_sort == lista_objetos:
    print("TEMA: Objetos")
  else:
    print("Erro / Não definido")

def escolherDificuldade():
  global dificuldade_atual
  global chances
  
  if dificuldade_atual is None:
    print("Dificuldades: fácil, normal, difícil ou insano!")
    print("(Ou do nível 1 até o 4)")
    opc_dif = input("\nEscolha o nível de dificuldade: ").strip().lower()
    if opc_dif in ["f", "facil", "fácil", "1"]:
      difFacil()
    elif opc_dif in ["n", "normal", "2"]:
      difNormal()
    elif opc_dif in ["d", "dificil", "difícil", "3"]:
      difDificil()
    elif opc_dif in ["i", "insano", "4"]:
      difInsano()
    else:
      print("\n-- Escolha uma opção válida --")
      return escolherDificuldade()
  else:
    if dificuldade_atual == dif_facil: 
      difFacil()
    elif dificuldade_atual == dif_normal:
      difNormal()
    elif dificuldade_atual == dif_dificil:
      difDificil()
    elif dificuldade_atual == dif_insano:
      difInsano()
      
  return dificuldade_atual, chances
  
def difFacil():
  global chances
  global dificuldade_atual 
  dificuldade_atual = 1
  if rodadas < 1:
    print("\n-- FÁCIL --")
    print("\nTente adivinhar a palavra, boa sorte!")
  imprimirTema()
  chances = tamanho_resposta + 2
  print(f"\nVocê começa com {chances} chances!") 
  print("\nPalavra: ")
  print(palavra_parcial)
  return dif_facil, chances, dificuldade_atual
  
def difNormal():
  global chances
  global dificuldade_atual 
  dificuldade_atual = 2
  if rodadas < 1:
    print("\n-- NORMAL --")
    print("\nTente adivinhar a palavra, boa sorte!")
  imprimirTema()
  chances = tamanho_resposta
  print(f"\nVocê começa com {chances} chances!") 
  print("\nPalavra: ")
  print(palavra_parcial)
  return dif_normal, chances, dificuldade_atual
  
def difDificil():
  global chances
  global dificuldade_atual 
  dificuldade_atual = 3
  if rodadas < 1:
    print("\n-- DIFÍCIL --")
    print("\nTente adivinhar a palavra, boa sorte!")
  chances = tamanho_resposta - 1
  print(f"\nVocê começa com {chances} chances!") 
  print("\nPalavra: ")
  print(palavra_parcial)
  return dif_dificil, chances, dificuldade_atual
    
def difInsano():
  global chances
  global dificuldade_atual 
  dificuldade_atual = 4
  if rodadas < 1:
    print("\n-- INSANO --")
    print("\nTente adivinhar a palavra, BOA SORTE.")
  chances = tamanho_resposta // 2
  print(f"\nVocê começa com {chances} chances!") 
  print("\nPalavra: ")
  print("???")
  return dif_insano, chances, dificuldade_atual
  
def encontraLetra(letra_digi, resposta_sort, palavra_parcial): 
  letra_digi_sem_acento = removeAcentos(letra_digi)
  resposta_sort_sem_acento = removeAcentos(resposta_sort)
  lista_palavra_parcial = list(palavra_parcial.replace(" ", ""))

  # indice = letras da palavra nesse caso
  for i in range(len(resposta_sort_sem_acento)):
    if resposta_sort_sem_acento[i] == letra_digi_sem_acento:
      lista_palavra_parcial[i] = resposta_sort[i]
  return " ".join(lista_palavra_parcial)

#função principal
def jogo():
  global chances
  global vitorias
  global derrotas
  global pontos
  global rodadas
  global dificuldade_atual 

  chances = 0
  acertos = 0
  
  inicio()

  if rodadas >= 1:
    print()
    print("================================")
    print()
    print("Rodadas:", rodadas + 1) 
    print()

  tema_sort, resposta_sort, palavra_parcial = tema() 
  escolherDificuldade() 
  
  #loop principal
  while chances >= 1: 
    letra_digi = str(input("\nDigite uma letra: ")).upper()

    if len(letra_digi) != 1:
      print("Por favor, digite apenas uma letra.")
      continue  # Retorna ao início do loop

    if letra_digi in resposta_sort:
      palavra_parcial = encontraLetra(letra_digi, resposta_sort, palavra_parcial)
      print("\nPalavra:")
      print(palavra_parcial) 
      acertos += 1
      if "_" not in palavra_parcial:
        print("\nParabéns, você ganhou a rodada!")
        chances = 0 # zerar as chances para não voltar pro começo do loop
        vitorias += 1
        pontos += 2
        break

      if acertos % 3 == 0: # se o resto da div do número de acertos por 3 for 0
        opc = str(input("\nJá sabe a palavra? (S/N) ")).lower()
        while opc not in ["s", "n", "sim", "não", "nao"]:
          print("Opção inválida, escolha novamente!")
          opc = str(input("\nJá sabe a palavra? (S/N) ")).lower()
        if opc in ["s", "sim"]:
          resp_inteira = input("Digite a palavra: ").upper()
          
          if resp_inteira == resposta_sort:
            print("\nParabéns, você ganhou a rodada!")
            chances = 0 # zerar as chances para não voltar pro começo do loop
            vitorias += 1
            pontos += 2
            break
          else:
            chances = 0 # zerar as chances para não voltar pro começo do loop
            derrotas += 1
            pontos -= 1
            print("\nVocê perdeu!!")
        elif opc in ["n", "nao", "não"]:
          continue

    else:
      print(f"A letra {letra_digi} não está na palavra!")
      chances -= 1
      if chances >= 2:
        print(f"Restam {chances} chances!")
      elif chances == 1:
        print("\nVocê tem apenas uma chance, é tudo ou nada!")
      else:
        print("\nSuas chances acabaram, você perdeu a rodada!")
        print(f"A palavra era: {resposta_sort.lower()}")
        pontos -= 1
        derrotas += 1

  opc = str(input("Quer jogar novamente? (s/n) ")).lower()
  if opc in["s", "sim"]:
    rodadas += 1
    jogo()
  else:
    rodadas += 1
    print("\n-- Jogo finalizado! --")
      
    return rodadas        

# Dificuldades para comparar na função
dif_facil = 1
dif_normal = 2
dif_dificil = 3
dif_insano = 4

# Início do programa
rodadas = 0 
vitorias = 0
derrotas = 0
pontos = 0
dificuldade_atual = None

if rodadas == 0:
  jogo()

if rodadas >= 1:
  opc_jogo = str(input("\nQuer reiniciar o jogo? (s/n) ")).lower()
  if opc_jogo in ["s", "sim"]:
    rodadas = 0
    vitorias = 0
    derrotas = 0
    pontos = 0
    dificuldade_atual = None  # Reseta a dificuldade para o novo jogo
    print()
    jogo()
  else:
    print("\nFim do programa!")

print()
print("Vitórias:", vitorias) 
print("Derrotas:", derrotas)
print("Pontuação:", pontos)
