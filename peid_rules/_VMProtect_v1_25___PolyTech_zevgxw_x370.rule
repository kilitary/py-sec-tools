rule __VMProtect_v1_25___PolyTech_zevgxw
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595E5F9D5D5B585E5A59C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
