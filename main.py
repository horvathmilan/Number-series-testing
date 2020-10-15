def tribonacci(n):
    validateParameter(n)
    if n == 0 or n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


def pellNumbers(n):
    validateParameter(n)
    if n == 0:
        return 0
    if n == 1:
        return 1
    return 2 * pellNumbers(n - 1) + pellNumbers(n - 2)


def lucasNumbers(n):
    validateParameter(n)
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucasNumbers(n - 1) + lucasNumbers(n - 2)


def validateParameter(param):
    parameterType = isinstance(param, int)
    if parameterType == False:
        raise Exception("Only numbers can be used!")
    if param < 0:
        raise Exception("Negative number can not be used!")
