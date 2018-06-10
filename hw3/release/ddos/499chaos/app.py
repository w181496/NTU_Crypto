#!/usr/bin/env python3
from flask import Flask, request, send_from_directory
from flag import FLAG

app = Flask(__name__)

plans = {
    'economical': {'flag': 'Thanks you for buying economical plan. Get premium for the flag!', 'free_for_vip': True, 'price': 99},
    'standard': {'flag': 'Thanks you for buying standard plan. Get premium for the flag!', 'free_for_vip': True, 'price': 299},
    'premium': {'flag': FLAG, 'free_for_vip': False, 'price': 499},
}

def isVIP(phone):
    return phone.startswith('9453')


@app.errorhandler(500)
def error(e):
    return repr(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return send_from_directory('', 'index.html')

    json = request.get_json()
    if json is None:
        return 'Please POST JSON data to me!'
    if all(json[plan] == 0 for plan in plans):
        return "Please buy at least one plan!"
    if any(json[plan] < 0 for plan in plans):
        return "You are so smart, isn't it? What do you mean by buying negative months?"

    count, phone = json, json['telephone']

    charge = 0
    bought_plans = []

    for plan_name, plan in plans.items():
        if count[plan_name] == 0:
            continue
        charge += count[plan_name] * plan['price']
        bought_plans.append(plan['flag'])

    for plan_name, plan in plans.items():
        if isVIP(phone) and plan['free_for_vip']:
            charge -= count[plan_name] * plan['price']

    if charge > 0:
        return 'You need NT$ ' + repr(charge) + 'to buy the plans!'

    if not charge <= 0:
        return 'How can this happend? I think you are a hacker, right?'

    return 'Transaction complete: ' + repr(bought_plans)
