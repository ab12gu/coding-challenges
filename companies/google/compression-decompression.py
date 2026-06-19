# Compression - Decompression Sample Question
#
# https://www.google.com/about/careers/applications/candidate-prep/swe?

class Data:

    def __init__(self, string):
        self.string = string
        pass

    def compression(self):
        pass

    def decompress(num):
        while self.string:

            i = self.string.pop()
            substring = ""
            outputstring = ""

            if i.isalpha():
                substring += i
            if i == "]":
                print("HELLO")
                for j in range(repeat):
                    outputstring += substring
                substring = ""
                number = False
                repeat = ""

            print(outputstring)

            return substring

    def decompression(self):
        outputstring = ""
        number = False
        substring = ""
        repeat = ""

        print(self.string)

        self.string = self.string.split().reverse()
        
        print(self.string)
        subs = ""
        while self.string:
            i = self.string.pop()
            print(i)
            if i == "[":
                number = True
                repeat = int(repeat)
                outputstring += decompress(repeat)
            if i == isdigit() and number == False:
                repeat += i
            if i.isalpha():
                substring += i

        print(substring)
        if substring:
            outputstring += substring

        return outputstring

if __name__ == '__main__':

    string = '300[abc]4[ab]c'
    
    data = Data(string)
    string = data.decompression()
    print(string)

    
