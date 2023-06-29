import os

def create_christmas_cards():
    with open('employees.txt', 'r') as names:
        employees = names.read().splitlines()
        
    with open('template.txt', 'r') as template_file:
        template = template_file.read()

    if not os.path.exists('christmasCards'):
        os.makedirs('christmasCards')

    for employee in employees:
        message = template.replace('NAME', employee)
        with open(f'christmasCards/{employee}.txt', 'w') as card:
            card.write(message)

if __name__ == "__main__":
  create_christmas_cards()

                    #Brought to life by: Petar Trajchevski ID: 5228 6/29/23