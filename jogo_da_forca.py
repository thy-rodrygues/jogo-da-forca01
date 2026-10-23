import random


def jogar_forca():
  # Lista com 10 palavras para o sorteio
  palavras = [
      "python",
      "programacao",
      "computador",
      "desenvolvedor",
      "algoritmo",
      "variavel",
      "funcao",
      "tecnologia",
      "inteligencia",
      "engenharia",
  ]

  # Sorteia a palavra secreta e converte para minúsculas
  palavra_secreta = random.choice(palavras).lower()

  # Inicialização do estado do jogo
  vidas = 6
  letras_reveladas = ["_" for _ in palavra_secreta]
  letras_tentadas = []

  print("========================================")
  print("      BEM-VINDO AO JOGO DA FORCA!       ")
  print("========================================")
  print(f"A palavra secreta tem {len(palavra_secreta)} letras.")

  # Loop principal do jogo
  while vidas > 0 and "_" in letras_reveladas:
    print("\n" + "-" * 40)
    print(f"❤️  Vidas restantes: {vidas}")
    print(
        "📝 Palavra: " + " ".join(letras_reveladas)
    )  # Exibe os traços/letras reveladas

    # Exibe as letras já tentadas de forma organizada
    if letras_tentadas:
      print(f"🔤 Letras já tentadas: {', '.join(sorted(letras_tentadas))}")
    else:
      print("🔤 Letras já tentadas: Nenhuma ainda")

    # Recebe o chute do jogador e converte para minúscula
    chute = input("👉 Digite uma letra: ").lower().strip()

    # Validação da entrada (garante que foi digitada apenas uma letra válida)
    if len(chute) != 1 or not chute.isalpha():
      print("⚠️ Entrada inválida! Por favor, digite apenas uma única letra.")
      continue

    # Verifica se a letra já foi tentada anteriormente (sem descontar vida)
    if chute in letras_tentadas:
      print(f"⚠️ Você já tentou a letra '{chute}'. Tente outra diferente!")
      continue

    # Adiciona a nova letra à lista de tentativas
    letras_tentadas.append(chute)

    # Verifica se a letra está na palavra secreta
    if chute in palavra_secreta:
      print(f"🎉 Muito bem! A letra '{chute}' está na palavra.")

      # Percorre a palavra utilizando for com range para atualizar todas as ocorrências
      for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == chute:
          letras_reveladas[i] = chute
    else:
      print(f"❌ Que pena! A letra '{chute}' não está na palavra.")
      vidas -= 1

  # Fim do jogo (Condições de vitória ou derrota)
  print("\n" + "=" * 40)
  if "_" not in letras_reveladas:
    print("🏆 PARABÉNS! Você venceu e descobriu a palavra!")
  else:
    print("💀 FIM DE JOGO! Suas vidas acabaram.")

  # Revela a palavra secreta ao final, independente do resultado
  print(f"🔑 A palavra secreta era: {palavra_secreta}")
  print("========================================")


# Executa o jogo
if __name__ == "__main__":
  jogar_forca()
