rule __PseudoSigner_0_1_PECompact_1_4__ilstyb
{
	meta:
		description = "_ PseudoSigner 0_1 _PECompact 1_4_"
	strings:
		$a = {9090909068????????6764FF360000676489260000F190909090EB066890909090C39C60E80290909033C08BC483C004938BE38B5BFC81}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
