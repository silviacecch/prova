from TikTokApi import TikTokApi # api wrapper import https://github.com/davidteather/TikTok-Api
import tiktok_dataset as td #su github mettere lib.tiktok_dataset as td
import pandas as pd
import json
import os.path
from pathlib import Path
import subprocess
import matplotlib.pyplot as plt

api = TikTokApi.get_instance(use_test_endpoints=True)

#controllo se nella cartella è presente un file con lo stesso nome
#se si creo un altro dataframe con quel dataset
hashtag="ITookANap"
td.buildDatasetByHashtag(hashtag,5)

#2 cose da sistemare sono:
#voglio che crei solo un csv aggiuntivo
#voglio che non sovrascriva i file se il nome è già esistente




#in un dataframe separato scarichiamo nuovi tik tok con lo stesso algoritmo
#data2=uniquify(pd.DataFrame(td.buildDatasetByHashtag(hashtag,5)))


#merge tra primo dataframe e secondo dataframe
#salvare il contenuto del dataframe dentro il primo csv
#stampiamo il numero di righe aggiunte ad ogni passo
#fatto in maniera iterativa con un for per n volte

#grafico su matplotlib per vedere quante righe sono state aggiunte 


    
