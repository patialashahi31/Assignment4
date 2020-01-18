import csv
data = csv.DictReader(open("addresses.csv"))
import matplotlib.pyplot as plt
def menu():
    print('-'*20 + "TOOTH FAIRY - ATO CASE" + '-'*20)
    print('-'*20+"Name" + '-'*5 + "Number"+'-'*20)
    print("1) Statistics")
    print("2) Export children details who haven\'t lost any tooth")
    print("3) Display number of claims per state")
    print("4) Compare 2 states")
    print("5) Exit")
    choice = int(input("Enter your choice [1-5]"))
    while(True):
        if choice==1:
            stats()
            break
        elif choice==2:
            exportstat()
            break
        elif choice==3:
            claims()
            break
        elif choice==4:
            compare()
            break
        elif choice==5:
            myExit()
            break
        else:
            print("Please enter valid number")
            choice = int(input("Enter your choice [1-5]"))



def myExit():
    print("Thanks for using services")


def stats():

    with open('addresses.csv', 'rt')as f:
        data = csv.reader(f)
        count = -1
        for row in data:
            count = count +1

    sum = 0
    neverlosttooth=0
    noOfBabyTeeth = 0
    expenditure = 0.0
    for row in data:
        noOfteethLost = int(row['Total number of teeth lost'])
        sum += noOfteethLost
        if(noOfteethLost==0):
            neverlosttooth = neverlosttooth+1
        if(noOfteethLost==20):
            noOfBabyTeeth += 1

        if(noOfteethLost==1):
            expenditure += 1
        elif(noOfteethLost>1):
            expenditure += 0.5

    print("Total number of children in the list : " + str(count))
    print("Average number of teeth claims over the years : "+ str(sum/count))
    print("Number of children who never lost a tooth: " + str(neverlosttooth))
    print("Number of children who lost all their baby teeth: " +str(noOfBabyTeeth))
    print(f"Total expenditure for this year : ${expenditure}")


def exportstat():
    neverlosttooth = 0
    for row in data:
        noOfteethLost = int(row['Total number of teeth lost'])
        if(noOfteethLost==0):
            neverlosttooth += 1
    filename = input("Enter a new file name")
    file  = open(filename,'w')
    file.write(f"{neverlosttooth} children never lost their teeth")
    print(f'{neverlosttooth} children have been saved in {filename}')




def claims():
    states = ['TAS','QLD','WA','NSW','SA',"VIC",'NT']
    claim = [0,0,0,0,0,0,0]
    for row in data:
        state = row['State']
        if state=='TAS':
            claim[0] += 1
        elif state == 'QLD':
            claim[1] += 1
        elif state=='WA':
            claim[2] += 1
        elif state=='NSW':
            claim[3] += 1
        elif state =='SA':
            claim[4] += 1
        elif state =='VIC':
            claim[5] += 1
        elif state=='NT':
            claim[6] += 1

    plt.bar(states, claim, align='center', alpha=0.5)
    plt.ylabel('Number of children')
    plt.xlabel('State')
    plt.title('Number of children per state')
    plt.grid(True)

    plt.show()

def compare():
    firstState = input("Enter first choice : (TAS/QLD/WA/NSW/SA/VIC/NT) : ")
    secondState = input("Enter second choice : (TAS/QLD/WA/NSW/SA/VIC/NT) : ")
    sumOfFirtState =0
    countOfFirstState =0
    sumOfSecondState =0
    countOfSecondState =0
    for row in data:
        if (row['State']==firstState):
            sumOfFirtState += int(row['Total number of teeth lost'])
            countOfFirstState += 1
        elif(row['State'] == secondState):
            sumOfSecondState += int(row['Total number of teeth lost'])
            countOfSecondState += 1

    state = [firstState,secondState]
    avg = [sumOfFirtState/countOfFirstState,sumOfSecondState/countOfSecondState]
    plt.bar(state, avg, align='center', alpha=0.5)
    plt.ylabel('Number of Teeth')
    plt.xlabel('State')
    plt.title('Average number of teeth lost across 2 states')
    plt.grid(True)

    plt.show()

menu()







