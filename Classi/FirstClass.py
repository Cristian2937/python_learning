class Persona:
    # DICHIARO IL COSTRUTTORE PER LA CLASSE Persona
    def __init__(self,nome="",cognome=""): # self SERVE A FAR CAPIRE A PYTHON CHE OGNI OGGETTO QUANDO VIENE INSTANZIATO E' UNICO
        self.nome = nome
        self.cognome = cognome
        
            
    def set_nome(self,nome):
        self.nome = nome
    def get_nome(self)->str:
        return self.nome
    def set_cognome(self,cognome):
        self.cognome = cognome
    def get_cognome(self)->str:
        return self.cognome
