rule _Can2Exe_v0_01_ndtfre
{
	meta:
		description = "Can2Exe v0_01"
	strings:
		$a = {0E1F0E07E8????E8????3AC673}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
