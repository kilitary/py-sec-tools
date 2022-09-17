rule __PseudoSigner_0_2_PESHiELD_0_25_toqbnm
{
	meta:
		description = "_ PseudoSigner 0_2 _PESHiELD 0_25"
	strings:
		$a = {60E82B0000009090909090909090909090909090909090909090909090909090909090909090909090909090909090CCCC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
