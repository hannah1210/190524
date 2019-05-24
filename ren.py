import os

os.chdir(r'C:\Users\Administrator\PycharmProjects\190524_2\dummy')

for filename in os.listdir('.'):
    os.rename(filename, filename.replace('지원자','합격자'))