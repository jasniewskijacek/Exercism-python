#nie działa z dodatkowymi testami

def flatten(iterable):
    p=str(iterable)
    for i in ["[","]"," "]:
        p=p.replace(i,"")
    return [int(x) for x in p.split(",") if x!="None"]
    pass