def fetch_stats(user, df):
    '''
        The fetch_stats fetch stats for the specific user.
    '''
    if user == "Overall":
        return df.shape[0]
    else:
        return df[df["user"] == user].shape[0]
    
    
def get_word_count(user, df):
    '''
        This get_word_count function fetch word count for a specific user.
    '''
    if user == "Overall":
        return df["message"].apply(lambda x: len(x.split())).sum()
    else:
        return df[df["user"] == user]["message"].apply(lambda x: len(x.split())).sum()