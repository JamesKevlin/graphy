class LinearFunctionService:
    def __init__(self,func):
        self.func = func.lower()
        self.seperators = ['*', '/', '+', '-', '^']

    def interpret_and_solve(self):
        
        # split_equation = self.seperate_equation()
        points = []
        half_amount  = 10
        
        for i in range((0-half_amount), (half_amount+1)):
            pre_eval_function = self.func.replace('x', '*' + str(i))
            post_eval_function = eval(pre_eval_function)

            points.append([i, post_eval_function])

        print(len(points))

        return {"result" : 'success' , 'points' : points}
        

    def validator(self,data) -> bool:
        return True

    def seperate_equation(self):
        ordered_split_function = []

        for char in self.func:
            piece = char
            print(piece)



        return ordered_split_function