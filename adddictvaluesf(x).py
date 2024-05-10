# alternative 1
def add_dict_values(**dict):
    print(sum(dict.values()))

add_dict_values(History=85, Biology=56, Math=65, Social_studies=78)
# alternative 2

def add_dict_values(**results):
    i=0
    sum=0
    if i<len(dict):
     for a,b in results.items():
        sum=sum+b
        return sum
    i=i+1
print(add_dict_values(History=85, Biology=56, Math=65, Social_studies=78))