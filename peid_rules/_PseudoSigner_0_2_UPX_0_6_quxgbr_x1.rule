rule __PseudoSigner_0_2_UPX_0_6_quxgbr
{
	meta:
		description = "_ PseudoSigner 0_2 _UPX 0_6"
	strings:
		$a = {60E8000000005883E83D508DB8000000FF578DB0E8000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
