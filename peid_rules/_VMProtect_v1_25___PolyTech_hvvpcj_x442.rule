rule __VMProtect_v1_25___PolyTech_hvvpcj
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B595F5B585A9D585E5DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
