rule __VMProtect_v1_25___PolyTech_ihohrp
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595F585B5F5A595D9D5EC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
