# Import Libraries
import pandas as pd
import itertools
#import csv

# Split function
def split_string(string):
  data = string.split(",")
  return data

# lower string
def lower_string(string):
  data = list((map(lambda x: x.lower(), string)))  
  return data

# Ranking function
def ranking_fun(resume_list,jd_list):
  comparisons = [a == b for (a, b) in itertools.product(resume_list,jd_list)]
  counter = comparisons.count(True)
  percentage = (counter/len(jd_list))*100
  return percentage

def main(resume_df,jd_df):
    # Skill
    score = []


    # For Job description
    for i in jd_df["SKILLS"]:
      jd_list = split_string(i)
      jd_list = lower_string(jd_list)

    # For resume
    for i in resume_df['SKILLS']:
      resume_list = split_string(i)
      resume_list = lower_string(resume_list)
      percentage = ranking_fun(resume_list,jd_list)
      score.append(percentage)
    resume_df = resume_df.assign(score=score)

    # Experience

    # For job description
    jd_experience = jd_df.EXPERIENCE.str.split('+').str[0]
    jd_df = jd_df.assign(EXPERIENCE_temp = jd_experience)
    jd_df.EXPERIENCE_temp = jd_df.EXPERIENCE_temp.astype(float)

    # For resume 
    experience = resume_df.EXPERIENCE.str.split('+').str[0]
    resume_df = resume_df.assign(EXPERIENCE_temp = experience)
    resume_df.EXPERIENCE_temp = resume_df.EXPERIENCE_temp.astype(float)
    resume_df = resume_df[resume_df['EXPERIENCE_temp'] >= float(jd_experience[0])]

    # Sorting by experience
    resume_df = resume_df.sort_values(by='EXPERIENCE_temp', ascending=False)

    # Remove Temp column
    jd_df.pop('EXPERIENCE_temp')
    resume_df.pop('EXPERIENCE_temp')

    print(resume_df)

    # sorting by skill score
    resume_df = resume_df.sort_values(by = 'score', ascending=False)
    return resume_df