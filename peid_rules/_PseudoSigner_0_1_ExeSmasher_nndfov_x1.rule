rule __PseudoSigner_0_1_ExeSmasher_nndfov
{
	meta:
		description = "_ PseudoSigner 0_1 _ExeSmasher"
	strings:
		$a = {9CFE039060BE909041908DBE9010FFFF5783CDFFEB1090909090909090909090909090909090FE0BE9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
