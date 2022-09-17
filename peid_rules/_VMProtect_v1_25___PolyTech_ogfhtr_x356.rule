rule __VMProtect_v1_25___PolyTech_ogfhtr
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595B5F5B9D595A5D585EC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
