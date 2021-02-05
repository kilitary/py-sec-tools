rule __PseudoSigner_0_1_DEF_1_0_shnctx
{
	meta:
		description = "_ PseudoSigner 0_1 _DEF 1_0"
	strings:
		$a = {BE000140006A0559807E070074118B46909090909090909090909090909090909083C101E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
