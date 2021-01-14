class Solution:
    def calc(self, inputs, start):
        # print(inputs, start)
        if inputs[start+1][0] ==  '+':
            a =inputs[start][0] + inputs[start+2][0]
        elif inputs[start+1][0] ==  '-':
            a =inputs[start][0] - inputs[start+2][0]
        else:
            a =inputs[start][0] * inputs[start+2][0]
        return inputs[:start] + [[a, "(" + inputs[start][1] + inputs[start+1][1] + inputs[start+2][1]   +")"]] + inputs[start+3:]
        
    def run_calc(self, inputs):
        if len(inputs) == 3:
            s = inputs[0][1] + inputs[1][1] + inputs[2][1]
            if s in self.answerset:
                return
            b = self.calc(inputs, 0)
            self.answers.append(b[0][0])
            self.answerset.add(s)
            return
            
        for i in range(0, len(inputs)-1, 2):
            self.run_calc(self.calc(inputs, i))
            
    def diffWaysToCompute(self, input: str) -> List[int]:
        self.answers = []
        self.answerset = set()
        input = input.replace(" ", "")
        inputs = []
        s = ""
        nset = {'1','2','3','4','5','6','7','8','9','0'}
        for c in input:
            if c in nset:
                s += c
            else:
                inputs.append([int(s), 0])
                s = ""
                inputs.append([c, c])
        inputs.append([int(s), 0])
        
        for i in range(0,len(inputs),2):
            inputs[i][1] = str(i)
        if len(inputs) == 1:
            return [inputs[0][0]]
        
        self.run_calc(inputs)
        
        return self.answers