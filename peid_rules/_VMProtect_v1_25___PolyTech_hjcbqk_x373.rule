rule __VMProtect_v1_25___PolyTech_hjcbqk
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595F585B9D5A5D5F5E59C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
