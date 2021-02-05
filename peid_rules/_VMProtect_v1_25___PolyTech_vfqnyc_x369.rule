rule __VMProtect_v1_25___PolyTech_vfqnyc
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595E5D5A5F59589D5B5BC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
