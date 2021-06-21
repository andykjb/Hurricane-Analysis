# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

#imports

# write your update damages function here:
damages_cleaned = []
def clean_damages(list):
    for item in list:
        if item == 'Damages not recorded':
            damages_cleaned.append(item)
        elif 'M' in item:
            damages_cleaned.append(float(item.strip('M'))*1000000)
        elif 'B' in item:
            damages_cleaned.append(float(item.strip('B'))*1000000000)
    
clean_damages(damages)
#print(damages_cleaned)


# write your construct hurricane dictionary function here:
hurricane_dict = {}

for i in range(len(names)):
    hurricane_dict.update({names[i]: {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Affected Areas': areas_affected[i], 'Damage': damages_cleaned[i], 'Deaths': deaths[i]}})

#print(list(hurricane_dict))
#print(hurricane_dict)

#print(hurricane_dict['Isabel'])




# write your construct hurricane by year dictionary function here:
hurricanes_by_year = {}

def hurricanes_by_year_funct(dict):
    for year in years:
        dict[year] = [hurricane for hurricane in hurricane_dict.values() if hurricane['Year'] == year]


#hurricanes_by_year_funct(hurricanes_by_year)
#print(hurricanes_by_year[2005])


# write your count affected areas function here:
def count_area(dict):
    area_frequency = {}
    for hurricane in dict.values():
        for areas in hurricane['Affected Areas']:
            if areas in area_frequency.keys():
                area_frequency[areas] = int(area_frequency[areas] + 1)
            else: 
                area_frequency[areas] = 1
    return area_frequency

areas_hurr_freq = count_area(hurricane_dict)
#print(areas_hurr_freq)
#print(areas_hurr_freq.values())


# write your find most affected area function here:

def max_count(dict):
    value = max(dict.values())
    area = list(dict.keys())[list(dict.values()).index(value)]
    return {area: value}

#print(max_count(areas_hurr_freq))




# write your greatest number of deaths function here:
def most_deaths(names_list, deaths_list):
    max_death = max(deaths_list)
    name = names_list[deaths_list.index(max_death)]
    return name, max_death

#print(most_deaths(names,deaths))



# write your catgeorize by mortality function here:
def mortality_rating(names_list, death_list):
    mortality_rating_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for i in range(len(names_list)):
        if death_list[i] == 0:
            mortality_rating_dict[0].append(names_list[i])
        elif death_list[i] <= 100:
            mortality_rating_dict[1].append(names_list[i])
        elif death_list[i] <= 500:
            mortality_rating_dict[2].append(names_list[i])
        elif death_list[i] <= 1000:
            mortality_rating_dict[3].append(names_list[i])
        elif death_list[i] <= 10000:
            mortality_rating_dict[4].append(names_list[i])
        elif death_list[i] > 10000:
            mortality_rating_dict[5].append(names_list[i])
    return mortality_rating_dict

print(mortality_rating(names,deaths))


# write your greatest damage function here:







# write your catgeorize by damage function here: