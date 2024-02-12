from Classi.FirstClass import Persona # metodo per importare un'altra classe nello stesso file
class Insegnante(Persona):
    def __init__(self, nome="", cognome="",categoria=""):
        super().__init__(nome, cognome) # super() viene utilizzato per ottenere i tipi di dato della classe ereditata
        self.categoria = categoria
    
    #  DATO CHE HO EREDITATO DALLA CLASSE PERSONA TUTTO QUELLO CHE ERA PRESENTE AL SUO INTERNO
    #  HO ANCHE EREDITATO I METODI GET E SET
    # def set_nome(self,nome):
    #     self.nome = nome
    # def get_nome(self)->str:
    #     return self.nome
    # def set_cognome(self,cognome):
    #     self.cognome = cognome
    # def get_cognome(self)->str:
    #     return self.cognome
    
    # UNA VOLTA EREDITATA UNA CLASSE POSSO A SUA VOLTA INSERIRE ALTRI PARAMETRI E METODI ESCLUSIVI PER LA CLASSE FIGLIA ES.
    def set_categoria(self,categoria):
        self.categoria = categoria
    def get_categoria(self)->str:
        return self.categoria
    
    # Eseguire l'override del metodo
    def saluta(self):
        print("Buongiorno sono "+ self.nome + " " + self.cognome)
    
    def to_string(self)-> str:  # creato un metodo to_string custom per la lettura dei dati
        return  "{} {}".format(self.nome,self.cognome)
    
