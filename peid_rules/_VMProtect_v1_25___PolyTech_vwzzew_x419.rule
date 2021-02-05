rule __VMProtect_v1_25___PolyTech_vwzzew
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5E5A5F595B5D585B9DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
