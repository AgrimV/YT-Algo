from googleapiclient.discovery import build

import platform
import os

api_key = ['AIzaSyB86BifF_MbhDgCe-0IdMsbhtrn7eaJ8LY',
           'AIzaSyAabXt4cAY5i20xOKI2BLKEvGifcECUrJw',
           'AIzaSyATS95kPrwlfKfAFOzwr841xiW-kg2EYvI',
           'AIzaSyDmGjPdQ24FrtulH6ng6VkPGGcERi1ULTA']

youtube_api = build('youtube', 'v3', developerKey=api_key[0])


def search(query):
    results = youtube_api.search().list(q=query, part='snippet', type='video',
                                        order='viewCount',
                                        maxResults=10).execute()
    search_result = []
    for result in results['items']:
        chan_info = int(channel_info(result['snippet']['channelId']))
        vid_info = video_info(result['id']['videoId'])
        if(int(vid_info['likes'])/int(vid_info['dislikes'])>=25):  
            search_result.append(result)
    return search_result


def video_info(videoId):
    """
    Returns video like dislike and view count
    """
    info = youtube_api.videos().list(id=videoId, part='statistics').execute()
    return {'likes': int(info['items'][0]['statistics']['likeCount']),
            'dislikes': int(info['items'][0]['statistics']['dislikeCount']),
            'views': int(info['items'][0]['statistics']['viewCount'])}


def channel_info(channel_id):
    """
    Return channel info
    """
    info = youtube_api.channels().list(part='statistics',
                                       id=channel_id).execute()
    return info['items'][0]['statistics']['subscriberCount']


def redirect(videoId):
    """
    Open YouTube Video
    """
    link = 'https://www.youtube.com/watch?v=' + videoId
    if platform.system() == 'Linux':
        os.system('sensible-browser ' + link)
    else:
        os.system('start ' + link)
