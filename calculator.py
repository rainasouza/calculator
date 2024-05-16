def calculator(operation, *args):

    if operation == "+":
            def addition(*args):
                result = 0
                for num in args:
                    result += num
                return result
            return addition(*args)    
    
    if operation == "-":
            def subtraction(*args):
                lista = list(args)
                result = lista[0] - sum(lista[1:])
                return result
            return subtraction(*args)
    
    if operation == "/":
        def division(*args):
            if 0 in args:  
                print("You can't divide by zero")
            else:
                result = args[0]  
                for num in args[1:]:
                    result /= num
                return result
        return division(*args)

    if operation == "*":
        def multiplication(*args):
            result = 1
            lista = list(args)
            for num in lista:
                result *= num
            return result
        return multiplication(*args)

calculator("/", 10,0)

