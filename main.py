from calc import draw_calc

draw_calc('data/time_2c.txt', 'data/voltage_2c.txt',\
          'output/popt_2c.txt', 'output/error_2c.txt',\
          'output/delta_2c.txt','output/epsilon_2c.txt',\
          [0,60,12])

draw_calc('data/time_c.txt', 'data/voltage_c.txt',\
          'output/popt_c.txt', 'output/error_c.txt',\
          'output/delta_c.txt','output/epsilon_c.txt',\
          [0,30,12])

draw_calc('data/time_c0.txt', 'data/voltage_c0.txt',\
          'output/popt_c0.txt', 'output/error_c0.txt',\
          'output/delta_c0.txt','output/epsilon_c0.txt',\
          [0,4.7,12])
