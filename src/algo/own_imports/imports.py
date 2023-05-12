from delta_checker import deltaBelowZeroChecker
from arguments_input import argumentsInput
from deltaBelowZero import zeroResultData
from deltaEqualZero import oneResultData
from deltaAboveZero import twoResultData

def calculator():
    print("Kalkulator funkcji kwadratowej")
    try:
        a, b, c = argumentsInput()
    except ValueError:
        print("Wszystkie argumenty muszą być liczbą!")
    print("------------------------------------------")
    deltaStatus = deltaBelowZeroChecker(a, b, c)
    if deltaStatus == 0:
       result = zeroResultData(a, b, c)
       return result
    elif deltaStatus == 1:
        result = oneResultData(a, b, c)
        return result
    elif deltaStatus == 2:
        result = twoResultData(a, b, c)
        return result
    return bStatus


calculatorResult = calculator()

print(calculatorResult)
print("------------------------------------------")
