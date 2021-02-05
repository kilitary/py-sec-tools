rule __VMProtect_v1_25___PolyTech_ttivyg
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????565352509C5155545768000000008B74242C89E581ECC000000089E70375008A06460FB6C08D0C85????????FF2189E883ED0266894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
