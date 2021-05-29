import numpy as np

# Chapter 4
def programpcex():
  N = 100 # numero di step temporali
  G = 20 * np.ones(N) 
  G[0] = 0 # tutte le quantità sono rappresentati con vettori colonna che sono assemblati nella matrice SIM 
  theta = 0.2 # tax rate
  alpha1 = 0.6 # alpha1 and alpha2 sono le costanti che determinano il consume formula 3.7
  alpha2 = 0.4
  lambda0 = 0.00
  lambda1 = 0.00
  lambda2 = 0.00
  r = 0.02
  Y = np.zeros(N) # vettore influssi di cassa per ogni household
  YD = np.zeros(N) # vettore del disposable income
  YDE = np.zeros(N) # vettore del expected disposable income
  C = np.zeros(N) # vettore consumo delle household nel periodo;
  T = np.zeros(N) # vettore tasse ad ogni step temporale
  HD = np.zeros(N) # vettore expected risparmio ad ogni ciclo
  BD = np.zeros(N) # vettore expected risparmio ad ogni ciclo
  V = np.zeros(N) # vettore expected risparmio ad ogni ciclo
  VE = np.zeros(N) # vettore expected risparmio ad ogni ciclo
  BH = np.zeros(N) # vettore ricchezza
  HH = np.zeros(N) # vettore incrememnto ricchezza ad ogni ciclo
  for t in range(1,N):
    if t >= 1: # Il risparmio iniziale ad ogni periodo è uguale al risparmio finale del period precedente. Il primo deve essere forzato a zero per cui il ciclo if
      YDE[t] = YD[t-1]
    elif t == 0:
      YDE[t] = G[t] - theta * G[t]
    
    C[t] = alpha1 * YDE[t] + alpha2 * V[t-1] # Determinazione del consume del periodo. È un numero sempre inferior a TD(i)
    VE[t] = V[t-1] + ( YDE[t] - C[t] )
    Y[t] = G[t] + C[t] # Y è il totale degli influssi 
    T[t] = theta * Y[t] # pagamentodelle tasse
    YD[t] = Y[t] - T[t] # Disposable income = pagamenti ricevuti meno tasse pagate
    BD[t] = VE[t] * ( lambda0 + lambda1 * r ) - lambda2 * YDE[t]
    HD[t] = VE[t] - BD[t]
    BH[t] = BD[t]
    HH[t] = HD[t] + ( YD[t] - YDE[t] )

    SIM = [G, Y, T] # matrice con tutti I termini precedent. Una riga è un ciclo i

  print(G[0], G[1], G[2], G[N-1])
  print(Y[0], Y[1], Y[2], Y[N-1])
  print(T[0], T[1],	T[2], T[N-1])
  print(BH[0], BH[1],	BH[2], BH[N-1])
  print(HH[0], HH[1],	HH[2], HH[N-1])
  

# Chapter 4
def programpc():
  # Il programma include due loop nested. Il loop esterno fa avanzare il tempo, il loop internofa avanzare I cicli di consume all’interno di un period.
  TIME = 100 # numero di step temporali

  theta = 0.2 # tax rate
  alpha1 = 0.6 # alpha1 and alpha2 sono le costanti che determinano il consume formula 3.7
  alpha2 = 0.4
  lambda2 = 0.001
  lambda1 = 0.02
  lambda0 = 0.2

  N = 100  # numero di iterazioni nel loop interno
  G = np.zeros(N) # tutte le quantità sono rappresentati con vettori colonna che sono assemblati nella matrice SIM 
  G[1] = 20 # valore costante del consume del governo

  HINIT = np.zeros(N)
  HFIN = np.zeros(N)
  VINIT = np.zeros(N)
  VFIN = np.zeros(N)
  BHINIT = np.zeros(N)
  BHFIN = np.zeros(N)
  YPERIOD = np.zeros(N)
  TPERIOD = np.zeros(N)
  VPERIOD = np.zeros(N)
  HPERIOD = np.zeros(N)
  BPERIOD = np.zeros(N)
  YDPERIOD = np.zeros(N)
  CPERIOD = np.zeros(N)
  DVPERIOD = np.zeros(N)
  BHPERIOD = np.zeros(N)

  for t in range(0,TIME):
    if t >= 1: #Il risparmio iniziale ad ogni periodo è uguale al risparmio finale del period precedente. Il primo deve essere forzato a zero per cui il ciclo if
        VINIT[t] = VFIN[t-1]
        HINIT[t] = HFIN[t-1]
        BHINIT[t] = BHFIN[t-1]
    elif t == 0:
        VINIT[0] = 0
        HINIT[0] = 0
        BHINIT[0] = 0

    r = 0.02 * np.ones(N) # vettore tassi di interesse
    Y = np.zeros(N) # vettore influssi di cassa per ogni household
    YD = np.zeros(N) # vettore del disposable income
    C = np.zeros(N) # vettore consume delle household; ATTN. ogni element del vettore è il consume in ogni ciclo interno non quello globale del periodo
    T = np.zeros(N) # vettore tasse ad ogni ciclo
    B = np.zeros(N) # bills posseduti dalle households
    BH = np.zeros(N) # bills posseduti dalle households
    DH = np.zeros(N) # vettore incrememnto risparmio ad ogni ciclo
    DV = np.zeros(N) # vettore incrememnto risparmio ad ogni ciclo
    DBH = np.zeros(N) # vettore incrememnto risparmio ad ogni ciclo
    V = np.zeros(N) # vettore incrememnto risparmio ad ogni ciclo
    V[0] = VINIT[t] # valore del risparmio iniziale ad ogni periodo; tutti gli altri elementi di V sono uguali a zero
    # inizia il loop interno per ogni time step; ad ogni valore di I corrisponde un ciclo complete, ricezione dell’ordine da parte delle aziende, pagamento dei dipendenti, pagamento delle tasse, consume e risparmio aggiornamento del risparmio
    for i in range(0,N):
      Y[i] = G[i] + C[i-1] # Y è il totale della transazione 
      T[i] = theta * ( Y[i] + r[i-1] * BH[i-1] ) # pagamentodelle tasse
      YD[i] = Y[i] - T[i] + r[i-1] * BH[i-1] # Disposable income = pagamenti ricevuti meno tasse pagate
      C[i] = alpha1 * YD[i] + alpha2 * V[i-1] # Determinazione del consume al prossimo periodo. È un numero sempre inferior a TD(i)
      DV[i] = YD[i] - C[i]
      DH[i] = DV[i] * ( 1 - lambda0 ) - lambda1 * r[i] + lambda2 * YD[i]
      DBH[i] = DV[i] * lambda0 + lambda1 * r[i] - lambda2 * YD[i]
              
    VFIN[t] = VINIT[t] + sum(DV)
    VPERIOD[t] = VFIN[t]
    HFIN[t] = HINIT[t] + sum(DH)
    HPERIOD[t] = HFIN[t]
    BHFIN[t] = BHINIT[t] + sum(DBH)
    BHPERIOD[t] = BHFIN[t]
    
    YPERIOD[t] = sum(Y)
    TPERIOD[t] = sum(T)
    YDPERIOD[t] = sum(YD)
    CPERIOD[t] = sum(C)
    DVPERIOD[t] = sum(DV)
    BPERIOD[t] = B[N-1]

  RES = [YPERIOD, TPERIOD, YDPERIOD, VPERIOD, CPERIOD,  HPERIOD, BPERIOD]

  print(YPERIOD[0], YPERIOD[1], YPERIOD[TIME-1])
  print(TPERIOD[0], TPERIOD[1], TPERIOD[TIME-1])
  print(YDPERIOD[0], YDPERIOD[1],	YDPERIOD[TIME-1])
  print(VPERIOD[0],	VPERIOD[1],	VPERIOD[TIME-1])
  print(CPERIOD[0],	CPERIOD[1],	CPERIOD[TIME-1])
  print(HPERIOD[0],	HPERIOD[1],	HPERIOD[TIME-1])
  print(BPERIOD[0],	BPERIOD[1],	BPERIOD[TIME-1])


# Chapter 3
def simex():
  N = 100 # numero di step temporali

  G = 20 * np.ones(N)
  G[0] = 0 # tutte le quantità sono rappresentati con vettori colonna che sono assemblati nella matrice SIM
  G[1] = 20 # valore costante del consume del governo

  theta = 0.2 # tax rate
  alpha1 = 0.6  # alpha1 and alpha2 sono le costanti che determinano il consume formula 3.7
  alpha2=0.4;

  Y = np.zeros(N) # vettore influssi di cassa per ogni household
  YD = np.zeros(N) # vettore del disposable income
  YDE = np.zeros(N) # vettore del expected disposable income
  C = np.zeros(N) # vettore consumo delle household nel periodo;
  T = np.zeros(N) # vettore tasse ad ogni step temporale
  H = np.zeros(N) # vettore ricchezza
  DH = np.zeros(N) # vettore incrememnto ricchezza ad ogni ciclo

  for t in range(0,N):
    if t >= 1: # Il risparmio iniziale ad ogni periodo è uguale al risparmio finale del period precedente. Il primo deve essere forzato a zero per cui il ciclo if
      YDE[t] = YD[t-1]
      
    elif t == 0:
      YDE[t] = G[t] - theta * G[t]
        
    C[t] = alpha1 * YDE[t] + alpha2 * H[t-1] # Determinazione del consume al prossimo periodo. È un numero sempre inferior a TD(i)
           
    Y[t] = G[t] + C[t] # Y è il totale della transazione 
    T[t] = theta * Y[t] # pagamentodelle tasse
    YD[t] = Y[t] - T[t] #Disposable income = pagamenti ricevuti meno tasse pagate
        
    DH[t] = YD[t] - C[t] # risparmio uguale al disposable income meno il consume
    H[t] = H[t-1] + DH[t] # risparmio alla fine del period t
    
    SIM=[G, Y, T, C, YDE, DH, H] # matrice con tutti I termini precedent. Una riga è un ciclo i
 
  print(G[N-1], Y[N-1], T[N-1], YDE[N-1], DH[N-1], H[N-1])
  

# Chapter 3
def sim():
  # Il programma include due loop nested. Il loop esterno fa avanzare il tempo, il loop internofa avanzare I cicli di consume all’interno di un period.
  T = 1000 # numero di step temporali
  theta = 0.2 # tax rate
  alpha1 = 0.6 # alpha1 and alpha2 sono le costanti che determinano il consume formula 3.7
  alpha2 = 0.4
  N = 1000 # numero di iterazioni nel loop interno

  G = np.zeros(N)  # tutte le quantità sono rappresentate con vettori colonna assemblati nella matrice SIM
  HINIT = np.zeros(N)
  HFIN = np.zeros(N)
  YPERIOD = np.zeros(N)
  TPERIOD = np.zeros(N)
  YDPERIOD = np.zeros(N)
  CPERIOD = np.zeros(N)
  DHPERIOD = np.zeros(N)

  for t in range(0,T):
    G[1] = 20 # valore costante del consume del governo
    if t>=1: # Il risparmio iniziale ad ogni periodo è uguale al risparmio finale del period precedente. Il primo deve essere forzato a zero per cui il ciclo if
      HINIT[t] = HFIN[t-1]
    elif t == 0:
      HINIT[0]=0
    
    F = np.zeros(N) # vettore dei pagamenti effettuati dale aziende che sono uguali agli incassi delle aziende
    L = np.zeros(N); # vettore incassi household
    Y = np.zeros(N) # vettore influssi di cassa per ogni household
    YD = np.zeros(N) # vettore del disposable income
    C = np.zeros(N) # vettore consume delle household; ATTN. ogni element del vettore è il consume in ogni ciclo interno non quello globale del periodo
    TAX = np.zeros(N) # vettore tasse ad ogni ciclo
    H = np.zeros(N) # vettore risparmio ad ogni ciclo
    DH = np.zeros(N) # vettore incrememnto risparmio ad ogni ciclo
    H[0] = HINIT[t] # valore del risparmio iniziale ad ogni period; tutti gli altri elementi di H sono uguali a zero
    
    # inizia il loop interno per ogni time step; ad ogni valore di I corrisponde un ciclo complete, ricezione dell’ordine da parte delle aziende, pagamento dei dipendenti, pagamento delle tasse, consume e risparmio aggiornamento del risparmio
    for i in range(1,N):
      F[i] = G[i] + C[i-1] # Le aziende ricevono gli ordini. G(i) è zero eccetto in G(2). Al ciclo I l’azienda riceve ordini sulla decisione di consume del ciclo i-1 
      L[i] = G[i] + C[i-1] # household ricevono I pagamenti
      Y[i] = G[i] + C[i-1] # Y è il totale della transazione 
      TAX[i] = theta * Y[i] # pagamentodelle tasse
      YD[i] = Y[i] - TAX[i] # Disposable income = pagamenti ricevuti meno tasse pagate
      C[i] = alpha1 * YD[i] + alpha2 * H[i-1] # Determinazione del consume al prossimo periodo. È un numero sempre inferior a TD(i)
      DH[i] = YD[i] - C[i] # risparmio uguale al disposable income meno il consumo

    HFIN[t] = HINIT[t] + sum(DH) # risparmio alla fine del period t

    SIM = [G, F, L, Y, TAX, YD, C, DH, H] # matrice con tutti I termini precedent. Una riga è un ciclo i

    YPERIOD[t] = sum(Y) # dati consolidati ad ogni period. Sono la somma delle tansazioni ad ogni ciclo
    TPERIOD[t] = sum(TAX)
    YDPERIOD[t] = sum(YD)
    CPERIOD[t] = sum(C)
    DHPERIOD[t] = sum(DH)

  print(YPERIOD[0], YPERIOD[1], YPERIOD[T-1])
  print(TPERIOD[0], TPERIOD[1], TPERIOD[T-1])
  print(YDPERIOD[0], YDPERIOD[1],	YDPERIOD[T-1])
  print(CPERIOD[0],	CPERIOD[1],	CPERIOD[T-1])
  print(DHPERIOD[0], DHPERIOD[1], DHPERIOD[T-1])


programpcex()