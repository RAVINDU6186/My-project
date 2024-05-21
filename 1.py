def counter(limit=10, reset=False):
    if reset:
        count = 0
    else:
        count = 0 if not hasattr(counter, 'count') else counter.count
    while count < limit:
        count += 1
        print(count)
    counter.count = count
