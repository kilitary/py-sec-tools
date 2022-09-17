rule __PseudoSigner_0_2_FSG_1_31_zvsdye
{
	meta:
		description = "_ PseudoSigner 0_2 _FSG 1_31"
	strings:
		$a = {BE90909000BF90909000BB9090900053BB90909000B280}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
