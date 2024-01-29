import uuid

import pandas
import random
import datetime
from faker import Faker
fake = Faker()

customers_df = pandas.read_csv('customers.csv')
merchants_df = pandas.read_csv('merchants.csv')
descriptions_df = pandas.read_csv('descriptions.csv')
accounts_df = pandas.read_csv('accounts.csv')

base = datetime.datetime.fromisoformat('2020-01-01')
date_list = [base + datetime.timedelta(days=x) for x in range(1200)]

status_list = ['authorized', 'posted']
card_resent_flags = ['1', '0', None]
movements = ['credit', 'debit']

out = []

for i in range(12000):
    out.append({
        'status': random.choice(status_list),
        'card_resent_flag': random.choice(card_resent_flags),
        'bpay_biller_code': '',
        'account_id': random.choice(accounts_df.account.tolist()),
        'currency': 'EUR',
        'txn_description': random.choice(descriptions_df.txn_description.tolist()),
        'merchant_id': random.choice(merchants_df.merchant_id.tolist()),
        'name': fake.name(),
        'city': fake.city(),
        'country': fake.country(),
        'date': random.choice(date_list).strftime('%d/%b/%Y'),
        'amount': f'{random.random() * 5000 + 10:,.2f}',
        'transaction_id': uuid.uuid4().hex,
        'customer_id': random.choice(customers_df.customer_id.tolist()),
        'movement': random.choice(movements)
    })

pandas.DataFrame(out).to_excel('transaction.xlsx', index=False)
