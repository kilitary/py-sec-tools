rule _Borland_C__DLL_wgvbup
{
	meta:
		description = "Borland C__ DLL"
	strings:
		$a = {EB1066623A432B2B484F4F4B90E9A1C1E002A38B}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
