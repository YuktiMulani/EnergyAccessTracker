
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector as sql
import pymysql
import sys
from sqlalchemy import create_engine
df=pd.read_csv('E:\yukti\csv files\project2.csv',sep='\t')
df1=pd.DataFrame(df)

def Menuset():
    ans='y'
    while ans=='y' or ans=='Y':
        opt:''
        print()
        print('-'*70)
        print('       ACCESS TO ENERGY AROUND THE WORLD         ')
        print('-'*70)
        print('1- Data Visualistaion\n')
        print('2-Analysis\n')
        print('3-Read the csv file\n')
        print('4-Export to MYSQL \n')
        print('5-Manipulation\n')
        print('6- EXIT')
        print('-'*70)
        opt=input('Enter your choice:')
        if opt=='1':
            visuals()
        elif opt=='2':
            analysis()
        elif opt=='3':
            read_csv_excel()
        elif opt=='4':
            exp_imp_sql()
        elif opt=='5':
            manipulation()
        elif opt=='6':
            my_chance=input('do you really want to exit(y/n)??')
            if my_chance=='y' or my_chance=='Y':
                print('Thank you exiting now.......')
                sys.exit()
        else:
            print('Invalid choice try again')
            continue
    else:
        ans=input('Do you want to continue(y/n)??')
 
def visuals():
    ch='y'
    while ( ch=='y' or ch=='Y'):
        print()
        print('-'*70)
        print('DATA VISUALISATION OF 10 COUNTRIES')
        print('-'*70)
        print('1.PEOPLE WITH ACCESS TO ELECTRICITY (PIE CHART)')
        print('2.PEOPLE WITHOUT ACCESS TO ELECTRICITY (LINE CHART)')
        print('3.COMPARISION OF PEOPLE WITH AND WITHOUT ACCES TO ELECTRICITY (LINE CHART)')
        print('4.PER CAPITA CONSUMPTION OF ENERGY (LINE CHART)')
        print('5.EXIT')
        print('-'*70)
        opt1=input('enter your choice:')
        if opt1=='1':
            pie1()
        elif opt1=='2':
            line_chart1()
        elif opt1=='3':
            line_chart2()
        elif opt1=='4':
            line_chart3()
        elif opt1=='5':
              chance=input('Do you really want to exit and go back to Main Menu(y/n)??')
              if chance=='y'or chance=='Y':
                  print('EXITIING.....')
                  break
        else:
            print('Invalid choice try again')
            continue
    else:
        ans=input('Do you want to continue(y/n)??')

def analysis():
    ch1='y'
    while (ch1=='y' or ch1=='Y'):
        print()
        print('-'*70)
        print(' ANALYSIS')
        print('-'*70)
        print('1.TOP RECORDS')
        print('2.BOTTOM RECORDS')
        print('3.PARTICULAR COUNTRY\'S RECORDS')
        print('4.PARTICULAR COLUMN')
        print('5.MULTIPLE COLUMNS')
        print('6.PARTICULAR YEAR')
        print('7.APPLY AGGREGATE FUNCTION FOR WORLD DATA')
        print('8.APPLY PIVOTING')
        print('9.EXIT')
        print('-'*70)
        opt2=input('enter your choice:')
        if opt2=='1':
            n=int(input('Enter the number of records to be displayed:'))
            print('Top',n,'records from the dataframe are:')
            pd.set_option('max_columns',None)
            print(df1.head(n))
        elif opt2=='2':
            n=int(input('Enter the number of records to be displayed:'))
            print('Bottom',n,'records from the dataframe are:')
            print(df1.tail(n))
        elif opt2=='3':
            a=input('Enter country name(Argentina,China,India,Japan,Mexico,Spain,South Korea\n,South Africa,Turkey,USA) for example:India:')
            if (a=='Argentina' or a=='argentina'):
                print(df1.head(27))
            elif(a=='China' or a=='china'):
                print(df1.iloc[27:54,])
            elif(a=='India' or a=='india'):
                print(df1.iloc[54:81,])
            elif(a=='Japan' or a=='japan'):
                print(df1.iloc[81:108,])
            elif(a=='Mexico' or a=='mexico'):
                print(df1.iloc[108:135,])
            elif(a=='South Africa' or a=='south africa'):
                print(df1.iloc[135:162,])
            elif(a=='South Korea' or a=='south korea'):
                print(df1.iloc[162:189,])
            elif(a=='Spain' or a=='spain'):
                print(df1.iloc[189:216,])
            elif(a=='Turkey' or a=='turkey'):
                print(df1.iloc[216:243,])
            elif(a=='USA' or a=='usa'):
                print(df1.tail(27))
            else:
                print('Country not found')
        elif opt2=='4':
            print('Name of the column \n',df1.columns)
            co=eval(input('enter the column name to be displayed, for example("Number of people\n without access to electricity"): '))
            pd.set_option('max_rows',None)
            print(df1[co])
        elif opt2=='5':
            print('Name of the column \n',df1.columns)
            co=eval(input('enter the column name brackets, for example-["Number of people without\n access to electricity","Code"]:'))
            pd.set_option('max_rows',None)
            print(df1[co])
        elif opt2=='6':
            a=input('enter column name(Energy consumption per capita (kWh),Number of people\n without access to electricity,Access to electricity (% of population),\n for example-Access to electricity (% of population):')
            df2=df1.pivot(index='Year',columns='Entity',values=a)
            x=int(input('enter the year'))
            print(df2.loc[x,:])
        elif opt2=='7':
            print('applying aggregate function')
            print('name of the column :Energy consumption per capita (kWh),Access to elec\ntricity (% of population),Number of people without access to electricity')
            co=eval(input('enter the column name as brackets, for example-["Access to electricity (\n% of population)","Number of people without access to electricity"]:'))
            f=input('enter the function name as( max ,min,mode,mean,median,sum,count), for example-sum:')
            if f=='max':
                print(df1[co].max())
            elif f=='min':
                print(df1[co].min())
            elif f=='mode':
                print(df1[co].mode())
            elif f=='mean':
                print(df1[co].mean())
            elif f=='median':
                print(df1[co].median())
            elif f=='min':
                print(df1[co].min())
            elif f=='sum':
                print(df1[co].sum())
            elif f=='count':
                print(df1[co].count())
            else:
                print('invalid choice')
        elif opt2=='8':
            a=input('enter column name(Energy consumption per capita (kWh),Number of people\n without access to electricity,Access to electricity (% of population)\n, for example- Number of people without access to electricity:')
            df2=df1.pivot(index='Entity',columns='Year',values=a)
            pd.set_option('max_rows',None)
            pd.set_option('max_columns',None)
            print(df2)
        elif opt2=='9':
              chance=input('Do you really want to exit and go back to Main Menu(y/n)??')
              if chance=='y'or chance=='Y':
                  print('EXITING.....')
                  break
        else:
            print('Invalid choice try again')
            continue
    else:
        ans=input('Do you want to continue(y/n)')
       
def read_csv_excel():
    while True:
        print('1.Read csv file to create and display dataframe')
        print('2.Press 2 to go back')
        choice=int(input('Enter your choice:'))
        if choice==1:
            df=pd.read_csv('E:\yukti\csv files\project2.csv',sep='\t')
            print(df)
        else:
            break
    
def exp_imp_sql():
    df=pd.read_csv('E:\yukti\csv files\project2.csv',sep='\t')
    df1=pd.DataFrame(df)
    engine=create_engine('mysql+pymysql://root:admin@localhost/Project')
    conn=engine.connect()
    df1.to_sql('energy',conn,index=False,if_exists='replace')
    mycon=sql.connect(host="localhost",user="root",passwd="admin",database="Project")
    if mycon.is_connected():
        print("Table created in mysql")
        df2=pd.read_sql("select * from energy;",mycon)
    else:
        print("not connected")


def manipulation():
    df=pd.read_csv('E:\yukti\csv files\project2.csv',sep='\t')
    df3=pd.DataFrame()
    print(df)
    while True:
        print('Manipulation Menu')
        print('_'*70)
        print('1. Add a Row')
        print('2. Delete a Row')
        print('3. Delete a Column')
        print('4. Go back to the main menu')
        ch= int(input('Enter your choice:'))
        if ch==1:
            col=df.columns
            print(col)
            j=0
            lst1=[]
            lst1=eval(input('Enter values in the sequences of columns:(for example:["India","IND",\n2020,15733.38,5689423,98.4]):'))
            print(lst1)
            s1=pd.Series(lst1,index=df.columns)
            df3=df.append(s1,ignore_index=True)
            print('New row inserted')
            print(df3)
        elif ch==2:
            y=input('Enter the year for deletion(1990 to 2016):')
            country=input('enter the country for deletion from(Argentina,China,India,Japan,Mexico,\nSouth Africa,South Korea,Spain,Turkey,United States),for example-India:')
            df4=df[((df.Entity!=country)|(df.Year!=y))]
            print(df4)
        elif ch==3:
            print(df.columns)
            col=input('Enter the column from above for deletion: for example Number of people\n without access to electricity :')
            choice=input('Do you really want to delete the column(y/n)??')
            if choice=='y' or choice=='Y':
                del df[col]
                print('Column -', col,' deleted successfully!!!')
                df4=pd.DataFrame()
                df4=df
                print(df4)
        else:
            break

    
def pie1():
    df2=df1.pivot(index='Year',columns='Entity',values='Access to electricity (% of population)')
    a=int(input('enter  year from 1990 to 2016:'))
    print(df2.loc[a])
    plt.pie(df2.loc[a],labels=['Argentina','China','India','Japan','Mexico','South Africa','South Korea','Spain','Turkey','USA'],autopct='%1.1f%%')
    b='Access to electricity in '
    plt.title(b+str(a))
    plt.show()

def line_chart1():
    df2=df1.pivot(index='Year',columns='Entity',values='Number of people without access to electricity')
    df2.plot()
    plt.title('Number of people without access to electricity')
    plt.xlabel('YEAR')
    plt.ylabel('Number of People')
    plt.show()

def line_chart2():
    a=pd.read_csv('E:\yukti\csv files\comparision.csv',sep='\t')
    df2=pd.DataFrame(a)
    df3=df2.pivot(index='Year',columns='Entity',values='Number of people without access to electricity')
    df4=df2.pivot(index='Year',columns='Entity',values='Number of people with access to electricity')
    b=input('Enter country name Argentina,China,India,Japan,Mexico,South Africa,\nSouth Korea,Spain,Turkey,United States ( for example :India):')
    plt.plot(df3[b], label='Number of people without access to electricity')
    plt.plot(df4[b], label='Number of people with access to electricity')
    plt.title('Comparision of Number of people with and without access to electricity in '+str(b))
    plt.xlabel('Year')
    plt.ylabel('Number of people')
    plt.legend()
    plt.show()

def line_chart3():
    df2=df1.pivot(index='Year',columns='Entity',values='Energy consumption per capita (kWh)')
    a=input('Enter country name Argentina,China,India,Japan,Mexico,South Africa,\nSouth Korea,Spain,Turkey,United States ( for example :India):')
    plt.plot(df2[a],label=a)
    plt.title('Energy consumption per capita (kWh)')
    plt.xlabel('Year')
    plt.ylabel('Energy consumption in kWh')
    plt.legend()
    plt.show()
Menuset()
                
                
        
            
        
    
            
        
