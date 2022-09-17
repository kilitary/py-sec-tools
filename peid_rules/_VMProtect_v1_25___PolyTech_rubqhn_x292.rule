rule __VMProtect_v1_25___PolyTech_rubqhn
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585A595F59589D5E5D5BC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
