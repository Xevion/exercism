# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry(object):
    def __init__(self, date, description, change):
        self.date, self.description, self.change = date, description, change

locales = {
    'en_US' : {
        'date' : 'Date',
        'desc' : 'Description',
        'change' : 'Change'
    },
    'nl_NL' : {
        'date' : 'Datum',
        'desc' : 'Omschrijving',
        'change' : 'Verandering'
    }
}

currencies = {
    'USD' : '$',
    'EUR' : '€'
}

def create_entry(date, description, change):
    return LedgerEntry(datetime.strptime(date, '%Y-%m-%d'), description, change)

def format_entries(currency, locale, entries):
    if locale == 'en_US':
        # Generate Header Row
        table = ' | '.join([locales[locale]['date'].ljust(10), locales[locale]['desc'].ljust(25), locales[locale]['change'].ljust(13)])
        
        entries.sort(key=lambda item : (item.date, item.change))
        
        while len(entries) > 0:
            table += '\n'
            entry = entries.pop(0)

            date_str = "{}/{}/{}".format(str(entry.date.month).zfill(2), str(entry.date.day).zfill(2), str(entry.date.year).zfill(4))
            table += date_str + ' | '

            # Write entry description to table
            # Truncate if necessary
            table += (entry.description[:22] + '...' if len(entry.description) > 25 else entry.description).ljust(25)
            table += ' | '

            # Write entry change to table
            if currency == 'USD':
                change_str = ''
                if entry.change < 0:
                    change_str = '('
                change_str += '$'
                change_dollar = abs(int(entry.change / 100.0))

                dollar_parts = []
                while change_dollar > 0:
                    dollar_parts.insert(0, str(change_dollar % 1000))
                    change_dollar = change_dollar // 1000
                if len(dollar_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += dollar_parts[0]
                        dollar_parts.pop(0)
                        if len(dollar_parts) == 0:
                            break
                        change_str += ','
                change_str += '.'
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                if entry.change < 0:
                    change_str += ')'
                else:
                    change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
            elif currency == 'EUR':
                change_str = ''
                if entry.change < 0:
                    change_str = '('
                change_str += u'€'
                change_euro = abs(int(entry.change / 100.0))
                euro_parts = []
                while change_euro > 0:
                    euro_parts.insert(0, str(change_euro % 1000))
                    change_euro = change_euro // 1000
                if len(euro_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += euro_parts[0]
                        euro_parts.pop(0)
                        if len(euro_parts) == 0:
                            break
                        change_str += ','
                change_str += '.'
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                if entry.change < 0:
                    change_str += ')'
                else:
                    change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
        return table


    elif locale == 'nl_NL':
        # Generate Header Row
        table = 'Datum'
        for _ in range(6):
            table += ' '
        table += '| Omschrijving'
        for _ in range(14):
            table += ' '
        table += '| Verandering'
        for _ in range(2):
            table += ' '

        while len(entries) > 0:
            table += '\n'

            # Find next entry in order
            min_entry_index = -1
            for i in range(len(entries)):
                entry = entries[i]
                if min_entry_index < 0:
                    min_entry_index = i
                    continue
                min_entry = entries[min_entry_index]
                if entry.date < min_entry.date:
                    min_entry_index = i
                    continue
                if (
                    entry.date == min_entry.date and
                    entry.change < min_entry.change
                ):
                    min_entry_index = i
                    continue
                if (
                    entry.date == min_entry.date and
                    entry.change == min_entry.change and
                    entry.description < min_entry.description
                ):
                    min_entry_index = i
                    continue
            entry = entries[min_entry_index]
            entries.pop(min_entry_index)

            # Write entry date to table
            day = entry.date.day
            day = str(day)
            if len(day) < 2:
                day = '0' + day
            date_str = day
            date_str += '-'
            month = entry.date.month
            month = str(month)
            if len(month) < 2:
                month = '0' + month
            date_str += month
            date_str += '-'
            year = entry.date.year
            year = str(year)
            while len(year) < 4:
                year = '0' + year
            date_str += year
            table += date_str
            table += ' | '

            # Write entry description to table
            # Truncate if necessary
            if len(entry.description) > 25:
                for i in range(22):
                    table += entry.description[i]
                table += '...'
            else:
                for i in range(25):
                    if len(entry.description) > i:
                        table += entry.description[i]
                    else:
                        table += ' '
            table += ' | '

            # Write entry change to table
            if currency == 'USD':
                change_str = '$ '
                if entry.change < 0:
                    change_str += '-'
                change_dollar = abs(int(entry.change / 100.0))
                dollar_parts = []
                while change_dollar > 0:
                    dollar_parts.insert(0, str(change_dollar % 1000))
                    change_dollar = change_dollar // 1000
                if len(dollar_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += dollar_parts[0]
                        dollar_parts.pop(0)
                        if len(dollar_parts) == 0:
                            break
                        change_str += '.'
                change_str += ','
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
            elif currency == 'EUR':
                change_str = u'€ '
                if entry.change < 0:
                    change_str += '-'
                change_euro = abs(int(entry.change / 100.0))
                euro_parts = []
                while change_euro > 0:
                    euro_parts.insert(0, str(change_euro % 1000))
                    change_euro = change_euro // 1000
                if len(euro_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += euro_parts[0]
                        euro_parts.pop(0)
                        if len(euro_parts) == 0:
                            break
                        change_str += '.'
                change_str += ','
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
        return table

entries = [
    create_entry('2015-01-02', 'Something', 0),
    create_entry('2015-01-02', 'Something', -1),
    create_entry('2015-01-02', 'Something', 1),
    create_entry('2015-01-01', 'Something', 0),
    create_entry('2015-01-01', 'Something', -1),
    create_entry('2015-01-01', 'Something', 1)
]
print(format_entries('USD', 'en_US', entries))