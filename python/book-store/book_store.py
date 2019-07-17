from itertools import combinations_with_replacement
PRICES = {1: 8, 2: 16 * 0.95, 3: 24 * 0.90, 4: 32 * 0.80, 5: 40 * 0.75}


def total(books):
    num_books = len(books)
    unique = len(set(books))
    counts = [books.count(book) for book in books]
    try:
        combos = combinations_with_replacement(range(1, unique+1), max(counts))
    except ValueError:
        return 0.00
    combos = (combo for combo in combos if sum(combo) == num_books)
    return round(min(sum(PRICES[c] for c in combo) for combo in combos)*100)