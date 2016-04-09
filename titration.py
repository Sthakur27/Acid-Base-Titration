    #acid bas titration
#############################################################################
import threading, random
from threading import Thread
import time
import sys
import tkinter
import msvcrt
import os
import math
from tkinter import *
while True:
    alpha=Tk()
    print("acid or base?")
    titraty=input()
    print("strong or weak?")
    strength=input()
    print("volume of solution in ml?")
    volume=(float(input()))/1000
    print("what is molarity?")
    intmolarity=float(input())
    if strength=="weak":
        if titraty=="acid":
            print("What is the Ka Value?")
        if titraty=="base":
            print("What is the Kb Value?")
        kvalue=(input())
        kvalue=eval(kvalue)
        #print("kvalue =",kvalue)
    if titraty=="acid":
        print("How much volume of strong base added?")
    else:
        print("How much volume of strong acid added?")
    vol2=input()
    vol2=float(vol2)/1000
    print("what is the Molarity of the titrating solution?")
    molarity2=input()
    molarity2=float(molarity2)
    pointlist=[]
    therange=volume*2
    truevol=vol2
    test=truevol
    vol2=0
    xcoord=[]
    ycoord=[]
    while vol2<therange:
        if titraty=="acid":
            if strength=="strong":
    #########################################################################
                #strong acid titrated with strong base
                #initial pH:
                molecomparison=(((volume)*intmolarity) - (((vol2)*molarity2)))
                if vol2==test:
                    print("voume =",volume)
                    print("intmolarity=",intmolarity)
                    print("vol2 =", vol2)
                    print("mol2=", molarity2)
                    print("molecomparison=", molecomparison) 
               # print ("difference in moles =", molecomparison)

                #initial pH
                if molecomparison==(volume*intmolarity):
                    a=0
                    pH=-math.log(intmolarity,10)
                    #print("Before titration, pH=",pH)
                    
                #equivalence point
                elif molecomparison==0:
                    pH=7
                    #print("At the equivalence point, pH=7")

                #more moles base than acid    
                elif molecomparison<0:
                    OHcon=(-1*molecomparison)/((vol2+volume))
                    #print(OHcon)
                    pOH=-math.log(OHcon,10)
                    pH=14-pOH
                    #print("pH =",pH)
                    
                #more moles acid than base   
                elif molecomparison>0:
                    Hcon=molecomparison/((vol2+volume))
                    #print(Hcon)
                    pH=-math.log(Hcon,10)
                    #print("pH =",pH)
                

    ###############################################################################
                #titrating a weak acid with a strong base
            if strength=="weak":
                molecomparison=(((volume)*intmolarity) - (((vol2)*molarity2)))
                
                #pH of original solution with no titration
                if molecomparison==(volume*intmolarity):
                    #Ka=[H+][X-]/[HX]   ->   [H+]^2= Ka*[HX]
                    Hcon=(kvalue*intmolarity)**0.5
                    pH=-math.log(Hcon,10)
                    #print("With no titration, pH=",pH)

                #pH @ equivalence point
                elif molecomparison==0:

                    #XH+ OH- -> X- + H20
                    #complete neutrilization. Now we have x moles of X-"
                    cbasecon=(volume*intmolarity)/(volume+vol2)
                    #X- + H20   <->  OH-  +  HX
                    # Kb= [OH-][HX]/[X-]
                    # [OH-]^2 = Kb*[X-]   -> [OH]= (Kb*[X-])^0.5
                    Kb=(10**-14)/kvalue
                    OHcon=(Kb*cbasecon)**0.5
                    pOH=-math.log(OHcon,10)
                    pH=14-pOH
                    #print("pH =",pH)

                    #more moles acid than base
                elif molecomparison>0:
                    #HX+OH- ->  H2O +X-     moles of X- = moles of OH-
                    molX=(vol2*molarity2)
                    molHX=(volume*intmolarity)-(vol2*molarity2)
                    Xcon=molX/(volume+vol2)
                    HXcon=molHX/(volume+vol2)
                    #Ka =  [X-]*[H+]/[HX]
                    Hcon=kvalue*HXcon/Xcon
                    pH=-math.log(Hcon,10)
                    #print(" pH =",pH)
                elif molecomparison<0:
                    #HX+OH- ->  H2O +X-     moles of X- = moles of OH-
                    molX=(volume*intmolarity)
                    molOH=(vol2*molarity2)-(molX)

                    OHcon=molOH/(volume+vol2)
                    #Kb =  [OH-]*[HX]/[X-]
                    pOH=-math.log(OHcon,10)
                    pH=14-pOH
                    #print(" pH =",pH)



                    
        if titraty=="base":
    ###############################################################################
            if strength=="strong":

                #strong acid titrated with strong base
                #initial pH:
                molecomparison=(((volume)*intmolarity) - (((vol2)*molarity2)))
                #print ("difference in moles =", molecomparison)

                #initial pH
                if molecomparison==(volume*intmolarity):
                    a=0
                    pOH=-math.log(intmolarity,10)
                    pH=14-pOH
                    #print("Before titration, pH=",pH)
                    
                #equivalence point
                elif molecomparison==0:
                    pH=7
                    #print("At the equivalence point, pH=7")

                #more moles base than acid    
                elif molecomparison>0:
                    OHcon=(molecomparison)/((vol2+volume))
                    #print(OHcon)
                    pOH=-math.log(OHcon,10)
                    pH=14-pOH
                    #print("pH =",pH)
                    
                #more moles acid than base   
                elif molecomparison<0:
                    Hcon=(-molecomparison)/((vol2+volume))
                    #print(Hcon)
                    pH=-math.log(Hcon,10)
                    #print("pH =",pH)
    #######################################################################################
            if strength=="weak":
                # X- +  H20  <->  HX + OH-
                #  X- + H  <->  HX
                molecomparison=(((volume)*intmolarity) - (((vol2)*molarity2)))
                if molecomparison==(volume*intmolarity):
                    #Kb=[OH-][HX]/[X-]   ->   [OH-]^2= Kb*[X-]
                    OHcon=(kvalue*intmolarity)**0.5
                    pOH=-math.log(OHcon,10)
                    pH=14-pOH
                    #print("With no titration, pH=",pH)

                #pH @ equivalence point
                elif molecomparison==0:
                    #complete neutrilization. Now we have x moles of HX"
                    cacidcon=(volume*intmolarity)/(volume+vol2)
                    
                    #HX  <->  H+  +  X-
                    # Ka= [H+][X-]/[HX]
                    # [H+]^2 = Ka*[HX]   -> [H+]= (Ka*[HX])^0.5
                    Ka=(10**-14)/kvalue
                    Hcon=(Ka*cacidcon)**0.5
                    pH=-math.log(Hcon,10)
                    #print("At the equivalence point, pH =",pH)

                    #more moles acid than base
                elif molecomparison>0:
                    #X- +           H+ ->        HX    moles of HX = moles of H+ added.
                #I  (vol*mol)       0             0
                #I2  vol*mol      vol2*mol2       0
                #C -vol2*mol2    -vol2*mol2     +vol2*mol2
                #E  volmol-vol2mol2   0             vol2*mol2
                    molHX=(vol2*molarity2)
                    molX=(volume*intmolarity)-(vol2*molarity2)
                    Xcon=molX/(volume+vol2)
                    HXcon=molHX/(volume+vol2)
                # HX <-> X- + H+
                    #pH= pKa + log([X-]/[HX])
                    pKa=-math.log(((10**-14)/kvalue),10)
                    pH=pKa+ math.log(Xcon/HXcon)
                    #print(" pH =",pH)
                elif molecomparison<0:
                    #X-+H+- ->  HX + H+    
                    molH=(vol2*molarity2)-(volume*intmolarity)
                    Hcon=molH/(volume+vol2)
                    #Kb =  [OH-]*[HX]/[X-]
                    pH=-math.log(Hcon,10) 
                    #print(" pH =",pH)
        xcoord.append(vol2)
        ycoord.append(pH)
        if vol2==(test):
            print("pH=",pH)
        vol2=vol2+(0.1/1000)
        vol2=round(vol2,4)
        #print(vol2*1000)
############################
    #graph
    graph_window=Tk()
    graph_window.configure(background='#00B88A')
    graph_window.title("Graph")
    graph_window.geometry('600x680+210+35')
    graph_window.resizable(width=FALSE, height=FALSE)
    canvus_1 = Canvas(graph_window,height=600,width=600,bg='white')
#domain
    xdom=(xcoord[len(xcoord)-1])*600*500
    realx=[num*xdom for num in xcoord]
    epoint=volume*xdom
    canvus_1.create_line(epoint,0,epoint,600)
    realy=[(600-(num*(600/14))) for num in ycoord]
    for i in range(0,(len(xcoord)-1)):
        canvus_1.create_line(realx[i],realy[i],realx[i+1],realy[i+1])
###################################################################################
    #y axis
    #canvus_1.create_line((50),0,(50),600)
    #x axis
    #canvus_1.create_line(0,(50),600,(50))
    #ph=7 line
    canvus_1.create_line(0,(300),600,(300))
    canvus_1.place(x=0,y=0)
    graph_window.mainloop()
    print("\n")            
                    






























                    


