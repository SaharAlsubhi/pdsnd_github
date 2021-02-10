import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
MONTH_DATA = {'january': 1, 'february': 2, 'march': 3,
              'april': 4, 'may': 5, 'june': 6, 'all': 7}
DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please enter the name of city:").lower()
        if city not in CITY_DATA:
            print("\nInvalid answer\n")
            continue
        else:
            break
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter the name of month:").lower()
        if month not in MONTH_DATA:
            print("\nInvalid answer\n")
            continue
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter the name of day:").lower()
        if day not in DAY_LIST:
            print("\nInvalid answer\n")
            continue
        else:
            break
    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    #df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('The most common month:', common_month)

    # display the most common day of week

   # df['day_of_week'] = df['Start Time'].dt.week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of week:', common_day)

    # display the most common start hour

   # df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most common start station:', common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most common end station:', common_end)

    # display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station']+'to'+df['End Station']
    common_combination = df['Combination'].mode()[0]
    print('The most common frequent combination:', common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print('The total travel time', total_travel)

    # display mean travel time
    average_travel = df['Trip Duration'].mean()
    print('The mean travel time', average_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(gender)
    except:
        print("\nThere is no Gender column in this file.")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        print(earliest)
        recent = df['Birth Year'].max()
        print(recent)
        common_birth = df['Birth Year'].mode()[0]
        print(common_birth)
    except:
        print("There are no birth year details in this file.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        print(df.iloc[0:5])
        start_loc += 5
        view_display = input("Do you wish to continue? Enter yes or no:").lower()
        if view_display != 'yes':
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
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
