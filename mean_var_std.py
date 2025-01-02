import numpy as np

def calculate(list):
    if (len(list) < 9):
        raise ValueError("List must contain nine numbers.")

    array = np.array(list).reshape(3, 3)

    mean0 = np.mean(array, axis=0).tolist()
    mean1 = np.mean(array, axis=1).tolist()
    meanFlat = np.mean(array)

    var0 = np.var(array, axis=0).tolist()
    var1 = np.var(array, axis=1).tolist()
    varFlat = np.var(array)
    
    std0 = np.std(array, axis=0).tolist()
    std1 = np.std(array, axis=1).tolist()
    stdFlat = np.std(array)

    max0 = np.max(array, axis=0).tolist()
    max1 = np.max(array, axis=1).tolist()
    maxFlat = np.max(array)

    min0 = np.min(array, axis=0).tolist()
    min1 = np.min(array, axis=1).tolist()
    minFlat = np.min(array)

    sum0 = np.sum(array, axis=0).tolist()
    sum1 = np.sum(array, axis=1).tolist()
    sumFlat = np.sum(array)

    calculations = {
        'mean': [mean0, mean1, meanFlat],
        'variance': [var0, var1, varFlat],
        'standard deviation': [std0, std1, stdFlat],
        'max': [max0, max1, maxFlat],
        'min': [min0, min1, minFlat],
        'sum': [sum0, sum1, sumFlat]
    }

    return calculations