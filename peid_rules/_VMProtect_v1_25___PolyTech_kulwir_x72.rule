rule __VMProtect_v1_25___PolyTech_kulwir
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8A06668B550083C502668914078D7601E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
