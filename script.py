import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
df1 = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
df2 = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
print(df1.head())
print(df2.head())
print(df1['Supplier'].nunique())
print(df2['Supplier'].nunique())
print(df1.groupby('Year of Rank').Name.count())
print(df2.groupby('Year Built').Name.count())

# write function to plot rankings over time for 1 roller coaster here:

df3 = df1[df1.Name == 'El Toro']
print(df3.head())

def plot_rank(name, park, data):
  newdf = data[(data.Name == name) & (data.Park == park)]
  plt.plot(newdf['Year of Rank'], newdf['Rank'])
  ax=plt.subplot()
  ax.invert_yaxis()
  plt.title('Ranking of ' + name + ' Over Time')
  plt.show()
  
plot_rank('El Toro','Six Flags Great Adventure',df1)


plt.clf()

# write function to plot rankings over time for 2 roller coasters here:

def plot_rank2(name1, name2, park1, park2, data):
  newdf1 = data[(data.Name == name1) & (data.Park == park1)]
  newdf2 = data[(data.Name == name2) & (data.Park == park2)]
  plt.plot(newdf1['Year of Rank'], newdf1['Rank'])
  plt.plot(newdf2['Year of Rank'], newdf2['Rank'])
  ax=plt.subplot()
  ax.invert_yaxis()
  plt.legend([name1, name2])
  plt.title('Ranking of ' + name1 + ' and ' + name2 + ' Over Time')
  plt.show()

plot_rank2('El Toro', 'Boulder Dash', 'Six Flags Great Adventure', 'Lake Compounce', df1)






plt.clf()

# write function to plot top n rankings over time here:


topdff = df1[df1['Rank'] <= 5]
print(topdff)


def toprank(n, data):
  topdf = data[data['Rank'] <= n]
  fig, ax = plt.subplots(figsize=(10,10))
  for coaster in set(topdf['Name']):
    coaster_rankings = topdf[topdf['Name'] == coaster]
    ax.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'], label=coaster)
  ax.invert_yaxis()
  ax.set_yticks(range(1,6))
  plt.title("Top 10 Rankings")
  plt.legend()
  plt.xlabel("Year")
  plt.ylabel("Ranking")
  plt.show()
  

toprank(5, df1)
  


plt.clf()

# load roller coaster data here:
df3 = pd.read_csv("roller_coasters.csv")
print(df3.head())


# write function to plot histogram of column values here:
def plot_hist(data, column):
  plt.hist(data[column].dropna())
  plt.title('Histogram of Roller Coaster {}'.format(column))
  plt.xlabel(column)
  plt.ylabel('Count')
  plt.show()
  
plot_hist(df3, "speed")









plt.clf()

# write function to plot inversions by coaster at a park here:

def num_inversion(data, park):
  park_coasters = data[data['park']==park]
  park_coasters = park_coasters.sort_values('num_inversions', ascending=False)
  coaster_names = park_coasters['name']
  number_inversions = park_coasters['num_inversions']
  plt.bar(range(len(number_inversions)), number_inversions)
  ax = plt.subplot()
  ax.set_xticks(range(len(number_inversions)))
  ax.set_xticklabels(coaster_names, rotation=90)
  plt.title('Number of Inversions Per Coaster at {}'.format(park))
  plt.xlabel('Roller Coaster')
  plt.ylabel('# of Inversions')
  plt.show()
  
num_inversion(df3, 'Parc Asterix')








plt.clf()
    
# write function to plot pie chart of operating status here:

def num_operating(data):
  opened = data[data['status'] == 'status.operating']
  closed = data[data['status'] == 'status.closed.definitely']
  num_opened = len(opened)
  num_closed = len(closed)
  status_counts = [num_opened, num_closed]
  plt.pie(status_counts, autopct='%0.1f%%', labels = ['Operating', 'Closed'])
  plt.axis('equal')
  plt.show()
  
num_operating(df3)








plt.clf()
  
# write function to create scatter plot of any two numeric columns here:

def scatter(data, column1, column2):
  plt.scatter(data[column1], data[column2])
  plt.title('Scatter Plot of {} and {}'.format(column2, column1))
  plt.xlabel(column1)
  plt.ylabel(column2)
  plt.show()

scatter(df3, 'speed', 'height')








plt.clf()