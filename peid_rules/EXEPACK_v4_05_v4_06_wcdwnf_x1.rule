rule _EXEPACK_v4_05_v4_06_wcdwnf
{
	meta:
		description = "EXEPACK v4_05_ v4_06"
	strings:
		$a = {8CC005????0E1FA3????0306????8EC08B0E????8BF94F8BF7FDF3A4}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
