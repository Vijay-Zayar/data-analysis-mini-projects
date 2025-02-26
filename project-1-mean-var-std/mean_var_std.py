import numpy as np

def calculate(number):
    if len(number) != 9:
        raise ValueError("List must contain nine numbers.")

    data = np.array(number).reshape(3,3)
    print(data)

    calculations = {
    'mean': [data.mean(axis=0).tolist(), data.mean(axis=1).tolist(), data.mean().tolist()],
    'variance': [data.var(axis=0).tolist(), data.var(axis=1).tolist(), data.var().tolist()],
    'standard deviation': [data.std(axis=0).tolist(),data.std(axis=1).tolist(),data.std().tolist()],
    'max': [data.max(axis=0).tolist(),data.max(axis=1).tolist(),data.max().tolist()],
    'min': [data.min(axis=0).tolist(),data.min(axis=1).tolist(),data.min().tolist()],
    'sum': [data.sum(axis=0).tolist(),data.sum(axis=1).tolist(),data.sum().tolist()]
    }

    return calculations