import sqlite3 as db 
from logs import *
class Saglaba(Logs):
  def __init__(self,cur,jaunu_saglabat,tab_nosauk,id,kolonu_nosauk):
    self.tab_nosauk = tab_nosauk
    self.kolonu_nosauk = kolonu_nosauk
    self.cur = cur
    self.jaunu_saglabat = jaunu_saglabat
    self.id=id
    super().__init__(self.cur) # super - atslegas vards- norada uz vecaku

# Izdruka visu tabulu ('Kategorija', 'Nosaukums', 'Tehn_raksturojums', 'Produkts', 'Noma', 'Nomnieks')  saturu
  def druka_tab(self, tab_nosauk):
    self.tab_nosauk = tab_nosauk
    print('\nTabula ', self.tab_nosauk)
    self.cur.execute(f"""  SELECT  * FROM '{self.tab_nosauk}' """)
    self.saturs = self.cur.fetchall()
    for rinda in self.saturs:
      print (rinda) 

  # saglaba ierakstus tabulas: 'Kategorija', 'Nosaukums', 'Tehn_raksturojums'
  def saglaba_jauno(self,cur,jaunu_saglabat,tab_nosauk,id,kolonu_nosauk): 
    self.cur.execute(f""" INSERT INTO '{self.tab_nosauk}' ('{self.kolonu_nosauk}') SELECT '{self.jaunu_saglabat}' WHERE NOT EXISTS(SELECT 1 FROM '{self.tab_nosauk}' WHERE "{self.kolonu_nosauk}" = '{self.jaunu_saglabat}') """)
    
    # atrast id, un pielikt self.id_produktiem
    self.cur.execute(f""" SELECT "{self.id}" FROM '{self.tab_nosauk}' WHERE "{self.kolonu_nosauk}" IN ('{self.jaunu_saglabat}') """)
    return(self.cur.fetchone()[0])
    #print("id= ",self.rez, self.id)
    #atrisinājums

# Saglaba jaunu produktu tabulaa Produkts ()
  def produkt_tab(self,id_produktiem,cena_dienaa):
    self.id_produktiem = id_produktiem
    self.cena_dienaa = cena_dienaa
    sql = "INSERT INTO Produkts ( id_kategorija, id_nosaukums, id_tehn_rakstur, nomas_cena_dienaa) VALUES( ?, ?, ?, ?)"
    val = (id_produktiem[0], id_produktiem[1], id_produktiem[2], self.cena_dienaa)
    self.cur.execute(sql, val)




# Dzesh ierakstus tabulaa Produkts, kuriem cena 15
  def produkt_dzesh(self):
    print("====================================")
    ped_ieraksts = self.cur.lastrowid 
    print( "pēdējās rindas id= ",ped_ieraksts)
    self.cur.execute("DELETE FROM Produkts WHERE nomas_cena_dienaa = 15")
