import numpy as np
import pandas as pd
from tkinter import *;
from tkinter import messagebox;
from tkinter import Button
from tkinter import Label
from tkinter import Tk
import winsound
from PIL import ImageTk, Image;
from random import *;
import math
bowling=  pd.read_csv("shakib_bowling_performance.csv")
bating = pd.read_csv("shakib_batting_performance.csv")


''' for all match average  '''
run_avrg_t=0
match_sum_t=0
total_sum_t=0
for i in range (0, bating.shape[0]):
    match_sum_t+=bating.iloc[i,2]
    total_sum_t+=bating.iloc[i,3]
run_avrg_t=total_sum_t/match_sum_t
'''End all match average  '''

''' last 20 match bat'''
march_sum_avg=0
run_total_avg=0
count_avg=0
last20_data=  pd.read_csv("last20_data.csv")
for i in range (0, last20_data.shape[0]):
    match_sum_avg=i+1
    run_total_avg+=last20_data.iloc[i,1]

avrg_avg=run_total_avg/match_sum_avg
l_limit_avg=avrg_avg-10
h_limit_avg=avrg_avg+10

for i in range (0, last20_data.shape[0]):
   if(last20_data.iloc[i,1]<=h_limit_avg and last20_data.iloc[i,1]>=l_limit_avg):
       count_avg+=1
p_met_avg=(count_avg/match_sum_avg)
average_run_per_20=p_met_avg*avrg_avg
'''end last 20 match bat'''

''' last 20 bow'''
last20bow=pd.read_csv("Individual_team\last_20_bow_data.csv")
last_20_bw_avrg=0
for i in range (0, last20bow.shape[0]):
    last_20_bw_avrg+=last20bow.iloc[i,1]
last_20_bw_avrg=last_20_bw_avrg/20
'''end last 20 bow '''
'''avrg wicket'''
wicket_t=0
given_r=0 
over_t=0
match_sm=0
for i in range (0, bowling.shape[0]):
    match_sm+=bowling.iloc[i,2]
    given_r+=bowling.iloc[i,3]
    wicket_t+=bowling.iloc[i,5]
    over_t+=bowling.iloc[i,4]
avrg_total_wicket=wicket_t/match_sm
wicket=(avrg_total_wicket+last_20_bw_avrg)/2
print("avrg_total_wicket=",wicket)
'''end avrg wicket'''
'''fun given run'''
given_run_t=0 
match_sum_t=0
for i in range (0, bowling.shape[0]):
   match_sum_t+=bowling.iloc[i,2]
   given_run_t+=bowling.iloc[i,3]
avrg_given_run_t=given_run_t/match_sum_t 
'''end given run'''
vns=1.5
vvns=1.1

''' Func england'''
def England_cal(master): 
    master.destroy()
    Round1 = Tk();
    Round1.title("SHAKIB VS ENGLAND");
    Round1.geometry("1300x650+25+25");
    Round1.resizable(False, False);
    #winsound.PlaySound('button1.wav', winsound.SND_ASYNC)
    ft = "cambria 10 bold"
    fc = "white"
    bc = "cyan"
    a=10
    t_run=bating.iloc[0,3]
    t_match=bating.iloc[0,2]
    run_avr=bating.iloc[0,3]/bating.iloc[0,2]
    wicket_t=bowling.iloc[0,5]
    
    England_data=  pd.read_csv("Individual_team\england_data.csv")

    run_total=0
    match_total=0
    avrg_run=0
    count=0
    
    for i in range (0, England_data.shape[0]):
        match_sum=i+1
        run_total+=England_data.iloc[i,1]
     
    avrg=run_total/match_sum
    l_limit=avrg-10
    h_limit=avrg+10
    
    for i in range (0, England_data.shape[0]):
       if(England_data.iloc[i,1]<=h_limit and England_data.iloc[i,1]>=l_limit):
           count+=1
           
    #print('count=',count,'  avrg=',avrg,'  t_run',run_total);
    
    p_met=(count/match_sum)
    Eng_pred=p_met*avrg
    if(p_met+p_met_avg<1):
        avrg_shakib=(1-p_met-p_met_avg)*run_avrg_t
    else:
        avrg_shakib=0
    n_vns=(vns*bating.iloc[0,0])
    predec_run=int((avrg_shakib+Eng_pred+average_run_per_20)+n_vns)
   #print('parameter=',p_met)
    wicket_mul=1
    if(wicket_t<=5 and  t_match>10):
        wicket_mul=0
    elif(wicket_t<10):
        wicket_mul=1
    elif(wicket_t>=10 and wicket_t<20):
        wicket_mul=1.3
    else:
        wicket_mul=1.6
    get_wicket=wicket_mul*wicket 
    if(get_wicket>1.5):
        get_wicket=math.ceil(wicket_mul*wicket)
    else:
        get_wicket=math.floor(wicket_mul*wicket)   
    n_avrg_given_run_t=math.ceil(avrg_given_run_t*1.5)
    welcomeMessageLabel = Label(Round1, text = "SHAKIB VS ENGLAND", font="Cambria 20 bold",  fg="blue");
    welcomeMessageLabel.place(relx=0.5, rely=0.05, anchor = "center");
    
    MessageLabel = Label(Round1, text = "TOTAL MATCH", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.25, anchor = "center");    
    MessageLabel = Label(Round1, text = t_match, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.2, rely=0.25, anchor = "center");
    
    MessageLabel = Label(Round1, text = "TOTAL RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.09, rely=0.35, anchor = "center");    
    MessageLabel = Label(Round1, text = t_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.35, anchor = "center");
    
    MessageLabel = Label(Round1, text = "AVERAGE RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.45, anchor = "center");    
    MessageLabel = Label(Round1, text = run_avr, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.30, rely=0.45, anchor = "center");
    
    MessageLabel = Label(Round1, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.07, rely=0.55, anchor = "center");    
    MessageLabel = Label(Round1, text = wicket_t, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.55, anchor = "center");
    

    MessageLabel = Label(Round1, text = "NEXT MATCH PREDICTION", font="Cambria 20 bold", bg="navy", fg="white");
    MessageLabel.place(relx=0.7, rely=0.20, anchor = "center");   
    
    MessageLabel = Label(Round1, text = "RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.30, anchor = "center"); 
    MessageLabel = Label(Round1, text = predec_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.7, rely=0.30, anchor = "center");
    
    MessageLabel = Label(Round1, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.40, anchor = "center"); 
    MessageLabel = Label(Round1, text = get_wicket,font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.40, anchor = "center");
    
    MessageLabel = Label(Round1, text = "GIVEN RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.50, anchor = "center"); 
    MessageLabel = Label(Round1, text = n_avrg_given_run_t,font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.50, anchor = "center");
   
    backButton = Button(Round1, text = "Back", font = "Cambria 14", width = 10, height = 1, fg="green"
    , command = lambda : BackFrom(Round1));
    backButton.place(relx=0.4, rely=0.95, anchor = "center");
    backButton.config(bg="darkred", fg="white")
''' End Func england '''   

''' func India '''                
def India_cal(master): 
    master.destroy()
    Round2 = Tk();
    Round2.title("SHAKIB VS INDIA");
    Round2.geometry("1300x650+25+25");
    Round2.resizable(False, False);
    #winsound.PlaySound('button1.wav', winsound.SND_ASYNC)
    ft = "cambria 10 bold"
    fc = "white"
    bc = "cyan"
    a=10
    t_run=bating.iloc[1,3]
    t_match=bating.iloc[1,2]
    run_avr=bating.iloc[1,3]/bating.iloc[1,2]
    wicket_t=bowling.iloc[1,5]
    
    India_data=  pd.read_csv("Individual_team\India_data.csv")
    run_total=0
    match_total=0
    avrg_run=0
    count=0
    
    for i in range (0, India_data.shape[0]):
        match_sum=i+1
        run_total+=India_data.iloc[i,1]
     
    avrg=run_total/match_sum
    l_limit=avrg-10
    h_limit=avrg+10
    
    for i in range (0, India_data.shape[0]):
       if(India_data.iloc[i,1]<=h_limit and India_data.iloc[i,1]>=l_limit):
           count+=1
           
    #print('count=',count,'  avrg=',avrg,'  t_run',run_total);
    
    p_met=(count/match_sum)
    Eng_pred=p_met*avrg
    if(p_met+p_met_avg<1):
        avrg_shakib=(1-p_met-p_met_avg)*run_avrg_t
    else:
        avrg_shakib=0
    n_vns=(vns*bating.iloc[1,0])
    predec_run=int(avrg_shakib+Eng_pred+average_run_per_20)+n_vns
    
    wicket_mul=1
    if(wicket_t<=5 and  t_match>10):
        wicket_mul=0
    elif(wicket_t<10):
        wicket_mul=1
    elif(wicket_t>=10 and wicket_t<20):
        wicket_mul=1.3
    else:
        wicket_mul=1.6
    get_wicket=wicket_mul*wicket
    if(get_wicket>1.5):
        get_wicket=math.ceil(wicket_mul*wicket)
    else:
        get_wicket=math.floor(wicket_mul*wicket) 
    n_avrg_given_run_t=math.ceil(avrg_given_run_t*1.45)
    welcomeMessageLabel = Label(Round2, text = "SHAKIB VS INDIA", font="Cambria 20 bold",  fg="blue");
    welcomeMessageLabel.place(relx=0.5, rely=0.05, anchor = "center");
    
    MessageLabel = Label(Round2, text = "TOTAL MATCH", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.25, anchor = "center");    
    MessageLabel = Label(Round2, text = t_match, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.2, rely=0.25, anchor = "center");
    
    MessageLabel = Label(Round2, text = "TOTAL RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.09, rely=0.35, anchor = "center");    
    MessageLabel = Label(Round2, text = t_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.35, anchor = "center");
    
    MessageLabel = Label(Round2, text = "AVERAGE RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.45, anchor = "center");    
    MessageLabel = Label(Round2, text = run_avr, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.30, rely=0.45, anchor = "center");
    
    MessageLabel = Label(Round2, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.07, rely=0.55, anchor = "center");    
    MessageLabel = Label(Round2, text = wicket_t, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.55, anchor = "center");
    
    MessageLabel = Label(Round2, text = "NEXT MATCH PREDICTION", font="Cambria 20 bold", bg="navy", fg="white");
    MessageLabel.place(relx=0.7, rely=0.20, anchor = "center"); 
    MessageLabel = Label(Round2, text = "RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.30, anchor = "center"); 
    MessageLabel = Label(Round2, text = predec_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.7, rely=0.30, anchor = "center");
    
    MessageLabel = Label(Round2, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.40, anchor = "center"); 
    MessageLabel = Label(Round2, text = get_wicket, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.40, anchor = "center");
    
    MessageLabel = Label(Round2, text = "GIVEN RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.50, anchor = "center"); 
    MessageLabel = Label(Round2, text = n_avrg_given_run_t,font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.50, anchor = "center");
    
    backButton = Button(Round2, text = "Back", font = "Cambria 14", width = 10, height = 1, fg="green"
    , command = lambda : BackFrom(Round2));
    backButton.place(relx=0.4, rely=0.95, anchor = "center");
    backButton.config(bg="darkred", fg="white")
'''end  func India '''   

'''func Safrica'''                       
def Safrica_cal(master): 
    master.destroy()
    Round3 = Tk();
    Round3.title("SHAKIB VS SOUTHAFRICA");
    Round3.geometry("1300x650+25+25");
    Round3.resizable(False, False);
    ft = "cambria 10 bold"
    fc = "white"
    bc = "cyan"
    a=10
    t_run=bating.iloc[2,3]
    t_match=bating.iloc[2,2]
    run_avr=bating.iloc[2,3]/bating.iloc[2,2]
    wicket_t=bowling.iloc[2,5]
    Safrica_data=  pd.read_csv("Individual_team\Safrica_data.csv")
    run_total=0
    match_total=0
    avrg_run=0
    count=0
    
    for i in range (0, Safrica_data.shape[0]):
        match_sum=i+1
        run_total+=Safrica_data.iloc[i,1]
     
    avrg=run_total/match_sum
    l_limit=avrg-10
    h_limit=avrg+10
    
    for i in range (0,Safrica_data.shape[0]):
       if(Safrica_data.iloc[i,1]<=h_limit and Safrica_data.iloc[i,1]>=l_limit):
           count+=1
        
    p_met=(count/match_sum)
    Eng_pred=p_met*avrg
    if(p_met+p_met_avg<1):
        avrg_shakib=(1-p_met-p_met_avg)*run_avrg_t
    else:
        avrg_shakib=0
    n_vns=(vns*bating.iloc[2,0])
    predec_run=int((avrg_shakib+Eng_pred+average_run_per_20)+n_vns)
   #print('parameter=',p_met)
    wicket_mul=1
    if(wicket_t<=5 and  t_match>10):
        wicket_mul=0
    elif(wicket_t<10):
        wicket_mul=1.1
    elif(wicket_t>=10 and wicket_t<20):
        wicket_mul=1.3
    else:
        wicket_mul=1.6
    get_wicket=wicket_mul*wicket
    print(get_wicket) 
    if(get_wicket>1.5):
        get_wicket=math.ceil(wicket_mul*wicket)
    else:
        get_wicket=math.floor(wicket_mul*wicket)
    n_avrg_given_run_t=math.ceil(avrg_given_run_t*1.4)   
    welcomeMessageLabel = Label(Round3, text = "SHAKIB VS SOUTHAFRICA", font="Cambria 20 bold",  fg="blue");
    welcomeMessageLabel.place(relx=0.5, rely=0.05, anchor = "center");
    
    MessageLabel = Label(Round3, text = "TOTAL MATCH", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.25, anchor = "center");    
    MessageLabel = Label(Round3, text = t_match, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.2, rely=0.25, anchor = "center");
    
    MessageLabel = Label(Round3, text = "TOTAL RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.09, rely=0.35, anchor = "center");    
    MessageLabel = Label(Round3, text = t_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.35, anchor = "center");
    
    MessageLabel = Label(Round3, text = "AVERAGE RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.45, anchor = "center");    
    MessageLabel = Label(Round3, text = run_avr, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.30, rely=0.45, anchor = "center");
    
    MessageLabel = Label(Round3, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.07, rely=0.55, anchor = "center");    
    MessageLabel = Label(Round3, text = wicket_t, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.55, anchor = "center");
    

    MessageLabel = Label(Round3, text = "NEXT MATCH PREDICTION", font="Cambria 20 bold", bg="navy", fg="white");
    MessageLabel.place(relx=0.7, rely=0.20, anchor = "center");   
    
    MessageLabel = Label(Round3, text = "RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.30, anchor = "center"); 
    MessageLabel = Label(Round3, text = predec_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.7, rely=0.30, anchor = "center");
    
    MessageLabel = Label(Round3, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.40, anchor = "center"); 
    MessageLabel = Label(Round3, text = get_wicket, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.40, anchor = "center");
    
    MessageLabel = Label(Round3, text = "GIVEN RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.50, anchor = "center"); 
    MessageLabel = Label(Round3, text = n_avrg_given_run_t,font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.50, anchor = "center"); 
    
    backButton = Button(Round3, text = "Back", font = "Cambria 14", width = 10, height = 1, fg="green"
    , command = lambda : BackFrom(Round3));
    backButton.place(relx=0.4, rely=0.95, anchor = "center");
    backButton.config(bg="darkred", fg="white")
'''end  func Safrica'''

'''fnc aus''' 
def Aus_cal(master): 
    master.destroy()
    Round4 = Tk();
    Round4.title("SHAKIB VS AUSTRALIA");
    Round4.geometry("1300x650+25+25");
    Round4.resizable(False, False);
    #winsound.PlaySound('button1.wav', winsound.SND_ASYNC)
    ft = "cambria 10 bold"
    fc = "white"
    bc = "cyan"
    t_run=bating.iloc[5,3]
    t_match=bating.iloc[5,2]
    run_avr=bating.iloc[5,3]/bating.iloc[5,2]
    wicket_t=bowling.iloc[5,5]
    
    Aus_data=  pd.read_csv("Individual_team\Australia_data.csv")

    run_total=0
    match_total=0
    avrg_run=0
    count=0
    
    for i in range (0, Aus_data.shape[0]):
        match_sum=i+1
        run_total+=Aus_data.iloc[i,1]
     
    avrg=run_total/match_sum
    l_limit=avrg-10
    h_limit=avrg+10
    
    for i in range (0,Aus_data.shape[0]):
       if(Aus_data.iloc[i,1]<=h_limit and Aus_data.iloc[i,1]>=l_limit):
           count+=1
           
    #print('count=',count,'  avrg=',avrg,'  t_run',run_total);
    
    p_met=(count/match_sum)
    Eng_pred=p_met*avrg
    if(p_met+p_met_avg<1):
        avrg_shakib=(1-p_met-p_met_avg)*run_avrg_t
    else:
        avrg_shakib=0
    n_vns=(vns*bating.iloc[5,0])
    predec_run=int((avrg_shakib+Eng_pred+average_run_per_20)+n_vns)
   #print('parameter=',p_met)
    wicket_mul=1
    if(wicket_t<10):
        wicket_mul=1.1
    elif(wicket_t>=10 and wicket_t<20):
        wicket_mul=1.3
    else:
        wicket_mul=1.6
    get_wicket=wicket_mul*wicket
    if(get_wicket>1.5):
        get_wicket=math.ceil(wicket_mul*wicket)
    else:
        get_wicket=math.floor(wicket_mul*wicket)
    n_avrg_given_run_t=math.ceil(avrg_given_run_t*1.35)   
    welcomeMessageLabel = Label(Round4, text = "SHAKIB VS AUSTRALIA", font="Cambria 20 bold",  fg="blue");
    welcomeMessageLabel.place(relx=0.5, rely=0.05, anchor = "center");
    
    MessageLabel = Label(Round4, text = "TOTAL MATCH", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.25, anchor = "center");    
    MessageLabel = Label(Round4, text = t_match, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.2, rely=0.25, anchor = "center");
    
    MessageLabel = Label(Round4, text = "TOTAL RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.09, rely=0.35, anchor = "center");    
    MessageLabel = Label(Round4, text = t_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.35, anchor = "center");
    
    MessageLabel = Label(Round4, text = "AVERAGE RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.45, anchor = "center");    
    MessageLabel = Label(Round4, text = run_avr, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.30, rely=0.45, anchor = "center");
    
    MessageLabel = Label(Round4, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.07, rely=0.55, anchor = "center");    
    MessageLabel = Label(Round4, text = wicket_t, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.55, anchor = "center");
    

    MessageLabel = Label(Round4, text = "NEXT MATCH PREDICTION", font="Cambria 20 bold", bg="navy", fg="white");
    MessageLabel.place(relx=0.7, rely=0.20, anchor = "center");   
    
    MessageLabel = Label(Round4, text = "RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.30, anchor = "center"); 
    MessageLabel = Label(Round4, text = predec_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.7, rely=0.30, anchor = "center");
    
    MessageLabel = Label(Round4, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.40, anchor = "center"); 
    MessageLabel = Label(Round4, text = get_wicket, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.40, anchor = "center");
    
    MessageLabel = Label(Round4, text = "GIVEN RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.50, anchor = "center"); 
    MessageLabel = Label(Round4, text = n_avrg_given_run_t,font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.50, anchor = "center");
    
    backButton = Button(Round4, text = "Back", font = "Cambria 14", width = 10, height = 1, fg="green"
    , command = lambda : BackFrom(Round4));
    backButton.place(relx=0.4, rely=0.95, anchor = "center");
    backButton.config(bg="darkred", fg="white")
''' End Func australia'''  
  
'''start pak'''
def Pak_cal(master): 
    master.destroy()
    Round5 = Tk();
    Round5.title("SHAKIB VS AUSTRALIA");
    Round5.geometry("1300x650+25+25");
    Round5.resizable(False, False);
    #winsound.PlaySound('button1.wav', winsound.SND_ASYNC)
    ft = "cambria 10 bold"
    fc = "white"
    bc = "cyan"
    t_run=bating.iloc[4,3]
    t_match=bating.iloc[4,2]
    run_avr=bating.iloc[4,3]/bating.iloc[4,2]
    wicket_t=bowling.iloc[4,5]
    
    Aus_data=  pd.read_csv("Individual_team\Pakistan_data.csv")

    run_total=0
    match_total=0
    avrg_run=0
    count=0
    
    for i in range (0, Aus_data.shape[0]):
        match_sum=i+1
        run_total+=Aus_data.iloc[i,1]
     
    avrg=run_total/match_sum
    l_limit=avrg-10
    h_limit=avrg+10
    
    for i in range (0,Aus_data.shape[0]):
       if(Aus_data.iloc[i,1]<=h_limit and Aus_data.iloc[i,1]>=l_limit):
           count+=1
           
    #print('count=',count,'  avrg=',avrg,'  t_run',run_total);
    
    p_met=(count/match_sum)
    Eng_pred=p_met*avrg
    if(p_met+p_met_avg<1):
        avrg_shakib=(1-p_met-p_met_avg)*run_avrg_t
    else:
        avrg_shakib=0
    n_vns=(vns*bating.iloc[4,0])
    predec_run=int((avrg_shakib+Eng_pred+average_run_per_20)+n_vns)
   #print('parameter=',p_met)
    wicket_mul=1
    if(wicket_t<=5 and  t_match>10):
        wicket_mul=0
    elif(wicket_t<10):
        wicket_mul=1.2
    elif(wicket_t>=10 and wicket_t<20):
        wicket_mul=1.4
    else:
        wicket_mul=1.7
    get_wicket=wicket_mul*wicket
    print(get_wicket) 
    if(get_wicket>1.5):
        get_wicket=math.ceil(wicket_mul*wicket)
    else:
        get_wicket=math.floor(wicket_mul*wicket)
    n_avrg_given_run_t=math.ceil(avrg_given_run_t*1.3)      
    welcomeMessageLabel = Label(Round5, text = "SHAKIB VS PAKISTAN", font="Cambria 20 bold",  fg="blue");
    welcomeMessageLabel.place(relx=0.5, rely=0.05, anchor = "center");
    
    MessageLabel = Label(Round5, text = "TOTAL MATCH", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.25, anchor = "center");    
    MessageLabel = Label(Round5, text = t_match, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.2, rely=0.25, anchor = "center");
    
    MessageLabel = Label(Round5, text = "TOTAL RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.09, rely=0.35, anchor = "center");    
    MessageLabel = Label(Round5, text = t_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.35, anchor = "center");
    
    MessageLabel = Label(Round5, text = "AVERAGE RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.45, anchor = "center");    
    MessageLabel = Label(Round5, text = run_avr, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.30, rely=0.45, anchor = "center");
    
    MessageLabel = Label(Round5, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.07, rely=0.55, anchor = "center");    
    MessageLabel = Label(Round5, text = wicket_t, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.55, anchor = "center");
    

    MessageLabel = Label(Round5, text = "NEXT MATCH PREDICTION", font="Cambria 20 bold", bg="navy", fg="white");
    MessageLabel.place(relx=0.7, rely=0.20, anchor = "center");   
    
    MessageLabel = Label(Round5, text = "RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.30, anchor = "center"); 
    MessageLabel = Label(Round5, text = predec_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.7, rely=0.30, anchor = "center");
    
    MessageLabel = Label(Round5, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.40, anchor = "center"); 
    MessageLabel = Label(Round5, text = get_wicket, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.40, anchor = "center");  
    
    MessageLabel = Label(Round5, text = "GIVEN RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.50, anchor = "center"); 
    MessageLabel = Label(Round5, text = n_avrg_given_run_t,font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.50, anchor = "center");
    
    backButton = Button(Round5, text = "Back", font = "Cambria 14", width = 10, height = 1, fg="green"
    , command = lambda : BackFrom(Round5));
    backButton.place(relx=0.4, rely=0.95, anchor = "center");
    backButton.config(bg="darkred", fg="white")
'''End Func PAKISTAN   '''

'''START FUN SRILANKA'''
def Sri_cal(master): 
    master.destroy()
    Round6 = Tk();
    Round6.title("SHAKIB VS SRILANKA");
    Round6.geometry("1300x650+25+25");
    Round6.resizable(False, False);
    #winsound.PlaySound('button1.wav', winsound.SND_ASYNC)
    ft = "cambria 10 bold"
    fc = "white"
    bc = "cyan"
    t_run=bating.iloc[6,3]
    t_match=bating.iloc[6,2]
    run_avr=bating.iloc[6,3]/bating.iloc[6,2]
    wicket_t=bowling.iloc[6,5]
    
    Sri_data=  pd.read_csv("Individual_team\Srilanka_data.csv")

    run_total=0
    match_total=0
    avrg_run=0
    count=0
    
    for i in range (0, Sri_data.shape[0]):
        match_sum=i+1
        run_total+=Sri_data.iloc[i,1]
     
    avrg=run_total/match_sum
    l_limit=avrg-10
    h_limit=avrg+10
    
    for i in range (0,Sri_data.shape[0]):
       if(Sri_data.iloc[i,1]<=h_limit and Sri_data.iloc[i,1]>=l_limit):
           count+=1
           
    #print('count=',count,'  avrg=',avrg,'  t_run',run_total);
    
    p_met=(count/match_sum)
    Eng_pred=p_met*avrg
    if(p_met+p_met_avg<1):
        avrg_shakib=(1-p_met-p_met_avg)*run_avrg_t
    else:
        avrg_shakib=0
    n_vns=(vvns*bating.iloc[6,0])
    predec_run=int((avrg_shakib+Eng_pred+average_run_per_20)+n_vns)
   #print('parameter=',p_met)
    wicket_mul=1
    if(wicket_t<=5 and  t_match>10):
        wicket_mul=0
    elif(wicket_t<10):
        wicket_mul=1.3
    elif(wicket_t>=10 and wicket_t<20):
        wicket_mul=1.5
    else:
        wicket_mul=1.7
    get_wicket=wicket_mul*wicket
    print(get_wicket) 
    if(get_wicket>1.5):
        get_wicket=math.ceil(wicket_mul*wicket)
    else:
        get_wicket=math.floor(wicket_mul*wicket)
    n_avrg_given_run_t=math.ceil(avrg_given_run_t*1.25)   
    welcomeMessageLabel = Label(Round6, text = "SHAKIB VS SRILANKA", font="Cambria 20 bold",  fg="blue");
    welcomeMessageLabel.place(relx=0.5, rely=0.05, anchor = "center");
    
    MessageLabel = Label(Round6, text = "TOTAL MATCH", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.25, anchor = "center");    
    MessageLabel = Label(Round6, text = t_match, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.2, rely=0.25, anchor = "center");
    
    MessageLabel = Label(Round6, text = "TOTAL RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.09, rely=0.35, anchor = "center");    
    MessageLabel = Label(Round6, text = t_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.35, anchor = "center");
    
    MessageLabel = Label(Round6, text = "AVERAGE RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.45, anchor = "center");    
    MessageLabel = Label(Round6, text = run_avr, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.30, rely=0.45, anchor = "center");
    
    MessageLabel = Label(Round6, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.07, rely=0.55, anchor = "center");    
    MessageLabel = Label(Round6, text = wicket_t, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.55, anchor = "center");
    

    MessageLabel = Label(Round6, text = "NEXT MATCH PREDICTION", font="Cambria 20 bold", bg="navy", fg="white");
    MessageLabel.place(relx=0.7, rely=0.20, anchor = "center");   
    
    MessageLabel = Label(Round6, text = "RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.30, anchor = "center"); 
    MessageLabel = Label(Round6, text = predec_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.7, rely=0.30, anchor = "center");
    
    MessageLabel = Label(Round6, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.40, anchor = "center"); 
    MessageLabel = Label(Round6, text = get_wicket, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.40, anchor = "center"); 
    
    MessageLabel = Label(Round6, text = "GIVEN RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.50, anchor = "center"); 
    MessageLabel = Label(Round6, text = n_avrg_given_run_t,font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.50, anchor = "center");
   
    backButton = Button(Round6, text = "Back", font = "Cambria 14", width = 10, height = 1, fg="green"
    , command = lambda : BackFrom(Round6));
    backButton.place(relx=0.4, rely=0.95, anchor = "center");
    backButton.config(bg="darkred", fg="white")
'''End Func SRILANKA   '''
'''START FUN WEST'''
def West_cal(master): 
    master.destroy()
    Round7 = Tk();
    Round7.title("SHAKIB VS WESTINDIES");
    Round7.geometry("1300x650+25+25");
    Round7.resizable(False, False);
    #winsound.PlaySound('button1.wav', winsound.SND_ASYNC)
    ft = "cambria 10 bold"
    fc = "white"
    bc = "cyan"
    t_run=bating.iloc[7,3]
    t_match=bating.iloc[7,2]
    run_avr=bating.iloc[7,3]/bating.iloc[7,2]
    wicket_t=bowling.iloc[7,5]
    
    Wes_data=  pd.read_csv("Individual_team\Westindies_data.csv")

    run_total=0
    match_total=0
    avrg_run=0
    count=0
    
    for i in range (0, Wes_data.shape[0]):
        match_sum=i+1
        run_total+=Wes_data.iloc[i,1]
     
    avrg=run_total/match_sum
    l_limit=avrg-10
    h_limit=avrg+10
    
    for i in range (0,Wes_data.shape[0]):
       if(Wes_data.iloc[i,1]<=h_limit and Wes_data.iloc[i,1]>=l_limit):
           count+=1
           
    #print('count=',count,'  avrg=',avrg,'  t_run',run_total);
    
    p_met=(count/match_sum)
    Eng_pred=p_met*avrg
    if(p_met+p_met_avg<1):
        avrg_shakib=(1-p_met-p_met_avg)*run_avrg_t
    else:
        avrg_shakib=0
    n_vns=(vvns*bating.iloc[7,0])
    predec_run=int((avrg_shakib+Eng_pred+average_run_per_20)+n_vns)
   #print('parameter=',p_met)
    wicket_mul=1
    if(wicket_t<=5 and  t_match>10):
        wicket_mul=0
    elif(wicket_t<10):
        wicket_mul=1.2
    elif(wicket_t>=10 and wicket_t<20):
        wicket_mul=1.4
    else:
        wicket_mul=1.7
    get_wicket=wicket_mul*wicket
    print(get_wicket) 
    if(get_wicket>1.5):
        get_wicket=math.ceil(wicket_mul*wicket)
    else:
        get_wicket=math.floor(wicket_mul*wicket)
    n_avrg_given_run_t=math.ceil(avrg_given_run_t*1.2)           
    welcomeMessageLabel = Label(Round7, text = "SHAKIB VS WESTINDIES", font="Cambria 20 bold",  fg="blue");
    welcomeMessageLabel.place(relx=0.5, rely=0.05, anchor = "center");
    
    MessageLabel = Label(Round7, text = "TOTAL MATCH", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.25, anchor = "center");    
    MessageLabel = Label(Round7, text = t_match, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.2, rely=0.25, anchor = "center");
    
    MessageLabel = Label(Round7, text = "TOTAL RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.09, rely=0.35, anchor = "center");    
    MessageLabel = Label(Round7, text = t_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.35, anchor = "center");
    
    MessageLabel = Label(Round7, text = "AVERAGE RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.45, anchor = "center");    
    MessageLabel = Label(Round7, text = run_avr, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.30, rely=0.45, anchor = "center");
    
    MessageLabel = Label(Round7, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.07, rely=0.55, anchor = "center");    
    MessageLabel = Label(Round7, text = wicket_t, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.55, anchor = "center");
    

    MessageLabel = Label(Round7, text = "NEXT MATCH PREDICTION", font="Cambria 20 bold", bg="navy", fg="white");
    MessageLabel.place(relx=0.7, rely=0.20, anchor = "center");   
    
    MessageLabel = Label(Round7, text = "RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.30, anchor = "center"); 
    MessageLabel = Label(Round7, text = predec_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.7, rely=0.30, anchor = "center");

    MessageLabel = Label(Round7, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.40, anchor = "center"); 
    MessageLabel = Label(Round7, text = get_wicket, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.40, anchor = "center"); 
  
    MessageLabel = Label(Round7, text = "GIVEN RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.50, anchor = "center"); 
    MessageLabel = Label(Round7, text = n_avrg_given_run_t,font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.50, anchor = "center");
    
    backButton = Button(Round7, text = "Back", font = "Cambria 14", width = 10, height = 1, fg="green"
    , command = lambda : BackFrom(Round7));
    backButton.place(relx=0.4, rely=0.95, anchor = "center");
    backButton.config(bg="darkred", fg="white")
'''End Func WESTINDIES   '''
'''START FUN AFGAN'''
def Afgan_cal(master): 
    master.destroy()
    Round8 = Tk();
    Round8.title("SHAKIB VS AGGANISTAN");
    Round8.geometry("1300x650+25+25");
    Round8.resizable(False, False);
    #winsound.PlaySound('button1.wav', winsound.SND_ASYNC)
    ft = "cambria 10 bold"
    fc = "white"
    bc = "cyan"
    t_run=bating.iloc[8,3]
    t_match=bating.iloc[8,2]
    run_avr=bating.iloc[8,3]/bating.iloc[8,2]
    wicket_t=bowling.iloc[8,5]
    
    Afg_data=  pd.read_csv("Individual_team\Afganistan_data.csv")

    run_total=0
    match_total=0
    avrg_run=0
    count=0
    
    for i in range (0,Afg_data.shape[0]):
        match_sum=i+1
        run_total+=Afg_data.iloc[i,1]
     
    avrg=run_total/match_sum
    l_limit=avrg-10
    h_limit=avrg+10
    
    for i in range (0,Afg_data.shape[0]):
       if(Afg_data.iloc[i,1]<=h_limit and Afg_data.iloc[i,1]>=l_limit):
           count+=1
           
    #print('count=',count,'  avrg=',avrg,'  t_run',run_total);
    
    p_met=(count/match_sum)
    Eng_pred=p_met*avrg
    if(p_met+p_met_avg<1):
        avrg_shakib=(1-p_met-p_met_avg)*run_avrg_t
    else:
        avrg_shakib=0
    n_vns=(vvns*bating.iloc[8,0])
    predec_run=int((avrg_shakib+Eng_pred+average_run_per_20)+n_vns)
   #print('parameter=',p_met)
    wicket_mul=1
    if(wicket_t<=5 and  t_match>10):
        wicket_mul=0
    elif(wicket_t<10):
        wicket_mul=1.3
    elif(wicket_t>=10 and wicket_t<20):
        wicket_mul=1.6
    else:
        wicket_mul=1.8
    get_wicket=wicket_mul*wicket
    print(get_wicket) 
    if(get_wicket>1.5):
        get_wicket=math.ceil(wicket_mul*wicket)
    else:
        get_wicket=math.floor(wicket_mul*wicket)
    n_avrg_given_run_t=math.ceil(avrg_given_run_t*1.1)            
    welcomeMessageLabel = Label(Round8, text = "SHAKIB VS AFGANISTAN", font="Cambria 20 bold",  fg="blue");
    welcomeMessageLabel.place(relx=0.5, rely=0.05, anchor = "center");
    
    MessageLabel = Label(Round8, text = "TOTAL MATCH", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.25, anchor = "center");    
    MessageLabel = Label(Round8, text = t_match, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.2, rely=0.25, anchor = "center");
    
    MessageLabel = Label(Round8, text = "TOTAL RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.09, rely=0.35, anchor = "center");    
    MessageLabel = Label(Round8, text = t_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.35, anchor = "center");
    
    MessageLabel = Label(Round8, text = "AVERAGE RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.45, anchor = "center");    
    MessageLabel = Label(Round8, text = run_avr, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.30, rely=0.45, anchor = "center");
    
    MessageLabel = Label(Round8, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.07, rely=0.55, anchor = "center");    
    MessageLabel = Label(Round8, text = wicket_t, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.55, anchor = "center");
    

    MessageLabel = Label(Round8, text = "NEXT MATCH PREDICTION", font="Cambria 20 bold", bg="navy", fg="white");
    MessageLabel.place(relx=0.7, rely=0.20, anchor = "center");   
    
    MessageLabel = Label(Round8, text = "RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.30, anchor = "center"); 
    MessageLabel = Label(Round8, text = predec_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.7, rely=0.30, anchor = "center");
    
    MessageLabel = Label(Round8, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.40, anchor = "center"); 
    MessageLabel = Label(Round8, text = get_wicket, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.40, anchor = "center"); 
   
    MessageLabel = Label(Round8, text = "GIVEN RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.50, anchor = "center"); 
    MessageLabel = Label(Round8, text = n_avrg_given_run_t,font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.50, anchor = "center");
    
    backButton = Button(Round8, text = "Back", font = "Cambria 14", width = 10, height = 1, fg="green"
    , command = lambda : BackFrom(Round8));
    backButton.place(relx=0.4, rely=0.95, anchor = "center");
    backButton.config(bg="darkred", fg="white")
'''END FUN AFGAN'''
'''START FUN ZIM'''
def Zimb_cal(master): 
    master.destroy()
    Round9 = Tk();
    Round9.title("SHAKIB VS ZIMBABWEA");
    Round9.geometry("1300x650+25+25");
    Round9.resizable(False, False);
    #winsound.PlaySound('button1.wav', winsound.SND_ASYNC)
    ft = "cambria 10 bold"
    fc = "white"
    bc = "cyan"
    t_run=bating.iloc[9,3]
    t_match=bating.iloc[9,2]
    run_avr=bating.iloc[9,3]/bating.iloc[9,2]
    wicket_t=bowling.iloc[9,5]
    
    Zim_data=  pd.read_csv("Individual_team\Zimbabwea_data.csv")

    run_total=0
    match_total=0
    avrg_run=0
    count=0
    
    for i in range (0, Zim_data.shape[0]):
        match_sum=i+1
        run_total+= Zim_data.iloc[i,1]
     
    avrg=run_total/match_sum
    l_limit=avrg-10
    h_limit=avrg+10
    
    for i in range (0, Zim_data.shape[0]):
       if( Zim_data.iloc[i,1]<=h_limit and  Zim_data.iloc[i,1]>=l_limit):
           count+=1
           
    #print('count=',count,'  avrg=',avrg,'  t_run',run_total);
    
    p_met=(count/match_sum)
    Eng_pred=p_met*avrg
    if(p_met+p_met_avg<1):
        avrg_shakib=(1-p_met-p_met_avg)*run_avrg_t
    else:
        avrg_shakib=0
    n_vns=(vvns*bating.iloc[9,0])
    predec_run=int((avrg_shakib+Eng_pred+average_run_per_20)+n_vns)
   #print('parameter=',p_met)
    wicket_mul=1
    if(wicket_t<=5 and  t_match>10):
        wicket_mul=0
    elif(wicket_t<10):
        wicket_mul=1.4
    elif(wicket_t>=10 and wicket_t<20):
        wicket_mul=1.8
    else:
        wicket_mul=1.9
    get_wicket=wicket_mul*wicket
    print(get_wicket) 
    if(get_wicket>1.5):
        get_wicket=math.ceil(wicket_mul*wicket)
    else:
        get_wicket=math.floor(wicket_mul*wicket)
    n_avrg_given_run_t=math.ceil(avrg_given_run_t*1.05)          
    welcomeMessageLabel = Label(Round9, text = "SHAKIB VS ZIMBABWEA", font="Cambria 20 bold",  fg="blue");
    welcomeMessageLabel.place(relx=0.5, rely=0.05, anchor = "center");
    
    MessageLabel = Label(Round9, text = "TOTAL MATCH", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.25, anchor = "center");    
    MessageLabel = Label(Round9, text = t_match, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.2, rely=0.25, anchor = "center");
    
    MessageLabel = Label(Round9, text = "TOTAL RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.09, rely=0.35, anchor = "center");    
    MessageLabel = Label(Round9, text = t_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.35, anchor = "center");
    
    MessageLabel = Label(Round9, text = "AVERAGE RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.45, anchor = "center");    
    MessageLabel = Label(Round9, text = run_avr, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.30, rely=0.45, anchor = "center");
    
    MessageLabel = Label(Round9, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.07, rely=0.55, anchor = "center");    
    MessageLabel = Label(Round9, text = wicket_t, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.55, anchor = "center");
    

    MessageLabel = Label(Round9, text = "NEXT MATCH PREDICTION", font="Cambria 20 bold", bg="navy", fg="white");
    MessageLabel.place(relx=0.7, rely=0.20, anchor = "center");   
    
    MessageLabel = Label(Round9, text = "RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.30, anchor = "center"); 
    MessageLabel = Label(Round9, text = predec_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.7, rely=0.30, anchor = "center");
    
    MessageLabel = Label(Round9, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.40, anchor = "center"); 
    MessageLabel = Label(Round9, text = get_wicket, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.40, anchor = "center"); 
   
    MessageLabel = Label(Round9, text = "GIVEN RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.50, anchor = "center"); 
    MessageLabel = Label(Round9, text = n_avrg_given_run_t,font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.50, anchor = "center");
    
    backButton = Button(Round9, text = "Back", font = "Cambria 14", width = 10, height = 1, fg="green"
    , command = lambda : BackFrom(Round9));
    backButton.place(relx=0.4, rely=0.95, anchor = "center");
    backButton.config(bg="darkred", fg="white")
'''END FUN Zim'''

'''START FUN NEW'''
def New_cal(master): 
    master.destroy()
    Round10 = Tk();
    Round10.title("SHAKIB VS ENGLAND");
    Round10.geometry("1300x650+25+25");
    Round10.resizable(False, False);
    #winsound.PlaySound('button1.wav', winsound.SND_ASYNC)
    ft = "cambria 10 bold"
    fc = "white"
    bc = "cyan"
    t_run=bating.iloc[3,3]
    t_match=bating.iloc[3,2]
    run_avr=bating.iloc[3,3]/bating.iloc[3,2]
    wicket_t=bowling.iloc[3,5]
    
    England_data=  pd.read_csv("Nland_data.csv")

    run_total=0
    match_total=0
    avrg_run=0
    count=0
    
    for i in range (0, England_data.shape[0]):
        match_sum=i+1
        run_total+=England_data.iloc[i,1]
     
    avrg=run_total/match_sum
    l_limit=avrg-10
    h_limit=avrg+10
    
    for i in range (0, England_data.shape[0]):
       if(England_data.iloc[i,1]<=h_limit and England_data.iloc[i,1]>=l_limit):
           count+=1
           
    #print('count=',count,'  avrg=',avrg,'  t_run',run_total);
    
    p_met=(count/match_sum)
    Eng_pred=p_met*avrg
    if(p_met+p_met_avg<1):
        avrg_shakib=(1-p_met-p_met_avg)*run_avrg_t
    else:
        avrg_shakib=0
    n_vns=(vns*bating.iloc[0,0])
    predec_run=int((avrg_shakib+Eng_pred+average_run_per_20)+n_vns)
   #print('parameter=',p_met)
    wicket_mul=1
    if(wicket_t<=5 and  t_match>10):
        wicket_mul=0
    elif(wicket_t<10):
        wicket_mul=1
    elif(wicket_t>=10 and wicket_t<20):
        wicket_mul=1.3
    else:
        wicket_mul=1.6
    get_wicket=wicket_mul*wicket
    print(get_wicket) 
    if(get_wicket>1.5):
        get_wicket=math.ceil(wicket_mul*wicket)
    else:
        get_wicket=math.floor(wicket_mul*wicket)
    n_avrg_given_run_t=math.ceil(avrg_given_run_t*1.2)   
    
    welcomeMessageLabel = Label(Round10, text = "SHAKIB VS NEWZELAND", font="Cambria 20 bold",  fg="blue");
    welcomeMessageLabel.place(relx=0.5, rely=0.05, anchor = "center");
    
    MessageLabel = Label(Round10, text = "TOTAL MATCH", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.25, anchor = "center");    
    MessageLabel = Label(Round10, text = t_match, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.2, rely=0.25, anchor = "center");
    
    MessageLabel = Label(Round10, text = "TOTAL RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.09, rely=0.35, anchor = "center");    
    MessageLabel = Label(Round10, text = t_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.35, anchor = "center");
    
    MessageLabel = Label(Round10, text = "AVERAGE RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.1, rely=0.45, anchor = "center");    
    MessageLabel = Label(Round10, text = run_avr, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.30, rely=0.45, anchor = "center");
    
    MessageLabel = Label(Round10, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.07, rely=0.55, anchor = "center");    
    MessageLabel = Label(Round10, text = wicket_t, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.21, rely=0.55, anchor = "center");
    

    MessageLabel = Label(Round10, text = "NEXT MATCH PREDICTION", font="Cambria 20 bold", bg="navy", fg="white");
    MessageLabel.place(relx=0.7, rely=0.20, anchor = "center");   
    
    MessageLabel = Label(Round10, text = "RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.30, anchor = "center"); 
    MessageLabel = Label(Round10, text = predec_run, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.7, rely=0.30, anchor = "center");
    
    MessageLabel = Label(Round10, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.40, anchor = "center"); 
    MessageLabel = Label(Round10, text = get_wicket,font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.40, anchor = "center");
    
    MessageLabel = Label(Round10, text = "GIVEN RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.65, rely=0.50, anchor = "center"); 
    MessageLabel = Label(Round10, text = n_avrg_given_run_t,font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.75, rely=0.50, anchor = "center");
    backButton = Button(Round10, text = "Back", font = "Cambria 14", width = 10, height = 1, fg="green"
    , command = lambda : BackFrom(Round10));
    backButton.place(relx=0.4, rely=0.95, anchor = "center");
    backButton.config(bg="darkred", fg="white")
''' End Func england '''

'''START FUN AVG_BAT'''
def Avrg_per_bt(master): 
    master.destroy()
    Round11 = Tk();
    Round11.title("SHAKIB AVRG");
    Round11.geometry("1300x650+25+25");
    Round11.title("First Round")
    Round11.resizable(False, False);
    #winsound.PlaySound('button1.wav', winsound.SND_ASYNC)
    ft = "cambria 10 bold"
    fc = "white"
    bc = "cyan"
    a=10
    bating = pd.read_csv("shakib_batting_performance.csv")
    run_avrg=0
    match_sum=0
    total_sum=0
    fifty=0
    hundrad=0
    for i in range (0, bating.shape[0]):
        match_sum+=bating.iloc[i,2]
        total_sum+=bating.iloc[i,3]
        run_avrg=total_sum/match_sum
        fifty+=bating.iloc[i,4]
        hundrad+=bating.iloc[i,5]
     
    welcomeMessageLabel = Label(Round11, text = "SHAKIB AVERAGE PERFORMANCE", font="Cambria 20 bold",  fg="blue");
    welcomeMessageLabel.place(relx=0.5, rely=0.05, anchor = "center");
    MessageLabel = Label(Round11, text = "TOTAL MATCH", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.4, rely=0.25, anchor = "center");    
    MessageLabel = Label(Round11, text = match_sum, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.5, rely=0.25, anchor = "center");
    
    MessageLabel = Label(Round11, text = "TOTAL RUN", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.39, rely=0.35, anchor = "center");    
    MessageLabel = Label(Round11, text = total_sum, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.5, rely=0.35, anchor = "center");
    
    MessageLabel = Label(Round11, text = "AVERAGE", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.38, rely=0.45, anchor = "center");    
    MessageLabel = Label(Round11, text = run_avrg, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.58, rely=0.45, anchor = "center");
    
    MessageLabel = Label(Round11, text = "FIFTY", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.36, rely=0.55, anchor = "center");    
    MessageLabel = Label(Round11, text = fifty, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.49, rely=0.55, anchor = "center");
    
    MessageLabel = Label(Round11, text = "HUNDRAD", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.38, rely=0.65, anchor = "center");    
    MessageLabel = Label(Round11, text = hundrad, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.49, rely=0.65, anchor = "center");
    
    
    backButton = Button(Round11, text = "Back", font = "Cambria 14", width = 10, height = 1, fg="green"
    , command = lambda : BackFrom(Round11));
    backButton.place(relx=0.4, rely=0.95, anchor = "center");
    backButton.config(bg="darkred", fg="white")       
'''END FUN AVG_BAT''' 

'''START FUN AVG_BOW'''  
def Avrg_per_bl(master): 
    master.destroy()
    Round12 = Tk();
    Round12.title("SHAKIB AVRG");
    Round12.geometry("1300x650+25+25");
    Round12.title("First Round")
    Round12.resizable(False, False);
    #winsound.PlaySound('button1.wav', winsound.SND_ASYNC)
    ft = "cambria 10 bold"
    fc = "white"
    bc = "cyan"
    welcomeMessageLabel = Label(Round12, text = "SHAKIB AVERAGE BOWLING PERFORMANCE", font="Cambria 20 bold",  fg="blue");
    welcomeMessageLabel.place(relx=0.5, rely=0.05, anchor = "center");
    wicket_total=0
    given_run=0 
    over_total=0
    match_sum=0
    for i in range (0, bowling.shape[0]):
         match_sum+=bowling.iloc[i,2]
         given_run+=bowling.iloc[i,3]
         wicket_total+=bowling.iloc[i,5]
         over_total+=bowling.iloc[i,4]
    avrg_total_wicket=wicket_total/match_sum
    economy=given_run/over_total
    Bowling_avg=given_run/wicket_total
    MessageLabel = Label(Round12, text = "TOTAL MATCH", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.4, rely=0.25, anchor = "center");    
    MessageLabel = Label(Round12, text = match_sum, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.5, rely=0.25, anchor = "center");
    
    MessageLabel = Label(Round12, text = "WICKET", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.37, rely=0.35, anchor = "center");    
    MessageLabel = Label(Round12, text = wicket_total, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.50, rely=0.35, anchor = "center");
    
    MessageLabel = Label(Round12, text = "ECHONOMY", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.39, rely=0.45, anchor = "center");    
    MessageLabel = Label(Round12, text = economy, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.58, rely=0.45, anchor = "center");
    
    MessageLabel = Label(Round12, text = "BOWLING AVERAGE", font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.42, rely=0.55, anchor = "center");    
    MessageLabel = Label(Round12, text =  Bowling_avg, font="Cambria 20 bold", bg="black", fg="white");
    MessageLabel.place(relx=0.68, rely=0.55, anchor = "center");
    
    backButton = Button(Round12, text = "Back", font = "Cambria 14", width = 10, height = 1, fg="green"
    , command = lambda : BackFrom(Round12));
    backButton.place(relx=0.4, rely=0.95, anchor = "center");
    backButton.config(bg="darkred", fg="white")
'''END FUN AVG_BOW'''                      
def BackFrom(Round1):
    Round1.destroy()
    #winsound.PlaySound('button1.wav', winsound.SND_ASYNC)
    main()

'''START FUN AVG_MAIN'''  
def main():
    master = Tk();
    master.title("shakib");
    master.geometry("1300x650+25+25");
    ft = "cambria 13 bold";
    titleFont = "cambria 20 bold";
    fc = "white"
    bc = "#0e73a2"
    msg = "Prediction of shakib al hasan";
    welcomeMessageLabel = Label(master, text = msg, font=titleFont, fg="white", bg="#0e73a5", width = 55, height = 2);
    welcomeMessageLabel.place(relx=0.5, rely=0.1, anchor = "center");
    
    teamLabel = Label(master, text="Criket team", font="cambria 18 bold", bg=bc, fg=fc, width = 67, height = 1);
    teamLabel.place(relx=0.5, rely=0.2, anchor="center");
    
    England = Button(master, text = "England", font = "Cambria 14", width = 20, height = 1, fg="cyan"
    ,command = lambda : England_cal(master));
    England.place(relx=0.28, rely=0.35, anchor = "center");
    England.config(bg="green", fg="white");
                   
    India = Button(master, text = "India", font = "Cambria 14", width = 20, height = 1, fg="green"
    ,command = lambda : India_cal(master));
    India.place(relx=0.28, rely=0.45, anchor = "center");
    India.config(bg="green", fg="white");
                 
    Southafrica = Button(master, text = "Southafrica", font = "Cambria 14", width = 20, height = 1, fg="green"
    ,command = lambda : Safrica_cal(master));
    Southafrica.place(relx=0.28, rely=0.55, anchor = "center");
    Southafrica.config(bg="green", fg="white");
                
    Newzealand = Button(master, text = "Newzealand", font = "Cambria 14", width = 20, height = 1, fg="green"
    ,command = lambda : New_cal(master));
    Newzealand.place(relx=0.28, rely=0.65, anchor = "center");
    Newzealand.config(bg="green", fg="white");
                      
    Pakistan = Button(master, text = "Pakistan", font = "Cambria 14", width = 20, height = 1, fg="green"
    ,command = lambda : Pak_cal(master));
    Pakistan .place(relx=0.28, rely=0.75, anchor = "center");
    Pakistan .config(bg="green", fg="white");
                     
    Australia = Button(master, text = "Australia", font = "Cambria 14", width = 20, height = 1, fg="green"
    ,command = lambda : FirstRound(master));
    Australia.place(relx=0.28, rely=0.85, anchor = "center");
    Australia.config(bg="green", fg="white");
                     
    Australia = Button(master, text = "Australia", font = "Cambria 14", width = 20, height = 1, fg="green"
    ,command = lambda : Aus_cal(master));
    Australia.place(relx=0.28, rely=0.85, anchor = "center");
    Australia.config(bg="green", fg="white");
                     
    Westindeas = Button(master, text = "Westindeas", font = "Cambria 14", width = 20, height = 1, fg="green"
    ,command = lambda :West_cal(master));
    Westindeas.place(relx=0.28, rely=0.95, anchor = "center");
    Westindeas.config(bg="green", fg="white");
                      
    Srilanka = Button(master, text = "Srilanka", font = "Cambria 14", width = 20, height = 1, fg="green"
    ,command = lambda : Sri_cal(master));
    Srilanka.place(relx=0.48, rely=.35, anchor = "center");
    Srilanka.config(bg="green", fg="white");
                    
    Afganistan = Button(master, text = "Afganistan", font = "Cambria 14", width = 20, height = 1, fg="green"
    ,command = lambda :Afgan_cal(master));
    Afganistan.place(relx=0.48, rely=.45, anchor = "center");
    Afganistan.config(bg="green", fg="white");
    
    Zimbabwe = Button(master, text = "Zimbabwe", font = "Cambria 14", width = 20, height = 1, fg="green"
    ,command = lambda : Zimb_cal(master));
    Zimbabwe.place(relx=0.48, rely=.55, anchor = "center");
    Zimbabwe.config(bg="green", fg="white");
                    
    Avg_bat = Button(master, text = "Average batting performance", font = "Cambria 14", width = 40, height = 2, fg="green"
    , command = lambda : Avrg_per_bt(master));
    Avg_bat.place(relx=0.7, rely=0.75, anchor = "center");
    Avg_bat.config(bg="indigo", fg="white");
                   
    Avg_bow = Button(master, text = "Average bowling performance", font = "Cambria 14", width = 40, height = 2, fg="green"
    , command = lambda : Avrg_per_bl(master));
    Avg_bow.place(relx=0.7, rely=0.85, anchor = "center");
    Avg_bow.config(bg="indigo", fg="white");
    '''
    img = Image.open("LMessi.png");
    img = img.resize((220, 270), Image.ANTIALIAS);
    photo = ImageTk.PhotoImage(img);
    Messi = Label(master,  image=photo);
    Messi.place(relx=0.88, rely=0.8, anchor="center");
    '''
    master.mainloop();
'''END FUN AVG_MAIN''' 

main();