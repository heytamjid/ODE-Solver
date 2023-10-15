from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect 
from .forms import *
import sympy



def home (request):
    return render (request, 'solver/home.html')

def frontpage (request):
    return render (request, 'solver/frontpage.html' )


def inputODE (request):
    try:
        if request.method == 'POST':
            number = request.POST.get('number')
            number = int(number)
            
            e = None
            if (number>20):
                e = "Currently this webapp can solve ODE upto 20th order. However, our command line program (which is yet to be implemented here) can solve any order ODE. You can check out the program at: https://github.com/kefaet03/mathproject03/"
                return render(request, 'solver/error.html', {'err' : e  })
            elif (number < 0):
                e = "You Seem Lost. Order Can't Be Negative..."
                return render(request, 'solver/error.html', {'err' : e  })
            
            number_list =  []
            selected_number_original = number
            visible_list = []
            for i in range (20-number, 20):
                number_list.append(i)
                visible_list.append(str(20-i))
            semicolon_list = []
            for i in range(selected_number_original):
                semicolon_list.append("'" * i)
            print(semicolon_list)
    except Exception as e:
            print("Something went wrong:" + str(e))
            #return HttpResponse("Soemthing went wrong: "+  str(e)) 
            return render(request, 'solver/error.html', {'err' :str(e) })

    return render(request, 'solver/inputODE.html', {'n' : selected_number_original,
                                                     'combined' : zip(number_list, visible_list),
                                                     'semicolon_list': semicolon_list}) 



def documentation(request):
    pass

def about (request):
    pass


def submitODE (request, num):
    try: 
        if request.method == 'POST':    
            n = 22               # Define the size of the array
            arr = [0]*n          # Initialize an array of size 20 with zeros
            
            x=sympy.symbols('x')
            y=sympy.Function('y')(x)
            
            function_dict = {'sin': sympy.sin, 'cos': sympy.cos, 'e': sympy.exp, 'root':sympy.sqrt}
            
            degree = num
            
            arr [21] = request.POST["constant"]
            arr [20] = request.POST["y"] 
            
            for i in range(19, 19-num, -1):
                arr [i] = request.POST[str(i)] 
                
            eq = sympy.Eq(y.diff(x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[0]) +
                        y.diff(x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[1]) + 
                        y.diff(x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[2]) + 
                        y.diff(x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[3]) +
                        y.diff(x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[4]) + 
                        y.diff(x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[5]) + 
                        y.diff(x,x,x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[6]) + 
                        y.diff(x,x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[7]) + 
                        y.diff(x,x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[8]) + 
                        y.diff(x,x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[9]) + 
                        y.diff(x,x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[10]) +
                        y.diff(x,x,x,x,x,x,x,x,x)*sympy.sympify(arr[11]) + 
                        y.diff(x,x,x,x,x,x,x,x)*sympy.sympify(arr[12]) +
                        y.diff(x,x,x,x,x,x,x)*sympy.sympify(arr[13]) +
                        y.diff(x,x,x,x,x,x)*sympy.sympify(arr[14]) + 
                        y.diff(x,x,x,x,x)*sympy.sympify(arr[15]) +
                        y.diff(x,x,x,x)*sympy.sympify(arr[16]) +
                        y.diff(x,x,x)*sympy.sympify(arr[17]) +
                        y.diff(x,x)*sympy.sympify(arr[18]) +
                        y.diff(x)*sympy.sympify(arr[19]) +
                        y*sympy.sympify(arr[20]),
                        sympy.sympify(arr[21]))
            
            print ("The ODE: ")
            sympy.pprint(eq)
            print('\n')
            
            try:
                gen_soln=sympy.dsolve(eq)
                print("The general solution is: ")
                sympy.pprint(gen_soln)
            except Exception as e:
                print("Something went wrong:" +  str(e))
                #return HttpResponse("Soemthing went wrong: "+  str(e)) 
                return render(request, 'solver/error.html',  {'err' : str(e) })
            print('\n')


        pairs = [(0, 0) for _ in range(degree)]
        particularexist = 1;
        initial_conditions = {}  # Initialize an empty dictionary for initial conditions
        part_soln = None

        #valterminal=input("Do you want to have initial condition solution? (Y/n) : ")
        checkbox_value = request.POST.get('particularcheckbox')
        if checkbox_value == 'on':
            semicolon_list = []   
            for i in range(degree):
                semicolon_list.append("'" * i)
            for xyz in range(degree):
                x_val = request.POST["particularx"+semicolon_list[xyz]]
                y_val = request.POST["particulary"+semicolon_list[xyz]]
                pairs[xyz]=(x_val,y_val)
            print("HERE GOES YOUR PAIRS")
            print(pairs)
            
            ivariable = 0
            for x_val, y_val in pairs:
                #initial_conditions[y(x_val)] = y_val
                initial_conditions[y.diff(x,ivariable).subs(x, x_val)] = y_val   #corrected
                ivariable = ivariable + 1
                
            print("HERE GOES YOUR DICTIONARY")
            print(initial_conditions)

            try:
                part_soln = sympy.dsolve(eq, ics=initial_conditions)
            except Exception as e:
                    print("Something went wrong:" + str(e))
                    #return HttpResponse("Soemthing went wrong: "+  str(e)) 
                    return render(request, 'solver/error.html', {'err' :str(e) })

            print("The particular solution is: ")
            sympy.pprint(part_soln)
            
            
            
        else:
            particularexist = 0      
        


    except Exception as e:
            print("Something went wrong:" + str(e))
            #return HttpResponse("Soemthing went wrong: "+  str(e)) 
            return render(request, 'solver/error.html', {'err' :str(e) })
        
    return render(request, 'solver/solution.html', {'particularexist' : particularexist ,'initial_conditions' : sympy.latex(initial_conditions), 'input': sympy.latex(eq), 'gsoln' : sympy.latex(gen_soln) , 'psoln' : sympy.latex(part_soln) }) #'stringg' : string_list  })


        
        