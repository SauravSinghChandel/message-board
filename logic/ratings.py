from storage import dataHandler as dH
from bottle import redirect, request
import json


dh = dH.dataBaseHandler()

def like(session_data, message_id):
    username = session_data['user']
    res = dh.getLikeList(message_id)
    res = json.loads(res[0])
    ratings = list(dh.getSpecificMessageRatings(message_id))
    if username in res:
        res.remove(username)
        ratings[2] -= 1
        # Need to decrement the Like count
    else:
        res.append(username)
        ratings[2] += 1
        # Need to increment the Like Count
    
    dh.updateMessageRating(message_id, *ratings)
    res = json.dumps(res)
    dh.setLikeList(message_id, res)
    redirect(f'/#{message_id}')
    
    
def dislike(session_data, message_id):
    username = session_data['user']
    res = dh.getDislikeList(message_id)
    res = json.loads(res[0])
    ratings = list(dh.getSpecificMessageRatings(message_id))
    if username in res:
        print("Removed: ", res)
        res.remove(username)
        ratings[3] -= 1
        # Need to decrement the Like count
    else:
        print("Added: ", res)
        res.append(username)
        ratings[3] += 1
        # Need to increment the Like Count
    
    dh.updateMessageRating(message_id, *ratings)
    res = json.dumps(res)
    dh.setDislikeList(message_id, res)
    redirect(f'/#{message_id}')
    
        
def structure(session_data, message_id):
    value = int(request.forms.get('structure'))
    username = session_data['user']
    res = dh.getStructureList(message_id)
    print(res)
    res = json.loads(res[0])
    ratings = list(dh.getSpecificMessageRatings(message_id))
    if username in res:
        print("Removed: ", res)
        res.remove(username)
        n = len(res)
        if n != 0:
            ratings[0] = (ratings[0]*n - value)/float(n)
        else: 
            ratings[0] = 0
        # Need to decrement the Like count
    else:
        print("Added: ", res)
        res.append(username)
        n = len(res)
        ratings[0] += (value - ratings[0])/float(n)
        # Need to increment the Like Count
    
    dh.updateMessageRating(message_id, *ratings)
    res = json.dumps(res)
    dh.setStructureList(message_id, res)
    redirect(f'/#{message_id}')
    
        
def quality(session_data, message_id):
    value = int(request.forms.get('quality'))
    username = session_data['user']
    res = dh.getQualityList(message_id)
    res = json.loads(res[0])
    ratings = list(dh.getSpecificMessageRatings(message_id))
    if username in res:
        print("Removed: ", res)
        res.remove(username)
        n = len(res)
        if n != 0:
            ratings[1] = (ratings[0] * n)/float(n)
        else:
            ratings[1] = 0
        # Need to decrement the Like count
    else:
        print("Added: ", res)
        res.append(username)
        n = len(res)
        ratings[1] += (value - ratings[0])/float(n)
        # Need to increment the Like Count
    
    dh.updateMessageRating(message_id, *ratings)
    res = json.dumps(res)
    dh.setQualityList(message_id, res)
    redirect(f'/#{message_id}')
    