from Modules.functions import Functions


from math import exp, log, pi
from csv import reader
from matplotlib.pyplot import bar, scatter, plot, boxplot, hist, ylabel, xlabel, title, legend, grid, show
from numpy import mean, std, var, cov, sum, array, sqrt, percentile, savetxt, linspace, log
from statistics import median
from scipy.stats import poisson, binom, norm, describe

from pandas import read_csv


# 1 Ferme industrielle

def exercice1():

    """1"""
    with open('dataMP.csv','r') as f:
        read = reader(f, delimiter = ';')
        rows = list(read)
        # Inverser les lignes et les colonnes
        transposed_rows = list(map(list, zip(*rows)))
        X = transposed_rows[1]
        # print(transposed_rows[2])
        Y = transposed_rows[2]
    X.pop(0)
    Y.pop(0)
    for i in range(len(X)):
        X[i] = float(X[i])
        Y[i] = float(Y[i])   
    print(X)
    print(Y)


    """ 2 """
    scatter(X, Y, label = 'X en fonciton de Y')

    """3"""
    x_ = mean(X)
    y_ = mean(Y)
    print('moyenne x :',x_)
    print('moyenne y :',y_)

    ecart_x = std(X)
    ecart_y = std(Y)
    print('ecart x :',ecart_x)
    print('ecart y :',ecart_y)


    """4"""
    cov_xy = cov(X,Y)[0,1]
    print("covariance = ",cov_xy)


    """5"""
    r = cov_xy/(ecart_x * ecart_y)
    print('r = ',r)
    #conclure sur r


    """6"""
    V_x = var(X)
    V_y = var(Y)

    a = cov_xy/V_x
    print("a : ",a)
    b = y_ - a*x_
    print("b : ",b)
    Y1 = []
    for i in range(len(X)):
        Y1.append(a*X[i] + b)
    plot(X, Y1, label="Y en fonction de X")


    """7"""
    scatter(x_,y_,label='G',color='r')
    print("Est-ce que le point G appartient à la droite?" ,y_== a*x_ + b)

    xlabel('X')
    ylabel('Y')
    legend()
    grid()
    show()


    """8"""
    Y_chap = []
    for i in X:
        Y_chap.append(a*i+b)

    epsi_2 = 0
    for i in range (len(Y)):
        epsi_2 += (Y[i]-Y_chap[i])**2
    V_r1 = (1/len(Y))*epsi_2 # pas de -2 car pas fait en cours
    print("Variance residuelle (M1) est ", V_r1)

    # Calcul de la variance résiduelle
    V_r2 = sum((array(Y) - array(Y_chap)) ** 2) / (len(Y)-2) #-2 car nbr de paramètre
    print("Variance residuelle (M2) est ", V_r2) #laquelle est la bonne


    V_e1 = a**2 * V_x
    print("Variance expliquée (M1) est ", V_e1)

    #Calcul de la variance expliquée
    V_e2 = sum((Y_chap - y_) ** 2)
    print("Variance expliquée (M2) est ", V_e2)

# 2 Décharge d'un condensateur

def exercice2():
    table = {0: log(5.098), 5: log(3.618), 10: log(2.581), 15: log(2.011), 20: log(1.486), 25: log(1.028), 30: log(0.845), 35: log(0.573), 40: log(0.429), 45: log(0.29), 50: log(0.2)}

    new = Functions(table, "Temps (ms)","Voltage condensateur (V)" )
    print(new.covxy)
    print(new.r)
    new.graph()

    def funcV(t):
        return round(5.1*exp(-t/16.66), 3)

    for i in range(0, 55, 5):
        print(i, funcV(i))

def exercice3():
    table = {100: 10, 61: 50, 76: 84, 74: 99, 90: 113, 93: 122, 102: 128, 98: 143, 103: 145, 110: 145, 117: 159, 118: 172, 112: 188, 115: 204, 116: 213, 121: 220, 134: 242, 130: 254}

    new = Functions(table, "Production agricole", "Production industrielle")

    # 3 . 1

    new.graph()
    print("covariance x, y : ", new.covxy)
    print("r : ", new.r)

    for x in table.keys():
        print(new.func(x))

    print("variance : ", new.covyy)
    print("variance résiduelle : ", new.residual_var())
    print("variance expliqué : ", new.explained_var())

    # 3 . 2

    for y in table.values():
        print(new.antifunc(y))

    print("variance : ", new.covxx)
    print("variance résiduelle : ", new.antiresidual_var())
    print("variance expliqué : ", new.antiexplained_var())

    new.graph(False)

def exercice4():
    
    #4.1
    #la population étudier est une liste de tailles de la rectrice centrale de 50 male gelinotte huppées
    
    #4.2
    #la variable statistique est la taille des plume de chaque mal 

    #4.3
    #c'est une variable discret 
    #elle sont toute numérique et il n'y a pas une infinité de valeur dans cette liste, il n'y a que 50 valeur par une de plus 

    #4.4
    BonasaUmbellus = [153, 165, 160, 150, 159, 151, 163, 160, 158, 150, 154, 153, 163, 150, 158, 150, 158, 155 ,163 ,159, 157 ,162, 160 ,152 ,164 ,158 ,153, 162, 166 ,162 ,165, 157 ,174, 158, 171, 162, 155, 156, 159, 162, 152, 158, 164, 164, 162, 158, 156, 171, 164, 158]

    #4.5
    min_BU = min(BonasaUmbellus); max_Bu= max(BonasaUmbellus); etendueBU = max_Bu-min_BU; moyenne_BU = sum(BonasaUmbellus)/len(BonasaUmbellus); mediane_BU = median(BonasaUmbellus); quartille_BU_Q1,quartille_BU_Q2, quartille_BU_Q3 = percentile(BonasaUmbellus, [25, 50, 75]); iqr_BU = quartille_BU_Q3 - quartille_BU_Q1

    #4.6
    variance_BU = var(BonasaUmbellus) ; ecart_type_BU = sqrt(variance_BU)   
    print(variance_BU,ecart_type_BU)
    print(moyenne_BU)
    #si ont calcule moyenne(+ou-) 2ecartype ==> (140 à 170) on trouve presque tout les valaleur du tableau (sauf 3) ce qui est plutot cohérant. 

    #4.7
    boxplot(BonasaUmbellus)
    title('Boîte à moustaches de la série de données')
    xlabel('Variable')
    ylabel('Valeurs')
    show()
    #on retrouve bien les même valeur suposer plus haut

    #4.8    
    hist(BonasaUmbellus, bins=10, color='blue', edgecolor='black')
    title('Répartition des longueurs')
    xlabel('Longueur')
    ylabel('Fréquence')
    show()
    #les valeur du tableau sont bien cohérante 

def exercice5():
    babysWeight = [2.8, 3, 2.9, 2.4, 2.9, 3.7, 2.1, 3.4, 2.3, 3.1, 3.2, 2.6, 3.5, 3.4, 2.8, 1.9, 3.4, 2.5, 3.5, 2.8, 3.8, 1.8, 3, 2, 2.7, 2.6, 2.8, 1.9, 2.9, 2.6]

    savetxt("data.dat", babysWeight)

    with open("data.dat", "w") as file:
        for value in babysWeight:
            file.write(f"{value}\n")
    # Dans le cas où le fichier de data est inexistant, il est récréé pas les deux lignes précédentes
            
    hist(babysWeight, bins=10, color='blue', edgecolor='black')
    xlabel('Poids du bébé (g)')
    ylabel('fréquence')
    title("histogramme du poids des bébé présents dans la matérnité")
    show()

    boxplot(babysWeight)
    title('Boîte à moustaches de la série de données')
    xlabel('Variable')
    ylabel('Valeurs')
    show()

    dict_babysWeight = {1.8: 3, 2: 2, 2.2: 1, 2.4: 2, 2.6: 4, 2.8: 7, 3: 3, 3.2: 1, 3.4: 5, 3.6: 2}

    esperance = sum([i * j for i, j in dict_babysWeight.items()]) / len(babysWeight)
    ecartType = sqrt(sum([i**2 * j for i, j in dict_babysWeight.items()]) / len(babysWeight) - esperance ** 2)

    print(esperance, ecartType)
        
    m1 = sum(babysWeight[:15]) / 15
    m2 = sum(babysWeight[15:]) / 15

    print(m1, m2)
    print((m1 + m2) / 2)

def exercice6():

    # Paramètres
    p = 0.031175  # probabilité de détection du portique
    n = 500  # nombre total de personnes

    moyenne_binomiale = n * p
    ecart_type_binomiale = (n * p * (1 - p))**0.5

    esperance_X = moyenne_binomiale
    interpretation_esperance = "L'espérance représente le nombre moyen de personnes faisant sonner le portique."

    prob_at_least_one = 1 - binom.pmf(0, n, p)

    prob_at_most_3 = sum(binom.pmf(k, n, p) for k in range(4))

    approx_normale = norm(loc=moyenne_binomiale, scale=ecart_type_binomiale)

    prob_X_gt_50_approx = 1 - approx_normale.cdf(50)

    prob_X_eq_70_approx = approx_normale.pdf(70)

    lambda_poisson = n * p
    approx_poisson = poisson(mu=lambda_poisson)

def exercice7():
    Y = 0.9 * 400 
    espe =360
    var = 36 
    ecart_type= 6 

    y_values = linspace(espe - 3*ecart_type, espe + 3*ecart_type, 100)
    pdf_values = 1/(ecart_type * sqrt(2 * pi)) * exp(-(y_values - espe)**2 / (2 * ecart_type**2))

    plot(y_values, pdf_values, label='Densité de probabilité')
    title('Courbe de densité de probabilité de Y')
    xlabel('Y (Nombre de réussites dans une année)')
    ylabel('Densité de probabilité')
    legend()
    show()

    probability1 = 1 - norm.cdf(345, espe, ecart_type)

    proba2_1 = norm.cdf(400-28, espe, ecart_type)

    critical_value = binom.ppf(0.99, 400, 1 - 0.9)

def exercice9():
    data = {54: 12, 56: 12, 58: 15, 60: 18, 62: 20, 64: 23}

    data_list = []
    for i, j in data.items():
        data_list += [i]*j

    data_form = [i * j / sum(data.values()) for i, j in zip(data.keys(), data.values())]
    data_forv = [i**2 * j / sum(data.values()) for i, j in zip(data.keys(), data.values())]

    hist(data_list, bins=6, color='blue', edgecolor='black')
    title('Histogramme du poids des oeufs')
    xlabel('Poids (g)')
    ylabel('Fréquence')

    m = sum(data_form)
    v = sum(data_forv) - sum(data_form)**2
    print("moyenne : ", m, "\necart-type : ", sqrt(v))

def exercice10():

    """ Données """

    donnees = read_csv(r"Project/ressources/televisions.dat", delimiter='\t', na_values=' ')
    P = donnees['pays'].tolist()
    EV = donnees['espvie'].tolist()
    RT = donnees['teleratio'].tolist()
    PR = donnees['physratio'].tolist()
    EF = donnees['espvieF'].tolist()
    EH = donnees['espvieH'].tolist()

    """ Fonctions """

    def histogramme(EV,RT,PR,EF,EH):
        P = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
        bar(P,EV)
        title("Espérance de vie en fonction des pays")
        xlabel("Pays")
        ylabel("Espérance de vie (en année)")
        show()
        bar(P,RT)
        title("Ratio télé en fonction des pays")
        xlabel("Pays")
        ylabel("Ratio télé")
        show()
        bar(P,PR)
        title("Ratio physique en fonction des pays")
        xlabel("Pays")
        ylabel("Ratio physique")
        show()
        bar(P,EF)
        title("Espérance de vie des femmes en fonction des pays")
        xlabel("Pays")
        ylabel("Espérance de vie (en année)")
        show()
        bar(P,EH)
        title("Espérance de vie des hommes en fonction des pays")
        xlabel("Pays")
        ylabel("Espérance de vie (en année)")
        show()

    def resume(x):
        r = describe(x)
        return r

    def valeur_bizarre(x,RT):
        for i in x:
            if i==RT[31]:
                print(f"{i} est une valeurs atypiques.")

    def camembert(EV,EF,EH):
        P = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
        bar(P,EV)
        title("Espérance de vie en fonction des pays")
        xlabel("Pays")
        ylabel("Espérance de vie (en année)")
        show()
        bar(P,EF)
        title("Espérance de vie des femmes en fonction des pays")
        xlabel("Pays")
        ylabel("Espérance de vie (en année)")
        show()
        bar(P,EH)
        title("Espérance de vie des hommes en fonction des pays")
        xlabel("Pays")
        ylabel("Espérance de vie (en année)")
        show()
        boxplot([EV,EF,EH],labels=["Général","Femmes","Hommes"])
        title("Espérance de vie")
        ylabel("Année")
        show()

    def nuage_5(EV,RT):
        scatter(EV, RT, label="Brut")
        RT2 = RT
        EV2 = EV
        RT2.pop(31)
        RT2.pop(38)
        EV2.pop(31)
        EV2.pop(38)
        scatter(EV,RT,label="Sans valeurs atypiques")
        RT3 = log(RT)
        scatter(EV,RT3,label="Log(RT)")
        legend()
        show()

    def nuage_6(PR):
        EV = donnees['espvie'].tolist()
        scatter(EV, PR, label="Brut")
        scatter(EV,PR,label="Sans valeurs atypiques")
        PR2 = log(PR)
        scatter(EV,PR2,label="Log(RT)")
        legend()
        show()
        
    """ Exercice """
    #1):
        
    print("Question 1:")
    print("")
    print("Les données importés donnent les histogrammes suivants :")
    histogramme(EV, RT, PR, EF, EH)
    print("")

    #2):
    R_EV = resume(EV)
    R_RT = resume(RT)
    R_PR = resume(PR)
    R_EF = resume(EF)
    R_EH = resume(EH)
    print("Question 2 :")
    print("")
    print("• Le résumé numerique de l'espérance de vie est :",R_EV)
    print("• Le résumé numerique du ratio télé est :",R_RT)
    print("• Le résumé numerique du ratio physique est :",R_PR)
    print("• Le résumé numerique de l'espérance de vie des femmes est :",R_EF)
    print("• Le résumé numerique de l'espérance de vie des hommes est :",R_EH)

    #3):
    print("Question 3 :")  
    print("")
    print("Les données atypiques du ratio télé sont :")
    print("Pays n°32 et n°40")
    print("Les données atypiques du ratio physique sont :")
    print("Aucune valeur")
    print("")

    #4):
    print("Question 4 :")  
    print("")
    print("Les histogrammes et les camemberts de l'espérance de vie général, des femmes et des hommes sont :")
    camembert(EV, EF, EH)
    print("")

    #5):

    print("Question 5 :")  
    print("")
    print("Le nuage de point des valeurs de l'espérance de vie en fonction du ratio télé est :")
    nuage_5(EV, RT)

    #6):

    print("Question 6 :")  
    print("")
    print("Le nuage de point des valeurs de l'espérance de vie en fonction du ratio physique est :")
    nuage_6(PR)

exercice10()