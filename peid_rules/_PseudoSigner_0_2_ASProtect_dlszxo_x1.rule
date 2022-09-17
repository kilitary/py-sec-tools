rule __PseudoSigner_0_2_ASProtect_dlszxo
{
	meta:
		description = "_ PseudoSigner 0_2 _ASProtect"
	strings:
		$a = {609090909090905D909090909090909090909003DD}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
