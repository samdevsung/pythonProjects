#formatted string literal
from datetime import datetime
now = datetime.now()
print(f"Current date: {now:%Y-%m-%d}") # Output: Current date: 2025-06-19 (example date)
print(f"Current date: {now}") # full date return form datetime