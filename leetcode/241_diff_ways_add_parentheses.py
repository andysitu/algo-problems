class Solution:
    def calc(self, inputs, start):
        # print(inputs, start)
        if inputs[start+1] ==  '+':
            a =inputs[start] + inputs[start+2]
        elif inputs[start+1] ==  '-':
            a =inputs[start] - inputs[start+2]
        else:
            a =inputs[start] * inputs[start+2]
        return inputs[:start] + [a] + inputs[start+3:]
        
    def run_calc(self, inputs):
        if len(inputs) == 1:
            return inputs
        a = []
        for i in range(1, len(inputs), 2):
            l = self.run_calc(inputs[:i])
            r = self.run_calc(inputs[i+1:])
            for nl in l:
                for nr in r:
                    if inputs[i] == '+':
                        a.append(nl + nr)
                    elif inputs[i] == '-':
                        a.append(nl - nr)
                    else:
                        a.append(nl * nr)
        return a
            
    def diffWaysToCompute(self, input: str) -> List[int]:
        input = input.replace(" ", "")
        inputs = []
        s = ""
        nset = {'1','2','3','4','5','6','7','8','9','0'}
        for c in input:
            if c in nset:
                s += c
            else:
                inputs.append(int(s))
                s = ""
                inputs.append(c)
        inputs.append(int(s))
        
        return self.run_calc(inputs)