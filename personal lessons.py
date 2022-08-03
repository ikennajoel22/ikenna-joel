x = [10,30,0,40,13]
new_x =[]
def selection_sort(x: list):
    for i in x:
        sm= min(x)
        if sm== i:
            new_x.append (i)
            x.remove (i)
            selection_sort (new_x)
        print(new_x)

selection_sort(x)