from graph.services.math.arithmetic import ArithmeticService


class LinearFunctionService:
    def __init__(self,func):
        self.func = func.lower().replace(' ','')
        self.looped = 0
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
        # half_amount  = -5
        try:
            for i in range(-15, 15):


                pre_eval_function = self.parse_and_lint(func=self.func,
                                                        x_val=i,
                                                        )
                

                evaluated_function = self.evaluate_function(pre_eval_function)
                points.append([i, evaluated_function]) 

            resp['result'] = 'success'
        except Exception as e:
            print("error in interpret_and_solve: ",e)
            resp['result'] = 'fail'
            resp['points'] = points

        print(points)
        resp['points'] = points
        return resp

    '''
    any linting math rules add here    
    
    '''

    def parse_and_lint(self, **kwargs):
        linters = [
            self.replace_x,
            self.add_multiply_for_parentheses,
            # self.validator
        ]

        for linter in linters:

            kwargs['func'] = linter(**kwargs)

        return kwargs['func']
    
    def evaluate_function(self, func):
        evaluated_func = None
        _has_parentheses = self.has_parentheses(func)


    

        if _has_parentheses:
            evaluated_func = self.evaluate_parentheses(func)
        else:
            evaluated_func = self.evaluate_expression(func)
        return evaluated_func

    def has_parentheses(self, func):
        has_parenthesis = False

        for char in func:
            if char in self.level_four:
                has_parenthesis = True
                break

        return has_parenthesis

    def replace_x(self, **kwargs):
        
        func = kwargs['func']
        replacement = str(kwargs['x_val'])
        counter = 0
        new_func = ""

        for char in func:
            if char == 'x':
                if counter == 0:
                    new_func = new_func + replacement
                else:
                    new_func = new_func + '(' + replacement + ')'
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

        func = self.handle_plus_minus(func)
        # func = self.handle_minus_plus(func) 
        func = self.handle_minus_minus(func)
        func = self.handle_multi_plus(func)

        # func = self.handle_minus_paren_minus(func)

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

            if left and right:
                
                result = str(self.arith_dict[middle](float(left),float(right)))
                
            if computation == func:
                func = result
            else:

                func = func.replace(computation, result)


        return func


    def evaluate_parentheses(self, func, loop_amount = 0):
        

        if func == '' or func == '(':
            
            return ''
        
        loop_amount +=1

        if loop_amount == 2000:
            raise RecursionError


        if self.has_parentheses(func):
            while self.has_parentheses(func):
                

                
                try:
                    return float(func)
                except Exception:
                    pass

                data = self.get_chunk(func)



                func_slice = data['chunk'] 
                solved_func_slice = self.evaluate_parentheses(func_slice,loop_amount=loop_amount)


                before_slice = ""
                after_slice = ""

                if data['start'] >= 0:

                    before_slice = func[0:data['start']]
                    after_slice = func[data['end']+1:]




                func = before_slice + solved_func_slice + after_slice
    


                func = self.handle_minus_minus(func)

        func = self.evaluate_expression(func)

        
        return func

    def get_chunk(self,func):
        start = -1
        end = -1

        left = []
        right = []

        chunk = ""

        for x in range(0,len(func)):
            if func[x] == '(':
                if start == -1:
                    start = x
                left.append(x)
            elif func[x] == ')':
                end = x
                right.append(x)

            if len(left) != 0 and len(left) == len(right):
                break


        if start != -1:
            chunk = func[start+1:end]
        
        try:

            if len(chunk) == (len(func)-2):
                chunk = str(float(chunk))
                
                start = -1
                end = -1
        except Exception:
            
            pass
        
        data = {
            'chunk' : chunk,
            'start' : start,
            'end'   : end
        }

        return data            

    def handle_plus_minus(self,func):
        counter = 0
        new_func = ""

        for char in func:
            if char == '+':
                if func[counter+1] != '-':
                    new_func = new_func + char
            else:
                new_func = new_func + char

            counter +=1
            

        return new_func


    def handle_minus_minus(self,func):

        counter = 0
        new_func = ""
        skip = False

        for char in func:
            if char == '-' and skip == False:
                if func[counter+1] != '-':
                    new_func = new_func + char
                else:
                    skip = True
                    new_func = new_func + '+'
            elif skip == False:
                new_func = new_func + char
            elif skip == True:
                skip = False

            counter +=1
            
        return new_func

    def handle_multi_plus(self,func):

        counter = 0
        new_func = ""
        skip = False

        for char in func:
            if char == '*' and skip == False:
                if func[counter+1] != '+':
                    new_func = new_func + char
                else:
                    skip = True
                    new_func = new_func + char
            elif skip == False:
                new_func = new_func + char
            elif skip == True:
                skip = False

            counter +=1

        return new_func


    def remove_negative_sign(self, func):

        if len(func) >= 3 and func[0] == '-' and func[1] == '-':
            func = func[1:]

        return func



    def get_computation_mark(self,func,level):
        index = 0
        for char in func:
            
            if char in level and not (index == 0 and func[0] == '-'):
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


            counter = 0
            for char in left_data:
                if char not in self.levels or (char == '-' and counter == 0):
                    if char == '-':
                        counter = 1
                    left = char + left
                else:
                    break

            counter = 0
            for char in right_data:
                if char not in self.levels or (char == '-' and counter == 0):
                    if char == '-':
                        counter = 1
                    right = right + char
                else:
                    break

            return left, right
        

    def validator(self,func) -> str:
        return func
