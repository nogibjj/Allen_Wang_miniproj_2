import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport


def read_dataset(file_path):
    df = None
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    return df


def generate_summary_statistics(df):
    summary_stats = df.describe()
    mean_values = df.mean(numeric_only=True)
    median_values = df.median(numeric_only=True)
    std_dev = df.std(numeric_only=True)
    # print(mean_values)
    return summary_stats, mean_values, median_values, std_dev


def create_save_visualization(df, column_name, save_filename=None):
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column_name], kde=True, color='skyblue', bins=30)
    plt.title(f'{column_name} Distribution', fontsize=16)
    plt.xlabel(column_name, fontsize=12)
    plt.ylabel('Frequency', fontsize=12)

    if save_filename:
        plt.savefig(save_filename, bbox_inches='tight')
    plt.show()


def generate_html_report(df):
    profile = ProfileReport(
        df, title='Titanic Profiling Report', explorative=True)
    profile.to_file('Titanic Profiling Report.html')


file_path = 'titanic.csv'
df = read_dataset(file_path)
summary_stats, mean_values, median_values, std_dev = generate_summary_statistics(
    df)

print("Summary Statistics:", summary_stats)
print("---------")
print("Mean Values:")
print(mean_values)
print("---------")
print("Median Values:")
print(median_values)
print("---------")
print("Standard Deviation")
print(std_dev)


create_save_visualization(df, 'Age', save_filename='age_distribution.png')
create_save_visualization(
    df, 'Survived', save_filename='survived_distribution.png')
create_save_visualization(
    df, 'Pclass', save_filename='pclass_distribution.png')
create_save_visualization(df, 'Sex', save_filename='sex_distribution.png')
create_save_visualization(df, 'Siblings/Spouses Aboard',
                          save_filename='Siblings_Spouses_Aboard_distribution.png')
create_save_visualization(df, 'Parents/Children Aboard',
                          save_filename='Parents_Children_Aboard_distribution.png')
create_save_visualization(df, 'Fare', save_filename='fare_distribution.png')


generate_html_report(df)
