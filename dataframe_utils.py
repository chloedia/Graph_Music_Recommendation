import pandas as pd
from os.path import exists
from tqdm import tqdm
import uuid
from IPython.display import clear_output
import numpy as np

def users(path):
    if not exists(path):
        logs_columns = ['userid', 'timestamp', 'artist-id', 'artist-name', 'track-id', 'track-name']
        user_id_logs = pd.read_csv('lastfm-dataset-1K/userid-logs.tsv', sep = '\t', header = None, names =  logs_columns )
        user_id_logs = user_id_logs.dropna(subset=['track-name','artist-name', 'artist-id'])
        """
        for loop taking 40 min to run
        """
        for _, row in tqdm(user_id_logs.iterrows()):
            row['track-id'] = uuid.uuid5(uuid.NAMESPACE_DNS, row['artist-name'] + "," + row['track-name'])
            row['artist-id'] = uuid.uuid5(uuid.NAMESPACE_DNS, str(row['artist-name']))
    else : 
        user_id_logs = pd.read_csv(path,index_col=0)
        user_id_logs = user_id_logs.dropna(subset=['track-name','artist-name', 'artist-id'])
        
    user_id_logs['timestamp'] = pd.to_datetime(user_id_logs['timestamp'], format='%Y-%m-%d')
    return user_id_logs

def get_only_top(df_logs,df_profile, n_top):
    new_df = pd.DataFrame(columns = ['track-name','artist-name'], dtype= np.str)
    for user_id in df_profile.values:
        test = df_logs[df_logs['userid']== user_id]
        try:
            test['count'] = test.groupby(['track-id'])[['track-id']].transform(lambda x: x.count())['track-id']
            test = test.sort_values(by = 'count', ascending = False)
            test = test.drop('timestamp', axis = 1)
            test = test.drop_duplicates()
            new_df = pd.concat([new_df, test[:n_top]], ignore_index=True)
        except:
            pass
        clear_output(wait = True)
        print("Just finished for",user_id)
    return new_df