import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'Y':[1, 3, 5, 7, 9], 'X':[0, 2, 4, 6, 8]})

df.plot(kind='line')
plt.show()