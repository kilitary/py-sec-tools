rule __PseudoSigner_0_1_CodeSafe_2_0_wxeldx
{
	meta:
		description = "_ PseudoSigner 0_1 _CodeSafe 2_0"
	strings:
		$a = {90909090909090909090909090909090909090909090EB0B83EC10535657E8C4010085E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
