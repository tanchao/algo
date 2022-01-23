"""

Part 1
Minimum 3 transactions are required to consider it as a recurring transaction
Same company, same amount, same number of days apart - recurring transactions

Input: Company, Amount, Timestamp (Day of the transaction)
Output: An array of companies who made recurring transactions

Part 2
The amounts and timestamps - similar
20% higher than minimum

(minimum of all amount) 10$ + 20% -> 12$
[10, 11, 12]

[
  ("Netflix", 9.99, 0),
  ("Netflix", 9.99, 10),
  ("Netflix", 9.99, 20),
  ("Netflix", 9.99, 30),
  ("Amazon", 27.12, 32),
  ("Sprint", 50.11, 45),
  ("Sprint", 50.11, 55),
  ("Sprint", 50.11, 65),
  ("Sprint", 60.13, 77),
  ("Netflix", 9.99, 50),
]

Map<String, List<Transaction>>

Transaction {
    double amount;
    int timestamp;
}

Sprint
[50, 50, 50, 60] ->

Amazon ->

Netflix
[9, 9, 9]
[10, 20, 30, 50] -> {10, 10, 20} ->

Number of items ->
Max timestamp -> Integer

"""

from ast import Str
from typing import List, Tuple


class Solution:
    # todo: exception handling, logging and monitoring
    def recurring_transactions(self, transactions: List) -> List:
      transaction_records = {} # key: str <Company>_<Amount>, value: List[int] [<Timestamp>...]
      # todo: validate input
      if transactions and len(transactions) >= 3:
        companies = []
        for transaction in transactions:
          cur_company, cur_amount, cur_timestamp = transaction
          if cur_company in companies: # already detected as recurring transaction
            continue
          key = self.__build_transaction_identifier(transaction)
          if key in transaction_records:
            transaction_records[key].append(cur_timestamp)
            # check if key is recurring
            if len(transaction_records[key]) >= 3 and self.__is_recurring_transactions(transaction_records[key]):
              companies.append(cur_company)
              transaction_records.pop(key) # cleanup space
          else:
            transaction_records[key] = [cur_timestamp] # init
        return companies
      else:
        return []

    def __is_recurring_transactions(self, timestamps: List[int]) -> bool:
      gaps = set()
      timestamps.sort()
      for i in range(1, len(timestamps)):
        for j in range(0, i):
          gap = timestamps[i] - timestamps[j]
          if gap in gaps:
            return True
          else:
            gaps.add(gap)
      return False

    def __build_transaction_identifier(self, transaction: Tuple) -> Str:
      cur_company, cur_amount, cur_timestamp = transaction
      return cur_company + '_' + str(cur_amount) # to simplify: <Company>_<Amount>


solution = Solution()
print("Expected:")
print("['Netflix']")
print("Actual:")
print(solution.recurring_transactions([("Netflix", 9.99, 0), ("Netflix", 9.99, 10), ("Netflix", 9.99, 20), ("Netflix", 9.99, 30), ("Amazon", 27.12, 32), ("Sprint", 27.12, 32)]))
print(solution.recurring_transactions([("Netflix", 9.99, 30), ("Netflix", 9.99, 20), ("Netflix", 9.99, 10), ("Netflix", 9.99, 0), ("Amazon", 27.12, 32), ("Sprint", 27.12, 32)]))
print(solution.recurring_transactions([("Netflix", 9.99, 0), ("Netflix", 9.99, 15), ("Netflix", 9.99, 20), ("Netflix", 9.99, 30), ("Amazon", 27.12, 32), ("Amazon", 27.12, 34), ("Amazon", 27.12, 36), ("Sprint", 27.12, 32)]))
print(solution.recurring_transactions([("Netflix", 9.99, 0)]))