rule __VMProtect_v1_25___PolyTech_dbwyef
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585E5A595D5B585F9D5FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
