import PySimpleGUI as sg
import sqlite3 as db 
#'-KATEG-' '-NOSAUK-' '-RAKSTUR-' '-Cena-'
class Logs():
  def __init__(self,cur):
    with db.connect('nomat.db') as con:
      cur = con.cursor()
      # izvelas vardus un uzvardus, arnoradito vardu 
      cur.execute(""" SELECT  kategorija FROM Kategorija """)
      self.kateg = cur.fetchall()
      cur.execute(""" SELECT  nosaukums FROM Nosaukums """)
      self.nosauk = cur.fetchall()
      cur.execute(""" SELECT  tehn_rakstur FROM Tehn_raksturojums """)
      self.tehn_rakst = cur.fetchall()
      cur.execute(""" SELECT  nomas_cena_dienaa FROM Produkts """)
      self.produkt = cur.fetchall()

  def izkarto(self):    
    self.layout = [  [sg.Text('Izvēlieties nopirkto produktu vai ievadiet jaunu  nopirkto produktu')], 
                [sg.Text('Kategorija'), sg.Listbox(values=self.kateg, key='-KATEG-', enable_events=True),
                 sg.InputText(key='T-KATEG-')],
                [sg.Text('Nosaukums ', size=(15, 1)), sg.Listbox(values=self.nosauk, size=(20, 1), key='-NOSAUK-', enable_events=True),
                 sg.InputText(key='T-NOSAUK-')],
                [sg.Text('Tehniskais raksturojums '), sg.Listbox(values=self.tehn_rakst, size=(30, 1),key='-RAKSTUR-', enable_events=True),
                 sg.InputText(key='T-RAKSTUR-')],
                [sg.Text('Nomas cena dienā ', size=(7, 1)), sg.Listbox(values=self.produkt, size=(30, 1), key='-Cena-', enable_events=True),
                 sg.InputText(key='T-Cena-')], 
                [sg.Button('Ievadīt'), sg.Button('Atcelt')] ]

  def logu_veido(self):
    Logs.izkarto(self)  
    #veido logu programmaa
    window = sg.Window('Datora komponentes', self.layout) 
    return (window)
