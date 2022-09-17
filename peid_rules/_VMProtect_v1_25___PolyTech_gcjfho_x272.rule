rule __VMProtect_v1_25___PolyTech_gcjfho
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC58585A5D5B5E595A9D5FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
