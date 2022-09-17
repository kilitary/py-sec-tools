rule __VMProtect_v1_25___PolyTech_tettjl
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????5650539C515752575568000000008B74242C89E581ECC000000089E70375008A060FB6C08D7601FF2485????????668B6D00E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
