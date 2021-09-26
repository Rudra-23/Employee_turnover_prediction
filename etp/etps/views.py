from django.shortcuts import render
import pickle

model  =pickle.load(open('./ETP.pkl','rb'))

# Create your views here.
def index(requests):
    ans = 2
    context ={
            'ans':ans,
            'flag':False
        }
    if requests.method =='POST':
        Satisfaction_level = requests.POST['Satisfaction_level']
        Time_spent_in_company =requests.POST['Time_spent_in_company']
        Last_evaluation = requests.POST['Last_evaluation']
        Work_accident = requests.POST['Work_accident']
        Salary_type =requests.POST['Salary_type']
        if Salary_type == 'High':
            Salary_type_High = 1
            Salary_type_Low = 0
        else:
            Salary_type_High = 0
            Salary_type_Low = 1
        
        Department_type =requests.POST['Department_type']
        if Department_type == 'RandD':
            Department_type_RandD = 1
            Department_type_Hr = 0
            Department_type_Management = 0
        elif Department_type == 'Hr':
            Department_type_RandD = 0
            Department_type_Hr = 1
            Department_type_Management = 0
        else:
            Department_type_RandD = 0
            Department_type_Hr = 0
            Department_type_Management = 1

        Promotion =requests.POST['Promotion']

        final_arr = []
        final_arr += [Satisfaction_level, Last_evaluation, Time_spent_in_company, Work_accident, Promotion]
        final_arr += [Department_type_RandD, Department_type_Hr, Department_type_Management]
        final_arr += [Salary_type_High, Salary_type_Low]

        ans =model.predict([final_arr])
        print(ans)
        context ={
            'ans':round(float(ans),2),
            'flag':True
        }
        return render(requests,'index.html',context=context)

    return render(requests,'index.html',context=context)