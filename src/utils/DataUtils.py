def isNumber(strInput):
    return isFloat(strInput) | isInteger(strInput)


def isFloat(strInput):
    try:
        float(strInput)
    except ValueError:
        return False
    return True


def isInteger(strInput):
    try:
        int(strInput)
    except ValueError:
        return False
    return True
