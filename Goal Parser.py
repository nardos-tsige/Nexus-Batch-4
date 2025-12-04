class Solution:
    def interpret(self, command: str) -> str:
        goalpra = "" 
        i = 0
        while i < len(command):
            if command[i] == "G":
                goalpra += "G"
                i += 1
            if command[i:i+2] == "()":
                goalpra += "o"
                i += 2
            if command[i:i+4] == "(al)":
                goalpra += "al"
                i += 4
        return goalpra
