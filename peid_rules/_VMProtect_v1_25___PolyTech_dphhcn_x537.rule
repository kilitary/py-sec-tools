rule __VMProtect_v1_25___PolyTech_dphhcn
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????9C515653525055525768000000008B74242C89E581ECC000000089E70375008A06460FB6C0FF2485????????8B550083C502368A0266894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
