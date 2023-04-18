import json

# excel helper
# get record number
# =MID(C2,FIND("Record_Number=",C2,1)+14,FIND("02.Authorization_Response",C2,1) - FIND("Record_Number=",C2,1) - 14)
# get authroized number
# =MID(C2,FIND("Authorized_Amount=",C2,1)+18,FIND("87.Account_Balance_1",C2,1) - FIND("Authorized_Amount=",C2,1) - 18)
def display_analysis():
    with open('<put the path here>....json') as f:
        content_json = json.load(f)
        tipSum = 0
        tipCount = 0
        authSum = 0
        count = 0
        lastTxnTime = 0
        firstTxnTime = 0
        for x in content_json['transaction_details']:
            count += 1
            txn = x['transaction']
            authAmount = txn['authorized_amount']
            authSum += int(authAmount)
            txnTime = int(txn['transaction_date'] + txn['transaction_time'])
            if txn['transaction_code'] != 'approved':
                print(txn['transaction_id'])
            if firstTxnTime == 0:
                firstTxnTime = txnTime
            firstTxnTime = min(firstTxnTime, txnTime)
            lastTxnTime = max(lastTxnTime, txnTime)
            if txn.get('tip_amount') is None:
                continue
            tipCount += 1
            tipSum = tipSum + int(txn['tip_amount'])
        print('Transaction count: ' + str(count))
        print('Authorized Amount Total ' + str(authSum))
        print('Tip count: ' + str(tipCount))
        print('Tip Amount Total ' + str(tipSum))
        print('First txn time: ' + str(firstTxnTime))
        print('Last txn time: ' + str(lastTxnTime))

if __name__ == "__main__":
    display_analysis()
