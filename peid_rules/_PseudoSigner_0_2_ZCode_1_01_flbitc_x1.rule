rule __PseudoSigner_0_2_ZCode_1_01_flbitc
{
	meta:
		description = "_ PseudoSigner 0_2 _ZCode 1_01"
	strings:
		$a = {E912000000000000000000000000000000E9FBFFFFFFC3680000000064FF3500000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
