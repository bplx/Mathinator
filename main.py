from time import sleep
history = {

}

# define our clear function
def init():
    print("============================================")
    print("||                                        ||")
    print("||   ______  __ __       __  __ __ __  __ ||")
    print("||  /  /  / /-/ / /_/ / / / /-/ / / / /_/ ||")
    print("|| /  /  / / / / / / / / / / / / /_/ / \\  ||")
    print("||                 V1.2.2                 ||")
    print("||                                        ||")
    print("============================================")
    print("")
    print("------------------")
    print("1. Calculator")
    print("2. Refresh system")
    print("3. Exit")
    print("4. How much do you have left? ")
    print("5. Help")
    print("6. Tape Diagram Solver")
    print("7. Update Log")
    print("8. History")
    print("------------------")
    print("")
    menu()

def historyread():
  clear()
  print("")
  print("====== History ======")
  llistr = len(history)
  llistr = str(llistr)
  for i, (x, y)in enumerate(history.items(), start=1):
    print("||", f"{i}: {x} = {y}")
  print("=====================")
  print("")
  print("Press enter to continue")
  petcfh = input("")
  if petcfh == "":
    clear()
    init()

def updatelog():
  clear()
  print("")
  print("""
    v1.2.2 ----
      Useful tweaks to history

    v1.2 ------
      Added History
      Added Intro Animation

    v1.1 ------
      Added Tape Diagram Solver
      Added Update Log
    
    v1 --------
      Added Calculator
      Added Refresh System
      Added Exit
      Added How much do you have left?
      Added Help
      Created Mathinator
  """)
  print(" ")
  print("Press enter to continue")
  petcful = input("")
  if petcful == "":
    clear()
    init()

def tapediag():
  clear()
  outft = 0
  print("")
  print("======= Input ========")
  tinp1 = input("|| Tape diagram number 1: ")
  tinp2 = input("|| Tape diagram total: ")
  print("======================")
  print("")
  tinp1 = int(tinp1)
  tinp2 = int(tinp2)
  outft = int(outft)
  outft = tinp2 - tinp1
  outft = str(outft)
  hisoutft = str(tinp2), "-", str(tinp1)
  history[hisoutft] = outft
  print("====== Output ======")
  print("|| " + outft)
  print("====================")
  print("")
  print("Press enter to continue")
  petc = input(" ")
  if petc == "":
    clear()
    init()
  

def help():
    clear()
    print("""
  Mathinator V1
  Help Manual

  CALCULATOR 
	  Calculator is a good calculator. 
	  Type two numbers at the prompt. For the operator, you pick from these options: 

	  add = Addition. 
	  subtract = Subtraction. 
	  multiply = Multiplication. 	
	  divide = Division.

  REFRESH SYSTEM
	  Enter this, and it will refresh the system. Use only in case of catastrophic error.

  EXIT
	  Self-explanatory.

  HOW MUCH DO YOU HAVE LEFT
	  This is a common problem in Eureka Math. Also pretty self-explanatory.

  TAPE DIAGRAM SOLVER
    It's similar to the calculator. For example,
    in this image (https://images.app.goo.gl/SVnNfTW4gi2rXjLW6)
    the first number is 1705, and the total is 3627.
    This program will calculate the number in the empty box.
    Cool, isn't it.

  HISTORY 
    Every calculation you've done will appear here in order.
    Pretty handy tool. 

      """)
    print(" ")
    print("   Press enter to continue.")
    contineeu = input(" ")
    if contineeu == "":
        clear()
        init()


def clear():
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')


def Hmduhl():
    clear()
    print("")
    print("===== Input =========")
    give = input("|| How much did you give?: ")
    total = input("|| How much did you have before?: ")
    print("=====================")
    try:
        give = int(give)
        total = int(total)
    except:
        print("stop toying with me. those aren't numbers.")

    outfh = total - give
    outfh = str(outfh)
    hisoutfh = str(total), "-", str(give)
    history[hisoutfh] = outfh
    print("")
    print("====== Output ======")
    print("|| " + outfh)
    print("====================")
    print("")
    print("Press enter to continue")
    continu = input(" ")
    if continu == "":
        clear()
        init()


def exitp():
    exit()


def calc():
    clear()
    import numbers
    print(" ")
    print("Dexter's \"Cool-As-Hell\" Calculator")
    print(" ")
    print("====== Input ============")
    num1inp = input("|| First Number: ")
    num2inp = input("|| Second Number: ")
    oper = input("|| Operator: ")
    print("=========================")
    print(" ")
    try:
        num1inp = int(num1inp)
        num2inp = int(num2inp)
    except:
        print("stop toying with me. those aren't numbers.")
        wait(1)
        clear()
        init()
    if oper == "add":
        out = num1inp + num2inp
        hisout = str(num1inp) + "+" + str(num2inp)
        history[hisout] = out
    elif oper == "subtract":
        out = num1inp - num2inp
        hisout = str(num1inp) + "-" + str(num2inp)
        history[hisout] = out
    elif oper == "multiply":
        out = num1inp * num2inp
        hisout = str(num1inp) + "*" + str(num2inp)
        history[hisout] = out
    elif oper == "divide":
        out = num1inp / num2inp
        hisout = str(num1inp) + "/" + str(num2inp)
        history[hisout] = out
    else:
        print("Enter add, subtract, multiply, or divide.")
        sleep(1)
        clear()
        init()
    out = int(out)
    lol = 1
    lol = int(lol)
    out = str(out)
    print("====== Output ======")
    print("|| " + out)
    print("====================")
    print("")
    print("Press enter to continue")
    calccontinue = input(" ")
    if calccontinue == "":
        clear()
        init()


def menu():
    choice = input("Tool: ")
    if choice == "1":
        calc()
    if choice == "2":
        init()
    if choice == "3":
        exitp()
    if choice == "4":
        Hmduhl()
    if choice == "5":
        help()
    if choice == "6":
        tapediag()
    if choice == "7":
        updatelog()
    if choice == "8":
        historyread()

def anim():
  print("M")
  clear()
  print("Ma")
  clear()
  print("Mat")

resizeplease = input("Drag the window to the edge of the screen so you don't see the code. Some programs require this. Press enter once you've done that.")

print("""
  ____
 / / /
/ / /
""")
sleep(0.1)
clear()
print("""
  ____
 / / / __
/ / / /_/\
""")
sleep(0.1)
clear()
print("""
  ____      
 / / / __  -/-
/ / / /_/\ /
""")
sleep(0.1)
clear()
print("""
  ____          
 / / / __  -/- /_
/ / / /_/\ /  / /
""")
sleep(0.1)
clear()
print("""
  ____          
 / / / __  -/- /_  .
/ / / /_/\ /  / / /
""")
sleep(0.1)
clear()
print("""
  ____          
 / / / __  -/- /_  . __
/ / / /_/\ /  / / / / /
""")
sleep(0.1)
clear()
print("""
  ____          
 / / / __  -/- /_  . __  __
/ / / /_/\ /  / / / / / /_/\
""")
sleep(0.1)
clear()
print("""
  ____          
 / / / __  -/- /_  . __  __  -/-
/ / / /_/\ /  / / / / / /_/\ /
""")
sleep(0.1)
clear()
print("""
  ____          
 / / / __  -/- /_  . __  __  -/- __
/ / / /_/\ /  / / / / / /_/\ /  /_/
""")
sleep(0.1)
clear()
print("""
  ____          
 / / / __  -/- /_  . __  __  -/- __  __
/ / / /_/\ /  / / / / / /_/\ /  /_/ /
""")
sleep(1)
clear()
init()

