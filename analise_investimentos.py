import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

inicio = "2022-01-01"
fim = "2024-01-01"

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
plt.plot(dados["PETR4"], label="PETR4")
plt.plot(dados["CDI"], label="CDI")
plt.plot(dados["IPCA"], label="IPCA")

plt.legend()
plt.grid()
plt.show()

print(dados.iloc[-1])