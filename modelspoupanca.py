import pyodbc


connection = pyodbc.connect('DRIVER={MySQL ODBC 3.51 Driver};SERVER=localhost;DATABASE=TMTST;UID=root;PWD=123;')

if connection:
    print("Yes, we are connected!!!\n")

sql = '''\

INSERT INTO `apcef`.`findice`
   (`Findice_codigo`,`Findice_nome`,`Findice_data`,`Findice_valor`)

VALUES  (?,?,?,?) ON DUPLICATE KEY UPDATE Findice_data = ?

'''


