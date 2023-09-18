import pandas as pd
from collections import counter
data=pd.read_csv('India Agriculture Crop Production.csv')
def mean(data):
    mean_=sum(data)/len(data)
    return mean_
def median(data):
    dataset= sorted(data)
    index=len(dataset)//2
    if len(data)%2!=0:
        return (dataset [index])/2
    if n%2==0:
        n1=data[n//2]
        n2=data[(n-1)//2]
        median = (n1+n2)/2
    else:
        median = data[n//2]

    return median

def mode(data):
    
    
    modd = Counter(data)
    d = dict(modd)
    max1=max(list(modd.values()))
    mod = [num for num, rep in d.items() if rep == max1]
    if len(mod) == len(data):
        print("No mode")
    else:
        return mod

def geometric_mean(data):
    if len(data) == 0:
        return None 
    product = 1
    for value in data:
        try:
            numeric_value = float(value)
            product *= numeric_value
        except ValueError:
            pass 
    return product ** (1 / len(data))

def harmonic_mean(data):
    if len(data) == 0:
        return None
    reciprocal_sum = 0
    for value in data:
        try:
            numeric_value = float(value) 
            reciprocal_sum += 1 / numeric_value
        except ValueError:
            pass
    return len(data) / reciprocal_sum



area=data['Area']

mean_area= mean(area)
print(mean_area)

med_area=median(area)
print(med_area)

mode_area = mode(area)
print(mode_area)

gm = geometric_mean(area)
print(gm)

hm = harmonic_mean(area)
print(hm)

