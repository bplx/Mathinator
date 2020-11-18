#  ______ _ __  _
# | .  . | | .\| |
# | |\/| | | |\\ |
# |_|  |_|_|_| \_| 
# 
# Mathinator 1.3.1
# Developed by Dexter Summering
# Open Source at github.com/bplx/Mathinator
#

from time import sleep
history = {}

# define our clear function
def init():
    print("============================================")
    print("||                                        ||")
    print("||   ______  __ __       __  __ __ __  __ ||")
    print("||  /  /  / /-/ / /_/ / / / /-/ / / / /_/ ||")
    print("|| /  /  / / / / / / / / / / / / /_/ / \\  ||")
    print("||                 V1.3.1                 ||")
    print("||                                        ||")
    print("============================================")
    print("|| 1. Calculator")
    print("|| 2. Refresh system")
    print("|| 3. Exit")
    print("|| 4. How much do you have left? ")
    print("|| 5. Help")
    print("|| 6. Tape Diagram Solver")
    print("|| 7. Update Log")
    print("|| 8. History")
    print("|| 9. Less Than, Greater Than, or Equal?")
    print("||")
    print("|| Enter a number into the dialog below and press enter.")
    menu()

def lgoe():
  clear()
  out = ""
  print("")
  print("====== Numbers ======")
  lgoei1 = input("|| First number: ")
  lgoei2 = input("|| Second number: ")
  print("=====================")
  print("")
  try:
    lgoei1 = int(lgoei1)
    lgoei2 = int(lgoei2)
  except:
    clear()
    print("")
    print("====== Oops! ======")
    print("|| Those aren't numbers.")
    print("===================")
    print("")
    sleep(1)
    clear()
    lgoe()

  if lgoei1 > lgoei2:
    lgoei1 = str(lgoei1)
    lgoei2 = str(lgoei2)
    out = lgoei1 + " is bigger than " + lgoei2
  if lgoei1 < lgoei2:
    lgoei1 = str(lgoei1)
    lgoei2 = str(lgoei2)
    out = lgoei1 + " is smaller than " + lgoei2
  if lgoei1 == lgoei2:
    lgoei1 = str(lgoei1)
    lgoei2 = str(lgoei2)
    out = lgoei1 + " is equal to " + lgoei2
  print("====== Solution ======")
  print("|| " + out + ".")
  print("======================")
  print("")
  print("Press enter to continue.")
  petcfl = input("")
  if petcfl == "":
    clear()
    init()


def o9ester():
  clear()
  print("")
  print("====== JFSHFSHSKJHL ======")
  print("|| stop stop stop stop stop stop stop")
  print("==========================")
  print("")
  sleep(1)
  clear()
  init()

def o9():
  clear()
  print("")
  print("========= Oops! ==========")
  print("|| That option doesn't exist...")
  print("==========================")
  print("")
  sleep(1)
  clear()
  init()

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
    v1.3.1 ----
      Division by 0 failsafe in the calculator
      Added Less Than, More Than, or Equal

    v1.3 ------
      Quality-of-life updates
      Many bug fixes
      More user-friendly UI 
      Updated Intro
      More failsafes

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
  print("======= Solver =======")
  tinp1 = input("|| Tape diagram number 1: ")
  tinp2 = input("|| Tape diagram total: ")
  print("======================")
  print("")
  try:
    tinp1 = int(tinp1)
    tinp2 = int(tinp2)
    outft = int(outft)
    outft = tinp2 - tinp1
    outft = str(outft)
    hisoutft = str(tinp2), "-", str(tinp1)
    history[hisoutft] = outft
  except:
    clear()
    print("")
    print("======= Oops! =======")
    print("|| Those aren't numbers.")
    print("=====================")
    print("")
    sleep(1)
    clear()
    tapediag()
  print("====== Answer ======")
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
    print("===== Solver ========")
    give = input("|| How much did you give?: ")
    total = input("|| How much did you have before?: ")
    print("=====================")
    try:
        give = int(give)
        total = int(total)
    except:
        clear()
        print("")
        print("======= Oops! ========")
        print("|| Those aren't numbers.")
        print("======================")
        print("")
        sleep(1)
        clear()
        Hmduhl()

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
    print("====== Calculator =======")
    num1inp = input("|| First Number: ")
    num2inp = input("|| Second Number: ")
    oper = input("|| Operator: ")
    print("=========================")
    print(" ")
    try:
        num1inp = int(num1inp)
        num2inp = int(num2inp)
    except:
        clear()
        print("")
        print("======= Oops! =======")
        print("|| Those aren't numbers.")
        print("=====================")
        sleep(1)
        clear()
        calc()
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
        if num2inp == 0:
          clear()
          print("")
          print("====== Oops! ======")
          print("|| You divided by 0.")
          print("===================")
          print("")
          sleep(1)
          clear()
          calc()
        else:
          out = num1inp / num2inp
          hisout = str(num1inp) + "/" + str(num2inp)
          history[hisout] = out
    else:
        clear()
        print("")
        print("======= Oops! =======")
        print("|| You entered an invalid operator.")
        print("=====================")
        print("")
        sleep(1)
        clear()
        calc()
    out = int(out)
    lol = 1
    lol = int(lol)
    out = str(out)
    print("====== Answer ======")
    print("|| " + out)
    print("====================")
    print("")
    print("Press enter to continue")
    calccontinue = input(" ")
    if calccontinue == "":
        clear()
        init()


def menu():
    choice = input("|| Choice: ")
    print("=================")
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
    if choice == "9":
        lgoe()
    else:
        o9()

def anim():
  print("M")
  clear()
  print("Ma")
  clear()
  print("Mat")

resizeplease = input(" Drag the window to the edge of the screen so you don't see the code. \n Some programs require this. \n Press enter once you've done that.")

print("""
  ____  /
 / / / /
/ / / /
""")
sleep(0.1)
clear()
print("""
  ____       /
 / / / __   /
/ / / /_/\ /
""")
sleep(0.1)
clear()
print("""
  ____          /
 / / / __  -/- /
/ / / /_/\ /  /
""")
sleep(0.1)
clear()
print("""
  ____              /
 / / / __  -/- /_  /
/ / / /_/\ /  / / /
""")
sleep(0.1)
clear()
print("""
  ____                /
 / / / __  -/- /_  . /
/ / / /_/\ /  / / / /
""")
sleep(0.1)
clear()
print("""
  ____                    /
 / / / __  -/- /_  . __  /
/ / / /_/\ /  / / / / / / 
""")
sleep(0.1)
clear()
print("""
  ____                         /
 / / / __  -/- /_  . __  __   / 
/ / / /_/\ /  / / / / / /_/\ /
""")
sleep(0.1)
clear()
print("""
  ____          
 / / / __  -/- /_  . __  __  -/- /
/ / / /_/\ /  / / / / / /_/\ /  /
""")
sleep(0.1)
clear()
print("""
  ____          
 / / / __  -/- /_  . __  __  -/- __
/ / / /_/\ /  / / / / / /_/\ /  /_/ /
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

