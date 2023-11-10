from bottle import request, redirect
from storage import dataHandler as dH
from HTML_Templates.Templates import search_page
from logic import fetching, post
import datetime


dataHandler = dH.dataBaseHandler()

def search_results():
    search_query = request.forms.get('search_box')
    res = []
    data = dataHandler.lookUpSpecificSubstring(search_query)
    if len(data) != 0:
        for message in data:
            res.append(post.post_formatter(fetching.post_data_formatter(message)))
    
    return res
    
    
    
def return_search_page():
    search_posts = search_results()
    
    return search_page.return_template(search_posts)