rule __PseudoSigner_0_1_PE_Pack_0_99_bbvxkg
{
	meta:
		description = "_ PseudoSigner 0_1 _PE Pack 0_99"
	strings:
		$a = {60E8110000005D83ED0680BDE0049090010F84F2FFCC0AE9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
