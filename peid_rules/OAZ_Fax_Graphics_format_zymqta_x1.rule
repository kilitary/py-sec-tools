rule _OAZ_Fax_Graphics_format_zymqta
{
	meta:
		description = "OAZ Fax Graphics format"
	strings:
		$a = {0F0F0F0F01000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
