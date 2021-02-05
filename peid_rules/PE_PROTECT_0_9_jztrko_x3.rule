rule _PE_PROTECT_0_9_jztrko
{
	meta:
		description = "PE_PROTECT 0_9"
	strings:
		$a = {50452D50524F5445435420302E39}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
