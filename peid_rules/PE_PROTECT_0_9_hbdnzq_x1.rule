rule _PE_PROTECT_0_9_hbdnzq
{
	meta:
		description = "PE_PROTECT 0_9"
	strings:
		$a = {E9CF0000000D0A0D0AC4C4C4C4C4C4C4C4C4C4C4}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
