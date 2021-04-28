from graph.services.math.arithmetic import ArithmeticService


class LinearFunctionService:
    def __init__(self,func):
        self.func = func.lower().replace(' ','')
        self.level_four = ['(', ')']
        self.level_three = ['^']
        self.level_two = ['*', '/']
        self.level_one = ['+', '-']
        self.level_array = [self.level_three, self.level_two , self.level_one]
        self.levels = self.level_one + self.level_two + self.level_three


        self.calculator = ArithmeticService()
        self.arith_dict = {
            "+" : self.calculator.add,
            "-" : self.calculator.subtract,
            "/" : self.calculator.divide,
            "*" : self.calculator.multiply,
            "^" : self.calculator.exponents,
        }

    # need to write a function to handle pemdas on a larger function
    def interpret_and_solve(self):
        
        
        points = []
        half_amount  = 10
        
        for i in range(0, half_amount):

            pre_eval_function = self.replace_x(self.func,i)

            post_eval_function = self.evaluate_function(pre_eval_function)



            points.append([i, post_eval_function])

        return {"result" : 'success' , 'points' : points}

    def replace_x(self, func, replacement):
        replacement = str(replacement)
        counter = 0
        new_func = ""
        for char in func:
            if char == 'x':
                if counter == 0:
                    new_func = new_func + replacement
                else:
                    new_func = new_func + '*' + replacement
            else:
                new_func = new_func + char
            counter += 1

        return new_func

        
    def evaluate_function(self,func):
        solved = False

        while not solved:
            index = 0
            solved = True


            for level in self.level_array:


                temp_index = self.get_computation_mark(func,level)

                

                if temp_index != 0:
                    index = temp_index
                    middle = func[index]
                    solved = False
                    break

            if index == 0:

                break

            left, right = self.sort_data(func,index)

            

            computation = "{}{}{}".format(left , middle , right)

            result = str(self.arith_dict[middle](float(left),float(right)))

            if computation == func:
                func = result
            else:
                func = func.replace(computation, result)

      

        return func

    def get_computation_mark(self,func,level):
        index = 0
        for char in func:
            
            if char in level:
                break
            index += 1

        if len(func) == index:
            return 0
        else:
            return index

    def sort_data(self, func, index):
            left = ""
            right = ""
            left_data = ""
            right_data=""
            
            for char in func[0:index]:
                left_data = char + left_data 

            for char in func[index+1:]:
                right_data = right_data + char



            left_data = [x for x in left_data]
            right_data = [x for x in right_data]


            for char in left_data:
                if char not in self.levels:
                    left = char + left
                else:
                    break

            for char in right_data:
                if char not in self.levels:
                    right = right + char
                else:
                    break
            
            return left, right
        

    def validator(self,data) -> bool:
        return True
