#!/usr/bin/env python3

import argparse
import sys


#overall description of program
parser = argparse.ArgumentParser(
    description="""Alignment of two (DNA) sequences with Needleman-Wunsch (global) 
    or Smith Waterman (local) algorithms""",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
    ) #show default value in help

#the following option(s) are required, so we create an own group for them, so they do not show up under 'optional arguments'
parser_req = parser.add_argument_group('required arguments')

# now we can add the required argument(s)
# metavar changes the name of the input variable displayed in the help, by default the variable name would be used
parser_req.add_argument('-a','--seq_1',
                    help='The first sequence, if "-i file", provide name of fasta file (*.fasta) ', metavar= 'STR',
                    required=True)

parser_req.add_argument('-b','--seq_2',
                    help='The second sequence, if "-i file", provide name of fasta file (*.fasta)', metavar= 'STR',
                    required=True)

parser_req.add_argument('-alg','--alg',
                    help='NW = Needleman-Wunsch, SW = Smith-Waterman algorithm', metavar= 'STR',
                    required=True)

#the remaining arguments have default values, so they are not required but optional (showing up in the default group)
parser.add_argument('-m','--match',
                    help='Score for match', metavar='INT',
                    type=int, default=1)

parser.add_argument('-mm','--mismatch',
                    help='Penalty for mismatch', metavar='INT',
                    type=int, default=-1)

parser.add_argument('-g','--gap',
                    help='Penalty for gaps', metavar='INT',
                    type=int, default=-2)

parser.add_argument('-o','--output',
                    help='If "-o file", output will be redirected to a textfile ', metavar='STR',
                    type=str, default=False)

parser.add_argument('-i','--input',
                    help="""Per default provide input sequnces via 
                    command line, if "-i file", provide fasta file name as *.fasta. 
                    Attention: if fasta files names are provided but "-i file" is not set,
                    the script will align the file names!!!""", 
                    metavar= 'STR',
                    )

args = parser.parse_args()
#print(args)

# print statements describing what is done
if args.alg == "NW":
    if args.input == "file":
        print(f"Aligning {args.seq_1.rsplit('.')[0]} and {args.seq_2.rsplit('.')[0]} with Needleman-Wunsch algorithm")
    else:
        print("Aligning seq1 and seq2 with Needleman-Wunsch algorithm")
     
if args.alg == "SW":
    if args.input == "file":
        print(f"Aligning {args.seq_1.rsplit('.')[0]} and {args.seq_2.rsplit('.')[0]} with Smith-Waterman algorithm")
    else:
        print("Aligning seq1 and seq2 with Smith-Waterman algorithm")

if args.output == "file":
    if args.input == "file":
        print(f"Writing output to {args.seq_1.rsplit('.')[0]}_{args.seq_2.rsplit('.')[0]}_{args.alg}.txt")
        sys.stdout = open(f"{args.seq_1.rsplit('.')[0]}_{args.seq_2.rsplit('.')[0]}_{args.alg}.txt",'wt')
    else:
        print(f"Writing output to seq1_seq2_{args.alg}.txt")
        sys.stdout = open(f"seq1_seq2_{args.alg}.txt",'wt')

if args.alg == "NW":
    if args.input == "file":
        print(f"Global alignment of {args.seq_1} and {args.seq_2} with Needleman-Wunsch algorithm")
    else:
        print("Global alignment of seq1 and seq2 with Needleman-Wunsch algorithm")
elif args.alg == "SW":
    if args.input == "file":
        print(f"Local alignment of {args.seq_1} and {args.seq_2} with Smith-Waterman algorithm")
    else:
        print("Local alignment of seq1 and seq2 with Smith-Waterman algorithm")
    
    
#read arguments for costs
match = int(args.match)
mismatch = int(args.mismatch)
gap = int(args.gap)
print(f"score match = {match}")
print(f"penalty mismatch = {mismatch}")
print(f"penalty gap = {gap}")

#dictionary for costs
costs = {'match': match,
            'mismatch': mismatch,
            'gap': gap}

#replace this with command line and/or file input
# seq1 = "gggtgattag"
# seq2 = "GCTGATatAGCT"

#seq1 = "gctgatatagct"
#seq2 = "gggtgattagct"


# source of input dependent on whether arg "-i" is "file" or not set
# we read the second line from fasta files and stript the newline
if args.input == "file":    
    with open(args.seq_1) as f1:
            lines = f1.readlines()
            seq1 = lines[1].strip() 
    with open(args.seq_2) as f2:
            lines = f2.readlines()
            seq2 = lines[1].strip()   
else:   
    seq1 = args.seq_1                       
    seq2 = args.seq_2

# just for checking, the sequences the script read are printed    
print(f"seq1: {seq1}")
print(f"seq2: {seq2}")

#compensate for potential lower case input from user, as we need to test for equal letters later on        
seq1 = seq1.upper()
seq2 = seq2.upper()

###################################################################################################

def Alignment(seq1,seq2,match,mismatch,gap):
    #create alignment matrix and identify maximum score(s)
    #compensate for potential lower case input from user, as we need to test for equal letters later on
    seq1.upper()
    seq2.upper()
    
    #we need one column and row more than sequences (first row/column are filled with only gapped values)
    cols = len(seq1) + 1
    rows = len(seq2) + 1
    
    #build a matrix with a list of lists
    matrix = []
    for i in range(rows):
        matrix.append([0] * cols)
        
            ########################
        # i indices for y-axis/rows/iterating throug i indices for y-axis/rows/iterating through seq2h seq2
        # j indices for x-axis/cols/iterating through seq1
        
        # Seq2
        #       A G G T     <- Seq1
        #     0
        #   A
        # i C
        #   G
        #   T
        ########### j #######

    
    if args.alg == "NW": 
        #iniate first row with gap costs
        #=> we have to iterate through the number of columns and stay in the first row
        for j in range(cols):
            matrix[0][j] = j * gap
    
        # #initiate first column with gap costs
        # #=> we have to iterate through the number of rows and stay in the first column
        for i in range(rows):            
            matrix[i][0] = i * gap       
                
    elif args.alg == "SW":
        # When Smith-Waterman, first row/first column stay at 0
        pass
    
    #we start with both coordinates at value 1, as row/column 0 is already filled up with gap values
    for i in range(1, rows):
        for j in range(1, cols):
            #check if match or mismatch at current position and save correct value
            if seq2[i - 1] == seq1[j - 1]:
                mis_or_match = match
            else:
                mis_or_match = mismatch
            #determine value for diagonal cost
            diag = matrix[i - 1][j - 1] + mis_or_match
            # determine value for introducing a gap in seq1 or horizontal
            hori = matrix[i - 1][j] + gap
            #determine value for introducing a gap in seq2 or vertical
            vert = matrix[i][j - 1] + gap
            
            #get highest value of all three possibilities and fill into current coordinate
            if args.alg == "NW":            
                matrix[i][j] = max(diag, hori, vert)
            # for SW, negative values are not permitted and set to "0"
            elif args.alg == "SW":            
                matrix[i][j] = max(diag, hori, vert, 0)
    
    # determine the maximum score(s)m and its/their i and j indices.
    # we iterate through the list of lists, find the maximum values and return their in indices
    # If the max score occurs multiple times, all coordinates will be returned as a list.
    # If SW algorithm, backtrace(i,j) is called with these indices
	
    global coord_i
    global coord_j
    lst_val_j = []
    lst_ind_j = []
    for j in matrix:
        ind_j = [x for x,y in enumerate(j) if y == max(j)]
        val_j = [y for x,y in enumerate(j) if y == max(j)]
        lst_ind_j.append(ind_j)
        lst_val_j.append(val_j)

    coord_i = [x for x,y in enumerate(lst_val_j) if y == max(lst_val_j)]
    coord_j = []
    for i in coord_i:
        coord_j += lst_ind_j[i]
    # print(coord_i)
    # print(coord_j)
    # print(len(coord_i))
    # print(len(coord_j))

    if args.alg == "NW":
        print("Needleman-Wunsch matrix (scores):")
    if args.alg == "SW":
        print("Smith-Waterman matrix (scores):")
    #print print  max score and indices 
    print(f"max score of {max(lst_val_j)} at: i = {coord_i}, j = {coord_j}")

    #unpack the list (*list) at row k and print tab separated to have matching columns        
    for k in (range(len(matrix))):
        print(*matrix[k], sep="\t")
        
Alignment(seq1,seq2,match=costs['match'],mismatch=costs['mismatch'],gap=costs['gap'])        


##########################################################################

#Let's keep track of our decision for each cell to enable backtracing
def Alignment_bt(seq1,seq2,match,mismatch,gap):
    
    cols = len(seq1) + 1
    rows = len(seq2) + 1

    matrix = []
    btmatrix = []
    for i in range(rows):
        matrix.append([0] * cols)
        btmatrix.append([0] * cols)

    if args.alg == "NW":
        for j in range(cols):
            btmatrix[0][j] = 'ho'
            #for the first index of all columns, we know we walked horizontal
            matrix[0][j] = j * gap
            

    if args.alg == "NW":
        for i in range(rows):
            btmatrix[i][0] = 've'
            #for the first index of all rows, we know we walked vertical
            matrix[i][0] = i * gap
            
    elif args.alg == "SW":
        "When Smith-Waterman, first row/first column stay at 0"
        pass
            
        

    #the upper left corner of our 'matrix' is 0 or undefined
    btmatrix[0][0] = '-'

    for i in range(1, rows):
        for j in range(1, cols):

            if seq2[i - 1] == seq1[j - 1]:
                mis_or_match = match
            else:
                mis_or_match = mismatch

            diag = matrix[i - 1][j - 1] + mis_or_match
            vert = matrix[i - 1][j] + gap
            hori = matrix[i][j - 1] + gap

            if args.alg == "NW":
                matrix[i][j] = max(diag, hori, vert)
            if args.alg == "SW":
                matrix[i][j] = max(diag, hori, vert, 0)
                

            #let's make a copy of our value matrix filled with directions 
            #instead of values to have an easy time backtracing the alignment
            # if a "zero" is found: if it comes from a direction: 
                #(max(diag, hori, vert) = 0, record the direction
            # if max(diag, hori, vert) was <= 0, keeps the "0" thats already in the list
                # at this position backtrace(i,j) should quit            
            if matrix[i][j] == hori:
                btmatrix[i][j] = 'ho'
            elif matrix[i][j] == vert:
                btmatrix[i][j] = 've'
            elif matrix[i][j] == diag:
                btmatrix[i][j] = 'di'
            

    #return the backtracing matrix
    return btmatrix 

#now our function returns the backtracing matrix which we can use to modify our sequences to print 
#the alignment (and to be able to easily check if the output is correct if we print it)
btmatrix = Alignment_bt(seq1,seq2,match=costs['match'],mismatch=costs['mismatch'],gap=costs['gap'])

#print the backtracing matrix

if args.alg == "NW":
    print("\nBacktracing the NW matrix:")
if args.alg == "SW":
    print("\nBacktracing the SW matrix:")
    
for k in (range(len(btmatrix))):
    print(*btmatrix[k], sep="\t")

#############################################################################

def backtrace(i,j):
#lets walk back the matrix we just received with our directions and 
#introduce 'gaps' i.e. '-' into the sequence accordingly before printing
   
#we need to set both solution variables to global to tell python, that we want to modify the global variables
    global seq1_sol
    global seq2_sol

    if i == 0 and j == 0:
        return
    
    if btmatrix[i][j] == 'di':
        seq1_sol = seq1[j-1] + seq1_sol
        seq2_sol = seq2[i-1] + seq2_sol
        backtrace(i-1,j-1)
    elif btmatrix[i][j] == 'ho':
        seq1_sol = seq1[j-1] + seq1_sol
        seq2_sol = '-' + seq2_sol
        backtrace(i,j-1)
    elif btmatrix[i][j] == 've':
        seq1_sol = '-' + seq1_sol
        seq2_sol = seq2[i-1] + seq2_sol
        backtrace(i-1,j)
    # probably not necessary, when a "0" is found stop the function
    # not necessary to make switch NW/SW, NW doesnt (shouldnt) have any zeros in the bt-matrix        
    elif btmatrix[i][j] == 0:
        backtrace(0,0)


if args.alg == "NW":
    # backtracing starts at bottom right corner 
    seq1_sol = ''
    seq2_sol = ''
    backtrace(len(seq2),len(seq1))
    # to make the ouput better looking, insert a middle row with "|" for matches
    middle = ""
    for i in range(len(seq1_sol)):
        if seq1_sol[i] == seq2_sol[i]:
            middle += "|"
        else:
            middle += " " 
        
    print("\nAlignment:\n",seq1_sol,"\n",middle, "\n",seq2_sol)
    
elif args.alg == "SW":
	# Backtracing starts at maximum score identified with Alignment(seq1,seq2,match,mismatch,gap)
        # we call the function with its j, i indices stored in the lists coord_i and coord_j.
	# in case there are more than one max in the SW matrix: return all possible alignments        
    for i in range(len(coord_i)):
        seq1_sol = ''
        seq2_sol = ''
        backtrace(coord_i[i], coord_j[i])
        # to make the ouput better looking, insert a middle row with "|" for matches
        middle = ""
        for i in range(len(seq1_sol)):
            if seq1_sol[i] == seq2_sol[i]:
                middle += "|"
            else:
                middle += " " 
        
        print("\nAlignment:\n",seq1_sol,"\n",middle, "\n",seq2_sol)
        







