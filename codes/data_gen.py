import pandas as pd 






def main() : 
    print("Creating the data sets....")

    features_columns = ['CGPA', 'Interactive', 'PracticalKnowledge', 'CommSkills', 'Label']
    data_df = [['>=9', 'Yes', 'Very good', 'Good', 'Yes'], 
                ['>=8', 'No', 'Good', 'Moderate', 'Yes'],
                ['>=9', 'No', 'Average', 'Poor', 'No'],
                ['<8', 'No', 'Average', 'Poor', 'No'], 
                ['>=8', 'Yes', 'Good', 'Moderate', 'Yes'],
                ['>=9', 'Yes', 'Good', 'Moderate', 'Yes'],
                ['<8', 'Yes', 'Good', 'Poor', 'No'],
                ['>=9', 'No', 'Very good', 'Good', 'Yes'],
                ['>=8', 'Yes', 'Very good', 'Good', 'Yes'],
                ['>=8', 'Yes', 'Average', 'Good', 'Yes']]

    job_data = pd.DataFrame(data_df, columns=features_columns)
    job_data

    job_data.to_csv('../data/jobs.csv', index=False)

if __name__ == '__main__' : 
    main()