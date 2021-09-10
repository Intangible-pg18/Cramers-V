#cramer's v
import numpy as np
import pandas as pd
import scipy.stats as ss

def cramers_v(x,y):
    contingency_table = pd.crosstab(df[x], df[y])
    if contingency_table.shape[0]==2:
        correct=False
    else:
        correct=True
    chi2 = ss.chi2_contingency(contingency_table)[0]
    n = contingency_table.sum().sum()
    phi2_coff = chi2/n
    r,c = contingency_table.shape
    unbiased_phi2_coff = max(0, (phi2_coff - (((c-1)*(r-1))/(n-1))))    
    r_corr = r - (((r-1)**2)/(n-1))
    c_corr = c - (((c-1)**2)/(n-1))
    return np.sqrt(unbiased_phi2_coff / min((c_corr-1), (r_corr-1)))

categorical_columns = list(df.select_dtypes('category').columns)
categorical_correlation_df = pd.DataFrame(index = categorical_columns, columns = categorical_columns)
for i in categorical_columns:
    for j in categorical_columns:
        categorical_correlation_df.loc[i, j] = cramers_v(i,j)
