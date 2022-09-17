rule __VMProtect_v1_25___PolyTech_ciyepq
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5E5B5A585D595F9D5FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
