from orm import Table
from connections import CONNECTION
Table.connect(config_dict=CONNECTION)

class Clienti(Table):
    table_name = 'clienti'