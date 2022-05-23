class Result_kasr:
    sorat_f = None
    makhraj_f = None

    def show_result(self):
        print(f'Result= {Result_kasr.sorat_f}/{Result_kasr.makhraj_f}')


class Kasr:
    sorat_1 = None
    makhraj_1 = None
    sorat_2 = None
    makhraj_2 = None
    op = None

    def get_input(self):
        self.sorat_1 = float(input("Please Inter Sorate Kasr:"))
        self.makhraj_1 = float(input("Please Inter Makhraj Kasr:"))
        self.op = self.chooice_amalgar()
        if self.op != '5':
            self.sorat_2 = float(input("Please Inter Sorate Kasr:"))
            self.makhraj_2 = float(input("Please Inter Makhraj Kasr:"))
        if self.op == '+':
            self.sum_kasr()
        if self.op == '-':
            self.menha_kasr()
        if self.op == '*':
            self.zarb_kasr()
        if self.op == '/':
            self.taghsim_kasr()
        if self.op == '5':
            Result_kasr.show_result(self)
            exit()

    def chooice_amalgar(self):
        print("1- +")
        print("2- -")
        print("3- *")
        print("4- /")
        # print("5- exit")
        op = input("Please Select Operator Number: ")
        if op == '+' or op == '-' or op == '*' or op == '/':
            return op
        else:
            print('invalid Operator Please try again')
            self.chooice_amalgar()

    def sum_kasr(self):
        if self.makhraj_1 == self.makhraj_2:
            Result_kasr.sorat_f = self.sorat_1 + self.sorat_2
            Result_kasr.makhraj_f = self.makhraj_1
            Result_kasr.show_result(self)
        else:
            Result_kasr.sorat_f = (self.sorat_1 * self.makhraj_2) + (self.sorat_2 * self.makhraj_1)
            Result_kasr.makhraj_f = (self.makhraj_1 * self.makhraj_2)
            Result_kasr.show_result(self)

    def menha_kasr(self):
        if self.makhraj_1 == self.makhraj_2:
            Result_kasr.sorat_f = self.sorat_1 - self.sorat_2
            Result_kasr.makhraj_f = self.makhraj_1
            Result_kasr.show_result(self)
        else:
            Result_kasr.sorat_f = (self.sorat_1 * self.makhraj_2) - (self.sorat_2 * self.makhraj_1)
            Result_kasr.makhraj_f = (self.makhraj_1 * self.makhraj_2)
            Result_kasr.show_result(self)

    def zarb_kasr(self):
        Result_kasr.sorat_f = self.sorat_1 * self.sorat_2
        Result_kasr.makhraj_f = (self.makhraj_1 * self.makhraj_2)
        Result_kasr.show_result(self)

    def taghsim_kasr(self):
        Result_kasr.sorat_f = self.sorat_1 * self.makhraj_2
        Result_kasr.makhraj_f = (self.makhraj_1 * self.sorat_2)
        Result_kasr.show_result(self)


Numbers_1 = Kasr()
while True:
    Numbers_1.get_input()
    edame = input('For exit typed "exit" or continue press any key')
    if edame == 'exit':
        exit()