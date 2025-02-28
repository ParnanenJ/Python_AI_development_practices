data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def print_transactions(transactions):
  for amount, statement in transactions:
    print(f"${amount} - {statement}")


def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions 
  if transaction[0] >= 0]
  withdrawals = [transaction[0] for transaction in transactions 
  if transaction[0] < 0]
  total_deposited = sum(deposits)
  total_withdrawn = sum(withdrawals)
  balance = total_deposited + total_withdrawn
  print(f"Total Deposited: ${total_deposited}")
  print(f"Total Withdrawn: ${total_withdrawn}")
  print(f"Balance: ${balance}")


def analyze_transactions(transactions):
  transactions.sort()
  largest_withdrawal = transactions[0]
  largest_deposit = transactions[-1]
  print(f"Largest withdrawal ${largest_withdrawal}")
  print(f"Largest deposit ${largest_deposit}")

  deposits = [transaction[0] for transaction in transactions 
  if transaction[0] >= 0]
  average_deposit = sum(deposits) / len(deposits) if deposits else 0
  print(f"Average deposit: {average_deposit}")

  withdrawals = [transaction[0] for transaction in transactions 
  if transaction[0] < 0]
  total_withdrawn = sum(withdrawals)
  average_withdraws = sum(withdrawals) / len(withdrawals) if withdrawals else 0
  print(f"Average withdraws: {average_withdraws}")


while True:
  print("Options: print, analyze, stop")
  choice = input("Select an option: ")
  if choice == "print":
    print_summary(data)
  elif choice == "analyze":
    analyze_transactions(data)
  elif choice == "stop":
    break
  else:
    print("Invalid choice")

