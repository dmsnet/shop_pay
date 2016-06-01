__author__ = 'dmsnet'
# -*- coding: utf-8 -*-

import hashlib ,constants,requests,json

def get_sign(request, keys_required):

    string_to_sign = ":".join(str(request[k]).encode("utf8") for k in keys_required) + constants.secret

    #print "KEY Sorted:" ,keys_required
    #print "Secret KEY: ",constants.secret
    #print "String to sign: ", string_to_sign
    sign = hashlib.md5(string_to_sign).hexdigest()
    #print "Sign: " , sign
    return sign


def send_postAPI(id,sign,req):
    url = 'https://central.pay-trio.com/invoice'
    request= {"shop_id":constants.shop_id, "amount": req["summ"], "payway": "w1_uah", "currency": 980, "shop_invoice_id":id ,"description":req["txt"],"sign":sign }
    headers = {'content-type': "application/json"}
    r = requests.post(url, data=json.dumps(request), headers=headers ,verify=False)
    return json.loads(r.text)

def getTIPsign(id,req):
    print req
    request= {"shop_id":constants.shop_id, "amount": req["summ"], "payway": "w1_uah", "currency": 643, "shop_invoice_id":id ,"description":req["txt"] }
    keys_sorted = ("amount", "currency", "shop_id",  "shop_invoice_id")
    return  get_sign(request, keys_sorted)

def getAPIsign(id,req):
    print req
    request= {"shop_id":constants.shop_id, "amount": req["summ"], "payway": "w1_uah", "currency": 980, "shop_invoice_id":id ,"description":req["txt"] }
    keys_sorted = ('amount', 'currency', 'payway', 'shop_id', 'shop_invoice_id')
    return  get_sign(request, keys_sorted)



#print test()
#send_postAPI(request)


#6b31315e0b13840cc9bccb9618c6e9fe
#6b31315e0b13840cc9bccb9618c6e9fe

