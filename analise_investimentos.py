import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

inicio = '2025-12-22'
fim = '2026-03-02'

acao = yf.download("PETR4.SA", start=inicio, end=fim)

if "Adj Close" in acao.columns:
    acao["retorno"] = acao["Adj Close"].pct_change()
else:
    acao["retorno"] = acao["Close"].pct_change()

cdi_diario = (1 + 0.13) ** (1/252) - 1
ipca_diario = (1 + 0.06) ** (1/252) - 1

dados = pd.DataFrame(index=acao.index)

dados["PETR4"] = (1 + acao["retorno"]).cumprod()
dados["CDI"] = [(1 + cdi_diario) ** i for i in range(len(dados))]
dados["IPCA"] = [(1 + ipca_diario) ** i for i in range(len(dados))]

dados = dados / dados.iloc[0] * 100

plt.figure(figsize=(10,5))
plt.plot(dados["CDI"], label="CDI", color='orange', zorder=1)
plt.plot(dados["IPCA"], label="IPCA", color='green', zorder=2)
# O zorder=3 coloca a linha azul por cima das outras
plt.plot(dados["PETR4"], label="PETR4", color='blue', linewidth=2, zorder=3)

plt.legend()
plt.grid()
# Definimos as cores e a ordem (zorder maior fica por cima)
plt.plot(dados["CDI"], label="CDI", color='orange', zorder=1)
plt.plot(dados["IPCA"], label="IPCA", color='green', zorder=2)
plt.plot(dados["PETR4"], label="PETR4", color='blue', zorder=3) # PETR4 por cima de tudo

# 2. Melhora as marcações das datas para tentar mostrar o final de 2025
plt.gcf().autofmt_xdate()
plt.show()


print(dados.iloc[-1])