
############################
#  Code for debt projections
# Author: Advait Moharir
##############################


#importing essential packages

from matplotlib import pyplot as plt
import  csv
import pandas as pd
import numpy as np
import random as rnd
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go

#Output can be displayed online or offline
pio.renderers.default='vscode'
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot, plot

##################################################
# Section 1: Projections
##################################################

# The section below runs projections for the period 2022-2027,
# for four scenarios described in the README. The corresponding 
# values for 2021 (which enter as debt_previous below) are  #
# obtained by running the same 4 scenarios for the debt ratio # starting 2020 (70.6 %). 



# Scenario 1: Fixed PB

# Define law of movement of debt
def debt_present(debt_previous, alpha, pr):
        return (alpha)*debt_previous+pr




debt_new_all = []

c = 0 # Init iterations
while c < 10000:
    c = c  + 1
    #Fixed PB
    debt_previous = 0.845 # Debt ratio for 2021
    debt_new = [] # Vector for output
    roi=[] # Vector for interest
    g=[] # Vector for growth
    pr=[0.03] # Fixed PB at 3%
    inf=[] # Vector for inflation
    alph=[] # Alpha= (1+i)/(1+g)
    no_of_years=6 # Iterate for 6 years
  

    for i in range(no_of_years):

        p = np.arange(0.02, 0.04, 0.000005)
        r =np.arange(0.05, 0.07, 0.000005)
        s=np.arange(0.06, 0.08, 0.000005)
        growth =rnd.sample(list(p), 1)
        g.extend(growth)
        
        primary_balance=pr
        
        inflation=rnd.sample(list(r), 1)
        inf.extend(inflation)
        rateofint=rnd.sample(list(s),1)
        roi.extend(rateofint)
       
        
        alpha=(1+roi[i])/(1+g[i]+inf[i])
        alph.append(alpha)
        debt_new.extend(debt_present(debt_previous, alpha, primary_balance))
        debt_previous = debt_present(debt_previous, alpha, primary_balance)
        #print(debt_new)
        
        
    debt_new_all.append(debt_new) # store the projected debt for all iterations
            

debt_final = []
for i in range(0,6):
    debt = np.average([item[i] for item in debt_new_all])
    debt_final.append(debt)
    
print(debt_final) # Final debt for each year (mean of 10K iterations)

# Scenario 2: Baseline\

def debt_present1(debt_previous1, alpha1, pr1):
    return (alpha1)*debt_previous1+pr1
#Asking user for previous debt levels
#Generating empty lists for endogenous variables

debt_new1_all = []
c = 0
while c < 10000:
    c = c  + 1
    debt_previous1 = 0.851
    debt_new1 = []
    roi1=[]
    g1=[]
    pr1=[]
    inf1=[]
    alph1=[]
    no_of_years=6
    for i in range(no_of_years):
        p1 = np.arange(0.02, 0.04, 0.000005)
        q1 = np.arange(0.03, 0.04, 0.000005)
        r1 =np.arange(0.05, 0.07, 0.000005)
        s1=np.arange(0.06, 0.08, 0.000005)
        growth1 = rnd.sample(list(p1),1)
        g1.extend(growth1)
        primary_balance1= rnd.sample(list(q1),1)
        pr1.extend(primary_balance1)
        inflation1=rnd.sample(list(r1), 1)
        inf1.extend(inflation1)
        rateofint1=rnd.sample(list(s1),1)
        roi1.extend(rateofint1)
        alpha1=(1+roi1[i])/(1+g1[i]+inf1[i])
        alph1.append(alpha1)
        debt_new1.extend(debt_present1(debt_previous1, alpha1, primary_balance1))
        debt_previous1 = debt_present1(debt_previous1, alpha1, primary_balance1)
        #print(debt_new1)
        debt_new1_all.append(debt_new1)
            
#print(debt_new_all) #for checking purposes

#example for explanation of code, can delete later
#debt_new_2020 = [item[0] for item in debt_new_all] 
#print(debt_new_2020)

debt_final1 = []
for i in range(0,6):
    debt1 = np.average([item[i] for item in debt_new1_all])
    debt_final1.append(debt1)
    
print(debt_final1)


# Scenario 3: Fixed roi

def debt_present2(debt_previous2, alpha2, pr2):
    return (alpha2)*debt_previous2+pr2
    #Asking user for previous debt levels
#Generating empty lists for endogenous variables
debt_new3_all = []
c = 0
while c < 10000:
    c = c  + 1
    debt_previous2 = 0.828
    debt_new3 = []
    roi2=[0.04] # Fix i at 4%
    g2=[]
    pr2=[]
    inf2=[]
    alph2=[]
    no_of_years=6
    for i in range(no_of_years):
        p2 = np.arange(0.02, 0.04, 0.000005)
        q2 = np.arange(0.03, 0.04, 0.000005)
        r2 =np.arange(0.05, 0.07, 0.000005)
        #s=np.arange(0.06, 0.08, 0.0005)
        growth2 = rnd.sample(list(p2),1)
        g2.extend(growth2)
        primary_balance2= rnd.sample(list(q2),1)
        pr2.extend(primary_balance2)
        inflation2=rnd.sample(list(r2), 1)
        inf2.extend(inflation2)
        #rateofint=rnd.sample(list(s),1)
        rateofint=roi2
        #roi.extend(rateofint)
        alpha2=(1+roi2[0])/(1+g2[i]+inf2[i])
        alph2.append(alpha2)
        debt_new3.extend(debt_present2(debt_previous2, alpha2, primary_balance2))
        debt_previous2 = debt_present2(debt_previous2, alpha2, primary_balance2)
        #print(debt_new3)
        debt_new3_all.append(debt_new3)
        
# Final debt

debt_final3 = []
for i in range(0,6):
    debt3 = np.average([item[i] for item in debt_new3_all])
    debt_final3.append(debt3)
    
print(debt_final3)

# Scenario 4: Rising Inflation

def debt_present3(debt_previous3, alpha3, pr3):
    return (alpha3)*debt_previous3+pr3
#Asking user for previous debt levels
debt_new4_all = []
c = 0
while c < 10000:
    c = c  + 1

    debt_previous3 = 0.838
    debt_new4 = []
    roi3=[]
    g3=[]
    pr3=[]
    inf3=[]
    alph3=[]
    no_of_years=6
    for i in range(no_of_years):
        p3 = np.arange(0.02, 0.04, 0.000005)
        q3 = np.arange(0.03, 0.04, 0.000005)
        r3 =np.arange(0.06, 0.09, 0.000005)
        s3=np.arange(0.06, 0.08, 0.000005)
        growth3 = rnd.sample(list(p3),1)
        g3.extend(growth3)
        primary_balance3= rnd.sample(list(q3),1)
        pr3.extend(primary_balance3)
        inflation3=rnd.sample(list(r3), 1)
        inf3.extend(inflation3)
        rateofint3=rnd.sample(list(s3),1)
        roi3.extend(rateofint3)
        alpha3=(1+roi3[i])/(1+g3[i]+inf3[i])
        alph3.append(alpha3)
        debt_new4.extend(debt_present3(debt_previous3, alpha3, primary_balance3))
        debt_previous3 = debt_present(debt_previous3, alpha3, primary_balance3)
        #print(debt_new4)
        
        debt_new4_all.append(debt_new4)

# Final debt

debt_final4 = []
for i in range(0,6):
    debt4 = np.average([item[i] for item in debt_new4_all])
    debt_final4.append(debt4)
    
print(debt_final4)

##################################################
# Section 2: Figures
##################################################

# Setup time var

years=np.arange(2022, 2028)
years=list(years)

# Create df
df=pd.DataFrame()

# Labels vars

df['Years']=years
df['Fixed Deficit']=debt_final
df['Baseline']=debt_final1
df['Fixed Interest']=debt_final3
df['Rising Inflation']=debt_final4

# Manually add 2020 and 2021 debt ratios for each scenario

line0 = pd.DataFrame({"Years": 2021, "Fixed Deficit":0.841, 
                     "Baseline":0.846, "Fixed Interest":0.824, 
                     'Rising Inflation': 0.834}, index=[-1])
line = pd.DataFrame({"Years": 2020, "Fixed Deficit":0.708, 
                     "Baseline":0.708, "Fixed Interest":0.708, 
                     'Rising Inflation': 0.708}, index=[-2])

# Append and sort

df = pd.concat([df,line], ignore_index=False)
df = pd.concat([df,line0], ignore_index=False)

# Save as df_proj
df_proj = df.sort_index().reset_index(drop=True)

# Figure-1 (Gross Fiscal Deficit)

data=pd.read_csv('01_data\Fig1.csv')
df=pd.DataFrame(data)

fig = px.line(df, x='Year', y=['Gross Fiscal Deficit', '3% line'],
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white')
fig.update_yaxes(tick0=0, tickvals=[0,1,2,3,4,5,6])
fig.update_xaxes(tick0=2004, dtick=2)
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))

fig.write_image("03_figures/fig1.jpeg",format="jpg", engine="kaleido")

# Figure-2 (Debt Projections)

fig = px.line(df_proj, x='Years', y=['Fixed Deficit', 'Baseline', 'Fixed Interest', 
                                'Rising Inflation'],
              labels={'value':'', 'variable':'', 'Years': ''}, 
              line_shape='spline', template='plotly_white')

fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
fig.write_image('03_figures/fig2.jpeg', format='jpg', engine='kaleido')

# Outsheeting projections data to csv
df_proj.to_csv('01_data/projections.csv', index=False)
 






