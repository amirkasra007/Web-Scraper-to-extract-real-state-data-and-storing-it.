from bs4 import BeautifulSoup as bs4
import requests
import numpy as np
import pandas as pd
from d_URLs import state_to_num

def address_crawler(ads_short, state):

  aa_ss = 'https://www.zvg-online.net/{}/{}/termin_00{}{}.php'
  titlessa3 =[]
  ss=[]
  for url in ads_short:
    for i in range(1,50):

      link = aa_ss.format(state_to_num(state), url,str(0),str(i))
      req=requests.get(link)
      soup=bs4(req.text, "html.parser")

      for j in soup.find_all('td'):
        ttl=j.getText()
        titlessa3.append(ttl)
      ss.append(titlessa3[84:93])
      titlessa3.clear()

  sss=[]
  for i in range(len(ss)):
    if ss[i][0] != '' :
      sss.append(ss[i])
    else:
      continue

  for i in range(len(sss)):
    sss[i].remove('Fehler melden')
    sss[i].remove('Grundstücksart:')
    sss[i].remove('Objekt / Lage:')
    sss[i].remove('Versteigerungsort:')
    sss[i].remove('')
  return sss


def df2xlxs(ads_short, state):
  sss_np = np.asarray((address_crawler(ads_short, state)))
  df = pd.DataFrame(sss_np, columns=['Geschäftszeichen','Grundstücksart','Objekt / Lage','Versteigerungsort'])
  df_exc = df.to_excel('{}.xlsx'.format(state), index=False)
  return df, df_exc
