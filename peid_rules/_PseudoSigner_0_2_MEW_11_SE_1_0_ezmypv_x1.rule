rule __PseudoSigner_0_2_MEW_11_SE_1_0_ezmypv
{
	meta:
		description = "_ PseudoSigner 0_2 _MEW 11 SE 1_0"
	strings:
		$a = {E909000000000000020000000C90}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
