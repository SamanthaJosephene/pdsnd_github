import time
import pandas as pd
import numpy as np 
import datetime 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
            city = input("Please choose a city: Chicago, New York City, or Washington:\n").lower()
            if city not in CITY_DATA:
                print('Invalid City')
                
            else:     
                break

    # get user input for month (all, january, february, ... , december)
    months = ('january', 'february', 'march', 'april', 'may')
    while True:
            month = input('Please input month:\n').lower()        
            if month != 'all' and month not in months:
                 print('Select the Correct Month')  
            else:
                break

    # get user input for day of week (all, monday, tuesday, ... sunday)    
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    while True:
            day = input('Please select a day of the week:\n ').lower()        
            if day != 'all' and day not in days:
                print('Wrong Day')
                
            else:
                break
    return city,month,day
    print('-'*40)

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data file into a data frame
    df = pd.read_csv(CITY_DATA[city])
    # extract year, month and day of week from start time to create new columns
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['year']= df['Start Time'].dt.year
    df['month']= df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applcale
    if month != 'all':
        months = ['january', 'february', 'march', 'april','june', 'may', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month)+1
        df=df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('The most common month of travel: ', common_month)
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week of travel: ',common_day_of_week)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour of travel: ',common_hour)
    print("\nThis took %s seconds." %round((time.time() - start_time),3))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('{} is the commonly used start startion.'.format(common_start))
# TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('{} is the commonly used start startion.'.format(common_end))
# TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']
    common_combination = df ['combination'].mode()[0]
    print('{} are the common combination.'.format(common_combination))
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
# TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal travel time: %s.'%str(datetime.timedelta(seconds = int(total_travel_time))))
# TO DO: display mean travel time 
    average_travel_time = df['Trip Duration'].mean()
    print('\nThe average travel time: %s.'%str(datetime.timedelta(seconds = average_travel_time)))
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
# TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('Number of users by type:', count_user_types)   
# TO DO: Display counts of gender
    try:
        count_gender = df['Gender'].value_counts()
        print('Count of gender: ', count_gender)
    except KeyError:
        print('No data available for the selected city')
# TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        earliest_year = int(earliest_birth_year)
        print('The earliest birth by year: ', earliest_year)
        most_recent_year = df['Birth Year'].max()
        recent_year = int(most_recent_year)
        print('The most recent birth by year: ', recent_year)
        most_common_birth = df['Birth Year'].mode()[0]
        common_birth = int(most_common_birth)
        print('The most common birth by year: ', common_birth)
        
        
    except KeyError:
        print('Not available data')
        print("\nThis took %s seconds." % round((time.time() - start_time),3))
        print('-'*40)     
        
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data.lower() == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input('Do you wish to continue?:Enter yes or no.\n' ).lower()               
        if view_display.lower() != 'yes':
            break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you love to restart? Enter Yes or No.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()
