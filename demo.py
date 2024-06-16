from bankChurn.exception import BankChurnException
import sys

try:
    a = 1 / "2"

except Exception as e:
    raise BankChurnException(e, sys) from e
