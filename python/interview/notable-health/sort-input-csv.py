# filename: sort-input-csv.py
# by: Abhay Gupta
# date: 23-08-28
#
# desc: There is a CSV with rows of patient data. Some of this data is duplicated patient data. 
#       We want to determine the duplicates and consolidate and merge their data. 
#
#       A row's data should be consolidated with another row's if 2 rows share an email in their 
#       corresponding list of emails and have the same last name.


#       Input Data:
#       First Name || Last Name || Email(s) || Phone Numbers(s)


import csv

class SortData:
    """ sort data corresponding to email & phone numbers"""

    def __init__(self):
        """ Constructor -- initialize class variables """
        self.data = []
        self.dictionary = {}
    
    def add_data(self, row):
        """ add data to sorted data """
        data = [ [],[],[],[] ]

        row = row.split("\"")
        
        # parse first element of row
        first = filter(None, row[0].split(","))
        first = [[i] for i in first]
        data[:len(first)] = first
       
        # parse remaining elements
        for c, elem in enumerate(row[1:]):
            elem = list(filter(None, elem.split(",")))
            
            if elem:
                if len(elem[0].split(".")[-1]) == 3:
                    data[2] = elem
                else:
                    data[3] = elem
        
        ## disjoint set check
        # check if last name & email is  previously used
        key_match = []
        last_name, = data[1]
        for key in self.dictionary:
            if last_name in key:
                for email in data[2]:
                    if email in key:
                        key_match.append(key)

        # add data to sorted data & update/add key-index pair
        if key_match:

            # remove duplicate keys
            for key in key_match[1:]:
                index = self.dictionary[key]
                data = list(map(lambda x, y: x+y, self.data[index], data))
                del self.dictionary[key]
            
            # combine new data with stored key
            index = self.dictionary[key_match[0]]
            self.data[index] = list(map(lambda x,y: list(set(x+y)), self.data[index], data))

            key_new = tuple(list(key) + data[2])
            if key_new != key_match[0]:
                del self.dictionary[key_match[0]]
                self.dictionary[key_new] = index
        else:
            # add element to dictionary
            key = data[2] + data[1]

            # update dictionary
            self.dictionary[tuple(key)] = len(self.data)

            self.data.append(data)

    def print_data(self):
        """ print sorted data """

        for i in self.data:
            print(i)
    
    def write_csv(self):
        """ write sorted data to csv file """

        with open('output.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            for row in self.data:

                row = [",".join(i) for i in row]
                csvwriter.writerow(row)
    
if __name__ == "__main__":
    """ run test cases """

    sorted_data = SortData()

    with open('input.csv') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            sorted_data.add_data(*row)

    sorted_data.print_data()
    sorted_data.write_csv()

