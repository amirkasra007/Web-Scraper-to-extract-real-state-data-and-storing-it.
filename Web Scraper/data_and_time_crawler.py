from bs4 import BeautifulSoup as bs4
import numpy as np
import requests
import pandas as pd
from d_URLs import all_Urls

def crawler_date_time(state, ads_short):

  out112=[]
  out222 =[]
  titlessa2 =[]

  link_aa2= "termin_000{}.php"

  for url in all_Urls(state, ads_short):
    req=requests.get(url)
    soup=bs4(req.text, "html.parser")

    for link in soup.find_all('a'):
      out112.append(link.get('href'))
    for i in range(100):
      if link_aa2.format(i) in out112: 
        out222.append(link_aa2.format(i))
    for j in soup.find_all('b'):
      ttl=j.getText()
      titlessa2.append(ttl)

    for k in range(len(out222)):
      try:
        titlessa2.remove('Versteigerungstermin:')
        titlessa2.remove('ZV-Erklärungen')
        titlessa2.remove('Etage')
        titlessa2.remove('Erdgeschoss')
        titlessa2.remove('Land_forstwirschaft')
        titlessa2.remove('Sonstige')
        titlessa2.remove('Seite 1')
        titlessa2.remove('1')
        titlessa2.remove('Seite 1')
        titlessa2.remove('1')
      except ValueError:
        continue

  c=0
  cc=0
  ccc=0
  cccc=0
  ccccc=0
  cccccc=0
  d=0
  e=0
  f=0
  n=0
  mmm=0

  g=0
  ee=0
  h=0
  j=0
  l=0
  ZV=0
  W=0
  Z=0
  mm=0
  for i in titlessa2:
    if i == 'Kaufpreis:':
      c+=1
    elif i == '1':
      cc+=1
    elif i == '2':
      ccc+=1
    elif i == '3':
      cccc+=1
    elif i == '4':
      ccccc+=1
    elif i == 'Seite 2':
      cccccc+=1
    elif i == 'Seite 3':
      d+=1
    elif i == '<< zurück':
      e+=1
    elif f == 'Land_forstwirschaft':
      f+=1
    elif i == 'Versteigerungstermin:':
      n+=1
    else:
      mmm+=1

  for i in range(c):
    titlessa2.remove('Kaufpreis:')
  for i in range(cc):
    titlessa2.remove('1')
  for i in range(ccc):
    titlessa2.remove('2')
  for i in range(cccc):
    titlessa2.remove('3')
  for i in range(ccccc):
    titlessa2.remove('4')
  for i in range(cccccc):
    titlessa2.remove('Seite 2')
  for i in range(d):
    titlessa2.remove('Seite 3')
  for i in range(e):
    titlessa2.remove('<< zurück')
  for i in range(f):
    titlessa2.remove('Land_forstwirschaft')
  for i in range(n):
    titlessa2.remove('Versteigerungstermin:')

  for i in titlessa2:
    if i == 'Etage':
      g+=1
    elif i == 'Erdgeschoss':
      h+=0
    elif i == 'Sonstige':
      j+=1
    elif i == 'Land_forstwirschaft':
      l+=1
    elif i == 'Seite 4':
      ee+=1
    elif i == 'ZV-Erklärungen':
      ZV+=1
    elif i == 'weiter >>':
      W+=1
    elif i == 'ZV-Erklärungen':
      Z+=1
    else:
      mm+=1

  for i in range(ee):
    titlessa2.remove('Seite 4')
  for i in range(g):
    titlessa2.remove('Etage')
  for i in range(h):
    titlessa2.remove('Erdgeschoss')
  for i in range(j):
    titlessa2.remove('Sonstige')
  for i in range(l):
    titlessa2.remove('Land_forstwirschaft')
  for i in range(ZV):
    titlessa2.remove('ZV-Erklärungen')
  for i in range(W):
    titlessa2.remove('weiter >>')
  for i in range(Z):
    titlessa2.remove('ZV-Erklärungen')

  for ii in range(2,len(titlessa2), 4):
    titlessa2[ii]=titlessa2[ii][18:]
  for jj in range(3,len(titlessa2),4):
    titlessa2[jj]=titlessa2[jj][12:]

  n=4
  aa2 = [titlessa2[i:i + n] for i in range(0, len(titlessa2), n)]
  return aa2


def df2exl(state, ads_short):
  np.asarray((crawler_date_time(state, ads_short)))
  df = pd.DataFrame(crawler_date_time(state), columns=['am','um','Geschäftszeichen','Amtsgericht'])
  df_exc = df.to_excel('{}.xlsx'.format(state), index=False)
  return df, df_exc
