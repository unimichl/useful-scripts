
### Usage ###
Alignment of two (DNA) sequences with Needleman-Wunsch (global) or Smith-Waterman (local) algorithms

optional arguments:
  -h, --help            show this help message and exit
  -m INT, --match INT   Score for match (default: 1)
  -mm INT, --mismatch INT
                        Penalty for mismatch (default: -1)
  -g INT, --gap INT     Penalty for gaps (default: -2)
  -o STR, --output STR  If "-o file", output will be redirected to a textfile (default: False)
  -i STR, --input STR   Per default provide input sequnces via command line, if "-i file", provide fasta file name as
                        *.fasta. Attention: if fasta files names are provided but "-i file" is not set, the script will
                        align the file names!!! (default: None)

required arguments:
  -a STR, --seq_1 STR   The first sequence, if "-i file", provide name of fasta file (*.fasta) (default: None)
  -b STR, --seq_2 STR   The second sequence, if "-i file", provide name of fasta file (*.fasta) (default: None)
  -alg STR, --alg STR   NW = Needleman-Wunsch, SW = Smith-Waterman algorithm (default: None)

### Try it ###
Place script in a folder and run it from there from bash command line

## Per default, the script runs with sequences provided as command line arguments, 
specify the preferred algorithm with argument "-alg" (NW or SW, required). 
   For, example try: 
	python align.py -a tgttacgg -b ggttgacta -alg NW
      or
	python align.py -a tgttacgg -b ggttgacta -alg SW

## If input sequences are provided as fasta files,  place them in the same folder, add option "-i file" and eg. run:
	python align.py -a aa.fasta -b bb.fasta -alg NW -i file
      or
	python align.py -a aa.fasta -b bb.fasta -alg SW -i file

  # !!!! Note: If fasta files are provided this way, but "-i file" is not set, the script will just align the file names !!!!, 
	you will probably notice anyway...

## Per default, the output is directed to stdout, if you wish the output to be redirected to a file, use option -o,
    the results will then be written to a *.txt file in the same folder, try with the provided fasta files: 
	python align.py -a tgttacgg -b ggttgacta -alg SW -o file
	python align.py -a tgttacgg -b ggttgacta -alg NW -o file
	python align.py -a aa.fasta -b bb.fasta -alg NW -i file -o file
	python align.py -a aa.fasta -b bb.fasta -alg SW -i file -o file

### Additional notes ###
In case the Smith-Waterman algorithm identifies more than one maximum score (of equal value) in the score matrix, 
an equal number of possible local alignments with traceback starting at the resepctive indices in the traceback matrix will be displayed.

### if bug == True: ####
Nobodys perfect, please report bugs to the author.......


