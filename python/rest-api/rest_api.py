import json

# Comments on this exercise:
    # I honestly kind of hate this problem because you're forced to store the users in a array essentially...
    # which means that users are not especially unique unless you add this functionality yourself, which is kind of hassle tbh.
    # This could be solved if we just had a dictionary of users where the values were users themselves. Bam. Problem solved.
    # This database is kind of useless because it's literally a dictionary with a single key, Users, which has a array, with the problem above.
    # Super annoying implementation I have to work with, and sure, 100%, you could just rewrite everything to convert databases from and to, but it's a hassle none the less of
    # converting and properly displaying databases with their conventions. >:(
    # Addtionally, the optional payloads are annoying. 
# Thoughts after solving:
    # I have no idea if ValueErrors were tested in this exercise, but I implemented them anyways in order to catch them if they ever appeared,
    # as after all, a large portion of the parameters that one could issue in this "Rest API" are optional to a point, and thus I assumed errors
    # were most definitely possible.
    # Not a bad exercise in the end, but it's annoying how this 'database' is implemented...

class RestAPI(object):
    def __init__(self, database=None):
        self.database = database or {"users" : []}

    def get(self, url, payload=None):
        if url == '/users':
            if not payload:
                return json.dumps(self.database)
            data = json.loads(payload)
            return json.dumps({"users" : [user for user in self.database["users"] if user['name'] in data['users']]})
        else:
            raise ValueError(f'Invalid URL \'{url}\'')

    def post(self, url, payload=None):
        if not payload:
            raise("No payload for URL \'{}\'".foramt(url))
        elif url == '/add':
            return self.add(payload) or json.dumps('?')
        elif url == '/iou':
            return self.iou(payload) or json.dumps('?')
        else:
            raise ValueError("Invalid URL \'{}\'".foramt(url))

    def get_user(self, name):
        found = [user for user in self.database['users'] if user['name'] == name]
        if len(found) >= 1:
            return found[0]
        else:
            raise ValueError('User \'{}\' does not exist.'.format(name))
            return False

    def set_user(self, name, data):
        found = [(index, user) for index, user in enumerate(self.database['users']) if user['name'] == name]
        if len(found) == 1:
            print('User {} set'.format(name))
            self.database['users'][found[0][0]] = data
            print(self.database['users'][found[0][0]])
        else:
            raise ValueError('User \'{}\' does not exist.'.format(name))
            return False

    # Add a user to the database
    def add(self, payload):
        data = json.loads(payload)
        if data['user'] in self.database.keys():
            raise ValueError('User {} already exists.'.format(data['name']))
        self.database['users'].append({'name' : data['user'], 'owes' : {}, 'owed_by' : {}, 'balance' : 0.0})
        return json.dumps(self.get_user(data['user']))

    def iou(self, payload):
        data = json.loads(payload)
        lender, borrower = self.get_user(data['lender']), self.get_user(data['borrower'])
        
        # if the lender owes the borrower money
        if data['borrower'] in lender['owes'].keys():
            dif = lender['owes'][data['borrower']] - data['amount']
            # lender still owes borrower money
            if dif > 0:
                lender['owes'][data['borrower']] = dif
                borrower['owed_by'][data['lender']] = dif
            # all ious paid between lender and borrower now
            elif dif == 0:
                del lender['owes'][data['borrower']]
                del borrower['owed_by'][data['lender']]
            # lender is now owed money by borrower
            elif dif < 0:
                del lender['owes'][data['borrower']]
                del borrower['owed_by'][data['lender']]
                lender['owed_by'][data['borrower']] = -dif
                borrower['owes'][data['lender']] = -dif

        # if the borrower already owes the lender money
        elif data['borrower'] in lender['owed_by'].keys():
            lender['owed_by'][data['borrower']] += data['amount']
            borrower['owes'][data['lender']] -= data['amount']

        # if the borrower and lender have no outstanding ious
        else:
            lender['owed_by'][data['borrower']] = data['amount']
            borrower['owes'][data['lender']] = data['amount']

        # Balance operations
        lender['balance'] += data['amount']
        borrower['balance'] -= data['amount']

        self.set_user(data['lender'], lender)
        self.set_user(data['borrower'], borrower)

        return json.dumps({"users" : [user for user in self.database["users"] if user['name'] in [data['lender'], data['borrower']]]})