import pandas as pd
import numpy as np
import dask.dataframe as dd
import matplotlib.pyplot as plt
import streamlit as st

kaz_2014 = pd.read_excel('https://github.com/drimuso/strlit/raw/main/qqw/kaz_2014.xlsx')
kaz_2015 = pd.read_excel('https://github.com/drimuso/strlit/raw/main/qqw/kaz_2014.xlsx')
kaz_2016 = pd.read_excel('https://github.com/drimuso/strlit/raw/main/qqw/kaz_2014.xlsx')
kaz_2017 = pd.read_excel('https://github.com/drimuso/strlit/raw/main/qqw/kaz_2014.xlsx')
krg_2014 = pd.read_excel('https://github.com/drimuso/strlit/raw/main/qqw/kaz_2014.xlsx')
krg_2015 = pd.read_excel('https://github.com/drimuso/strlit/raw/main/qqw/kaz_2014.xlsx')
krg_2016 = pd.read_excel('https://github.com/drimuso/strlit/raw/main/qqw/kaz_2014.xlsx')
krg_2017 = pd.read_excel('https://github.com/drimuso/strlit/raw/main/qqw/kaz_2014.xlsx')
uzb_2014 = pd.read_excel('https://github.com/drimuso/strlit/raw/main/qqw/kaz_2014.xlsx')
uzb_2015 = pd.read_excel('https://github.com/drimuso/strlit/raw/main/qqw/kaz_2014.xlsx')
uzb_2016 = pd.read_excel('https://github.com/drimuso/strlit/raw/main/qqw/kaz_2014.xlsx')
uzb_2017 = pd.read_excel('https://github.com/drimuso/strlit/raw/main/qqw/kaz_2014.xlsx')
tadj_2014 = pd.read_excel('https://github.com/drimuso/strlit/raw/main/qqw/kaz_2014.xlsx')
tadj_2015 = pd.read_excel('https://github.com/drimuso/strlit/raw/main/qqw/kaz_2014.xlsx')
tadj_2016 = pd.read_excel('https://github.com/drimuso/strlit/raw/main/qqw/kaz_2014.xlsx')
tadj_2017 = pd.read_excel('https://github.com/drimuso/strlit/raw/main/qqw/kaz_2014.xlsx')
 

pd_df_kz_2014 = kaz_2014
pd_df_kz_2015 = kaz_2015
pd_df_kz_2016 = kaz_2016
pd_df_kz_2017 = kaz_2017

pd_df_tajk_2014 = tadj_2014
pd_df_tajk_2015 = tadj_2015
pd_df_tajk_2016 = tadj_2016
pd_df_tajk_2017 = tadj_2017

pd_df_kgz_2014 = krg_2014
pd_df_kgz_2015 = krg_2015
pd_df_kgz_2016 = krg_2016
pd_df_kgz_2017 = krg_2017

pd_df_uzb_2014 = uzb_2014
pd_df_uzb_2015 = uzb_2015
pd_df_uzb_2016 = uzb_2016
pd_df_uzb_2017 = uzb_2017


numeric_columns_kz_2014 = pd_df_kz_2014.select_dtypes(include=[np.number]).columns
pd_df_kz_2014[numeric_columns_kz_2014] = pd_df_kz_2014[numeric_columns_kz_2014].fillna(0)

numeric_columns_tajk_2014 = pd_df_tajk_2014.select_dtypes(include=[np.number]).columns
pd_df_tajk_2014[numeric_columns_tajk_2014] = pd_df_tajk_2014[numeric_columns_tajk_2014].fillna(0)

numeric_columns_kgz_2014 = pd_df_kgz_2014.select_dtypes(include=[np.number]).columns
pd_df_kgz_2014[numeric_columns_kgz_2014] = pd_df_kgz_2014[numeric_columns_kgz_2014].fillna(0)

numeric_columns_uzb_2014 = pd_df_uzb_2014.select_dtypes(include=[np.number]).columns
pd_df_uzb_2014[numeric_columns_uzb_2014] = pd_df_uzb_2014[numeric_columns_uzb_2014].fillna(0)



numeric_columns_kz_2015 = pd_df_kz_2015.select_dtypes(include=[np.number]).columns
pd_df_kz_2015[numeric_columns_kz_2015] = pd_df_kz_2015[numeric_columns_kz_2015].fillna(0)

numeric_columns_tajk_2015 = pd_df_tajk_2015.select_dtypes(include=[np.number]).columns
pd_df_tajk_2015[numeric_columns_tajk_2015] = pd_df_tajk_2015[numeric_columns_tajk_2015].fillna(0)

numeric_columns_kgz_2015 = pd_df_kgz_2015.select_dtypes(include=[np.number]).columns
pd_df_kgz_2015[numeric_columns_kgz_2015] = pd_df_kgz_2015[numeric_columns_kgz_2015].fillna(0)

numeric_columns_uzb_2015 = pd_df_uzb_2015.select_dtypes(include=[np.number]).columns
pd_df_uzb_2015[numeric_columns_uzb_2015] = pd_df_uzb_2015[numeric_columns_uzb_2015].fillna(0)




numeric_columns_kz_2016 = pd_df_kz_2016.select_dtypes(include=[np.number]).columns
pd_df_kz_2016[numeric_columns_kz_2016] = pd_df_kz_2016[numeric_columns_kz_2016].fillna(0)

numeric_columns_tajk_2016 = pd_df_tajk_2016.select_dtypes(include=[np.number]).columns
pd_df_tajk_2016[numeric_columns_tajk_2016] = pd_df_tajk_2016[numeric_columns_tajk_2016].fillna(0)

numeric_columns_kgz_2016 = pd_df_kgz_2016.select_dtypes(include=[np.number]).columns
pd_df_kgz_2016[numeric_columns_kgz_2016] = pd_df_kgz_2016[numeric_columns_kgz_2016].fillna(0)

numeric_columns_uzb_2016 = pd_df_uzb_2016.select_dtypes(include=[np.number]).columns
pd_df_uzb_2016[numeric_columns_uzb_2016] = pd_df_uzb_2016[numeric_columns_uzb_2016].fillna(0)





numeric_columns_kz_2017 = pd_df_kz_2017.select_dtypes(include=[np.number]).columns
pd_df_kz_2017[numeric_columns_kz_2017] = pd_df_kz_2017[numeric_columns_kz_2017].fillna(0)

numeric_columns_tajk_2017 = pd_df_tajk_2017.select_dtypes(include=[np.number]).columns
pd_df_tajk_2017[numeric_columns_tajk_2017] = pd_df_tajk_2017[numeric_columns_tajk_2017].fillna(0)

numeric_columns_kgz_2017 = pd_df_kgz_2017.select_dtypes(include=[np.number]).columns
pd_df_kgz_2017[numeric_columns_kgz_2017] = pd_df_kgz_2017[numeric_columns_kgz_2017].fillna(0)

numeric_columns_uzb_2017 = pd_df_uzb_2017.select_dtypes(include=[np.number]).columns
pd_df_uzb_2017[numeric_columns_uzb_2017] = pd_df_uzb_2017[numeric_columns_uzb_2017].fillna(0)




dask_df_kz_2014 = dd.from_pandas(pd_df_kz_2014, npartitions=1)
dask_df_kz_2015 = dd.from_pandas(pd_df_kz_2015, npartitions=1)
dask_df_kz_2016 = dd.from_pandas(pd_df_kz_2016, npartitions=1)
dask_df_kz_2017 = dd.from_pandas(pd_df_kz_2017, npartitions=1)

dask_df_tajk_2014 = dd.from_pandas(pd_df_tajk_2014, npartitions=1)
dask_df_tajk_2015 = dd.from_pandas(pd_df_tajk_2015, npartitions=1)
dask_df_tajk_2016 = dd.from_pandas(pd_df_tajk_2016, npartitions=1)
dask_df_tajk_2017 = dd.from_pandas(pd_df_tajk_2017, npartitions=1)

dask_df_kgz_2014 = dd.from_pandas(pd_df_kgz_2014, npartitions=1)
dask_df_kgz_2015 = dd.from_pandas(pd_df_kgz_2015, npartitions=1)
dask_df_kgz_2016 = dd.from_pandas(pd_df_kgz_2016, npartitions=1)
dask_df_kgz_2017 = dd.from_pandas(pd_df_kgz_2017, npartitions=1)

dask_df_uzb_2014 = dd.from_pandas(pd_df_uzb_2014, npartitions=1)
dask_df_uzb_2015 = dd.from_pandas(pd_df_uzb_2015, npartitions=1)
dask_df_uzb_2016 = dd.from_pandas(pd_df_uzb_2016, npartitions=1)
dask_df_uzb_2017 = dd.from_pandas(pd_df_uzb_2017, npartitions=1)




Prob_Mod_Sev_kz_2014 = (dask_df_kz_2014['Prob_Mod_Sev'] * dask_df_kz_2014['wt']).sum() / dask_df_kz_2014['wt'].sum()
Prob_Mod_Sev_kz_2015 = (dask_df_kz_2015['Prob_Mod_Sev'] * dask_df_kz_2015['wt']).sum() / dask_df_kz_2015['wt'].sum()
Prob_Mod_Sev_kz_2016 = (dask_df_kz_2016['Prob_Mod_Sev'] * dask_df_kz_2016['wt']).sum() / dask_df_kz_2016['wt'].sum()
Prob_Mod_Sev_kz_2017 = (dask_df_kz_2017['Prob_Mod_Sev'] * dask_df_kz_2017['wt']).sum() / dask_df_kz_2017['wt'].sum()

Prob_Mod_Sev_tajk_2014 = (dask_df_tajk_2014['Prob_Mod_Sev'] * dask_df_tajk_2014['wt']).sum() / dask_df_tajk_2014['wt'].sum()
Prob_Mod_Sev_tajk_2015 = (dask_df_tajk_2015['Prob_Mod_Sev'] * dask_df_tajk_2015['wt']).sum() / dask_df_tajk_2015['wt'].sum()
Prob_Mod_Sev_tajk_2016 = (dask_df_tajk_2016['Prob_Mod_Sev'] * dask_df_tajk_2016['wt']).sum() / dask_df_tajk_2016['wt'].sum()
Prob_Mod_Sev_tajk_2017 = (dask_df_tajk_2017['Prob_Mod_Sev'] * dask_df_tajk_2017['wt']).sum() / dask_df_tajk_2017['wt'].sum()

Prob_Mod_Sev_kgz_2014 = (dask_df_kgz_2014['Prob_Mod_Sev'] * dask_df_kgz_2014['wt']).sum() / dask_df_kgz_2014['wt'].sum()
Prob_Mod_Sev_kgz_2015 = (dask_df_kgz_2015['Prob_Mod_Sev'] * dask_df_kgz_2015['wt']).sum() / dask_df_kgz_2015['wt'].sum()
Prob_Mod_Sev_kgz_2016 = (dask_df_kgz_2016['Prob_Mod_Sev'] * dask_df_kgz_2016['wt']).sum() / dask_df_kgz_2016['wt'].sum()
Prob_Mod_Sev_kgz_2017 = (dask_df_kgz_2017['Prob_Mod_Sev'] * dask_df_kgz_2017['wt']).sum() / dask_df_kgz_2017['wt'].sum()

Prob_Mod_Sev_uzb_2014 = (dask_df_uzb_2014['Prob_Mod_Sev'] * dask_df_uzb_2014['wt']).sum() / dask_df_uzb_2014['wt'].sum()
Prob_Mod_Sev_uzb_2015 = (dask_df_uzb_2015['Prob_Mod_Sev'] * dask_df_uzb_2015['wt']).sum() / dask_df_uzb_2015['wt'].sum()
Prob_Mod_Sev_uzb_2016 = (dask_df_uzb_2016['Prob_Mod_Sev'] * dask_df_uzb_2016['wt']).sum() / dask_df_uzb_2016['wt'].sum()
Prob_Mod_Sev_uzb_2017 = (dask_df_uzb_2017['Prob_Mod_Sev'] * dask_df_uzb_2017['wt']).sum() / dask_df_uzb_2017['wt'].sum()


a, b, c, d = Prob_Mod_Sev_kz_2014.compute(), Prob_Mod_Sev_tajk_2014.compute(), Prob_Mod_Sev_kgz_2014.compute(), Prob_Mod_Sev_uzb_2014.compute()

a_1, b_1, c_1, d_1 = Prob_Mod_Sev_kz_2015.compute(), Prob_Mod_Sev_tajk_2015.compute(), Prob_Mod_Sev_kgz_2015.compute(), Prob_Mod_Sev_uzb_2015.compute()


a_2, b_2, c_2, d_2 = Prob_Mod_Sev_kz_2016.compute(), Prob_Mod_Sev_tajk_2016.compute(), Prob_Mod_Sev_kgz_2016.compute(), Prob_Mod_Sev_uzb_2016.compute()

a_3, b_3, c_3, d_3 = Prob_Mod_Sev_kz_2017.compute(), Prob_Mod_Sev_tajk_2017.compute(), Prob_Mod_Sev_kgz_2017.compute(), Prob_Mod_Sev_uzb_2017.compute()


years = range(2014, 2018)



Prob_Mod_Sev_kz_values = [a, a_1, a_2, a_3]



Prob_Mod_Sev_tjk_values = [b, b_1, b_2, b_3]


Prob_Mod_Sev_kgz_values = [c, c_1, c_2, c_3]


Prob_Mod_Sev_uzb_values = [d, d_1, d_2, d_3]



#plt.figure(figsize=(10, 6))
#plt.title('Казахстан')
#plt.plot(years, Prob_Mod_Sev_kz_values, marker='o', linestyle='-')
#plt.xticks(years)
#plt.yticks(np.arange(0, 0.31, 0.05))
#plt.grid(True)
#plt.show()



#plt.figure(figsize=(10, 6))
#plt.plot(years, Prob_Mod_Sev_kz_values, marker='o', linestyle='-', label='Казахстан')
#plt.plot(years, Prob_Mod_Sev_uzb_values, marker='o', linestyle='-', label='Узбекистан')
#plt.plot(years, Prob_Mod_Sev_kgz_values, marker='o', linestyle='-', label='Кыргызстан')
#plt.plot(years, Prob_Mod_Sev_tjk_values, marker='o', linestyle='-', label='Таджикистан')
#plt.title('Центральная Азия')
#plt.xticks(years)
#plt.yticks(np.arange(0, 0.3, 0.05))
#plt.legend()
#plt.grid(True)
#plt.show()


def plot_empty_chart():
    plt.figure(figsize=(10, 6))
    plt.title('Центральная Азия')
    plt.xticks(years)
    plt.yticks(np.arange(0, 0.3, 0.05))
    plt.grid(True)
    return plt


years = range(2014, 2018)

data = {
    'Казахстан': Prob_Mod_Sev_kz_values,
    'Узбекистан': Prob_Mod_Sev_uzb_values,
    'Кыргызстан': Prob_Mod_Sev_kgz_values,
    'Таджикистан': Prob_Mod_Sev_tjk_values
}

colors = {
    'Казахстан': 'blue',
    'Узбекистан': 'green',
    'Кыргызстан': 'red',
    'Таджикистан': 'purple'
}


selected_country = st.radio('Выберите страну', list(data.keys()))
st.write("Выбранная страна:", f"<span style='font-family: Arial; font-size: 16px;'>{selected_country}</span>", unsafe_allow_html=True)


fig = plot_empty_chart()


plt.plot(years, data[selected_country], marker='o', linestyle='-', color=colors[selected_country], label=selected_country)



st.pyplot(fig)







