rule __VMProtect_v1_25___PolyTech_xzbasy
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5D9D5A5B59585E585FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
