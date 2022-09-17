rule __PseudoSigner_0_1_Microsoft_Visual_C__6_0_Debug_Version__qfrfdm
{
	meta:
		description = "_ PseudoSigner 0_1 _Microsoft Visual C__ 6_0 _Debug Version_"
	strings:
		$a = {558BEC5190909001019090909068????????90909090909090909090909000019090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909000019090909090}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
