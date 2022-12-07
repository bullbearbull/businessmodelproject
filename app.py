import streamlit as st
import pandas as pd
import numpy as np
from time import localtime
from time import strftime
from pandas.core.reshape.tile import to_datetime
import shelve



# def make_ind_data() :
#   i_name = st.text_input('이름을 입력해주세요 :')
#   i_birth = st.number_input('생년월일을 입력해주세요 :')
#   sex_cat = ['여성', '남성']
#   i_sex = st.multiselect('성별을 선택해주세요 :', sex_cat)
#   dis_cat = ['당뇨', '고혈압', '관절염', '폐질환', '위염', '치매', '간질환', '소화기질환']
#   i_disease = st.multiselect('질병을 입력해주세요 :', dis_cat)
#   i_data = pd.DataFrame({'name':[i_name], 'birth':[i_birth], 'sex':[i_sex], 'disease':[i_disease]})
#   i_data.set_index('name', inplace=True)
#   st.write(i_data)
#   return st.write(i_data, i_name, i_birth)

def main() :

  st.title('나만의 요리사')
  st.subheader('맞춤형 식단과 체계적인 관리 시스템을 제공합니다')


  i_name = st.text_input('이름을 입력해주세요 :')
  i_birth = st.number_input('생년월일을 입력해주세요 :')
  sex_cat = ['여성', '남성']
  i_sex = st.multiselect('성별을 선택해주세요 :', sex_cat)
  dis_cat = ['당뇨', '고혈압', '관절염', '폐질환', '위염', '치매', '간질환', '소화기질환']
  i_disease = st.multiselect('질병을 입력해주세요 :', dis_cat)
  i_data = pd.DataFrame({'name': [i_name], 'birth': [i_birth], 'sex': [i_sex], 'disease': [i_disease]})
  i_data.set_index('name', inplace=True)
  st.write(i_data)
  i_data.to_csv(f'{i_name}_{i_birth}_.csv')


main()