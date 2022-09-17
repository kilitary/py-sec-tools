rule _Borland_C__1992_1994_kiadgq
{
	meta:
		description = "Borland C__ 1992_ 1994"
	strings:
		$a = {8CC88ED88C1E????8C06????8C06????8C06}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
