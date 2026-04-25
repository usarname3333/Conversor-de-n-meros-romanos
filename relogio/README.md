# 🏛️ Conversor de Números Romanos

Um aplicativo desktop elegante e moderno desenvolvido em Python que permite a conversão instantânea e bidirecional entre Números Romanos e Números Decimais (Base 10).

> **Aviso:** Adicione uma captura de tela (screenshot) do seu aplicativo rodando aqui para deixar o repositório ainda mais atraente!
> *(Substitua este aviso pela imagem: `![Screenshot do App](link-da-imagem.png)`)*

## ✨ Funcionalidades (Features)

* **🔄 Conversão Bidirecional:** Converta facilmente de Romano para Decimal e de Decimal para Romano usando os mesmos campos de interface.
* **⚡ Tempo Real (Real-time):** A conversão ocorre de forma fluida enquanto você digita, sem a necessidade de clicar em botões de "Converter".
* **🎨 Interface Premium e Moderna:** O design não utiliza os padrões antigos e rígidos. Ele apresenta uma interface estilo "Card Flutuante", tipografia profissional (Segoe UI), remoção de bordas clássicas e micro-interações de foco nos campos de texto (Focus Highlights).
* **🛡️ Validação Inteligente:** Prevenção de erros robusta. O sistema avisa visualmente o usuário caso ele tente inserir símbolos romanos inexistentes ou letras nos campos destinados aos números decimais.
* **🧹 Limpeza Rápida:** Um botão dedicado para resetar todos os estados do aplicativo instantaneamente.

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Interface Gráfica (GUI):** Tkinter (Biblioteca Nativa)
* **Estilização:** CSS-like Colors e Custom Tkinter Frames para simular propriedades visuais modernas.

## 🛠️ Como Executar o Projeto na Sua Máquina

Como o projeto utiliza apenas bibliotecas nativas do Python, você não precisa instalar nenhuma dependência externa (como o `pip install`).

1. Certifique-se de ter o **Python** instalado em seu computador (versão 3.6 ou superior).
2. Faça o clone deste repositório ou baixe os arquivos.
3. Abra o seu terminal ou prompt de comando na pasta do projeto.
4. Execute o seguinte comando:

```bash
python "conversor de números romanos.py"
```

O aplicativo se abrirá centralizado na sua tela!

## 🧠 Como Funciona a Lógica?

O algoritmo lida com as regras matemáticas do sistema numérico da Roma Antiga:
* **Romano para Decimal:** Iteramos pelos símbolos de trás para frente. Se um valor atual é menor que o valor anterior (ex: I antes de V no caso do 4), nós subtraímos. Caso contrário, somamos.
* **Decimal para Romano:** Utilizamos duas listas paralelas agrupando do maior para o menor valor (1000 = M, 900 = CM, 500 = D...). Percorremos os números, fazendo a divisão inteira e anexando os caracteres de forma sequencial.

---

Feito com 💙 e muito código!
