from Utils import Utils


class Console:
    def __init__(self):
        utils = Utils()
        self.finite_automata = utils.readFromFile('FA.in')

    def showAll(self):
        print(self.finite_automata)

    def showStates(self):
        print(self.finite_automata.Q)

    def showAlphabet(self):
        print(self.finite_automata.E)

    def showTransitions(self):
        print(self.finite_automata.transitions)

    def showSetOfFinalStates(self):
        print(self.finite_automata.F)

    def checkIfAccepted(self):
        sequence = input('Read sequence>>')
        print(self.finite_automata.isValid(sequence))

    def __displayMenu(self):
        print("0. Exit")
        print("1. Show everything")
        print("2. Show States")
        print("3. Show Alphabet")
        print("4. Show transitions")
        print("5. Show final states")
        print("6: Check sequence is valid")

    def run(self):
        commands = {'1': self.showAll, '2': self.showStates, '3': self.showAlphabet, '4': self.showTransitions,
                    '5': self.showSetOfFinalStates, '6': self.checkIfAccepted}
        exit = False
        while not exit:
            self.__displayMenu()
            print(">>")
            command = input()
            if command in commands.keys():
                commands[command]()
            elif command == '0':
                exit = True
            else:
                continue
