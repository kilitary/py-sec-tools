rule __VMProtect_v1_25___PolyTech_iylvkr
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????5253505653579C555168000000008B74242C89E581ECC000000089E70375008A06460FB6C08D0C85????????FF2189EC58595D9D5F5A5E585B5AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
