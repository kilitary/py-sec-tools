rule __VMProtect_v1_25___PolyTech_zjivke
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8D475039C50F87????????8D4F4029E18D458029C889C49C5689FE8DBD40FFFFFF57FCF3A45F5E9DE9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
