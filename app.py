import pandas as pd,pickle as pk, streamlit as st

with open ('model.pkl','rb') as file:

 model=pk.load(file)

st.title('credit card authenticity checker')

Time = st.number_input('Enter the Time')

V1 = st.number_input('Enter the V1')

V2 = st.number_input('Enter the V2')

V3 = st.number_input('Enter the V3')

V4 = st.number_input('Enter the V4')

V5 = st.number_input('Enter the V5')

V6 = st.number_input('Enter the V6')

V7 = st.number_input('Enter the V7')

V8 = st.number_input('Enter the V8')

V9 = st.number_input('Enter the V9')

V10 = st.number_input('Enter the V10')

V11 = st.number_input('Enter the V11')

V12 = st.number_input('Enter the V12')

V13 = st.number_input('Enter the V13')

V14 = st.number_input('Enter the V14')

V15 = st.number_input('Enter the V15')

V16 = st.number_input('Enter the V16')

V17 = st.number_input('Enter the V17')

V18 = st.number_input('Enter the V18')

V19 = st.number_input('Enter the V19')

V20 = st.number_input('Enter the V20')

V21 = st.number_input('Enter the V21')

V22 = st.number_input('Enter the V22')

V23 = st.number_input('Enter the V23')

V24 = st.number_input('Enter the V24')

V25 = st.number_input('Enter the V25')

V26 = st.number_input('Enter the V26')

V27 = st.number_input('Enter the V27')

V28 = st.number_input('Enter the V28')

Amount= st.number_input('Enter the Amount')

ip_data=pd.DataFrame([[Time	,V1	,V2	,V3	,V4	,V5	,V6	,V7	,V8	,V9	,V10	,V11	,V12	,V13	,V14	,V15	,V16	,V17	,V18	,V19	,V20	,V21	,V22	,V23	,V24	,V25	,V26	,V27	,V28	,Amount]],columns=['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
       'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
       'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount'])



if st.button('Check :'):

  prediction = model.predict(ip_data)[0]

  if prediction==1:

   st.success('Valid Credit Score')

  else:

   st.success('Invalid Credit score')