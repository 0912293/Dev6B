import random
from flask import Flask, render_template, request
from string import Template

class Development:

    def generateCode(self, max):
        code = ""
        for i in range(0,max):
            code += str(random.randint(0,9))
        return Development.encodeString(self, code)

    def encodeString(self, string):
        result = ""
        count = 0
        for i in string:
            if count !=0 and count %4 == 0:
                result += '-'
            result += i
            count += 1
        return result

    def getDecryptedCode(self, code):
        result = ""
        for i in code:
            if i != '-':
                if int(i) < 5:
                    result += str(int(i) + 4)
                else:
                    result += str(int(i) - 3)
        return Development.encodeString(self, result)

    def get(self):
        print("1")
        temp = Template(render_template("development.html"))
        code = self.generateCode(12)
        answer = self.getDecryptedCode(code)
        print('Code: ' + code)
        print('Answer: ' + answer)
        return temp.substitute(numbercode=code, answercode=answer)