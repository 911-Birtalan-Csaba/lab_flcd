%{
#include "y.tab.h"
#include <stdio.h>
#include <stdlib.h>

//#define YYDEBUG 1
%}

%token BN;
%token ARR;
%token VAR;
%token IF;
%token PRINT;
%token READ;
%token ELSE;
%token ELSEIF;
%token WHILE;
%token FOR;
%token SETNTH;
%token GETNTH;
%token RETURN;

%token IDENTIFIER;
%token INTCONSTANT;
%token STRINGCONSTANT;

%token LEN;

%token NEWLINE;

%token PLUS;
%token MINUS;
%token TIMES;
%token DIV;
%token MOD;
%token EQ;
%token BIGGER;
%token BIGGEREQ;
%token LESS;
%token LESSEQ;
%token EQQ;
%token NEQ;
%token AND;
%token OR;
%token NOT;

%token FALSE;
%token TRUE;

%token EMPTYSTRING;
%token OPEN;
%token CLOSE;
%token BRACKETOPEN;
%token BRACKETCLOSE;
%token COMMA;
%token DIEZ;
%token VERTICAL;
%token SEPARATOR;

%start compound_statement 

%%

compound_statement : statement SEPARATOR {printf("compound_statement -> statement \n");};
    | statement SEPARATOR compound_statement {printf("compound_statement -> satement_list\n");};
statement : assignment_statement {printf("statement -> assignment_statement\n");}
    | if_statement {printf("statement -> if_statement\n");}
    | while_statement {printf("statement -> while_statement\n");}
    | for_statement {printf("statement -> for_statement\n");}
    | function_call_statement {printf("statement -> function_call_statement\n");};
function_call_statement : READ OPEN IDENTIFIER CLOSE {printf("statement -> --> ( IDENTIFIER )\n");}
    | PRINT OPEN IDENTIFIER CLOSE {printf("statement -> <-- ( IDENTIFIER )\n");}
    | PRINT OPEN INTCONSTANT CLOSE {printf("statement -> <-- ( INTCONSTANT )\n");}
    | PRINT OPEN STRINGCONSTANT CLOSE {printf("statement -> <-- ( STRINGCONSTANT )\n");};
if_statement : IF OPEN condition CLOSE DIEZ compound_statement DIEZ {printf("if_statement -> IF ( condition ) # compound_statement #\n");} 
    | IF OPEN condition CLOSE DIEZ compound_statement DIEZ ELSE DIEZ compound_statement DIEZ {printf("if_statement -> IF ( condition ) # compound_statement # else # compound_statement #\n");};
while_statement : WHILE OPEN condition CLOSE DIEZ compound_statement DIEZ {printf("assignment_statement : while ( condition ) # compound_statement #\n");};
for_statement : FOR for_header DIEZ compound_statement DIEZ {printf("for_statement : for ( for_header ) # compound_statement #\n");};
for_header : assignment_statement VERTICAL condition VERTICAL assignment_statement {printf("for_header : assignment_statement | condition | assignment_statement\n");};
condition : expression relation expression {printf("condition : expression relation expression");};
relation : LESS {printf("relation : <");}
    | LESSEQ {printf("relation : <=");}
    | BIGGER {printf("relation : >");}
    | BIGGEREQ {printf("relation : >=");}
    | NEQ {printf("relation : !=");}
    | EQQ {printf("relation : ==");};
assignment_statement : IDENTIFIER EQ expression {printf("assignment_statement -> IDENTIFIER = expression\n");} 
    | IDENTIFIER EQ array_statement {printf("assignment_statement -> IDENTIFIER = array_statement\n");};
array_statement : BRACKETOPEN BRACKETCLOSE {printf("array_statement -> [ ]\n");} 
    | BRACKETOPEN expression_list BRACKETCLOSE {printf("array_statement -> [ expression_list ]\n");};
expression : expression PLUS term {printf("expression -> expression + term\n");} 
    | expression MINUS term {printf("expression -> expression - term\n");} 
    | term {printf("expression -> term\n");};
term : term TIMES factor {printf("term -> term * factor\n");} 
    | term DIV factor {printf("term -> term / factor\n");} 
    | factor {printf("term -> factor\n");};
factor : OPEN expression CLOSE {printf("factor -> ( expression )\n");} 
    | IDENTIFIER {printf("factor -> IDENTIFIER\n");} 
    | INTCONSTANT {printf("factor -> INTCONSTANT\n");};
expression_list : expression {printf("expression_list -> expression\n");} 
    | expression COMMA expression_list {printf("expression -> expression , expression_list\n");};

%%
int yyerror(char *s)
{	
	printf("%s\n",s);
}


extern FILE *yyin;

int main(int argc, char **argv)
{
	if(argc>1) yyin =  fopen(argv[1],"r");
	if(!yyparse()) fprintf(stderr, "\tOK\n");
} 