rule __PseudoSigner_0_1_VBOX_4_3_MTE_addgyu
{
	meta:
		description = "_ PseudoSigner 0_1 _VBOX 4_3 MTE"
	strings:
		$a = {0BC00BC00BC00BC00BC00BC00BC00BC0E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
