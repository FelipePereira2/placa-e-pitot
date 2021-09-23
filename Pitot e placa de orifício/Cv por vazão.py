import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

uri='https://raw.githubusercontent.com/FelipePereira2/placa-e-pitot/main/dados%20filtrados%20-%20Planilha1.csv'
df=pd.read_csv(uri)
x=df['Vazão [m³/s]']
y=df['Cv']
plt.scatter(x,y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),'--r')
plt.xlabel('Vazão [m³/s]')
plt.ylabel('Coeficiente do tubo de pitot')
plt.title('Coeficiente do tubo de pitot para cada vazão')
plt.legend(["Curva de tendência","Testes"])
plt.grid()
plt.show()