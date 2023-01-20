function count_seqs {
  echo "Number of samples: $(grep '^>' $1 | wc -l)" > $2
  echo "Number of unique dates: $(awk -F'(_| )' 'NF==4{printf "%s\n",$2}' $1 | sort | uniq -c | wc -l)" >> $2
  # -F is the field separator
  # NF is the number of fields in the captured line
}

