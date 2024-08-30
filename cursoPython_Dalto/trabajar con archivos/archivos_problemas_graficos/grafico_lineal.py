import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("cursoPython_Dalto\\trabajar con archivos\\archivos_problemas_graficos\\pedos.csv")


sns.lineplot(x="fecha", y="pedos", data=df)

plt.plot("01-sep", 17,"o")
plt.show()