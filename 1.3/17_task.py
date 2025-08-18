def LineAnalysis(line):
    if not line.startswith('*') or not line.endswith('*'):
        return False
    words = line.split('*')[1:-1]
    sample = next((i for i in words if i), None) 
    if sample is None:
        return True
    return(all(i == sample or not i for i in words)  and 
           (all(not i for i in words) or all(i for i in words))) 