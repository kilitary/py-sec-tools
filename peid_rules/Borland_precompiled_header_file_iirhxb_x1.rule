rule _Borland_precompiled_header_file_iirhxb
{
	meta:
		description = "Borland precompiled header file"
	strings:
		$a = {545053}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
