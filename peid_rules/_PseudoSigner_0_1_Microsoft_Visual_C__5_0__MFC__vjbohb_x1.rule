rule __PseudoSigner_0_1_Microsoft_Visual_C__5_0__MFC__vjbohb
{
	meta:
		description = "_ PseudoSigner 0_1 _Microsoft Visual C__ 5_0_ _MFC_"
	strings:
		$a = {558BEC6AFF68????????68????????64A10000000050E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
