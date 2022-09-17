rule _Borland_C__DLL_vpgcpw
{
	meta:
		description = "Borland C__ DLL"
	strings:
		$a = {EB1066623A432B2B484F4F4B90}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
