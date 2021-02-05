rule __PseudoSigner_0_1_PEX_0_99_fyczxa
{
	meta:
		description = "_ PseudoSigner 0_1 _PEX 0_99"
	strings:
		$a = {60E8010000005583C404E801000000905D81FFFFFF0001E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
