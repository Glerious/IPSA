import pandas as pd
from matplotlib.pyplot import scatter, show, title
from functions import Functions


#import de donnée
data = pd.read_csv("Au311_Analyse_donnée/TP2/ressources/alcanes.csv", sep=";", encoding="latin1" , engine='python')

# détermination des colonnes de lectures
pe = data.iloc[:,2]
na = data.iloc[:,3]
h = data.iloc[:,4]
x1 = data.iloc[:,5]

given : dict = dict(zip(h, pe))

correlation = Functions(given=given)
correlation.graph()
print(correlation.r)









