rule __PseudoSigner_0_1_LTC_1_3_vbiycb
{
	meta:
		description = "_ PseudoSigner 0_1 _LTC 1_3"
	strings:
		$a = {54E8000000005D8BC581EDF67340002B858775400083E806E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
