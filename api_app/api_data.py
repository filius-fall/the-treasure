import json
import redis

api_json_values = [
    {
        'id' : 0,
        'title' : 'Test link',
        'url' : 'https://www.hackerearth.com/blog/developers/twitter-client-using-flask-redis/',
        'descryption' : 'This link is for making a clone of twitter app using Flask Framework',
    },
    {
        'id' : 1,
        'title' : 'Test link 2',
        'url' : 'https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask',
        'descryption' : 'This link is for using API with Flask'
    }
]


external_data = {
    'id' : 0,
    'title' : '',
    'url' : '',
    'descryption' : ''
}