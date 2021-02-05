rule __VMProtect_v1_25___PolyTech_hfefzr
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A58595E5D5F5B9D5A5FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
