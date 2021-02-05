rule __VMProtect_v1_25___PolyTech_fneday
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595D5F5A5E5D5B589D59C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
