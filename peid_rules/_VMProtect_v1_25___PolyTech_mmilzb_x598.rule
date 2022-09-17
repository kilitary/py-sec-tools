rule __VMProtect_v1_25___PolyTech_mmilzb
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????565255505751539C5468000000008B74242C89E581ECC000000089E70375008A0683C6010FB6C0FF2485????????89E883ED0266894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
