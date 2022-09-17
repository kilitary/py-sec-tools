rule __VMProtect_v1_25___PolyTech_rhwwrv
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595E595F5B5D585A9D5EC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
