rule __PseudoSigner_0_1_ASProtect_unvcvi
{
	meta:
		description = "_ PseudoSigner 0_1 _ASProtect"
	strings:
		$a = {609090909090905D909090909090909090909003DDE9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
