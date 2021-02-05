rule __VMProtect_v1_25___PolyTech_xdcohk
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5F5E9D5F595A5D585BC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
