rule __VMProtect_v1_25___PolyTech_bxffbh
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC589D5D595F5E58585A5BC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
