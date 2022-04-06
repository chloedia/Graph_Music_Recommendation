KEY = '03760190a1dd81410b18ab94b17f786d'
import tqdm
## import the requests library
import requests
##import the pandas library
import pandas as pd
## create a function that will return the data from the API request

def get_data(url, track_name, artist_name):

    ## set the url variable to the url we want to get data from
    url = url

    ## set the headers to the headers we want to use
    headers = {'method' : 'track.gettoptags', 'artist': artist_name.lower(), 'track': track_name.lower(), 'api_key': KEY, 'format':'json' }
    ## make the request and store the response in the variable r
    r = requests.get(url, params=headers)

    ## return the data from the API
    return r.json()

## create a function that will take a dataframe and pass the data to the API
def get_tags(df):
    url = 'http://ws.audioscrobbler.com/2.0/'
    ## create an empty list to store the tags
    tags = []
    ## loop through the dataframe
    for index, row in tqdm.tqdm(df.iterrows()):
        ## get the tags for each row
        json_data = get_data(url, row['track-name'], row['artist-name'])
        try:
            data = json_data['toptags']['tag'][:5]
        except:
            data = []
        top_genre = [d['name'] for d in data if len(d) > 0]
        ## append the tags to the list
        tags.append(top_genre)
    ## return the tags
    return tags

if __name__ == '__main__':
    ## call the function and store the returned data in the variable data
    df = pd.read_csv('lastfm-dataset-1K/user_id_logs_v2.tsv',index_col=0)
    df.drop('timestamp', axis=1, inplace=True)
    df = df.drop_duplicates()
    #get the top tags
    tags = get_tags(df)
    df['tags'] = tags
    df.to_csv('lastfm-dataset-1K/user_id_logs_v2_tags.tsv', sep='\t')
    ## print the data
    print(tags)