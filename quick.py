def data(input):
    print(f'adsorb{input} = absorb.loc[:,["{input}.1", "{input}.2", "{input}.3"]]')

def graph(input,colour):
    print(f"graph(adsorb{input},'{colour}','{input} µg/mL')")

def compile(values): # input concentrations/sample identifier in an array
    for value in values:
        data(value)

    colors = ['firebrick','orange','green','blue','indigo','orchid','gold','darkcyan','gray','brown','black']
    index = 0
    for value in values:
        graph(value,colors[index])
        index += 1
        if index == 11: index = 0

compile([40,100,200,400,'500s','1s','5s','10s'])
compile([1,5,10,20,'500s','1s','5s','10s'])