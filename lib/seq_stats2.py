
def gc_content(dna_str):
    from collections import Counter
    seq = dna_str.upper().replace("N","")
    gc = 0
    gc += seq.count('G')
    gc += seq.count('C')
    percentGC = float(gc)*100/len(seq)
    return percentGC

