import pandas as pd



df = pd.read_csv("India Agriculture Crop Production.csv'")
print(df)

def mean(data):
    mean1 = sum(area)/len(area)
    return mean1
def rang(data):

    cal_range= max(data) - min(data)
    return cal_range

'''variance'''

def var(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data)/(len(data)-1)
    return variance



def sd(data):
    std= var(data) ** 0.5
    return std


def ir(data):
    s=sorted(data)
    n = len(s)
    q1 = (n + 1) // 4
    q3 = 3 * q1
    iqr= (s[q3 - 1] + s[q3]) / 2 - (s[q1 - 1] + s[q1]) / 2
    return iqr

def mean_absolute_deviation(data):
    if len(data) == 0:
        return None 
    mean = sum(data) / len(data) 
    mad = sum(abs(x - mean) for x in data) / len(data) 
    return mad



area=df['Area']
mean_area= mean(area)

r=rang(area)
print(r)

v=var(area)
print(v)

s=sd(area)
print(s)

iq=ir(area)
print(iq)

mad = mean_absolute_deviation(area)
print(mad)
