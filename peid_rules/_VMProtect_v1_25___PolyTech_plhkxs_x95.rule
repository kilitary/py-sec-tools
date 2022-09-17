rule __VMProtect_v1_25___PolyTech_plhkxs
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????0FB60666988D76019883ED04894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
