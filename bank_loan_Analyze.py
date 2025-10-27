import numpy as np

# Total number of customers
n_customers = 1000

# Random data generation
np.random.seed(42)
income = np.random.randint (20000, 150000, n_customers)  # yearly income
loan_amount = np.random.randint(5000, 50000, n_customers) # loan requested
credit_score = np.random.randint(300, 850, n_customers)  # credit score (300, 850)

# Loan approval logic: approve if credit_score > 650 and income > 40000
loan_status = np.where((credit_score > 650) & (income > 40000), 1, 0)  # 1=approved, 0=rejected


# --- ANALYSIS ---

print("📊 Loan Data Analysis (NumPy Only)")
print ('-'* 40)

# average income
print ('Average income is:', np.mean(income))

# Approval rate
approvel_rate = np.mean(loan_status)* 100
print ('Loan Approvel Rate:', round(approvel_rate, 2), '%')

# Average credit score for approved vs rejected
avg_approved_score = np.mean(credit_score[loan_status==1])
avg_rejected_score = np.mean(credit_score[loan_status==0])
print('Average crerit score (Approved):', round(avg_approved_score, 2))
print ('Average credit score (Rejected):', round(avg_rejected_score, 2))

# Customers with high income (>100k) approval rate
hight_income = loan_status[income>100000]
print ('Approvel Rate for High_income customers:', round(np.mean(hight_income)*100, 2), '%')


# Correlation (basic idea)
correlation = np.corrcoef(income, credit_score)[0, 1]
print("Correlation between Income and Credit Score:", round(correlation, 3))