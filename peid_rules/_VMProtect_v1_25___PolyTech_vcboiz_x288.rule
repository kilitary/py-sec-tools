rule __VMProtect_v1_25___PolyTech_vcboiz
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC58595F585A9D5D5E5E5BC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
