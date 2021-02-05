rule __PseudoSigner_0_2_Microsoft_Visual_Basic_5_0__6_0_vpquiz
{
	meta:
		description = "_ PseudoSigner 0_2 _Microsoft Visual Basic 5_0 _ 6_0"
	strings:
		$a = {68????????E80A00000000000000000030000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
