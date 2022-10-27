from LanguageLexical import LanguageLexical
from TokenIdentifier import TokenIdentifier
from scanner import Scanner

if __name__ == '__main__':
    lexical = LanguageLexical()
    token_identifier = TokenIdentifier(lexical)

    # print("Analyzing p1...")
    # p1_source = open("examples/p1.in", "r")
    # token_identifier.read_tokens(p1_source)

    # print("Analyzing p2...")
    # p1_source = open("examples/p2.in", "r")
    # token_identifier.read_tokens(p1_source)

    print("Analyzing p3...")
    p1_source = open("examples/p3.in", "r")
    token_identifier.read_tokens(p1_source)

    # print("Analyzing perr...")
    # p1_source = open("examples/perr.in", "r")
    # token_identifier.read_tokens(p1_source)
