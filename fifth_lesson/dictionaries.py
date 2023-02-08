#dictionary

countries_and_capitals = {
    'Lithuania': 'Vilnius',
    'Poland': 'Warsaw',
    'Latvia': {
        'capital': 'Riga',
        'population': 2000000,
        'rich': 'poor'
    }
}

population = countries_and_capitals['Latvia']['population']
print(f'About {population} people live in Riga')

print(list(countries_and_capitals.items()))
print(list(countries_and_capitals.keys()))
print(list(countries_and_capitals.values()))

countries_and_capitals.pop('Latvia')
print(countries_and_capitals)