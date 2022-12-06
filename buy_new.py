from jugaad_trader import Zerodha
import pause
import datetime
kite = Zerodha()
kite.set_access_token()
stocklist=['10IGG','10DPD','10DPR','10AGG','10DRR','10ADD','10DRD','10ARR','10ADR','07AGG','07BPB','07DPD']
pricelist=[]
quantitylist=[]

def p(hours, mins, secs, nanosecond):
    t = datetime.datetime.today()
    pause.until(datetime.datetime(t.year, t.month, t.day, hours, mins, secs, nanosecond))
    return
def upperCircuit(stockName, exchange):
    symbol=(f'{exchange}:{stockName}')
    priceUpperCircuit=kite.quote(symbol)[symbol].get('upper_circuit_limit')
    return priceUpperCircuit
def checkBse(stockName):
    symbol=(f'BSE:{stockName}')
    sell_q= kite.quote(symbol)[symbol].get('sell_quantity')
    if sell_q!=0:
        return True
def quantity_check(stockName, exchange):
    symbol=(f'{exchange}:{stockName}')
    puc=kite.quote(symbol)[symbol].get('upper_circuit_limit')
    if puc*100000>20000:
        q=round(20000/puc)
    else:
        q=100000
    return q


def list_creater():
    for i in stocklist:
        pricelist.append(upperCircuit(i,'BSE'))
        quantitylist.append(quantity_check(i,'BSE'))



def orderBse ():
    try:
        for (a, b, c) in zip(stocklist, pricelist, quantitylist):
            order_id = kite.place_order(variety=kite.VARIETY_AMO,
                                tradingsymbol=a,
                                exchange=kite.EXCHANGE_BSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=c,
                                order_type=kite.ORDER_TYPE_LIMIT,
                                price=b,
                                product=kite.PRODUCT_CNC,
                                validity=kite.VALIDITY_DAY)
            #forCheckBse.append(stockName)
        return order_id
    except Exception as e:
        print(f'{a} skipped due to error:\n{e}')
       # errorList.append(stockName)
        pass

def orderBse1 (stockName):
    exchange = 'BSE'
    try:
        totalQ = quantity_check(stockName, exchange)
        p=upperCircuit(stockName, exchange)
        for i in range (1):
            order_id = kite.place_order(variety=kite.VARIETY_AMO,
                                tradingsymbol=stockName,
                                exchange=kite.EXCHANGE_BSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=totalQ,
                                order_type=kite.ORDER_TYPE_LIMIT,
                                price=p,
                                product=kite.PRODUCT_CNC,
                                validity=kite.VALIDITY_DAY)
            #forCheckBse.append(stockName)
        return order_id
    except Exception as e:
        print(f'{stockName} skipped due to error:\n{e}')
        #errorList.append(stockName)
        pass
#list_creater()

def fun():
    print("Waiting for time:09_00")
    p(17,45
    ,59,80000)
    for i in stocklist:
        orderBse1(i)
    #orderBse()

fun()
print(stocklist, pricelist, quantitylist)