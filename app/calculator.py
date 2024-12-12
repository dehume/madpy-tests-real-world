class Calculator:
    def addition(self, args: list[int]) -> int:
        output = 0
        for arg in args:
            output += arg
        return output

    def multiplication(self, args: list[int]) -> int:
        num_args = len(args)
        if num_args <= 1:
            raise Exception("More than 1 arguments required")

        output = args.pop(0)
        for arg in args:
            output = output * arg
        return output


class CalculatorCache:
    cache = 0

    def addition(self, args: list[int]) -> int:
        for arg in args:
            self.cache += arg
        return self.cache
