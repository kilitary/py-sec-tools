rule __VMProtect_v1_25___PolyTech_dtvdpn
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A58595E5F5D5B5A5A9DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
