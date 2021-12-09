import os 
my_list = os.listdir('data_set')

#function to generate retrained_labels.txt
def retrained_labels(my_list):
    with open('retrained_labels.txt', 'w') as f:
        for i in range(len(my_list)):
            f.write(my_list[i].replace('_', ' ') + '\n')

if __name__ == '__main__':
    retrained_labels(my_list)
    print('retrained_labels.txt generated...')