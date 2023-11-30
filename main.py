import sqlite3 as db 
from logs import *
from saglaba import *
import PySimpleGUI as sg
key_ievad = ('T-KATEG-','T-NOSAUK-','T-RAKSTUR-','T-Cena-')
key_li = ('-KATEG-','-NOSAUK-','-RAKSTUR-','-Cena-')
tab_nosauk =['Kategorija', 'Nosaukums', 'Tehn_raksturojums', 'Produkts', 'Noma', 'Nomnieks']
id_visi = ['id_kategorija', 'id_nosaukums', 'id_tehn_rakstur','id_produkts' , 'id_nomnieks']
#id_visi = ['id_kategorija', 'id_nosaukums', 'id_tehn_rakstur','id_produkts' , 'id_produkts','id_nomnieks']
kolonu_nosauk = ['kategorija', 'nosaukums', 'tehn_rakstur']
id_produktiem = []
# https://www.pysimplegui.org/en/latest/#jump-start
with db.connect('nomat.db') as con:
  cur = con.cursor()
  logs = Logs(cur)
  window = logs.logu_veido()
  event = ""
  while event != sg.WIN_CLOSED and event != 'Atcelt':
    event, values = window.read()
    if event in key_li: # atrod izveleto list notikumu
      text_event = 'T'+event # parveido par atbiltosho teksta notikumu
      #no_list_tuple uz str: [('urbjmašīna',)] uz urbjmašīna
      values[event] = values[event][0][0] #no_list_tuple uz str
      window[text_event].update(values[event]) #atjauno, lai redzetu
    elif (event == "Ievadīt"): # nospiesta poga "Ievadīt"
      flag = 1; # pārbauda vai visi ievaditi
      saglabat =[] # iztira sarakstu, kura saglabas ievadito
      for x in key_ievad:
        if values[x] == '':
          flag = 0 ; break
        else:
          saglabat.append(values[x]) #pievieno ievadito parametru
      if flag : 
        sg.popup(saglabat, background_color='#007733') 
        # saglabaa jaunam produktam 3 tabulas ar ID
        prod1=Saglaba(cur,saglabat[0],tab_nosauk[0],id_visi[0],kolonu_nosauk[0])
        for nr in range(3): 
          id_produktiem.append(
            prod1.saglaba_jauno(cur,saglabat[nr],tab_nosauk[nr],id_visi[nr],kolonu_nosauk[nr])
          ) 
        print("id_produktiem[nr] = ",id_produktiem)
        prod1.produkt_tab(id_produktiem,saglabat[3])
        con.commit()  #	Pec apstiprinajuma datus ievietot datu baze
        #izdruka tabulu nosauk, saturu
        for vards in tab_nosauk:
          prod1.druka_tab(vards)
        prod1.produkt_dzesh() 
        con.commit()  #	Pec apstiprinajuma datus ievietot datu baze
        for vards in tab_nosauk:
          prod1.druka_tab(vards)
          #hggfffghhfhsssf
      else:
        sg.popup('Kļūda', 'Aizpildīt visus laukus', background_color='#FF0000')
    
  window.close()


