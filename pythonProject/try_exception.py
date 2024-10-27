
try:
    age=int(input("enete your age :"))
    income=20000
    risk=income/age
except ZeroDivisionError:
    print("division by zero not allowed")
except ValueError:
    print("eneter valid integer value")

