rule __VMProtect_v1_25___PolyTech_ruhwuy
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595B5F585A5E9D5D5959C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
