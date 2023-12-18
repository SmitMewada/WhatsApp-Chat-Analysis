from urlextract import URLExtract

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
    
    
def get_links_count(user, df):
    links = []
    extractor = URLExtract()
    
    if user == "Overall":
        for message in df["message"]:
            links.extend(extractor.find_urls(message))
            
    else:
        for message in df[df["user"] == user]["message"]:
            links.extend(extractor.find_urls(message))
            
    return len(links)
    
def get_image_count(user, df):
    '''
        This get_image_count counts the number of images shared by the person.
    '''

    if user == "Overall":
        return df[df["message"] == "Yes"]["message"].count()
    else:
        return df[df["message"] == 'Yes']["message"].count()