rule __VMProtect_v1_25___PolyTech_mlffap
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B5D9D595F5D585E5A5BC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
