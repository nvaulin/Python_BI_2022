import os.path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib.patches import ConnectionPatch
import seaborn as sns

### Task 1, rRNAs

def read_gff(file: str) -> pd.DataFrame:
    cols = ["chromosome", "source", "type", "start", "end", "score", "strand", "phase", "attributes"]
    df = pd.read_csv(file, sep='\t', comment="#", header=None)

    df.columns = cols
    return df


def read_bed6(file: str) -> pd.DataFrame:
    cols = ["chromosome", "start", "end", "name", "score", "strand"]
    df = pd.read_csv(file, sep='\t', header=None)
    df.columns = cols
    return df


gff = os.path.join('data', 'rrna_annotation.gff')
df_gff = read_gff(gff)
df_gff.head()


bed = os.path.join('data', 'alignment.bed')
df_bed = read_bed6(bed)
df_bed.head()

chr_att_ct = pd.crosstab(df_gff.chromosome, df_gff.attributes)
stacked = chr_att_ct.stack().reset_index()

sns.set(rc={'figure.figsize': (15, 9)})
sns.set_style("white")

rna_amounts = sns.barplot(x=stacked.chromosome, y=stacked[0], hue=stacked.attributes)
rna_amounts.set(xlabel='Sequence', ylabel='Count')
rna_amounts.set_xticklabels(rna_amounts.get_xticklabels(), rotation=90)
plt.legend(title='RNA type', loc='upper right')

plt.plot();


df_inter = df_gff.merge(df_bed, on='chromosome')
df_inter = df_inter.query('start_x >= start_y +1 and end_x <= end_y + 1')
df_inter
# Here we added 1 to y coordinates since bed files are 0-based while gff files are 1-based



### Task 2, volcano plot

file = os.path.join('data', 'diffexpr_data.tsv.gz')
df_volc = pd.read_csv(file, sep='\t')
df_volc.head()


Hues = {'True_True': 'Significantly upregulated',
        'True_False': 'Significantly downregulated',
        'False_True': 'Non-significantly upregulated',
        'False_False': 'Non-significantly downregulated'
        }

palette = {'Significantly upregulated': 'tab:orange',
           'Significantly downregulated': 'tab:blue',
           'Non-significantly upregulated': 'tab:red',
           'Non-significantly downregulated': 'tab:green'
           }


df_volc['signif'] = df_volc.pval_corr <= 0.05
df_volc['regulation'] = df_volc.logFC >= 0
df_volc['Hue'] = df_volc[['signif', 'regulation']].astype(str).agg('_'.join, axis=1).replace(Hues)


top_2_down = df_volc.query('Hue == "Significantly downregulated"').sort_values(
                            by=['logFC']).head(2).Sample.index.tolist()
top_2_up = df_volc.query('Hue == "Significantly upregulated"').sort_values(
                            by=['logFC']).tail(2).Sample.index.tolist()
top_2 = top_2_down + top_2_up

sns.set_theme(style="ticks", font='sans-serif', rc={'figure.figsize': (8.8, 5.03)})
plt.rcParams['figure.dpi'] = 800
plt.rcParams['font.size'] = 3
plt.rcParams['font.weight'] = 'bold'
plt.rcParams["legend.markerscale"] = 1

volcano = sns.scatterplot(data=df_volc, x='logFC', y='log_pval', hue='Hue', palette=palette, s=5, linewidth=0)
plt.text(6, 2, 'p value = 0.05', c='grey', fontfamily='sans-serif', size='small', weight='bold')
plt.axhline(y=1.301, color='grey', linestyle='--', linewidth=0.9)
plt.axvline(x=0, color='grey', linestyle='--', linewidth=0.9)

# Adding annotations manually (the example of usage .annotate() i left for another plot)
for i, row in df_volc.loc[top_2].iterrows():
    plt.text(row["logFC"] - 0.3, row["log_pval"] + 6, row["Sample"], fontfamily='sans-serif', size=6,
             weight='extra bold')
    plt.arrow(row["logFC"], row["log_pval"] + 5, dx=0, dy=-3, head_width=0.15, head_length=1, width=0.07, linewidth=0.2,
              fc='r', ec='k')

# Reordering the legend
handles, labels = plt.gca().get_legend_handles_labels()
order = [1, 3, 0, 2]
volcano.legend([handles[i] for i in order], [labels[i] for i in order], title=None, shadow=True)

# Managing axis width (here can be color as well etc)
for axis in ['top', 'bottom', 'left', 'right']:
    volcano.spines[axis].set_linewidth(1)

# Managing x axis limits
x_lim = df_volc.logFC.abs().max() + 1
plt.xlim(-x_lim, x_lim)

# Setting ticks
volcano.set_xticks(np.linspace(-11, 11, 23), minor=True)
volcano.set_yticks(np.linspace(-5, 115, 25), minor=True)
volcano.tick_params(which='minor', length=2, width=0.8)

# Setting figure texts
volcano.set_title('Volcano plot', weight='black', style='italic', fontsize=20)
volcano.set_xlabel('log$_2$(fold change)', weight='black', style='italic')
volcano.set_ylabel('-log$_{10}$(p value corrected)', weight='black', style='italic')

plt.savefig('my_volcano.png', dpi=700)
plt.show()



### Task 3, pie chart


plots = ['Violin plot', 'Density plot', 'Boxplot', 'Histogram', 'Scatter plot', 'Barplot', 'Other']
values = [40, 40, 25, 30, 30, 15, 1]

other = ['Dotplot', 'Bubble chart', 'Spagetti plot', 'Sunburts plot', 'Pie chart']
other_values = [40, 20, 24, 18, 1]

df_pie = pd.DataFrame(values, columns=['Value'],
                      index=plots)

df_bar = pd.DataFrame({
    'plot': other,
    'Value': other_values,
    '_': '_'
})


fig = plt.figure(figsize=(15, 7.5))
gs = gridspec.GridSpec(1, 2, width_ratios=[5, 1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])

colors = sns.color_palette('Set2')
sns.despine()
sns.set_theme(style="white")

shrink = 1
explode = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.07]

wedges, texts = ax1.pie(df_pie.Value, explode=explode, startangle=1, colors=colors);
ax2 = sns.histplot(df_bar, x='_', hue='plot', weights='Value',
                   multiple='stack', palette='tab20c', shrink=shrink);
ax2.get_legend().remove()

# Deleting axis from stacked bar
ax2.set(yticklabels=[], xticklabels=[], ylabel=None, xlabel=None)
ax2.tick_params(left=False)
for axis in ['top', 'bottom', 'left', 'right']:
    ax2.spines[axis].set_linewidth(0)

# Labeling the stacked bar
for i in range(len(ax2.containers)):
    cont = ax2.containers[i]
    lab = df_bar[df_bar.Value == cont.datavalues[0]]['plot'].values[0]
    ax2.bar_label(cont, labels=[lab], label_type='center')

# Making connection lines between pie and stacked bar
xp = 1.07
yp = 0.015
con1 = ConnectionPatch(xyA=(-shrink / 2, sum(other_values)), coordsA=ax2.transData,
                       xyB=(xp, yp), coordsB=ax1.transData)
con2 = ConnectionPatch(xyA=(-shrink / 2, 0), coordsA=ax2.transData,
                       xyB=(xp, -yp), coordsB=ax1.transData)
for con in [con1, con2]:
    con.set_color([0, 0, 0])
    con.set_linewidth(1)
    ax2.add_artist(con)

# Creating annotation for pie pieces 
for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1) / 2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    ax1.annotate(df_pie.index[i], xy=(x, y), xytext=(1.4 * np.sign(x), 1.5 * y),
                 bbox={'fc': 'w', 'ec': 'k'},
                 arrowprops={'arrowstyle': '-',
                             'connectionstyle': 'angle,angleA=0,angleB=90,rad=20',
                             'mutation_scale': 10, 'color': 'k'})

plt.suptitle('The plot styles value and usefulness', weight='black', style='italic', fontsize=20)
plt.show()



### Task 4, owid covid EDA


file = os.path.join('data', 'owid-covid-data.csv')
df_covid = pd.read_csv(file)
df_covid.head()


# it was taken from some web-forum some time ago,
# but i like it and use with my own data so...
# i asked myself to share this plot here and i got the permission

sns.set_theme(style="white")
plt.rcParams['font.weight'] = 'light'

plt.figure(figsize=(10, 6))
dis = sns.displot(
    data=df_covid.isna().melt(value_name="missing"),
    y="variable",
    hue="missing",
    multiple="fill",
    aspect=1.25
);
plt.xlabel("Fraction")
plt.ylabel("Features")
dis.tick_params(labelsize=5)
plt.title("Fraction of missing values")
plt.show()

Looking at this graph, I want to remove some columns entirely.


df_covid.drop(['excess_mortality', 'excess_mortality_cumulative_per_million',
               'excess_mortality_cumulative', 'excess_mortality_cumulative_absolute',
               'total_boosters_per_hundred', 'icu_patients', 'icu_patients_per_million',
               'hosp_patients', 'hosp_patients_per_million', 'weekly_icu_admissions',
               'weekly_icu_admissions_per_million', 'weekly_hosp_admissions',
               'weekly_hosp_admissions_per_million', 'total_boosters'], axis=1, inplace=True)


However, this graph looks scary. If you work honestly with this dataset, you need to spend a week to correctly clean up all the missing values. In some columns there are simply a lot of them, and not all of the missing values are actually missing. All this should be checked. A separate problem is that igt is better not to just drop observations, since we have a time series feature. 

Let's see some example


df_covid.continent.unique()

We will check what locations a in entries with the missing continent.


df_covid[df_covid.continent.isna()].location.value_counts()

So, great! We see a lot of stuff to do. we can restore continent from the location for many observation. Moreover we have 'International' and 'World' values that mean the continent is not actually missing. It is the Earth.... 

And... there are some strange values. 'Hight income'? 'Upper middle income'? Is it a location? By the way, we don't have any actual location information for that entries. In this case it may be better to contact the data provider in order to get some metadata for this dataset. Maybe i would drop this entries with 'income...', or maybe i would create another columns. 

Yeah, i hound metadata here: https://github.com/owid/covid-19-data/blob/master/public/data/README.md

By the way, i see nothing about income.


> So, that's an examle reasoning about the dataset. That's the way i would do if needed. We have many-many features so in case of NA-filling we should do it in group-wise manner making different groups important for some features. Also the group-wise NA filling should be done with respect to time-series feature in our dataset: we can't do some constant-replacing like with average - there should be some methods as backward or forward filling or linear interpolation for instance. 
>
> Maybe some NA-values can be restored directly from the existing ones for example in case when the NA value means that no new data obtained since last observation.
>
> By the way, it is not the point of our task and moreover i don't want do honestly and carefully such a big job just for 5 additional points. At least 5 additional thousand of rubbles if it were the real case for real project. 


#### Lest's just do some plots and data-scientology `



df_covid = df_covid[df_covid.continent != 'NaN']



mean_deaths = df_covid.query('new_deaths > 0').new_deaths.mean()
median_deaths = df_covid.query('new_deaths > 0').new_deaths.median()
max_deaths = df_covid.query('new_deaths > 0 ').new_deaths.max()
print(f'\nThe average number of new deaths is {mean_deaths}')
print(f'\nThe median number of new deaths is {median_deaths}')
print(f'\nThe maximum number of new deaths is {max_deaths}')

plt.hist(df_covid.query('location != "World" and location != "Intarnational"').new_deaths, bins=20);
plt.axvline(x=mean_deaths, color='r', linestyle='solid', label="Average");
plt.axvline(x=median_deaths, color='g', linestyle='solid', label="Median");
plt.ylabel('Number of cases')
plt.xlabel('New deaths')
plt.yscale('log')
plt.legend();

We see that the statistic contains half of all values to the left of 13, while having a very large and heavy tail on the right. It's already brushed off world values!


We can do some feature generation, for example:

df_covid['total_reсoveries'] = df_covid.total_cases - df_covid.total_deaths

df_covid['date']  = pd.to_datetime(df_covid['date'] , format = '%m/%d/%Y')
df_covid['weekday'] = df_covid['date'].dt.day_name()

def plot_per_weekday(df_covid, var):
    df_weekday = df_covid.groupby(['weekday'])[var].mean().reset_index()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    mapping = {day: i for i, day in enumerate(weekdays)}
    df_weekday = df_weekday.iloc[df_weekday.weekday.map(mapping).argsort()]
    plot = plt.bar(df_weekday.weekday, df_weekday[var], color='maroon', width=0.4);
    return plot

plot_per_weekday(df_covid.query('location == "Russia"'), 'new_deaths')
plot_per_weekday(df_covid.query('location == "France"'), 'new_cases')

Here I show the stereotype plots (it was popular during covid) - some data on the days of the week. During covid, many hypotheses were made based on this. I just wanted to get something like this myself. In the simplest case, we get a visual representation of on which days the regular goverment statisticians had a day off.