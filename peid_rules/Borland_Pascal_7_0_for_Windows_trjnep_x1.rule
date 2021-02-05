rule _Borland_Pascal_7_0_for_Windows_trjnep
{
	meta:
		description = "Borland Pascal 7_0 for Windows"
	strings:
		$a = {9AFFFF00009AFFFF00005589E531C09AFFFF0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
