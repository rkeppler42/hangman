# 🪢 Hangman

A classic Hangman game running in the terminal, built with Python.

## 📋 Description

The computer picks a random word from a list of 1000 words and challenges you to guess it letter by letter. You have 6 attempts before the hangman is complete. Each wrong guess reveals a new part of the drawing.

## 🗂️ Project Structure

```
hangman/
├── main.py           # Main game logic
├── words.py          # List of 1000 words
├── hangman_art.py    # ASCII art stages (0–6 wrong guesses)
└── README.md
```

## ▶️ How to Run

No external dependencies required — only Python 3.10+.

```bash
python main.py
```

## 🎮 How to Play

1. The computer thinks of a word and shows it as a series of `_`
2. Type a letter and press Enter to guess
3. Correct guesses reveal the letter in the word
4. Wrong guesses add a body part to the hangman
5. You win by guessing all letters before 6 wrong guesses

## ✨ Features

- 1000-word dictionary
- Animated "thinking" loading effect
- Input validation (letters only, no repeats)
- ASCII art hangman with 7 progressive stages
- Clear win/loss messages

## 📝 Credits

ASCII hangman art adapted from *Automate the Boring Stuff with Python* by Al Sweigart.  
All game logic was designed and implemented independently.

## 👤 Author

**Roberto Keppler** — [@rkeppler42](https://github.com/rkeppler42)

---

# 🪢 Hangman

Um jogo clássico de Forca rodando no terminal, feito em Python.

## 📋 Descrição

O computador escolhe uma palavra aleatória de uma lista com 1000 palavras e desafia você a descobri-la letra por letra. Você tem 6 tentativas antes de o boneco ser completado. Cada erro revela uma nova parte do desenho.

## 🗂️ Estrutura do Projeto

```
hangman/
├── main.py           # Lógica principal do jogo
├── words.py          # Lista de 1000 palavras
├── hangman_art.py    # Arte ASCII dos estágios (0–6 erros)
└── README.md
```

## ▶️ Como Rodar

Nenhuma dependência externa necessária — apenas Python 3.10+.

```bash
python main.py
```

## 🎮 Como Jogar

1. O computador pensa em uma palavra e a exibe como uma sequência de `_`
2. Digite uma letra e pressione Enter para adivinhar
3. Acertos revelam a letra na posição correta da palavra
4. Erros adicionam uma parte do corpo ao boneco
5. Você vence ao descobrir todas as letras antes de 6 erros

## ✨ Funcionalidades

- Dicionário com 1000 palavras
- Efeito de carregamento animado enquanto o computador "pensa"
- Validação de input (somente letras, sem repetição)
- Arte ASCII com 7 estágios progressivos
- Mensagens claras de vitória e derrota

## 📝 Créditos

Arte ASCII do boneco adaptada de *Automate the Boring Stuff with Python* de Al Sweigart.  
Toda a lógica do jogo foi desenvolvida de forma independente.

## 👤 Autor

**Roberto Keppler** — [@rkeppler42](https://github.com/rkeppler42)
