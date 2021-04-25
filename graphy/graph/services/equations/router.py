from .linear import LinearFunctionService

class EquationDataService:
    def __init__(self,data):
        if self.validator(data):
            self.validated = True
            self.data = data
        else:
            self.validated = False
            self.data = None

        self.handler = None

    def get_function_service(self):
        if self.validated:
            self.handler = LinearFunctionService(self.data['equation'])



    def solve_function(self):
        if self.handler != None:
            return self.handler.interpret_and_solve()

    def validator(self,data) -> bool:
        return True