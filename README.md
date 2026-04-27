# 📉 Análise Quantitativa e Comparativa de Ativos Financeiros

Este projeto utiliza Python para realizar uma análise de performance de ativos, comparando papéis de renda variável (ex: PETR4) com indicadores de referência do mercado brasileiro (Benchmarks), como o **CDI** e o **IPCA**.

### 🎯 Objetivos da Análise
* **Cálculo de Retorno Real:** Avaliar o ganho dos ativos descontando a inflação (IPCA).
* **Volatilidade e Risco:** Analisar a variação de preços para entender o perfil de risco da alocação.
* **Comparação com CDI:** Validar se a estratégia de investimento superou o custo de oportunidade livre de risco.

### 🛠 Tecnologias Utilizadas
* **Python:** Para processamento e automação dos cálculos.
* **Pandas:** Manipulação de séries temporais financeiras.
* **YFinance:** Extração de dados históricos diretamente da B3/Yahoo Finance.
* **Matplotlib/Seaborn:** Visualização de curvas de patrimônio e correlações.

### 📊 Metodologia Analítica
1. **Coleta:** Importação automatizada de cotações históricas.
2. **Normalização:** Ajuste de bases para comparação direta (Base 100).
3. **Visualização:** Gráficos de linha para acompanhamento da rentabilidade acumulada.

### 📈 Performance Acumulada (Base 100)
![Gráfico de Investimentos](Gráfico.png)

### 📝 Resultados Obtidos

* **Performance Superior (Alfa):** Através da normalização para a Base 100, observa-se que o ativo (PETR4) apresentou um desempenho significativamente superior ao CDI e ao IPCA no período analisado.
* **Ganho Real:** A distância entre a linha azul (Ativo) e a linha tracejada verde (IPCA) demonstra um ganho real robusto, superando a inflação e o custo de oportunidade livre de risco.
* **Validação Estratégica:** Análise gráfica comprova que a estratégia de alocação no ativo foi bem-sucedida em termos de rentabilidade absoluta e relativa.
