'''
c => Craete (INSET INTO)
R => Reas (SELECT)
U => Update (Udate)
D => Delete (DELATE)

UPDATE AND DELETE NEED A WHERE CLAUSE
'''
from database import con , cur
import os
def main_menu():
    print("::: MAIN MENU:::")
    print("[1]. Create user ")
    print("[2]. List users ")
    print("[3]. Salir")
    opt = int(input('press any option:'))
    return opt

def create_user():
    new_user_query ='''
    INSERT INTO users(username,email,password) 
        VALUES('Tatiana','ximenatatianadiazrosero@gmail.com','123456')
    '''
    con.execute(new_user_query)
    con.commit()
    
    print('user create succesfully.')
    os.system('pause')
    con.close()
    
create_user()