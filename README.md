# Portfolio-Value-and-Return-Calculation-System
# Portfolio Value and Return Calculation System

## Project Overview
The **Portfolio Value and Return Calculation System** is a Python-based tool designed to process investment transaction data and provide essential financial metrics, including net units, net values, total portfolio value, and XIRR (Extended Internal Rate of Return). The system simplifies portfolio management by automating calculations that help investors assess the performance of their investments.

## Key Features
- **Data Processing**: Reads transaction data from a `.docx` file and converts it into a usable JSON format.
- **Portfolio Calculations**: Computes net units, net values for each fund, total portfolio value, and XIRR based on the transactions.
- **User-Friendly Output**: Generates clear and formatted outputs for easy interpretation of financial metrics.

## Technologies Used
- Python (with libraries such as `json`, `collections`, `datetime`, `docx`, and `scipy`)

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.
- Required Python libraries can be installed using:
  ```bash
  pip install python-docx scipy

### Output
--> Net Units Per Fund
Net Units Per Fund:
INF209K01UN8: 291.05
INF090I01JR0: 0.00
INF194K01Y29: 147.12

--> Net Value Per Fund
Net Value Per Fund:
INF209K01UN8: 13190.25
INF090I01JR0: 0.00
INF194K01Y29: 26415.40

--> Total Portfolio Value
Total Portfolio Value: 39605.65
--> Total Portfolio Gain
Total Portfolio Gain: 18106.14
--> XIRR
XIRR: 0.1534


## Acknowledgments
I would like to express my gratitude to Saffron Founders for the opportunity to undertake this project as part of my internship selection process. Special thanks to the mentors and peers who provided guidance and support throughout the development of this project. 

I would also like to acknowledge the creators of the libraries utilized in this project, including `python-docx`, `scipy`, and `collections`, which greatly facilitated the development of this tool.

