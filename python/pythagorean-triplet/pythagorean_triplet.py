def is_triplet(triplet):
    return (triplet[0]**2 + triplet[1]**2) == triplet[2]**2

def triplets_with_sum(number):
    triplets = []
    for a in range(number):
        for b in range(number):
            for c in range(number):
                # if a + b + c == number:
                    # if is_triplet((a, b, c)):
                triplets.append((a, b, c))
    return triplets

x = triplets_with_sum(10001)
print(len(x))

def triplets_in_range(start, end):
    return