source countSeqs.sh

function main {
	count_seqs $1 $2
	python alignment_comparison.py $1 $2
	echo "done"
}

main ExampleAlignment.fasta log.txt
