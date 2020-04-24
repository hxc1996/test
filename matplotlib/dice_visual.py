import pygal
from die import Die

die_1=Die()
die_2=Die()
results=[]
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies=[]
max_result = die_1.num_sides + die_2.num_sides
for value in range(1,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist=pygal.Bar()
hist.title = 'results of rolling one D6 1000 times'
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.y_title = 'frequency of result'
hist.x_title = 'result'
hist.add('D6 + D6',frequencies)
hist.render_to_file('D:\\die_visual2.svg')