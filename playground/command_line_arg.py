import argparse

#construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-n', '--name', required=True, help='name of the user')
args = vars(ap.parse_args())

#display a frendly message to the user
print('Hi, there {}, it\'s nice to meet you!'.format(args['name']))

#and run -> python command_line_arg.py -n Michał