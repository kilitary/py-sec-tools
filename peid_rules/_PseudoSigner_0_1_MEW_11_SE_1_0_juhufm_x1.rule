rule __PseudoSigner_0_1_MEW_11_SE_1_0_juhufm
{
	meta:
		description = "_ PseudoSigner 0_1 _MEW 11 SE 1_0"
	strings:
		$a = {E909000000000000020000000C90E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
