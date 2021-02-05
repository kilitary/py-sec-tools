rule _Borland_C__1994_syglgk
{
	meta:
		description = "Borland C__ 1994"
	strings:
		$a = {8CCA2E89??????B430CD218B2E????8B1E????8EDAA3????8C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
