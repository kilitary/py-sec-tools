rule __PseudoSigner_0_2_ExeSmasher_ujotem
{
	meta:
		description = "_ PseudoSigner 0_2 _ExeSmasher"
	strings:
		$a = {9CFE039060BE909041908DBE9010FFFF5783CDFFEB1090909090909090909090909090909090FE0B}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
