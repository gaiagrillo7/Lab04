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
