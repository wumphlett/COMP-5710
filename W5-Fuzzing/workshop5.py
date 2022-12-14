import traceback


def simpleCalculator(v1, v2, operation):
    print('The operands are:', v1, v2, operation)
    valid_ops = ['+', '-', '*', '/']
    res = 0 
    if operation in valid_ops:
        if operation=='+':
            res = v1 + v2 
        elif operation=='-':
            res = v1 - v2 
        elif operation=='*':
            res = v1 * v2 
        elif operation=='/':                
            res = v1 / v2 
        elif operation=='%':                
            res = v1 % v2 
        print('After calculation the result is:' , res) 
    else: 
        print('Operation not allowed. Allowable operations are: +, -, *, /, %')
        print('No calculation was done.') 
    return res 


def checkNonPermissiveOperations(): 
    # operation_ = '=' 
    # op_list = [ x for x in range(100) ]
    # for op_ in op_list:
    operation_ = "../../../../../../../../../../../etc/passwd%00"
    simpleCalculator( 100, 1,  operation_  ) 
    print('='*100)

def fuzzValues():
    invalid_operands = [
        ("1", "2", "*"),
        (1, 0, "/"),
        ("one", "two", "/"),
        (True, False, "/"),
        (1, None, "+"),
        ([], {}, "-"),
        (1.0, "0", "/"),
        # The following are calls that do not throw errors but are likely not intended behaviors
        (True, False, "*"),
        ("1", "2", "+"),
        ([1, 2, 3], 5, "*"),
    ]
    for v1, v2, operation in invalid_operands:
        try:
            simpleCalculator(v1, v2, operation)
        except Exception as exc:
            traceback.print_exc()

def simpleFuzzer(): 
    # Complete the following methods 
    fuzzValues()
    # checkNonPermissiveOperations()


if __name__=='__main__':
    # val1, val2, op = 100, 1, '+'

    # data = simpleCalculator(val1, val2, op)
    # print('Operation:{}\nResult:{}'.format(  op, data  ) )

    simpleFuzzer()