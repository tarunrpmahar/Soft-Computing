import numpy as np
import skfuzzy as fuzz
#import matplotlib.pyplot as plt
from skfuzzy import control as ctrl


# Generate universe variables
#   * Quality and service on subjective ranges [0, 10]
#   * Tip has a range of [0, 25] in units of percentage points
#input for fuzzy
ca = ctrl.Antecedent(np.arange(0, 26, 1), 'ca')
att = ctrl.Antecedent(np.arange(0, 6, 1), 'att')
mte = ctrl.Antecedent(np.arange(0, 21, 1), 'mte')
ete = ctrl.Antecedent(np.arange(0, 51, 1), 'ete')
#output for fuzzy
cgpa = ctrl.Consequent(np.arange(0, 11, 1), 'cgpa')

# Generate fuzzy membership functions
ca.automf(3)
att.automf(3)
mte.automf(3)
ete.automf(3)
cgpa.automf(3)

##mte['low'] = fuzz.trimf(mte.universe, [0, 0, 5])
##mte['med'] = fuzz.trimf(mte.universe, [0, 5, 10])
##mte['hi'] = fuzz.trimf(mte.universe, [5, 10, 10])
##ete['low'] = fuzz.trimf(ete.universe, [0, 0, 5])
##ete['med'] = fuzz.trimf(ete.universe, [0, 5, 10])
##ete['hi'] = fuzz.trimf(ete.universe, [5, 10, 10])
##cgpa['low'] = fuzz.trimf(cgpa.universe, [0, 0, 13])
##cgpa['med'] = fuzz.trimf(cgpa.universe, [0, 13, 25])
##cgpa['hi'] = fuzz.trimf(cgpa.universe, [13, 25, 25])

# Visualize these universes and membership functions
#ca.view()
#att.view()
mte.view()

ete.view()
cgpa.view()

rule1 = ctrl.Rule(mte['poor'] | ete['poor'] | att['poor'] | ca['poor'], cgpa['poor'])
rule2 = ctrl.Rule(ca['average'] | mte['average'] | ete['average'], cgpa['average']) 
rule3 = ctrl.Rule(att['good'] |ca['good'] | ete['good'] | mte['good'], cgpa['good'])
rule4 = ctrl.Rule(ca['average'] | mte['poor'] | ete['average'], cgpa['average'])

cgpa_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4]) #base class to contain fuzzy control system

cgpa_cal = ctrl.ControlSystemSimulation(cgpa_ctrl)   # calculate result from control system
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
##ca marks calculation

print("Enter your best 2 ca marks :")
ca1Marks = int(input("ca1:"))
ca2Marks = int(input("ca2:"))
CA= (((ca1Marks+ca2Marks)/60)*25)
cgpa_cal.input['ca'] = CA

##Attendance marks calculation

print("attendance percentage:")
attendance = int(input())
if(attendance >= 75 and attendance<=79):
    temp = 2
elif(attendance >= 80 and attendance<=84 ):
    temp = 3
elif(attendance >= 85 and attendance<=89):
    temp = 4
elif(attendance >= 90):
    temp = 5
else:
    temp = 0
#print(temp)    
cgpa_cal.input['att']=temp

## Mte marks calculation
print("Enter mte marks : ")
midterm = int(input())
midterm = (midterm / 40) * 20
print(midterm)
cgpa_cal.input['mte']=midterm

##ete marks calculation

endterm = int(input('Enter ete marks'))
endterm = (endterm / 70) * 50
print(endterm)
cgpa_cal.input['ete']= endterm

##computiing final output

cgpa_cal.compute()
print(cgpa_cal.output['cgpa'])
cgpa.view(sim=cgpa_cal)


if(cgpa_cal.output['cgpa'] >=6.5):
    print('You got O grade')
elif(cgpa_cal.output['cgpa'] >=6.0 and cgpa_cal.output['cgpa'] <6.5):
    print('You got A grade')
elif(cgpa_cal.output['cgpa'] >=5.5 and cgpa_cal.output['cgpa'] <6.0):
    print('You got B grade')
elif(cgpa_cal.output['cgpa'] >=5.0 and cgpa_cal.output['cgpa'] <5.5):
    print('You got C grade')
elif(cgpa_cal.output['cgpa'] >=4.5 and cgpa_cal.output['cgpa'] <5):
    print('You got D grade')
elif(cgpa_cal.output['cgpa'] <4.5):
    print('You got F grade')
