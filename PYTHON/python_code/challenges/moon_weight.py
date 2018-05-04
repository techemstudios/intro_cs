# your weight on the moon if you gain a kilo in weight every year for the next 15 years
#weight = 30
#for year in range(1, 16):
#    weight = weight + 1
#    moon_weight = weight * 0.165
#    print('Year %s is %s' % (year, moon_weight))

# Basic Moon weight function
#def moon_weight(weight, increase):
#    for year in range(1, 16):
#        weight = weight + increase
#        moon_weight = weight * 0.165
#        print('Year %s is %s' % (year, moon_weight))
#        moon_weight(40, 0.5)

# Moon weight function and years
def moon_weight(weight, increase, years):
    years = years + 1
    for year in range(1, years):
        weight = weight + increase
        moon_weight = weight * 0.165
        print('Year %s is %s' % (year, moon_weight))
