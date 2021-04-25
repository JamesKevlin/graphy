class LinearFunctionService:
    def __init__(self,func):
        self.func = func
        self.seperators = ['*', '/', '+', '-', '^']

    def interpret_and_solve(self):
        
        split_equation = self.seperate_equation()


        return {"result" : 'success' , 'points' : [[1,1],[2,2]]}
        

    def validator(self,data) -> bool:
        return True

    def seperate_equation(self):
        ordered_split_function = []

        for char in self.func:
            piece = char
            print(piece)



        return ordered_split_function