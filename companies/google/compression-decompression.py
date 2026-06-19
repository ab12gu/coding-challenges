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
        number = False
        repeat = ""
        for i in string:
            if i == "[":
                number = True
                repeat = int(repeat)
            if i.isdigit() and number == False:
                repeat += i
                pass
            if i.isalpha():
                substring += i
                pass
            if i == "]":
                for j in range(repeat):
                    outputstring += substring
                substring = ""
                number = False
                repeat = ""
        if substring:
            outputstring += substring

        return outputstring

if __name__ == '__main__':

    string = '300[abc]4[ab]c'
    
    data = Data()
    string = data.decompression(string)
    print(string)

    
