from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect 
from .forms import *
import sympy



def home (request):
    return render (request, 'solver/home.html')


def inputODE (request):
    if request.method == 'POST':
        number = request.POST.get('number')
        number = int(number)
         
        number_list =  []
        #string_list = []
        #ind = 0
        selected_number_original = number
        # while (number>0):
            
        #     number_list.insert(ind, number)
        #     number-=1
        #     ind +=1

        visible_list = []
        for i in range (20-number, 20):
            number_list.append(i)
            visible_list.append(str(20-i))


        print(type(visible_list[1]))

        
            
        
        # ind2 = 0 
        # number = selected_number_original
        # while (selected_number_original>0):
            
        #     string_list.insert(ind2, number)
        #     number-=1
        #     ind2 +=1
        
        
        print("YOU SELCTTTTTTTTTTTTTTTTTTTT ", end="")
        print(selected_number_original)
        for x in number_list:
            print(x)
            
        n = 4
        semicolon_list = []

        for i in range(selected_number_original):
            semicolon_list.append("'" * i)

        print(semicolon_list)

        

    return render(request, 'solver/inputODE.html', {'order_list': number_list, 'n' : selected_number_original,
                                                    'visible_list' : visible_list, 'sizee' : len(number_list),
                                                     'combined' : zip(number_list, visible_list),
                                                     'semicolon_list': semicolon_list}) #'stringg' : string_list  })

# i know i am writing a non readable mess but currently i am just so desparate to finish this project
# deadline sucks



def documentation(request):
    pass

def about (request):
    pass


def submitODE (request, num):
    if request.method == 'POST':    
        n = 22               # Define the size of the array
        arr = [0]*n          # Initialize an array of size 20 with zeros
        x=sympy.symbols('x')
        y=sympy.Function('y')
        function_dict = {'sin': sympy.sin, 'cos': sympy.cos, 'e': sympy.exp, 'root':sympy.sqrt}
        degree = num


        arr [21] = request.POST["constant"]
        arr [20] = request.POST["y"]

        # for i in range(20-degree,n):
        #     element = input(f"Enter the f(x) co-efficient of {str[i]} : ")
            
        #     arr[i] = request.POST[""]

            #rr [20] = request.POST["20"]


       
        for i in range(19, 19-num, -1):

            arr [i] = request.POST[str(i)]






        # arr [19] = request.POST["19"]
        # arr [18] = request.POST["18"]
        # arr [16] = request.POST["16"]
        # arr [15] = request.POST["15"]
        # arr [14] = request.POST["14"]
        # arr [13] = request.POST["13"]
        # arr [12] = request.POST["12"]
        # arr [11] = request.POST["11"]
        # arr [10] = request.POST["10"]
        # arr [9] = request.POST["9"]
        # arr [8] = request.POST["8"]
        # arr [7] = request.POST["7"]
        # arr [6] = request.POST["6"]
        # arr [5] = request.POST["5"]
        # arr [4] = request.POST["4"]
        # arr [3] = request.POST["3"]
        # arr [2] = request.POST["2"]
        # arr [1] = request.POST["1"]
        # arr [0] = request.POST["0"]



        

        eq = sympy.Eq(y(x).diff(x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[0]) +
                    y(x).diff(x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[1]) + 
                    y(x).diff(x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[2]) + 
                    y(x).diff(x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[3]) +
                    y(x).diff(x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[4]) + 
                    y(x).diff(x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[5]) + 
                    y(x).diff(x,x,x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[6]) + 
                    y(x).diff(x,x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[7]) + 
                    y(x).diff(x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[8]) + 
                    y(x).diff(x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[9]) + 
                    y(x).diff(x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[10]) +
                    y(x).diff(x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[11]) + 
                    y(x).diff(x,x,x,x,x,x,x,x)*sympy.sympify(arr[12]) +
                    y(x).diff(x,x,x,x,x,x,x)*sympy.sympify(arr[13]) +
                    y(x).diff(x,x,x,x,x,x)*sympy.sympify(arr[14]) + 
                    y(x).diff(x,x,x,x,x)*sympy.sympify(arr[15]) +
                    y(x).diff(x,x,x,x)*sympy.sympify(arr[16]) +
                    y(x).diff(x,x,x)*sympy.sympify(arr[17]) +
                    y(x).diff(x,x)*sympy.sympify(arr[18]) +
                    y(x).diff(x)*sympy.sympify(arr[19]) +
                    y(x)*sympy.sympify(arr[20]),
                    sympy.sympify(arr[21]))

        print ("The ODE: ")
        sympy.pprint(eq)

        print('\n')

        gen_soln=sympy.dsolve(eq)
        print("The general solution is: ")
        sympy.pprint(gen_soln)

        print('\n')
        
        
        #next part
        
    logarithmic_term_present = False

    # def has_logarithmic_term(expr):
    #     return any(isinstance(term, sympy.log) for term in sympy.postorder_traversal(expr))

    # # Check each term in the general solution for logarithmic terms
    # for term in gen_soln.args[1:]:
    #     if has_logarithmic_term(term):
    #         logarithmic_term_present = True
    #         break

    str1=["initial equation","1st derivative","2nd derivative","3rd derivative","4th derivative","5th derivative","6th derivative","7th derivative",
            "8th derivative","9th derivative","10th derivative","11th derivative","12th derivative","13th derivative","14th derivative","15th derivative",
            "16th derivative","17th derivative","18th derivative","19th derivative","20th derivative"]

    pairs = [(0, 0) for _ in range(20)]

    #valterminal=input("Do you want to have initial condition solution? (Y/n) : ")
    checkbox_value = request.POST.get('particularcheckbox')
    if checkbox_value == 'on':
        # if logarithmic_term_present: #temporarily emitted 
        #     print("Enter the value of x ensuring x≠0(logx issues)")
        
        
        
        
        #ekhane asol kaj
                    
                    
                    
        # i=0
        # while i < degree:
        #     # Code to be executed while i is less than or equal degree

        #     x_val=int(input(f"The value of x(for {str1[i]}) : "))
        #     y_val=int(input(f'Initial condition for y({i})({x}) : ')) 
        #     pairs[i]=[x_val,y_val]
        #     i+=1
         
        semicolon_list = []   
        for i in range(degree):
            semicolon_list.append("'" * i)

        print(semicolon_list)
        

        for xyz in range(degree, 0, -1):
            x_val = request.POST["particularx"+semicolon_list[degree-xyz]]
            y_val = request.POST["particulary"+semicolon_list[degree-xyz]]
            pairs[xyz]=(x_val,y_val)
        
        print(pairs)
            
            
            
    # else:
    #     sys.exit()

    initial_conditions = {}  # Initialize an empty dictionary for initial conditions
    for x_val, y_val in pairs:
        initial_conditions[y(x_val)] = y_val

    part_soln = sympy.dsolve(eq, ics=initial_conditions)

    print("The particular solution is: ")
    sympy.pprint(part_soln)







    #     x=sympy.symbols('x')
    #     y=sympy.Function('y')
    #     function_dict = {'sin': sympy.sin, 'cos': sympy.cos, 'tan':sympy.tan,'sec':sympy.sec,'e': sympy.exp, 'root':sympy.sqrt}

    #     degree = n
        
    #     latexeq1 = None
    #     latexeq2 = None
    #     latexeq3 = None
        
    #     if degree==1:
    #         # p=input('p: ')
    #         # # p = sympy.sympify(p, locals=function_dict)
    #         # q=input('q: ')
    #         # # q = sympy.sympify(q, locals=function_dict)
    #         # r=input('r: ')
    #         # # r = sympy.sympify(r, locals=function_dict)
            
    #         p = request.POST["1"]
    #         q = request.POST["y"]
    #         r = request.POST["constant"]

    #         eq = sympy.Eq(y(x).diff(x)*sympy.sympify(p)+sympy.sympify(q)*y(x),sympy.sympify(r))
    #         print ("The ODE: ")
    #         sympy.pprint(eq)
    #         latexeq1 = sympy.latex(eq)

    #         print('\n')

    #         gen_soln=sympy.dsolve(eq)
    #         print("The general solution is: ")
    #         sympy.pprint(gen_soln)

    #         print('\n')

    #         logarithmic_term_present = False

    #         def has_logarithmic_term(expr):
    #             return any(isinstance(term, sympy.log) for term in sympy.postorder_traversal(expr))

    #         # Check each term in the general solution for logarithmic terms
    #         for term in gen_soln.args[1:]:
    #             if has_logarithmic_term(term):
    #                 logarithmic_term_present = True
    #                 break
            
    #         # Check if any logarithmic term is present
    #         if logarithmic_term_present:
    #             print("The general solution contains at least one logarithmic(log 0==undefined) term.")
    #         else:
    #             val=print("Do you want to have initial condition solution? (Y/n) : ")
    #             if val=='Y':
    #                 y0 = float(input('Initial condition y(0): '))
    #                 y0_prime = float(input("Initial condition for y'(0): "))
    #                 part_soln = sympy.dsolve(eq, ics={y(0): y0, y(x).diff(x).subs(x, 0): y0_prime})
    #                 print("The particular solution is: ")
    #                 sympy.pprint(part_soln)

    # #----------------------------------------------------2nd Order-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #     elif degree==2:
    #         # p=input('p: ')
    #         # # p = sympy.sympify(p, locals=function_dict)
    #         # q=input('q: ')
    #         # # q = sympy.sympify(q, locals=function_dict)
    #         # r=input('r: ')
    #         # # r = sympy.sympify(r, locals=function_dict)
    #         # s=input('s: ')
    #         # # s = sympy.sympify(s, locals=function_dict)
            
    #         p = request.POST["2"]
    #         q = request.POST["1"]
    #         r = request.POST["y"]
    #         s = request.POST["constant"] 

    #         print('\n')

    #         eq = sympy.Eq(y(x).diff(x,x)*sympy.sympify(p)+y(x).diff(x)*sympy.sympify(q)+sympy.sympify(r)*y(x),sympy.sympify(s))
    #         print ("The ODE: ")
    #         sympy.pprint(eq)
    #         latexeq1 = sympy.latex(eq)

    #         print('\n')

    #         gen_soln=sympy.dsolve(eq)
    #         print("The general solution is: ")
    #         sympy.pprint(gen_soln)

    #         print('\n')

    #         logarithmic_term_present = False

    #         def has_logarithmic_term(expr):
    #             return any(isinstance(term, sympy.log) for term in sympy.postorder_traversal(expr))

    #         # Check each term in the general solution for logarithmic terms
    #         for term in gen_soln.args[1:]:
    #             if has_logarithmic_term(term):
    #                 logarithmic_term_present = True
    #                 break

    #         # Check if any logarithmic term is present
    #         if logarithmic_term_present:
    #             print("The general solution contains at least one logarithmic(log 0==undefined) term.")
    #         else:
    #             val=print("Do you want to have initial condition solution? (Y/n) : ")    
    #             if val=='Y':
    #                 y0 = float(input('Initial condition y(0): '))
    #                 y0_prime = float(input("Initial condition for y'(0): "))
    #                 part_soln = sympy.dsolve(eq, ics={y(0): y0, y(x).diff(x).subs(x, 0): y0_prime})
    #                 print("The particular solution is: ")
    #                 sympy.pprint(part_soln)

    # #----------------------------------------------------3rd Order---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #     elif degree==3:
    #         # p=input('p: ')
    #         # # p = sympy.sympify(p, locals=function_dict)
    #         # q=input('q: ')
    #         # # q = sympy.sympify(q, locals=function_dict)
    #         # r=input('r: ')
    #         # # r = sympy.sympify(r, locals=function_dict)
    #         # s=input('s: ')
    #         # # s = sympy.sympify(s, locals=function_dict)
    #         # t=input('t: ')
    #         # # s = sympy.sympify(s, locals=function_dict)
            
            
    #         p = request.POST["3"]
    ### arr [20] = request.POST["20"]
    #         q = request.POST["2"]
    #         r = request.POST["1"]
    #         s = request.POST["y"] 
    #         t = request.POST["constant"] 

    #         print('\n')

    #         eq = sympy.Eq(y(x).diff(x,x,x)*sympy.sympify(p)+y(x).diff(x,x)*sympy.sympify(q)+y(x).diff(x)*sympy.sympify(r)+sympy.sympify(s)*y(x),sympy.sympify(t))
    #         print ("The ODE: ")
    #         sympy.pprint(eq)
    #         latexeq1 = sympy.latex(eq)

    #         print('\n')

    #         gen_soln=sympy.dsolve(eq)
    #         print("The general solution is: ")
    #         sympy.pprint(gen_soln)

    #         print('\n')

    #         logarithmic_term_present = False

    #         def has_logarithmic_term(expr):
    #             return any(isinstance(term, sympy.log) for term in sympy.postorder_traversal(expr))

    #         # Check each term in the general solution for logarithmic terms
    #         for term in gen_soln.args[1:]:
    #             if has_logarithmic_term(term):
    #                 logarithmic_term_present = True
    #                 break

    #         # Check if any logarithmic term is present
    #         if logarithmic_term_present:
    #             print("The general solution contains at least one logarithmic(log 0==undefined) term.")
    #         else:
    #             val=print("Do you want to have initial condition solution? (Y/n) : ")
    #             if val=='Y':  
    #                 y0 = float(input('Initial condition y(0): '))
    #                 y0_prime = float(input("Initial condition for y'(0): "))
    #                 part_soln = sympy.dsolve(eq, ics={y(0): y0, y(x).diff(x).subs(x, 0): y0_prime})
    #                 print("The particular solution is: ")
    #                 sympy.pprint(part_soln)

    #     #----------------------------------------------------4th Order----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #     elif degree==4:
    #         # p=input('p: ')
    #         # # p = sympy.sympify(p, locals=function_dict)
    #         # q=input('q: ')
    #         # # q = sympy.sympify(q, locals=function_dict)
    #         # r=input('r: ')
    #         # # r = sympy.sympify(r, locals=function_dict)
    #         # s=input('s: ')
    #         # # s = sympy.sympify(s, locals=function_dict)
    #         # t=input('t: ')
    #         # # s = sympy.sympify(s, locals=function_dict)
    #         # u=input('u: ')
    #         # # s = sympy.sympify(s, locals=function_dict)

    #         p = request.POST["4"]
    #         q = request.POST["3"]
    #         r = request.POST["2"]
    #         s = request.POST["1"] 
    #         t = request.POST["y"] 
    #         u = request.POST["constant"] 

            
            
    #         print('\n')

    #         eq = sympy.Eq(y(x).diff(x,x,x,x)*sympy.sympify(p)+y(x).diff(x,x,x)*sympy.sympify(q)+y(x).diff(x,x)*sympy.sympify(r)+y(x).diff(x)*sympy.sympify(s)+y(x)*sympy.sympify(t),sympy.sympify(u))
    #         print ("The ODE: ")
    #         sympy.pprint(eq)
    #         latexeq1 = sympy.latex(eq)

    #         print('\n')

    #         gen_soln=sympy.dsolve(eq)
    #         print("The general solution is: ")
    #         sympy.pprint(gen_soln)

    #         print('\n')

    #         logarithmic_term_present = False

    #         def has_logarithmic_term(expr):
    #             return any(isinstance(term, sympy.log) for term in sympy.postorder_traversal(expr))

    #         # Check each term in the general solution for logarithmic terms
    #         for term in gen_soln.args[1:]:
    #             if has_logarithmic_term(term):
    #                 logarithmic_term_present = True
    #                 break

    #         # Check if any logarithmic term is present
    #         if logarithmic_term_present:
    #             print("The general solution contains at least one logarithmic(log 0==undefined) term.")
    #         else:
    #             val=print("Do you want to have initial condition solution? (Y/n) : ")
    #             if val=='Y':
    #                 print("Do you want to have initial condition solution? (Y/n) : ")    
    #                 y0 = float(input('Initial condition y(0): '))
    #                 y0_prime = float(input("Initial condition for y'(0): "))
    #                 part_soln = sympy.dsolve(eq, ics={y(0): y0, y(x).diff(x).subs(x, 0): y0_prime})
    #                 print("The particular solution is: ")
    #                 sympy.pprint(part_soln)

    #     #----------------------------------------------------5th Order----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #     elif degree==5:
    #         # p=input('p: ')
    #         # # p = sympy.sympify(p, locals=function_dict)
    #         # q=input('q: ')
    #         # # q = sympy.sympify(q, locals=function_dict)
    #         # r=input('r: ')
    #         # # r = sympy.sympify(r, locals=function_dict)
    #         # s=input('s: ')
    #         # # s = sympy.sympify(s, locals=function_dict)
    #         # t=input('t: ')
    #         # # s = sympy.sympify(s, locals=function_dict)
    #         # u=input('u: ')
    #         # # s = sympy.sympify(s, locals=function_dict)
    #         # v=input('v: ')
            
            
    #         p = request.POST["5"]
    #         q = request.POST["4"]
    #         r = request.POST["3"]
    #         s = request.POST["2"] 
    #         t = request.POST["1"] 
    #         u = request.POST["y"] 
    #         v = request.POST["constant"] 


    #         print('\n')

    #         eq = sympy.Eq(y(x).diff(x,x,x,x,x)*sympy.sympify(p)+y(x).diff(x,x,x,x)*sympy.sympify(q)+y(x).diff(x,x,x)*sympy.sympify(r)+y(x).diff(x,x)*sympy.sympify(s)+y(x).diff(x)*sympy.sympify(t)+y(x)*sympy.sympify(u),sympy.sympify(v))
    #         print ("The ODE: ")
    #         sympy.pprint(eq)
    #         latexeq1 = sympy.latex(eq)

    #         print('\n')

    #         gen_soln=sympy.dsolve(eq)
    #         print("The general solution is: ")
    #         sympy.pprint(gen_soln)

    #         print('\n')

    #         logarithmic_term_present = False

    #         def has_logarithmic_term(expr):
    #             return any(isinstance(term, sympy.log) for term in sympy.postorder_traversal(expr))

    #         # Check each term in the general solution for logarithmic terms
    #         for term in gen_soln.args[1:]:
    #             if has_logarithmic_term(term):
    #                 logarithmic_term_present = True
    #                 break

    #         # Check if any logarithmic term is present
    #         if logarithmic_term_present:
    #             print("The general solution contains at least one logarithmic(log 0==undefined) term.")
    #         else:
    #             val=print("Do you want to have initial condition solution? (Y/n) : ")
    #             if val=='Y':
    #                 print("Do you want to have initial condition solution? (Y/n) : ")    
    #                 y0 = float(input('Initial condition y(0): '))
    #                 y0_prime = float(input("Initial condition for y'(0): "))
    #                 part_soln = sympy.dsolve(eq, ics={y(0): y0, y(x).diff(x).subs(x, 0): y0_prime})
    #                 print("The particular solution is: ")
    #                 sympy.pprint(part_soln)

    #     #----------------------------------------------------6th Order---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #     elif degree==6:
    #         # p=input('p: ')
    #         # # p = sympy.sympify(p, locals=function_dict)
    #         # q=input('q: ')
    #         # # q = sympy.sympify(q, locals=function_dict)
    #         # r=input('r: ')
    #         # # r = sympy.sympify(r, locals=function_dict)
    #         # s=input('s: ')
    #         # # s = sympy.sympify(s, locals=function_dict)
    #         # t=input('t: ')
    #         # # s = sympy.sympify(s, locals=function_dict)
    #         # u=input('u: ')
    #         # # s = sympy.sympify(s, locals=function_dict)
    #         # v=input('v: ')
    #         # w=input('w: ')

            
            
    #         p = request.POST["6"]
    #         q = request.POST["5"]
    #         r = request.POST["4"]
    #         s = request.POST["3"] 
    #         t = request.POST["2"] 
    #         u = request.POST["1"] 
    #         v = request.POST["y"] 
    #         w = request.POST["constant"] 
            
    #         print('\n')



    #         eq = sympy.Eq(y(x).diff(x,x,x,x,x,x)*sympy.sympify(p)+y(x).diff(x,x,x,x,x)*sympy.sympify(q)+y(x).diff(x,x,x,x)*sympy.sympify(r)+y(x).diff(x,x,x)*sympy.sympify(s)+y(x).diff(x,x)*sympy.sympify(t)+y(x).diff(x)*sympy.sympify(u)+y(x)*sympy.sympify(v),sympy.sympify(w))
    #         print ("The ODE: ")
    #         sympy.pprint(eq)
    #         latexeq1 = sympy.latex(eq)

    #         print('\n')

    #         gen_soln=sympy.dsolve(eq)
    #         print("The general solution is: ")
    #         sympy.pprint(gen_soln)

    #         print('\n')

    #         logarithmic_term_present = False

    #         def has_logarithmic_term(expr):
    #             return any(isinstance(term, sympy.log) for term in sympy.postorder_traversal(expr))

    #         # Check each term in the general solution for logarithmic terms
    #         for term in gen_soln.args[1:]:
    #             if has_logarithmic_term(term):
    #                 logarithmic_term_present = True
    #                 break

    #         # Check if any logarithmic term is present
    #         if logarithmic_term_present:
    #             print("The general solution contains at least one logarithmic(log 0==undefined) term.")
    #         else:
    #             val=print("Do you want to have initial condition solution? (Y/n) : ")
    #             if val=='Y':
    #                 y0 = float(input('Initial condition y(0): '))
    #                 y0_prime = float(input("Initial condition for y'(0): "))
    #                 part_soln = sympy.dsolve(eq, ics={y(0): y0, y(x).diff(x).subs(x, 0): y0_prime})
    #                 print("The particular solution is: ")
    #                 sympy.pprint(part_soln)
        
        
    return render(request, 'solver/solution.html', {'input': sympy.latex(eq), 'gsoln' : sympy.latex(gen_soln) , 'psoln' : sympy.latex(part_soln) }) #'stringg' : string_list  })


        
        