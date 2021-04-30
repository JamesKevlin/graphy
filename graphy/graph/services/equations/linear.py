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
        
        resp = {}
        points = []
        half_amount  = 1
        try:
            for i in range(0, half_amount):

                pre_eval_function = self.parse_and_lint(func=self.func,
                                                        x_val=i,
                                                        )


                evaluated_function = self.evaluate_function(pre_eval_function)
                points.append([i, evaluated_function]) 

            resp['result'] = 'success'
        except Exception as e:
            print(e)
            resp['result'] = 'fail'
            resp['points'] = points

        resp['points'] = points
        return resp

    '''
    any linting math rules add here    
    
    '''

    def parse_and_lint(self, **kwargs):
        linters = [
            self.replace_x,
            self.add_multiply_for_parentheses
        ]

        for linter in linters:

            kwargs['func'] = linter(**kwargs)

        return kwargs['func']
    
    def evaluate_function(self, func):
        evaluated_func = None
        has_parenthesis = False

        for char in func:
            if char in self.level_four:
                has_parenthesis = True

        if has_parenthesis:
            evaluated_func = self.evaluate_parentheses(func)
        else:
            evaluated_func = self.evaluate_expression(func)
        return evaluated_func

    def replace_x(self, **kwargs):
        
        func = kwargs['func']
        replacement = str(kwargs['x_val'])
        counter = 0
        new_func = ""

        for char in func:
            if char == 'x':
                if counter == 0:
                    new_func = new_func + replacement
                elif func[counter].isnumeric():
                    new_func = new_func + '*' + replacement
                else:
                    new_func = new_func + replacement
            else:
                new_func = new_func + char
            counter += 1


        return new_func

    def add_multiply_for_parentheses(self, **kwargs):
        func = kwargs['func']
        temp_func = ""
        prev = ""
        curr = ""

        for char in func:
            
            multiply = "*"
            prev = curr
            curr = char

            if curr == '(' and prev.isnumeric() or prev == ')' and curr == '(':
                prev = prev + multiply


            if prev != "":
                temp_func = temp_func + prev

        temp_func = temp_func + curr

        return temp_func
        



    def evaluate_expression(self,func):
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

    def evaluate_parentheses(self, func):
        # TODO
        left = []
        right = []
        pairs = []

        counter = 0
        for char in func:
            if char == '(':
                left.append(counter)
            elif char == ')':
                right.append(counter)

            if len(left) != 0 and len(right) != 0:
                pairs.append(
                                (
                                    left[len(left)-1],
                                    right[0],
                                    
                                )
                            )
                left.pop(len(left)-1)
                right.pop(0)
                


            counter +=1

        if len(left) != len(right):
            print("oh no")
            # TODO raise error
            pass


        print(pairs)
        for pair in pairs:
            print(func[pair[0]:pair[1]+1])

        '''
        output of : 1+(8(-3)(9-3))

        [(5, 8), (10, 14), (2, 15)]
        pairs:
            - (-3)
            - (9-3)
            - (8*(-3)*(9-3))
        '''




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
