#creo una classe che contenga le aziende che espongono nell centro Lingotto Fiere
class Espositore:
    def __init__(self, codice, nome, cognome):
        self._codice = codice
        self._nome = nome
        self._cognome = cognome

    @property                     #avendo protetto con '_' gli attributi della classe espositore
    def codice(self):             #utilizzo il decoratore GETTER per avere accesso agli stessi
        return self._codice
    @property
    def nome(self):
        return self._nome
    @property
    def cognome(self):
        return self._cognome

    # ridefinisco il metodo per il confronto di due espositori
    def __eq__(self, other):
        if isinstance(other, Espositore):   #isinstance mi serve per assicurarmi che il confronto avvenga effettivamnete
            return self.codice == other.codice    #tra due oggetti appartenenti alla classe
        return False

    #metodi per la rappresentazione testuale
    def __str__(self):
        return f"{self.codice} - {self.nome} - {self.cognome}"

    def __repr__(self):
        return self.__str__()

#creo la classe padre Stand
class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self._codice = codice
        self._superficie = float(superficie)
        self._padiglione = int(padiglione)
        self._prezzo_base = float(prezzo_base)
#inizializzo l'atributo espositore, che al momento è None perchè verrà riempito quando uno stand verrà assegnato
#ad un espositore
        self._espositore = None

#decoratore GETTER
    @property
    def codice(self): return self._codice
    @property
    def superficie(self): return self._superficie
    @property
    def padiglione(self): return self._padiglione
    @property
    def prezzo_base(self): return self._prezzo_base

#gestione dell'espositore
    @property
    def espositore(self): return self._espositore
    @espositore.setter                             #permette di assegnare l'espositore tramite
    def espositore(self, nuovo_espositore):        #stand.espositore =
        self._espositore = nuovo_espositore

    @property                 #definisco questa proprietà per conodita: restituisce True se lo stand è libero
    def disponibile(self):    #false se è occupato
        return self._espositore is None

#metodo per il calcolo del prezzo
    def calcola_prezzo(self):       #calcola il prezzo degli stand, per quelli standard corrisponderà a quello base
        return self._prezzo_base    #farò poi overriding per le classi figlie

#metodo per l'odinamneto
    def __lt__(self, other):
        if isinstance(other, Stand):
            return self.calcola_prezzo() < other.calcola_prezzo()
        return NotImplemented
#metodo per l'guaglianza, due stand sono uguali se hanno lo stesso codice
    def __eq__(self, other):
        if isinstance(other, Stand):
            return self._codice == other.codice
        return False

    def __str__(self):
        #costruisco lo stato di disponibilità
        stato = "Diponibile" if self.disponibile() else f"Assegnato a {self._espositore.codice}"
        mq = int(self._superficie) if self._superficie.is_integer() else self._superficie
        return f"{self.superficie}: Standard | {mq} mq - Padiglione {self._padiglione} - Prezzo {self.calcola_prezzo():.2f} - {stato}"

    def __repr__(self):
        return self.__str__()

#creo le classi figlie StandPrese e StandPremium
class StandPrese(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, numero_prese):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self._numero_prese = int(numero_prese)

    @property
    def numero_prese(self):
        return self._numero_prese


#POLIMORFISMO: faccio overriding di calcola prezzo della classe padre
    def calcola_prezzo(self):
        #applica un sovrapprezzo del 7% per ogni presa elettrica
        return self.prezzo_base * (1 + 0.07 * self._numero_prese)

    def __str__(self):
        stato = "Disponibile" if self.disponibile() else f"Assegnato a {self._espositore.codice}"
        mq = int(self.superficie) if self.superficie.is_integer() else self.superficie
        return (f"{self._codice}: Prese Extra | {mq} mq - Padiglione {self._padiglione} - "
                f"Prezzo {self.calcola_prezzo():.2f}€ - Prese aggiuntive: {self._numero_prese} - {stato}")

class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self._posizione = str(posizione)

    @property
    def posizione(self):
        return self._posizione
#POLIMORFISMO: faccio overriding di calcola_prezzo
    def calcola_prezzo(self):           #applica una maggiorazione del 30% sul prezzo base
        return self.prezzo_base * 1.30

    def __str__(self):
        stato = "Disponibile" if self.disponibile else f"Assegnato a {self._espositore.codice}"
        mq = int(self.superficie) if self.superficie.is_integer() else self.superficie
        return (f"{self._codice}: Premium | {mq} mq - Padiglione {self._padiglione} - "
                f"Prezzo {self.calcola_prezzo():.2f}€ - Posizione: {self._posizione} - {stato}")
















class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
