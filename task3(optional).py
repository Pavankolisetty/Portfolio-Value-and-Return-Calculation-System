import json
from collections import defaultdict
from datetime import datetime
from docx import Document
from scipy.optimize import newton

def calculate_xirr(transactions, current_value):
    cash_flows = []
    dates = []
    
    for txn in transactions:
        amount = float(txn['trxnAmount'])
        date = datetime.strptime(txn['trxnDate'], '%d-%b-%Y')
        
        if amount != 0:
            cash_flows.append(-amount)
            dates.append(date)
    
    if current_value != 0:
        cash_flows.append(current_value)
        dates.append(datetime.today())

    print("Cash Flows:", cash_flows)
    print("Dates:", dates)

    return xirr(cash_flows, dates)

def xirr(cash_flows, dates):
    sorted_cash_flows_dates = sorted(zip(cash_flows, dates), key=lambda x: x[1])
    sorted_cash_flows, sorted_dates = zip(*sorted_cash_flows_dates)

    def npv(rate):
        total = 0
        for cash_flow, date in zip(sorted_cash_flows, sorted_dates):
            if rate == -1:
                return float('inf')
            days = (date - sorted_dates[0]).days / 365
            if days < 0:
                continue
            try:
                total += cash_flow / ((1 + rate) ** days)
            except OverflowError:
                return float('inf')
        return total

    try:
        return newton(npv, 0.05)
    except RuntimeError as e:
        print(f"Error in XIRR calculation: {e}")
        return None

def load_transactions_from_docx(input_file):
    doc = Document(input_file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)

    doc_text = '\n'.join(full_text)
    
    try:
        data = json.loads(doc_text)
    except json.JSONDecodeError:
        raise ValueError("The DOCX file does not contain valid JSON data")

    return data['data'][0]['dtTransaction']

if __name__ == "__main__":
    input_file = r'C:\Users\pavan kumar\OneDrive\Desktop\Backend Assignement\data.docx'

    current_nav = {
        "INF209K01UN8": 45.32,
        "INF090I01JR0": 76.4465,
        "INF194K01Y29": 179.550,
    }

    transactions = load_transactions_from_docx(input_file)

    total_value = 39605.64604

    xirr_value = calculate_xirr(transactions, total_value)
    print("XIRR:", xirr_value)
