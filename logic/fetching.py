from storage import dataHandler as dH

dh = dH.dataBaseHandler()

def post_data_formatter(message_table) -> dict:
    res = dict()
    res['date'] = message_table[0]
    res['username'] = message_table[1]
    res['topic'] = message_table[2]
    res['message'] = message_table[3]
    res['message_id'] = message_table[4]
    rating = dh.getSpecificMessageRatings(res['message_id'])
    res['structure'] = rating[0]
    res['quality'] = rating[1]
    res['likeStat'] = rating[2]
    res['dislikeStat'] = rating[3]

    return res