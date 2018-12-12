left = [['Bob', 'Accounting'],
         ['Jake', 'Engineering'],
         ['Lisa', 'HR']]
right = [['Lisa', 2004],
         ['Bob', 2008], 
         ['Jake', 2012], 
         ['Sue', 2014]]

def merge(left, right, left_on, right_on):
    merged = []
    for l in left:
        for r in right:
            if l[left_on] == r[right_on]:
                merged.append(l+r)
    print(merged)
    return merged


merge(left,right,0,0)


