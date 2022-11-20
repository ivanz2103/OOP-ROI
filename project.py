class ROI():

    def __init__(self, income, expenses, cash_flow):
        self.income = []
        self.expenses = []
        self.cash_flow = []

    def add_income(self):
        income = input(
            "Which source of income would you like to add? (Rental,Laundry,Storage,Sh): ").lower()

        if income == 'rental':
            rental = int(input("Input your monthly rental income: "))
            self.income.append(rental)
            print(f'Your rental income is: {rental}')

        elif income == 'laundry':
            laundry = int(input("Input your monthly laundry income: "))
            self.income.append(laundry)
            print(f'Your laundry income is: {laundry}')

        elif income == 'storage':
            storage = int(input("Input your monthly storage income: "))
            self.income.append(storage)
            print(f'Your storage income is: {storage}')

        elif income == 'sh':
            sh = int(input("Input your other income: "))
            self.income.append(sh)
            print(f'Your side hustle income is: {sh}')

        elif income == 'quit':
            pass

        else:
            print("Try another command")

        monthly_income = int(sum(self.income))

        print(f"Your total monthly income is: {monthly_income}.")

    def add_expenses(self):
        define_expenses = (input(
            "Which expense would you like to state? (Tax,Insurance,Utilities,Hoa,Lsc,Vacancy,Repairs,Future,Property,Mortgage,Unexpected): ")).lower()

        if define_expenses == 'tax':
            tax = int(input("Input your tax expense: "))
            self.expenses.append(tax)
            print(f'Your tax expense is: {tax}')

        elif define_expenses == 'insurance':
            insurance = int(input("Input your insurance expense: "))
            self.expenses.append(insurance)
            print(f'Your insurance expense is: {insurance}')

        elif define_expenses == 'utilities':
            utilities = int(input("Input your utilities expense: "))
            self.expenses.append(utilities)
            print(f'Your utilities expense is: {utilities}')

        elif define_expenses == 'hoa':
            hoa = int(input("Input your HOA expense: "))
            self.expenses.append(hoa)
            print(f'Your HOA expense is: {hoa}')

        elif define_expenses == 'lsc':  # lawn/snow care
            lsc = int(input("Input your lsc expense: "))
            self.expenses.append(lsc)
            print(f'Your lawn or snow care expense is: {lsc}')

        elif define_expenses == 'vacancy':
            vacancy = int(input("Input your vacancy expense: "))
            self.expenses.append(vacancy)
            print(f'Your vacancy expense is: {vacancy}')

        elif define_expenses == 'repairs':
            repairs = int(input("Input your repairs expense: "))
            self.expenses.append(repairs)
            print(f'Your repairs expense is: {repairs}')

        elif define_expenses == 'future':
            future = int(input("Your future expense: "))
            self.expenses.append(future)
            print(f'Your future expense is: {future}')

        elif define_expenses == 'property':
            property = int(input("Your property expense: "))
            self.expenses.append(property)
            print(f'Your property expense is: {property}')

        elif define_expenses == 'mortgage':
            mortgage = int(input("Input your mortgage expense: "))
            self.expenses.append(mortgage)
            print(f'Your mortgage expense is: {mortgage}')

        elif define_expenses == 'unexpected':
            unexpected = int(input("Input any unexpected expenses: "))
            self.expenses.append(unexpected)
            (f'Your unexpected expense is: {unexpected}')

        else:
            print("You have entered an invalid command. Please try again.")

        monthly_expenses = int(sum(self.expenses))

        print(f"Your monthly expenses total to: {monthly_expenses}")

    def add_cash_flow(self):
        current_cash_flow = sum(self.income) - sum(self.expenses)
        self.cash_flow.append(current_cash_flow)
        print(f"Current cash flow is: {current_cash_flow}")

    def display_ROI(self):
        initial_investment = int(input("Input your initial investment: "))
        closing_costs = int(input("Input your closing costs: "))
        rehab_budget = int(input("Input your rehab budget: "))
        total_investment = initial_investment + closing_costs + rehab_budget
        cashFlow = sum(self.cash_flow)
        annual_cashFlow = cashFlow * 12
        ROI = (annual_cashFlow / total_investment) * 100

        print(f"Investment worth = {ROI} percent.")


investment_worth = ROI([], [], [])


def runner():
    while True:
        response = input(
            "Select one of the following options: (I)ncome,(E)xpenses,(C)ash Flow,(R)OI or (Q)uit)")

        if response.lower() == 'i':
            investment_worth.add_income()
        elif response.lower() == 'e':
            investment_worth.add_expenses()
        elif response.lower() == 'c':
            investment_worth.add_cash_flow()
        elif response.lower() == 'r':
            investment_worth.display_ROI()
        elif response.lower() == 'q':
            break
        else:
            print("Try another command")


runner()
