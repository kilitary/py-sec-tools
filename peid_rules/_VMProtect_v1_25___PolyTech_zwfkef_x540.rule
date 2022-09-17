rule __VMProtect_v1_25___PolyTech_zwfkef
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????9C535656505551575268000000008B74242C89E581ECC000000089E70375008A060FB6C046FF2485????????8B450083C502668B0066894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
