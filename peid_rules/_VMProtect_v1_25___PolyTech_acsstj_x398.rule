rule __VMProtect_v1_25___PolyTech_acsstj
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A595F5F5E5D5A5B9D58C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
