# 🌊 Análise da Mudança Global do Nível do Mar

Este repositório contém scripts para a **análise e previsão da mudança média global do nível do mar** desde 1880. Utilizando **Pandas**, **Matplotlib** e **SciPy**, o projeto explora dados históricos para prever a elevação do nível do mar até o ano de **2050**.

## 🚀 Tecnologias Utilizadas

- **Python**
- **Pandas**: Importação e manipulação de dados.
- **Matplotlib**: Criação de gráficos de dispersão e linhas de tendência.
- **SciPy**: Cálculo da regressão linear para previsões.

## 💻 Descrição dos Dados

- **Fonte**: Arquivo `epa-sea-level.csv`.
- **Linhas**: Representam os anos de medições.
- **Colunas**: Incluem o **Ano** e o **Nível do Mar Ajustado do CSIRO**.

Os dados foram utilizados para explorar a relação entre o tempo e a elevação do nível do mar, com foco em prever as mudanças até 2050.

## 📈 Tarefas Realizadas

1. **Importação de Dados**:
   - Utilização do **Pandas** para importar o arquivo `epa-sea-level.csv`.

2. **Criação de Gráficos**:
   - Gráfico de dispersão com o **Ano** no eixo X e o **Nível do Mar Ajustado do CSIRO** no eixo Y.

3. **Análise de Regressão Linear**:
   - Uso da função **`linregress`** da biblioteca **SciPy** para obter a inclinação e interceptação da linha de melhor ajuste.
   - Traço da linha de melhor ajuste sobre o gráfico de dispersão.
   - Extensão da linha até o ano **2050** para prever a elevação futura.

4. **Análise de Dados Recentes**:
   - Criação de uma nova linha de melhor ajuste utilizando apenas os dados de **2000** em diante.
   - Previsão da elevação do nível do mar até **2050** considerando a taxa recente de aumento.

5. **Personalização do Gráfico**:
   - **Eixo X**: Ano
   - **Eixo Y**: Nível do Mar (polegadas)
   - **Título**: Elevação do Nível do Mar

## 📦 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sea_level_predict.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd analise-nivel-do-mar
   ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate    # Windows
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute o script principal:
   ```bash
   python sea_level_predict.py
   ```

## 📊 Exemplos de Visualizações

- Gráfico de dispersão com linha de regressão até 2050.
- Comparativo entre a previsão global e a previsão baseada em dados recentes.

## ✨ Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests. 🙌

---
Feito com 🌊, 📈 e muita curiosidade científica! 🚀

# Sea Level Predictor

This is the boilerplate for the Sea Level Predictor project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor
