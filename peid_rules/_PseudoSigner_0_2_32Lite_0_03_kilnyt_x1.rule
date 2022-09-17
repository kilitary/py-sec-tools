rule __PseudoSigner_0_2_32Lite_0_03_kilnyt
{
	meta:
		description = "_ PseudoSigner 0_2 _32Lite 0_03"
	strings:
		$a = {6006FC1E07BE909090906A04689010909068}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
