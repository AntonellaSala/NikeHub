# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:00:48 2019

@author: Anto & Elena
"""
#%%

rule30 = {"000": '.',
          "00.": '.',
          "0.0": '.',
          "...": '.',
          "0..": '0',
          ".00": '0',
          ".0.": '0',
          "..0": '0',
         }


#%%

#%%file Es1_rule30byAnto.py

def generate_state():
    return "..........0..........."

def bordi(tipo_bordo,stato_dato):
    # bordo costante .
    if tipo_bordo==1: stato_dummy = "."+ stato_dato + "." 
    # bordo costante 0
    if tipo_bordo==2: stato_dummy = "0"+ stato_dato + "0" 
    # bordo circolare
    if tipo_bordo==3: stato_dummy = stato_dato[len(stato_dato)-1] + stato_dato + stato_dato[0] 
    #bordo riflesso
    if tipo_bordo==4: stato_dummy =stato_dato[0] + stato_dato + stato_dato[len(stato_dato)-1]
    return stato_dummy
    
def evolve(stato_dato):
    stato_sotto = ""
    for posto in range(len(stato_dato)-1):
        trio=stato_dato[posto:posto+3]
        for KEY,VALUE in rule30.items():
            if trio==KEY:
                stato_sotto += VALUE
    return stato_sotto

def simulation(nsteps):
    initial_state = generate_state()
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = bordi(tipo_bordo,states_seq[-1])
        new_state = evolve(old_state)
        states_seq.append(new_state)
    return states_seq
#%%
    
# inizio programma
# sezione di input
tipo_bordo = int(input("1-> fisso punto\n2-> fisso zero\n3-> circolare\n4-> riflesso\nSe valore errato -> default fisso punto\nInput tipo bordo: "))
if tipo_bordo <1 or tipo_bordo>4: tipo_bordo=1
iterazioni = int(input("\nNumero iterazioni: "))
# esecuzione simulazione
simulation(iterazioni)
#%%

########################################################

def test_generation_valid_state():
    state = generate_state()
    assert set(state) == {'.', '0'}
    

def test_generation_single_alive():
    state = generate_state()
    num_of_0 = sum(1 for i in state if i=='0')
    assert num_of_0 == 1
    
#%%

