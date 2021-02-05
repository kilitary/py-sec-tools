rule __VMProtect_v1_25___PolyTech_bqxgtz
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????569C5155525157505368000000008B74242C89E581ECC000000089E70375008A060FB6C08D76018D0C85????????FF21668B6D00E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
