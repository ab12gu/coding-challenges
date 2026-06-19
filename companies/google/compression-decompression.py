# Compression - Decompression Sample Question
#
# https://www.google.com/about/careers/applications/candidate-prep/swe?

class Data:
    def __init__(self):
        pass

    def compression(self):
        pass

    def decompression(self, string):
        substring = ""
        outputstring = ""
        for i in string:
            if i.isdigit():
                repeat = int(i)
            if i.isalpha():
                substring += i
            if i == "]":
                for j in range(repeat):
                    outputstring += substring
                substring = ""
        return outputstring

if __name__ == '__main__':

    string = '3[abc]4[ab]c'
    
    data = Data()

    string = data.decompression(string)

    print(string)

    
