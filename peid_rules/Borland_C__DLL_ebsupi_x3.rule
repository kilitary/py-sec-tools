rule _Borland_C__DLL_ebsupi
{
	meta:
		description = "Borland C__ DLL"
	strings:
		$a = {EB1066623A432B2B484F4F4B90E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
