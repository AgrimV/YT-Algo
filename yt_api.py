from googleapiclient.discovery import build

api_key = ['AIzaSyB86BifF_MbhDgCe-0IdMsbhtrn7eaJ8LY',
           'AIzaSyAabXt4cAY5i20xOKI2BLKEvGifcECUrJw',
           'AIzaSyATS95kPrwlfKfAFOzwr841xiW-kg2EYvI']

youtube_api = build('youtube', 'v3', developerKey=api_key[1])


def search(query):
    results = youtube_api.search().list(q=query, part='snippet', type='video',
                                        order='viewCount',
                                        maxResults=10).execute()
    search_result = []
    for result in results['items']:
        search_result.append(result)

    return search_result


print(search('alouette'))
