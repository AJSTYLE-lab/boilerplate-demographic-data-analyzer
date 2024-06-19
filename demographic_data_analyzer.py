import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    
    # Calculate race count
    race_count = df['race'].value_counts()
    
    # Calculate average age of men
    average_age_by_sex = df.groupby('sex')['age'].mean()
    average_age_men = average_age_by_sex['Male']

    # Calculate percentage of people who have a Bachelor's degree
    total_occupation = len(df)
    bachelor_degree = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = (bachelor_degree / total_occupation) * 100

    # Calculate percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) who earn >50K
    education_categories = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(education_categories)]
    lower_education = df[~df['education'].isin(education_categories)]

    higher_education_rich = (len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education)) * 100
    lower_education_rich = (len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education)) * 100

    # Calculate minimum number of hours a person works per week
    min_work_hours = df['hours-per-week'].min()

    # Calculate percentage of the people who work the minimum number of hours per week and have a salary of >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    total_min_workers = len(num_min_workers)
    rich_min_hours_workers = len(num_min_workers[num_min_workers['salary'] == '>50K'])
    rich_percentage = (rich_min_hours_workers / total_min_workers) * 100

    # Identify the country with the highest percentage of people that earn >50K
    high_salary = df[df['salary'] == '>50K']
    percentage_high_salary = (high_salary['native-country'].value_counts() / df['native-country'].value_counts()) * 100
    highest_earning_country = percentage_high_salary.idxmax()
    highest_earning_country_percentage = percentage_high_salary.max()

    # Identify the most popular occupation for those who earn >50K in India
    high_income_india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = high_income_india['occupation'].mode()[0]

    # Print results
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelor's degrees: {percentage_bachelors:.2f}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich:.2f}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich:.2f}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage:.2f}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage:.2f}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
