rule __PseudoSigner_0_2_NorthStar_PE_Shrinker_1_3_cixzpt
{
	meta:
		description = "_ PseudoSigner 0_2 _NorthStar PE Shrinker 1_3"
	strings:
		$a = {9C60E8000000005DB8B38540002DAC8540002BE88DB500000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
