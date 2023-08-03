import os
import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.preprocessing import normalize

def getRecommendations(index):
    if os.stat("D:\\WWW\\diplom\\backend\\music_site\\artist.csv").st_size != 0 and os.stat("D:\\WWW\\diplom\\backend\\music_site\\user_scrobble.csv").st_size != 0:
        titles_df = pd.read_csv("D:\\WWW\\diplom\\backend\\music_site\\artist.csv", sep=";")
        interactions_df = pd.read_csv("D:\\WWW\\diplom\\backend\\music_site\\user_scrobble.csv", sep=";")
        titles_df.index = titles_df["artist_id"]
        titles_dict = titles_df["artist_name"].to_dict()
        print(titles_dict.keys())
        rows, r_pos = np.unique(interactions_df.values[:, 0], return_inverse=True)
        cols, c_pos = np.unique(interactions_df.values[:, 1], return_inverse=True)
        interactions_sparce = sparse.csr_matrix((interactions_df.values[:, 2], (r_pos, c_pos)))
        Pui = normalize(interactions_sparce, norm="l2", axis=1)
        sim = Pui.T * Pui
        sim.todense()
        list__recom = [titles_dict[i + 1] for i in sim[int(index)-1].toarray().argsort()[0][-4:]]
        return list__recom
    else:
        return 'Данных нет'

