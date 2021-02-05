rule __VMProtect_v1_25___PolyTech_dlgeef
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5D5F5A5B5E589D595FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
