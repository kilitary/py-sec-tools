rule __VMProtect_v1_25___PolyTech_jmnqvs
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B5F5F5B58595D5A5E9DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
