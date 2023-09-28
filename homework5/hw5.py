import json
import os

file_path = os.path.join(os.path.dirname(__file__), 'purchase_log.txt')

with open(file_path, 'r') as f:
    purchases = {}
    for line in f:
        purchase = json.loads(line.strip())
        purchases[purchase['user_id']] = purchase['category']

    # for i, (user_id, category) in enumerate(purchases.items()):
    #     if i >= 5:
    #         break
    #     print(f'{user_id}: {category}')