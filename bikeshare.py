import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities=['chicago', 'new york city', 'washington']
months=['january', 'february', 'march', 'april', 'may', 'june','all']
days= ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday','all' ]
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

            city = input("Would you like to see data for Chicago, New york city or Washington\n-> ").lower()
            if city not in cities:
                print("Please enter only one of these cities (Chicago/ New york/ Washington)")
                continue
            else:
                break

# get user input for month (all, january, february, ... , june)
    while True:
            month = input("Which month?january, february, ... , june,All\n->").lower()
            if month not in months:
                print("Please enter a valid month ('January', 'February', 'March', 'April', 'May', 'June','All')")
                continue
            else:
                break
        # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
            day = input("Which day?monday, tuesday, ... sunday,all\n->").lower()
            if day not in days:
                print("Please enter a valid day ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday','all')")
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
    df=pd.read_csv(CITY_DATA[city])
    print('You chose a city: {}, month: {} and day: {} '.format(city, month, day))
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['hour']=df['Start Time'].dt.hour
    df['month']=df['Start Time'].dt.month
    df['days']=df['Start Time'].dt.day_name()

    if month != 'all' :
        month = months.index(month)+1
        df = df[df['month'] == month]
    if day != 'all' :
        df = df[df['days'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    most_common_month=df['month'].mode()[0]
    print('the most common month is: {}'.format(most_common_month))

    # display the most common day of week

    most_common_day_of_week=df['days'].mode()[0]
    print("most common day of week is:",most_common_day_of_week)

    # display the most common start hour

    most_common_start_hour=df['hour'].mode()[0]
    print("the most common start hour is:",most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_commonly_used_start_station=df['Start Station'].mode()[0]
    print("most_commonly_used_start_station is:" ,most_commonly_used_start_station)

    # display most commonly used end station

    most_commonly_used_end_station=df['End Station'].mode()[0]
    print("most_commonly_used_end_station is:", most_commonly_used_end_station)

    # display most frequent combination of start station and end station trip
    df['start_to_end']=df['Start Station']+" "+df['End Station']
    most_frequent_start_end_station=df['start_to_end'].mode()[0]
    print("most frequent combination of start station and end station trip is: ",most_frequent_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("total travel time is: ",total_travel_time, "s")
    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("mean travel time is: ", round(mean_travel_time), "s")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_types=df['User Type'].value_counts()
    print("counts of user types is: ",counts_of_user_types)

    # Display counts of gender
    if city !='washington':
        counts_of_gender=df['Gender'].value_counts()
        print("counts of gender is: ",counts_of_gender)

        # Display earliest, most recent, and most common year of birth
        earliest_year_of_birth=df['Birth Year'].min()
        print("earliest_year_of_birth is: ",int(earliest_year_of_birth))
        most_recent_year_of_birth = df['Birth Year'].max()
        print("most_recent_year_of_birth is: ",int(most_recent_year_of_birth))
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print(" most_common_year_of_birth is: ", int(most_common_year_of_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_individual_trip(df):
    i=0
    j=5
    while True:
        question=input("Would You like to view individual trip data? type 'Yes' or 'No'\n->").lower()
        if question =='yes':
            print(df.iloc[i:j])
            i+=5
            j+=5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        view_individual_trip(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
