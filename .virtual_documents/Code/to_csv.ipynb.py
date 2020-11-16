import tabula


filea_path = '../Downloads/Hyd substations.pdf'


dfa = tabula.convert_into(filea_path,'test.csv',lattice = True,pages='all')



