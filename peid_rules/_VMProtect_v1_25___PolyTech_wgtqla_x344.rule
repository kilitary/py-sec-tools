rule __VMProtect_v1_25___PolyTech_wgtqla
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5959585B5D5F5E5A5F9DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
