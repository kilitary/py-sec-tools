rule __VMProtect_v1_25___PolyTech_mgbeqi
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A585B5D5E5A5E599D5FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
