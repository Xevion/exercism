def is_valid(isbn):
    # Filter out hyphens or any other junk
    isbn = [num for num in isbn if num in '0123456789X']
    # Check length as well as out of place 'X' chars
    if len(isbn) < 10 or len(isbn) > 10 or any([True if (isbn[i] == 'X' and i < 9) else False for i in range(len(isbn))]): return False
    # Convert to ints then calculate isbn validity
    isbn = [int(digit) if digit != 'X' else 10 for digit in isbn]
    return (isbn[0] * 10 + isbn[1] * 9 + isbn[2] * 8 + isbn[3] * 7 + isbn[4] * 6 + isbn[5] * 5 + isbn[6] * 4 + isbn[7] * 3 + isbn[8] * 2 + isbn[9] * 1) % 11 == 0