import json
from collections import defaultdict
from datetime import datetime
from docx import Document

def load_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    
    doc_text = '\n'.join(full_text)
    
    try:
        json_data = json.loads(doc_text)
    except json.JSONDecodeError:
        raise ValueError("The DOCX file does not contain valid JSON data")
    
    return json_data

def process_transactions(transactions):
    portfolio = defaultdict(lambda: defaultdict(list))

    for txn in transactions:
        folio = txn['folio']
        scheme = txn['isin']
        units = float(txn['trxnUnits'])
        price = float(txn['purchasePrice']) if txn['purchasePrice'] else 0
        
        if units > 0:
            portfolio[folio][scheme].append((units, price))
        else:
            sell_units = abs(units)
            while sell_units > 0 and portfolio[folio][scheme]:
                buy_units, buy_price = portfolio[folio][scheme][0]
                if buy_units > sell_units:
                    portfolio[folio][scheme][0] = (buy_units - sell_units, buy_price)
                    sell_units = 0
                else:
                    portfolio[folio][scheme].pop(0)
                    sell_units -= buy_units

    return portfolio

def calculate_portfolio_value(portfolio, current_nav):
    net_units = defaultdict(float)
    net_value = defaultdict(float)
    total_value = 0

    for folio, schemes in portfolio.items():
        for scheme, holdings in schemes.items():
            units = sum([u for u, _ in holdings])
            if scheme in current_nav:
                nav = current_nav[scheme]
                value = units * nav
                net_units[scheme] += units
                net_value[scheme] += value
                total_value += value

    return net_units, net_value, total_value

def calculate_portfolio_gain(portfolio, current_nav):
    total_gain = 0
    for folio, schemes in portfolio.items():
        for scheme, holdings in schemes.items():
            units = sum([u for u, _ in holdings])
            acquisition_cost = sum([u * p for u, p in holdings])
            if scheme in current_nav:
                current_value = units * current_nav[scheme]
                total_gain += (current_value - acquisition_cost)

    return total_gain

def main(input_file, current_nav):
    data = load_docx(input_file)
    transactions = data['data'][0]['dtTransaction']

    portfolio = process_transactions(transactions)

    net_units, net_value, total_value = calculate_portfolio_value(portfolio, current_nav)
    
    total_gain = calculate_portfolio_gain(portfolio, current_nav)

    print("Net Units Per Fund:")
    for scheme, units in net_units.items():
        print(f"{scheme}: {units:.2f}")

    print("\nNet Value Per Fund:")
    for scheme, value in net_value.items():
        print(f"{scheme}: {value:.2f}")

    print(f"\nTotal Portfolio Value: {total_value:.2f}")
    print(f"Total Portfolio Gain: {total_gain:.2f}")

if __name__ == "__main__":
    current_nav = {
        "INF209K01UN8": 45.32,
        "INF090I01JR0": 76.4465,
        "INF194K01Y29": 179.550,
    }

    input_file = r'C:\Users\pavan kumar\OneDrive\Desktop\Backend Assignement\data.docx'
    main(input_file, current_nav)
