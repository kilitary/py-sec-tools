rule __PseudoSigner_0_1_FSG_1_31_jckyda
{
	meta:
		description = "_ PseudoSigner 0_1 _FSG 1_31"
	strings:
		$a = {BE90909000BF90909000BB9090900053BB90909000B280E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
