from bs4 import BeautifulSoup as bs4
import requests

def state_to_num(state):

    # """ This function takes in the name of the state in the ZVG website
    # and returns the corrosponding number of it in the URL.
    # """
    state = state.lower()
    state_ = state[0].upper() + state[1:]

    if '-' in state_:
        a = state_[state_.index('-')+1].upper()
        state_ = state_[0:state_.index('-')] + '-' + a + state_[state_.index('-')+2:]
    else:
        pass

    dic = {'Baden-Württemberg': 1100, 'Bayern': 1200, 'Berlin': 1300, 'Brandenburg': 1400, 
    'Bremen': 1500, 'Hessen': 1700, 'Nordrhein-Westfalen': 2000, 'Saarland':2200,
    'Sachsen': 2300, 'Sachsen-Anhalt': 2400 }
    return dic[state_]


def func_urls(link):

    # """ This function takes in the link of the ZVG website
    # and returns all URLs available on that website for the next part.
    # """
    page_urls =[]
    all_urls=[]
    for i in range(1100, 2600,100):
        if i != 1600 and i != 1900 and i!=2100:
            page_urls.append(link.format(i))
        else:
            continue
    for url in page_urls:
        req=requests.get(url)
        soup=bs4(req.text, "html.parser")
        for link in soup.find_all('a'):
            all_urls.append(link.get('href'))
    return all_urls


def seperate_URLs(link,state):

    # """ This function takes in the name of the state and the link of the website and 
    ## returns the corrosponding URLs of each state district.
    # """

    if state == 'Baden Wuerttemberg':
        ads_Baden_Wuerttemberg =[]
        start_ind_Baden = func_urls(link).index("1116851874/ag_seite_001.php")
        end_begin_Baden = func_urls(link).index("1116852296/ag_seite_001.php")
        for i in range(start_ind_Baden, end_begin_Baden+1):
            ads_Baden_Wuerttemberg.append(func_urls(link)[i])
        return ads_Baden_Wuerttemberg

    elif state == 'Bayern':
        ads_bayern =[]
        start_ind_Bayern = func_urls(link).index("1116852357/ag_seite_001.php")
        end_begin_Bayern = func_urls(link).index("1116852669/ag_seite_001.php")
        for i in range(start_ind_Bayern, end_begin_Bayern+1):
            ads_bayern.append(func_urls(link)[i])
        return ads_bayern

    elif state == 'Berlin':
        ads_berlin =[]
        start_ind_berlin = func_urls(link).index("1106731585/ag_seite_001.php")
        end_begin_berlin = func_urls(link).index("1106731985/ag_seite_001.php")
        for i in range(start_ind_berlin, end_begin_berlin+1):
            ads_berlin.append(func_urls(link)[i])
        return ads_berlin

    elif state == 'brandenburg':

        ads_brandenburg =[]
        start_ind_brandenburg = func_urls(link).index("1104747536/ag_seite_001.php")
        end_begin_brandenburg = func_urls(link).index("1104748234/ag_seite_001.php")
        for i in range(start_ind_brandenburg, end_begin_brandenburg+1):
            ads_brandenburg.append(func_urls(link)[i])
        return ads_brandenburg

    elif state == 'Bremen':
        ads_bremen =[]
        start_ind_bremen  = func_urls(link).index("1107953613/ag_seite_001.php")
        end_begin_bremen = func_urls(link).index("1219048817/ag_seite_001.php")
        for i in range(start_ind_bremen, end_begin_bremen+1):
            ads_bremen.append(func_urls(link)[i])
        return ads_bremen

    elif state == 'Hessen':
        ads_hessen =[]
        start_ind_hessen = func_urls(link).index("1116849611/ag_seite_001.php")
        end_begin_hessen = func_urls(link).index("1116850615/ag_seite_001.php")
        for i in range(start_ind_hessen, end_begin_hessen+1):
            ads_hessen.append(func_urls(link)[i])
        return ads_hessen

    elif state == 'North Rhine Westphalia':
        ads_Nw =[]
        start_ind_Nw = func_urls(link).index("1116853647/ag_seite_001.php")
        end_begin_Nw = func_urls(link).index("1116854707/ag_seite_001.php")
        for i in range(start_ind_Nw, end_begin_Nw+1):
            ads_Nw.append(func_urls(link)[i])
        return ads_Nw

    elif state == 'Saarland':
        ads_Baden_Saarland =[]
        start_ind_Saarland = func_urls(link).index("1116854825/ag_seite_001.php")
        end_begin_Saarland = func_urls(link).index("1116854959/ag_seite_001.php")
        for i in range(start_ind_Saarland, end_begin_Saarland+1):
            ads_Baden_Saarland.append(func_urls(link)[i])
        return ads_Baden_Saarland

    elif state == 'Sachen':
        ads_Sachen =[]
        start_ind_Sachen = func_urls(link).index("1107955622/ag_seite_001.php")
        end_begin_Sachen = func_urls(link).index("1107955183/ag_seite_001.php")
        for i in range(start_ind_Sachen, end_begin_Sachen+1):
            ads_Sachen.append(func_urls(link)[i])
        return ads_Sachen

    elif state == 'Sachen_anheilt':
        ads_Sachen_anheilt =[]
        start_ind_Sachen_anheilt = func_urls(link).index("1264765702/ag_seite_001.php")
        end_begin_Sachen_anheilt = func_urls(link).index("1107952695/ag_seite_001.php")
        for i in range(start_ind_Sachen_anheilt, end_begin_Sachen_anheilt+1):
            ads_Sachen_anheilt.append(func_urls(link)[i])
        return ads_Sachen_anheilt
    else:
        raise NameError('The variable or func_urls(link)ed you entered is invalid')


def ads_short(state , link):
    ads_short =[seperate_URLs(func_urls(link), state)[i][0:10] for i in range(len(seperate_URLs(func_urls(link), state)))]
    return ads_short

def all_Urls(state, ads_short):
    pages_to_scrape =5
    ads_all = []
    for i in ads_short:
        for j in range(1,pages_to_scrape):
            url = ('https://www.zvg-online.net/{}/{}/ag_seite_00{}.php').format(state_to_num(state),i,j)
            ads_all.append(url)
    return ads_all

