import re
from re import match

from LanguageLexical import LanguageLexical
from Utils import Utils
from hash_table import HashTable
from pif import Pif


class TokenIdentifier:
    def __init__(self, languageLexical: LanguageLexical):
        self.__languageLexical = languageLexical
        self.__symbolTable = HashTable()
        self.__pif = Pif()
        self.__utils = Utils()
        self.__identifierFA = self.__utils.readFromFile('program/identifier_FA.in')
        self.__is_integer_constantFA = self.__utils.readFromFile('program/integer_constant_FA.in')
        self.__is_string_FA = self.__utils.readFromFile("program/stringFA.in")

    def is_identifier(self, token: str) -> bool:
        return self.__identifierFA.isValid(token)

    def is_integer_constant(self, token: str) -> bool:
        return self.__is_integer_constantFA.isValid(token)

    def is_string_constant(self, token: str) -> bool:
        return match(r'^"(.*)"$', token) is not None

    def is_reserved_word(self, token: str) -> bool:
        return self.__languageLexical.reserved_words.get(token)

    def is_operator(self, token: str) -> bool:
        return self.__languageLexical.operators.get(token)

    def __get_split_string(self):
        split_string = ""
        for separator in self.__languageLexical.separators.get_all_keys():
            split_string += "[" + separator + "]" + "|"
        return split_string[:-1]

    def find(self, s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

    def add_separators_to_pif(self, line: str):
        separators = ["#", ",", "|", "[", "]", "="]
        for separator in separators:
            positions = self.find(line, separator)
            for pos in positions:
                self.__pif.insert(separator, "-1")

    def read_tokens(self, program_file):
        current_line = 1
        split_string = self.__get_split_string()

        is_correct = True
        invalid_token = ""
        for line in program_file:
            self.add_separators_to_pif(line)
            tokens = list(filter(None, re.split(split_string, line)))
            if not tokens:
                continue
            print(tokens)

            for token in tokens:
                is_token_correct = False
                is_token_correct = is_token_correct or self.is_reserved_word(token)
                if is_token_correct:
                    continue

                is_token_correct = is_token_correct or self.is_operator(token)
                if is_token_correct:
                    continue

                is_token_correct = is_token_correct or self.is_identifier(token)
                if is_token_correct:
                    try:
                        num1, num2 = self.__symbolTable.insert(token)
                        self.__pif.insert(token, (num1, num2))
                    except Exception:
                        pass

                is_token_correct = is_token_correct or self.is_integer_constant(token)

                is_token_correct = is_token_correct or self.is_string_constant(token)
                if is_token_correct:
                    try:
                        num1, num2 = self.__symbolTable.insert(token)
                        self.__pif.insert(token, (num1, num2))
                    except Exception:
                        pass

                if not is_token_correct:
                    invalid_token = token
                    is_correct = False
                    break

            if not is_correct:
                break
            current_line += 1
        if is_correct:
            print("Program is lexically correct!")
        else:
            print(f"Lexical error at line {current_line} on {invalid_token}!")
        st_file = open("ST.out", "w")
        st_file.write(str(self.__symbolTable))
        st_file.close()

        pif_file = open("PIF.out", "w")
        pif_file.write(str(self.__pif))
        pif_file.close()
