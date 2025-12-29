def square_root_bisection(number, tolerance = 1e-7, maximum = 100):
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    if number == 0 or number == 1:
        print(f'The square root of {number} is {number}')
        return number

    if number > 0:
        low = 0.0
        high = max(1, number)
        root= 0.0

        for i in range (maximum):
            root = (low + high) / 2.0
            target_square = root ** 2 
            if abs(root - number/root) <= tolerance or abs(high - low) <= tolerance:
                print(f'The square root of {number} is approximately {root}')
                return root               
            
            if target_square < number:
                low = root
            else:
                high = root

        else:
            print(f'Failed to converge within {maximum} iterations')
            return None

            




square_root_bisection(0, 0, 0)
square_root_bisection(0.001, 1e-7, 50)
square_root_bisection(225, 1e-7, 10)
square_root_bisection(81, 1e-3, 50)
square_root_bisection(0.25, 1e-7, 50)