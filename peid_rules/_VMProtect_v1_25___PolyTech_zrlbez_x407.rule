rule __VMProtect_v1_25___PolyTech_zrlbez
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5B599D5D5A5E585F5FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
