rule _PKLITE32_1_1_ruitrc
{
	meta:
		description = "PKLITE32 1_1"
	strings:
		$a = {68??????0068??????006800000000E8????????E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
