# Trabalho 1 - Busca no Labirinto (Não Informada e Informada)

Este trabalho tem como objetivo implementar algoritmos de busca de forma a solucionar um labirinto fornecido através de um arquivo `.txt`.  

---

## Estrutura do Projeto

Foram construídos **4 scripts em Python**:

- **Adj.py**  
  Lê o arquivo `trabalho1/data/maze.txt` e cria uma matriz de adjacência que será utilizada para a execução do algoritmo.

- **Heuristics.py**  
  Possui a implementação das funções heurísticas que serão utilizadas para definir os parâmetros das funções de busca:  
  - *Distância Euclidiana*  
  - *Distância de Manhattan*

- **Search.py**  
  Contém as funções de busca a serem utilizadas:  
  - `bfs`  
  - `dfs`  
  - `Busca Gulosa`  
  - `A*`

- **Maze.py**  
  Contém a função `main`, além de outras funções que geram os arquivos de saída.  
  Deste arquivo, os outros são chamados automaticamente.

---

## Utilização

### 1. Pré-requisitos
- Certifique-se de ter o **Python 3.12** ou superior instalado em seu sistema.  
- O **PATH** deve estar configurado corretamente.  
- Mova o arquivo `maze.txt`, contendo o labirinto, para o diretório: `trabalho1/data/maze.txt`

### Dependências
Para instalar as dependências, abra um terminal e execute o seguinte comando
```bash
pip install colorama matplotlib memory_profiler
```
---

### 2. Execução
Abra um terminal e navegue até o diretório raiz do projeto.  
Execute o comando:

```bash
python trabalho1/src/Maze.py
```
### 3. Saída

Para **cada algoritmo executado**, será gerado:

- Um arquivo `.txt` na pasta `trabalho1/output` contendo:
  - O caminho encontrado  
  - O tempo de execução  
  - A quantidade de nós gerados  

- Um arquivo `.png` contendo o **gráfico de uso de memória** durante a execução.

# Trabalho 2 — 8 Rainhas com Hill Climbing
Este trabalho tem como objetivo implementar algoritmos de busca de forma a solucionar um labirinto fornecido através de um arquivo `.txt`.  

---

# Especificações do Teste
Os testes foram executados utilizando as seguintes especificações de máquina:

| Componente | Modelo / Especificação |
|-------------|------------------------|
| **Processador** | AMD Ryzen 3 4350G 3.8GHz|
| **Placa-mãe** | ASRock B450 Steel Legend |
| **Memória RAM** | 32 GB Crucial Ballistix 3800 MT/s CL16 |
| **Sistema Operacional** | Windows 11 24H2 |
| **Versão do Python** | 3.12.10 |


# Autores

<table style="margin: 0 auto; text-align: center;">
  <tr>
    <td colspan="5"><strong>Alunos</strong></td>
  </tr>
  <tr>
      <td>
      <img src="https://avatars.githubusercontent.com/u/83346676?v=4" alt="Avatar de Arthur Santana" style="border-radius:50%; border:4px solid #4ECDC4; box-shadow:0 0 10px #4ECDC4; width:100px;"><br>
      <strong>Arthur Santana</strong><br>
      <a href="https://github.com/Rutrama">
        <img src="https://img.shields.io/github/followers/Rutrama?label=Seguidores&style=social&logo=github" alt="GitHub - Arthur Santana">
      </a>
    </td>
        <td>
      <img src="https://avatars.githubusercontent.com/u/114318721?v=4" alt="Avatar de João Vitor" style="border-radius:50%; border:4px solid #4ECDC4; box-shadow:0 0 10px #4ECDC4; width:100px;"><br>
      <strong>João Vitor</strong><br>
      <a href="https://github.com/JV-NC">
        <img src="https://img.shields.io/github/followers/JV-NC?label=Seguidores&style=social&logo=github" alt="GitHub - João Vitor">
      </a>
    </td>
