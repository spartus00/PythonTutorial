import os

os.chdir('/home/matt/Documents/The Power of Habit - Charles Duhigg/02 - Part One - The Habits of Individuals')
# print(os.getcwd())
for f in os.listdir():
    # print(f)
    # print(os.path.splitext(f))    #split off extension from the file name
    f_name, f_ext = os.path.splitext(f)
    f_seq, f_ch, f_name, f_part = f_name.split('-')

    f_ch = f_ch.strip()[3:]
    f_seq = f_seq.strip()
    f_name = f_name.strip()
    f_ext = f_ext.strip()

    # print('{}-{}-{}{}'.format(f_ch, f_seq, f_name, f_ext))
    new_name = '{}-{}-{}{}'.format(f_ch, f_seq, f_name, f_ext)

    os.rename(f, new_name)
