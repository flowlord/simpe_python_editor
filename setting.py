from re import*

try:
    setting_file = open('user.grx', 'r')
except FileNotFoundError:
    setting_file = open('user.grx', 'x')
    setting_file.write("\n<bg = '#343434'>\n")
    setting_file.write("\n<fg = '#00996D'>\n")
    setting_file = open('user.grx', 'r')

setting_read = setting_file.read()

bg = search("<bg = ('.*')>",setting_read)
fg = search("<fg = ('.*')>",setting_read)

bg = bg.group(1)
bg = bg.replace("'","")

fg = fg.group(1)
fg = fg.replace("'","")




