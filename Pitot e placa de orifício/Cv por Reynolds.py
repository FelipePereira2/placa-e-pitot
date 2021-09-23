import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

uri='https://raw.githubusercontent.com/FelipePereira2/placa-e-pitot/main/dados%20filtrados%20-%20Planilha1.csv'
df=pd.read_csv(uri)
x=df['Reynolds']
y=df['Cv']
plt.scatter(x,y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),'--r')
plt.xlabel('Coeficiente de Reynolds')
plt.ylabel('Coeficiente do tubo de Pitot')
plt.title('Coeficiente do tubo de Pitot por Reynolds')
plt.legend(["Curva de tendência","Testes"])
plt.grid()
plt.show()