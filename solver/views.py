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
        selected_number = request.POST.get('selectNumber')
        selected_number = int(selected_number)
         
        number_list =  []
        string_list = []
        ind = 0
        selected_number_original = selected_number
        while (selected_number>0):
            
            number_list.insert(ind, selected_number)
            selected_number-=1
            ind +=1
        
        # ind2 = 0 
        # selected_number = selected_number_original
        # while (selected_number_original>0):
            
        #     string_list.insert(ind2, selected_number)
        #     selected_number-=1
        #     ind2 +=1
        
        
        print("YOU SELCTTTTTTTTTTTTTTTTTTTT ", end="")
        print(selected_number_original)
        for x in number_list:
            print(x)
        

    return render(request, 'solver/inputODE.html', {'order_list': number_list, 'n' : selected_number_original }) #'stringg' : string_list  })



def documentation(request):
    pass

def about (request):
    pass


def submitODE (request, n):
    if request.method == 'POST':    
        x=sympy.symbols('x')
        y=sympy.Function('y')
        function_dict = {'sin': sympy.sin, 'cos': sympy.cos, 'tan':sympy.tan,'sec':sympy.sec,'e': sympy.exp, 'root':sympy.sqrt}

        degree = n
        
        latexeq1 = None
        latexeq2 = None
        latexeq3 = None
        
        if degree==1:
            # p=input('p: ')
            # # p = sympy.sympify(p, locals=function_dict)
            # q=input('q: ')
            # # q = sympy.sympify(q, locals=function_dict)
            # r=input('r: ')
            # # r = sympy.sympify(r, locals=function_dict)
            
            p = request.POST["1"]
            q = request.POST["y"]
            r = request.POST["constant"]

            eq = sympy.Eq(y(x).diff(x)*sympy.sympify(p)+sympy.sympify(q)*y(x),sympy.sympify(r))
            print ("The ODE: ")
            sympy.pprint(eq)
            latexeq1 = sympy.latex(eq)

            print('\n')

            gen_soln=sympy.dsolve(eq)
            print("The general solution is: ")
            sympy.pprint(gen_soln)

            print('\n')

            logarithmic_term_present = False

            def has_logarithmic_term(expr):
                return any(isinstance(term, sympy.log) for term in sympy.postorder_traversal(expr))

            # Check each term in the general solution for logarithmic terms
            for term in gen_soln.args[1:]:
                if has_logarithmic_term(term):
                    logarithmic_term_present = True
                    break
            
            # Check if any logarithmic term is present
            if logarithmic_term_present:
                print("The general solution contains at least one logarithmic(log 0==undefined) term.")
            else:
                val=print("Do you want to have initial condition solution? (Y/n) : ")
                if val=='Y':
                    y0 = float(input('Initial condition y(0): '))
                    y0_prime = float(input("Initial condition for y'(0): "))
                    part_soln = sympy.dsolve(eq, ics={y(0): y0, y(x).diff(x).subs(x, 0): y0_prime})
                    print("The particular solution is: ")
                    sympy.pprint(part_soln)

    #----------------------------------------------------2nd Order-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        elif degree==2:
            # p=input('p: ')
            # # p = sympy.sympify(p, locals=function_dict)
            # q=input('q: ')
            # # q = sympy.sympify(q, locals=function_dict)
            # r=input('r: ')
            # # r = sympy.sympify(r, locals=function_dict)
            # s=input('s: ')
            # # s = sympy.sympify(s, locals=function_dict)
            
            p = request.POST["2"]
            q = request.POST["1"]
            r = request.POST["y"]
            s = request.POST["constant"] 

            print('\n')

            eq = sympy.Eq(y(x).diff(x,x)*sympy.sympify(p)+y(x).diff(x)*sympy.sympify(q)+sympy.sympify(r)*y(x),sympy.sympify(s))
            print ("The ODE: ")
            sympy.pprint(eq)
            latexeq1 = sympy.latex(eq)

            print('\n')

            gen_soln=sympy.dsolve(eq)
            print("The general solution is: ")
            sympy.pprint(gen_soln)

            print('\n')

            logarithmic_term_present = False

            def has_logarithmic_term(expr):
                return any(isinstance(term, sympy.log) for term in sympy.postorder_traversal(expr))

            # Check each term in the general solution for logarithmic terms
            for term in gen_soln.args[1:]:
                if has_logarithmic_term(term):
                    logarithmic_term_present = True
                    break

            # Check if any logarithmic term is present
            if logarithmic_term_present:
                print("The general solution contains at least one logarithmic(log 0==undefined) term.")
            else:
                val=print("Do you want to have initial condition solution? (Y/n) : ")    
                if val=='Y':
                    y0 = float(input('Initial condition y(0): '))
                    y0_prime = float(input("Initial condition for y'(0): "))
                    part_soln = sympy.dsolve(eq, ics={y(0): y0, y(x).diff(x).subs(x, 0): y0_prime})
                    print("The particular solution is: ")
                    sympy.pprint(part_soln)

    #----------------------------------------------------3rd Order---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        elif degree==3:
            # p=input('p: ')
            # # p = sympy.sympify(p, locals=function_dict)
            # q=input('q: ')
            # # q = sympy.sympify(q, locals=function_dict)
            # r=input('r: ')
            # # r = sympy.sympify(r, locals=function_dict)
            # s=input('s: ')
            # # s = sympy.sympify(s, locals=function_dict)
            # t=input('t: ')
            # # s = sympy.sympify(s, locals=function_dict)
            
            
            p = request.POST["3"]
            q = request.POST["2"]
            r = request.POST["1"]
            s = request.POST["y"] 
            t = request.POST["constant"] 

            print('\n')

            eq = sympy.Eq(y(x).diff(x,x,x)*sympy.sympify(p)+y(x).diff(x,x)*sympy.sympify(q)+y(x).diff(x)*sympy.sympify(r)+sympy.sympify(s)*y(x),sympy.sympify(t))
            print ("The ODE: ")
            sympy.pprint(eq)
            latexeq1 = sympy.latex(eq)

            print('\n')

            gen_soln=sympy.dsolve(eq)
            print("The general solution is: ")
            sympy.pprint(gen_soln)

            print('\n')

            logarithmic_term_present = False

            def has_logarithmic_term(expr):
                return any(isinstance(term, sympy.log) for term in sympy.postorder_traversal(expr))

            # Check each term in the general solution for logarithmic terms
            for term in gen_soln.args[1:]:
                if has_logarithmic_term(term):
                    logarithmic_term_present = True
                    break

            # Check if any logarithmic term is present
            if logarithmic_term_present:
                print("The general solution contains at least one logarithmic(log 0==undefined) term.")
            else:
                val=print("Do you want to have initial condition solution? (Y/n) : ")
                if val=='Y':  
                    y0 = float(input('Initial condition y(0): '))
                    y0_prime = float(input("Initial condition for y'(0): "))
                    part_soln = sympy.dsolve(eq, ics={y(0): y0, y(x).diff(x).subs(x, 0): y0_prime})
                    print("The particular solution is: ")
                    sympy.pprint(part_soln)

        #----------------------------------------------------4th Order----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        elif degree==4:
            # p=input('p: ')
            # # p = sympy.sympify(p, locals=function_dict)
            # q=input('q: ')
            # # q = sympy.sympify(q, locals=function_dict)
            # r=input('r: ')
            # # r = sympy.sympify(r, locals=function_dict)
            # s=input('s: ')
            # # s = sympy.sympify(s, locals=function_dict)
            # t=input('t: ')
            # # s = sympy.sympify(s, locals=function_dict)
            # u=input('u: ')
            # # s = sympy.sympify(s, locals=function_dict)

            p = request.POST["4"]
            q = request.POST["3"]
            r = request.POST["2"]
            s = request.POST["1"] 
            t = request.POST["y"] 
            u = request.POST["constant"] 

            
            
            print('\n')

            eq = sympy.Eq(y(x).diff(x,x,x,x)*sympy.sympify(p)+y(x).diff(x,x,x)*sympy.sympify(q)+y(x).diff(x,x)*sympy.sympify(r)+y(x).diff(x)*sympy.sympify(s)+y(x)*sympy.sympify(t),sympy.sympify(u))
            print ("The ODE: ")
            sympy.pprint(eq)
            latexeq1 = sympy.latex(eq)

            print('\n')

            gen_soln=sympy.dsolve(eq)
            print("The general solution is: ")
            sympy.pprint(gen_soln)

            print('\n')

            logarithmic_term_present = False

            def has_logarithmic_term(expr):
                return any(isinstance(term, sympy.log) for term in sympy.postorder_traversal(expr))

            # Check each term in the general solution for logarithmic terms
            for term in gen_soln.args[1:]:
                if has_logarithmic_term(term):
                    logarithmic_term_present = True
                    break

            # Check if any logarithmic term is present
            if logarithmic_term_present:
                print("The general solution contains at least one logarithmic(log 0==undefined) term.")
            else:
                val=print("Do you want to have initial condition solution? (Y/n) : ")
                if val=='Y':
                    print("Do you want to have initial condition solution? (Y/n) : ")    
                    y0 = float(input('Initial condition y(0): '))
                    y0_prime = float(input("Initial condition for y'(0): "))
                    part_soln = sympy.dsolve(eq, ics={y(0): y0, y(x).diff(x).subs(x, 0): y0_prime})
                    print("The particular solution is: ")
                    sympy.pprint(part_soln)

        #----------------------------------------------------5th Order----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        elif degree==5:
            # p=input('p: ')
            # # p = sympy.sympify(p, locals=function_dict)
            # q=input('q: ')
            # # q = sympy.sympify(q, locals=function_dict)
            # r=input('r: ')
            # # r = sympy.sympify(r, locals=function_dict)
            # s=input('s: ')
            # # s = sympy.sympify(s, locals=function_dict)
            # t=input('t: ')
            # # s = sympy.sympify(s, locals=function_dict)
            # u=input('u: ')
            # # s = sympy.sympify(s, locals=function_dict)
            # v=input('v: ')
            
            
            p = request.POST["5"]
            q = request.POST["4"]
            r = request.POST["3"]
            s = request.POST["2"] 
            t = request.POST["1"] 
            u = request.POST["y"] 
            v = request.POST["constant"] 


            print('\n')

            eq = sympy.Eq(y(x).diff(x,x,x,x,x)*sympy.sympify(p)+y(x).diff(x,x,x,x)*sympy.sympify(q)+y(x).diff(x,x,x)*sympy.sympify(r)+y(x).diff(x,x)*sympy.sympify(s)+y(x).diff(x)*sympy.sympify(t)+y(x)*sympy.sympify(u),sympy.sympify(v))
            print ("The ODE: ")
            sympy.pprint(eq)
            latexeq1 = sympy.latex(eq)

            print('\n')

            gen_soln=sympy.dsolve(eq)
            print("The general solution is: ")
            sympy.pprint(gen_soln)

            print('\n')

            logarithmic_term_present = False

            def has_logarithmic_term(expr):
                return any(isinstance(term, sympy.log) for term in sympy.postorder_traversal(expr))

            # Check each term in the general solution for logarithmic terms
            for term in gen_soln.args[1:]:
                if has_logarithmic_term(term):
                    logarithmic_term_present = True
                    break

            # Check if any logarithmic term is present
            if logarithmic_term_present:
                print("The general solution contains at least one logarithmic(log 0==undefined) term.")
            else:
                val=print("Do you want to have initial condition solution? (Y/n) : ")
                if val=='Y':
                    print("Do you want to have initial condition solution? (Y/n) : ")    
                    y0 = float(input('Initial condition y(0): '))
                    y0_prime = float(input("Initial condition for y'(0): "))
                    part_soln = sympy.dsolve(eq, ics={y(0): y0, y(x).diff(x).subs(x, 0): y0_prime})
                    print("The particular solution is: ")
                    sympy.pprint(part_soln)

        #----------------------------------------------------6th Order---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        elif degree==6:
            # p=input('p: ')
            # # p = sympy.sympify(p, locals=function_dict)
            # q=input('q: ')
            # # q = sympy.sympify(q, locals=function_dict)
            # r=input('r: ')
            # # r = sympy.sympify(r, locals=function_dict)
            # s=input('s: ')
            # # s = sympy.sympify(s, locals=function_dict)
            # t=input('t: ')
            # # s = sympy.sympify(s, locals=function_dict)
            # u=input('u: ')
            # # s = sympy.sympify(s, locals=function_dict)
            # v=input('v: ')
            # w=input('w: ')

            
            
            p = request.POST["6"]
            q = request.POST["5"]
            r = request.POST["4"]
            s = request.POST["3"] 
            t = request.POST["2"] 
            u = request.POST["1"] 
            v = request.POST["y"] 
            w = request.POST["constant"] 
            
            print('\n')



            eq = sympy.Eq(y(x).diff(x,x,x,x,x,x)*sympy.sympify(p)+y(x).diff(x,x,x,x,x)*sympy.sympify(q)+y(x).diff(x,x,x,x)*sympy.sympify(r)+y(x).diff(x,x,x)*sympy.sympify(s)+y(x).diff(x,x)*sympy.sympify(t)+y(x).diff(x)*sympy.sympify(u)+y(x)*sympy.sympify(v),sympy.sympify(w))
            print ("The ODE: ")
            sympy.pprint(eq)
            latexeq1 = sympy.latex(eq)

            print('\n')

            gen_soln=sympy.dsolve(eq)
            print("The general solution is: ")
            sympy.pprint(gen_soln)

            print('\n')

            logarithmic_term_present = False

            def has_logarithmic_term(expr):
                return any(isinstance(term, sympy.log) for term in sympy.postorder_traversal(expr))

            # Check each term in the general solution for logarithmic terms
            for term in gen_soln.args[1:]:
                if has_logarithmic_term(term):
                    logarithmic_term_present = True
                    break

            # Check if any logarithmic term is present
            if logarithmic_term_present:
                print("The general solution contains at least one logarithmic(log 0==undefined) term.")
            else:
                val=print("Do you want to have initial condition solution? (Y/n) : ")
                if val=='Y':
                    y0 = float(input('Initial condition y(0): '))
                    y0_prime = float(input("Initial condition for y'(0): "))
                    part_soln = sympy.dsolve(eq, ics={y(0): y0, y(x).diff(x).subs(x, 0): y0_prime})
                    print("The particular solution is: ")
                    sympy.pprint(part_soln)
        
        
        return render(request, 'solver/solution.html', {'input': latexeq1, 'gsoln' : sympy.latex(gen_soln) ,  }) #'stringg' : string_list  })


        
        