from datetime import datetime

# Currency formatters
def ENUS_(v, c): v /= 100.0; return ('(' if v < 0 else ' ') + c + format(abs(v), ',.2f') + (')' if v < 0 else ' ')
def NLNL_(v, c): v /= 100.0; return c + (' -' if v < 0 else ' ') + format(abs(v), ',.2f').translate(str.maketrans(',.', '.,')) + ' '

# Date formatters (could be made intro a format creator which is called in locales dict)
def MDY_(date): return "{}/{}/{}".format(str(date.month).zfill(2), str(date.day).zfill(2), str(date.year).zfill(4))
def DMY_(date): return "{}-{}-{}".format(str(date.day).zfill(2), str(date.month).zfill(2), str(date.year).zfill(4))

locales = {
    'en_US' : {
        'date' : 'Date',
        'desc' : 'Description',
        'change' : 'Change',
        'date_formatter' : MDY_,
        'currency_formatter' : ENUS_
    },
    'nl_NL' : {
        'date' : 'Datum',
        'desc' : 'Omschrijving',
        'change' : 'Verandering',
        'date_formatter' : DMY_,
        'currency_formatter' : NLNL_
    },
}

locales_currency = {
    'USD' : '$',
    'EUR' : u'€'
}

class LedgerEntry(object):
    def __init__(self, date, desc
    6ption, change):
        self.date, self.description, self.change = date, description, change

create_entry = lambda date, description, change: LedgerEntry(datetime.strptime(date, '%Y-%m-%d'), description, change)

def format_entries(currency, locale, entries):
    table = []

    # Table header.
    table.append(' | '.join([
        locales[locale]['date'].ljust(10),
        locales[locale]['desc'].ljust(25),
        locales[locale]['change'].ljust(13)]
        ))
    
    # Sort entries to ring out by date, then by change amount
    entries.sort(key=lambda item : (item.date, item.change))    
    
    # Process all entries given
    for entry in entries:
        # Using the locale given, get it's date formatter
        date = locales[locale]['date_formatter'](entry.date)
        # Truncate description
        description = (entry.description[:22] + '...' if len(entry.description) > 25 else entry.description).ljust(25)
        # Using the locale and currency given, get the currency formatter and justify
        change = locales[locale]['currency_formatter'](entry.change, locales_currency[currency]).rjust(13)
        # Write entry change to table
        table.append(' | '.join([date, description, change]))

    return '\n'.join(table)