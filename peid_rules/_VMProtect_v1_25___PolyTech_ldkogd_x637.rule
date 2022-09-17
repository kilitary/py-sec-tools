rule __VMProtect_v1_25___PolyTech_ldkogd
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????55535151565052579C68000000008B74242C89E581ECC000000089E70375008A060FB6C083C601FF2485????????8B45008B00894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
