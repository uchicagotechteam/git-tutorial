import requests
import json

def get_total_expenditures(name):
    name = name.replace(' ', '%20')

    base_url = "https://www.illinoissunshine.org/api/committees/?"
    base_url += 'name__like=' + name
    response = requests.get(base_url).json()
    c_id = response['objects'][0]['id']

    exp_url = 'https://www.illinoissunshine.org/api/expenditures/?committee_id='\
              + str(c_id)
    response = requests.get(exp_url).json()
    exp_list = response['objects'][0]['expenditures']

    total = 0
    count = 0

    for expenditure in exp_list:
        total += expenditure['amount']
        count += 1

    dic = {}
    dic['total amount'] = total
    dic['count'] = count

    return dic
